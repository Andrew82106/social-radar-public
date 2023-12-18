"use client";
import React, { useEffect, useRef } from "react";
import useSWR from "swr";
import { useEventId } from "@/components/hooks/EventIdContext";
import * as d3 from "d3";
import Loading from "@/components/common/Loading";
import { Chart as ChartJS, registerables } from "chart.js";
import { Line } from "react-chartjs-2";
import PlatformSelect from "@/components/widgets/select/PlatformSelect";

ChartJS.register(...registerables);

export default function Page() {
  const { eventId, platform, activePlatform, setEventId, setActivePlatform } = useEventId();
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data: data1, error: error1 } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/summaryLocationByPlatform/?eventID=${eventId}&Platform=${activePlatform}`,
    fetcher
  );
  if (error1) return <div>Failed to load</div>;
  if (!data1) return <Loading />;
  return (
    <main className="w-full h-full">
      <PlatformSelect />
      {activePlatform}
      <Heatmap data={data1.data} />
      <LineChart />
    </main>
  );
}

const Heatmap = ({ data }) => {
  const ref = useRef();

  useEffect(() => {
    d3.select(ref.current).selectAll("*").remove();
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
  }, [data]);

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
  const { eventId, platform, activePlatform, setEventId, setActivePlatform } = useEventId();

  const urls = [
    `${process.env.NEXT_PUBLIC_API_URL}/timequota/gettimeseqdetail/?eventid=${eventId}?platform=${activePlatform}`, // 时间热度
    `${process.env.NEXT_PUBLIC_API_URL}/SensitiveDataDetail/?eventID=${eventId}&Platform=${activePlatform}`, // 内容敏感度
    `${process.env.NEXT_PUBLIC_API_URL}/UserDataByDate/?eventid=${eventId}&platform=${activePlatform}`, // 用户真实度
    `${process.env.NEXT_PUBLIC_API_URL}/EmotionDataDetail/?eventID=${eventId}&Platform=${activePlatform}&mode=date`, // 情感激烈性
    `${process.env.NEXT_PUBLIC_API_URL}/OpinionDataDetail/?eventID=${eventId}&Platform=${activePlatform}`, // 观点对立性
    `${process.env.NEXT_PUBLIC_API_URL}/SummaryQuota/?eventid=${eventId}&platform=${activePlatform}`, // 总指标
  ];
  const fetcher = (urls) =>
    Promise.all(urls.map((url) => fetch(url).then((res) => res.json())));
  const { data, error } = useSWR(urls, fetcher);
  if (error) return <div>{error.message}Failed to load</div>;
  if (!data) return <div>Loading...</div>;

  const labels = Object.keys(data[0].data); // Assuming all datasets have the same labels

  const chartData = {
    labels: labels,
    datasets: data.map((dataset, index) => ({
      label: dataset.platform,
      data: Object.values(dataset.data),
      fill: false,
      backgroundColor: `rgb(${index * 50}, ${index * 100}, ${index * 150})`, // Change color for each dataset
      borderColor: `rgba(${index * 50}, ${index * 100}, ${index * 150}, 0.6)`, // Change color for each dataset
    })),
  };

  return <Line data={chartData} />;
};
