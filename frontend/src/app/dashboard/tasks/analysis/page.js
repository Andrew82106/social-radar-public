"use client";
import React, { useEffect, useRef } from "react";
import useSWR from "swr";
import { useEventId } from "@/components/hooks/EventIdContext";
import * as d3 from "d3";
import Loading from "@/components/common/Loading";
import { Chart as ChartJS, registerables } from "chart.js";
import { Line } from "react-chartjs-2";
import SelectDemo from "@/components/widgets/select/PlatformSelect";

ChartJS.register(...registerables);

export default function Page() {
  const { eventId, setEventId } = useEventId();
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data: data1, error: error1 } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/summaryLocationall/?eventID=${eventId}`,
    fetcher
  );
  if (error1) return <div>Failed to load</div>;
  if (!data1) return <Loading />;
  return (
    <main className="w-full h-full">
    <SelectDemo></SelectDemo>
      <Heatmap data={data1.data} />
      <LineChart />
    </main>
  );
}

const Heatmap = ({ data }) => {
  const ref = useRef();

  useEffect(() => {
    d3.json("/china_simplify.json").then((topology) => {
      console.log(JSON.stringify(topology));
      const geoData = topology;

      const width = 1000;
      const height = 800;

      const projection = d3
        .geoMercator()
        .center([107, 31])
        .scale(750)
        .translate([width / 2, height / 2 + 50]);

      const path = d3.geoPath().projection(projection);

      const color = d3
        .scaleQuantize()
        .domain([0, d3.max(Object.values(data))])
        .range(d3.schemeBlues[9]);

      const svg = d3
        .select(ref.current)
        .attr("width", width)
        .attr("height", height);

      svg
        .selectAll("path")
        .data(geoData.features)
        .enter()
        .append("path")
        .attr("d", path)
        .attr("fill", (d) => color(data[d.properties.name]))
        .attr("stroke", "#fff")
        .attr("stroke-width", 1)
        .on("mouseover", function (event, d) {
          d3.select(this).attr("fill", "#FFC0CB");
          const tooltip = document.getElementById("tooltip");
          tooltip.style.display = "block";
          tooltip.style.left = event.pageX + "px";
          tooltip.style.top = event.pageY + "px";
          tooltip.textContent = `${d.properties.name}: ${
            data[d.properties.name] || 0
          }`;
        })
        .on("mouseout", function (event, d) {
          d3.select(this).attr("fill", (d) => color(data[d.properties.name]));
          const tooltip = document.getElementById("tooltip");
          tooltip.style.display = "none";
        });
    });
  }, []);

  return (
    <>
      <svg ref={ref} />
      <div
        id="tooltip"
        style={{
          position: "absolute",
          display: "none",
          backgroundColor: "#222",
          color: "white",
          border: "1px solid #f8f8f8",
          padding: "10px",
          borderRadius: "5px",
          pointerEvents: "none",
          fontFamily: "'Arial', sans-serif",
          fontSize: "14px",
          boxShadow: "0px 0px 10px rgba(0, 0, 0, 0.5)",
        }}
      ></div>
    </>
  );
};

const LineChart = () => {
  const { eventId, setEventId } = useEventId();
  const fetcher = url => fetch(url).then(res => res.json())
  const { data: timequota, error } = useSWR(`${process.env.NEXT_PUBLIC_API_URL}/timequota/gettimeseq/?eventid=${eventId}&mode=date`, fetcher)
  const { data: sentitive, error1 } = useSWR(`${process.env.NEXT_PUBLIC_API_URL}/SensitiveDataOverAll/?eventID=${eventId}`, fetcher)
  if (error) return <div>Failed to load</div>
  if (!timequota || !sentitive) return <div>Loading...</div>
  const data = sentitive.data

  const longestDataset = Object.values(data).reduce((a, b) => (Object.keys(a).length > Object.keys(b).length ? a : b));
  const labels = Object.keys(longestDataset);

  const chartData = {
    labels: labels,
    datasets: Object.entries(data).map(([name, values]) => ({
      label: name,
      data: Object.values(values),
      fill: false,
      backgroundColor:
        name === "bilibili"
          ? "rgb(75, 192, 192)"
          : name === "wangyi"
          ? "rgb(255, 99, 132)"
          : "rgb(255, 205, 86)",
      borderColor:
        name === "bilibili"
          ? "rgba(75, 192, 192, 0.2)"
          : name === "wangyi"
          ? "rgba(255, 99, 132, 0.2)"
          : "rgba(255, 205, 86, 0.2)",
    })),
  };
  return <Line data={chartData} />;
};
