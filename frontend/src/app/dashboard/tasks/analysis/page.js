"use client";
import React, { useEffect, useRef } from "react";
import useSWR from "swr";
import { useEventId } from "@/components/hooks/EventIdContext";
import * as d3 from "d3";
import Loading from "@/components/common/Loading";
import { Chart as ChartJS, registerables } from "chart.js";
import { Line } from "react-chartjs-2";

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

const LineChart = ({}) => {
  const data = {
    bilibili: {
      "2021-05-18": 132,
      "2021-05-19": 146,
      "2021-05-20": 46,
      "2021-05-21": 211,
      "2021-05-22": 76,
      "2021-05-23": 23,
      "2021-05-24": 2,
      "2021-05-25": 4,
      "2021-05-26": 4,
      "2021-05-29": 4,
      "2021-05-30": 5,
      "2021-06-03": 2,
      "2021-06-07": 2,
      "2021-06-08": 4,
      "2021-06-09": 2,
      "2021-06-16": 68,
      "2021-06-17": 55,
      "2021-06-18": 7,
      "2021-06-19": 1,
      "2021-06-21": 2,
      "2021-06-22": 1,
      "2021-06-23": 1,
      "2021-06-25": 3,
      "2021-06-26": 1,
      "2021-06-27": 1,
      "2021-06-28": 1,
      "2021-07-02": 2,
      "2021-07-05": 2,
      "2021-07-06": 3,
      "2021-07-07": 1,
      "2021-07-08": 1,
      "2021-08-03": 1,
      "2021-09-15": 1,
      "2021-09-19": 2,
      "2021-12-10": 2,
      "2022-01-17": 2,
      "2022-03-05": 1,
      "2022-03-18": 2,
      "2022-03-22": 1,
      "2022-05-05": 2,
      "2022-05-07": 1,
      "2022-05-31": 2,
      "2022-06-12": 1,
      "2022-06-18": 2,
      "2022-06-21": 1,
      "2022-08-09": 2,
      "2022-11-25": 1,
      "2023-01-23": 2,
      "2023-02-01": 2,
      "2023-02-18": 2,
      "2023-06-12": 4,
      "2023-09-16": 2,
      "2023-09-26": 2,
      "2023-10-04": 1,
      "2023-10-07": 1,
      "2023-10-08": 709,
      "2023-10-09": 1125,
      "2023-10-10": 879,
      "2023-10-11": 702,
      "2023-10-12": 1572,
      "2023-10-13": 1529,
      "2023-10-14": 1712,
      "2023-10-15": 1142,
      "2023-10-16": 1067,
      "2023-10-17": 1660,
      "2023-10-18": 2827,
      "2023-10-19": 1988,
      "2023-10-20": 1847,
      "2023-10-21": 1759,
      "2023-10-22": 1068,
      "2023-10-23": 1612,
      "2023-10-24": 935,
    },
    wangyi: {
      "2023/11/22": 1,
      "2023/11/24": 4,
      "2023/11/25": 15,
      "2023/11/26": 5,
      "2023/11/27": 8,
      "2023/11/28": 10,
      "2023/11/29": 12,
      "2023/11/30": 25,
      "2023/12/1": 17,
      "2023/12/2": 13,
      "2023/12/3": 16,
      "2023/12/4": 21,
      "2023/12/5": 2,
    },
    zhihu: {
      "2023-11-29": 12,
      "2023-11-30": 125,
      "2023-12-01": 74,
      "2023-12-02": 60,
      "2023-12-03": 35,
      "2023-12-04": 14,
      "2023-12-05": 2,
    },
  };

  const datasetData = Object.values(data.bilibili);

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
