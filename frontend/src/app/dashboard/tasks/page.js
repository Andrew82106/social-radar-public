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

import { scaleSequential } from "d3-scale";
import { interpolateViridis } from "d3-scale-chromatic";

// 定义颜色比例尺
const colorScale = scaleSequential(interpolateViridis).domain([0, 100]);

export default function Page() {
  const { eventId, setEventId, platform, setPlatform } = useEventId();
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data: data1, error: error1 } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/summaryLocationall/?eventid=${eventId}`,
    fetcher
  );
  if (error1) return <div>Failed to load</div>;
  if (!data1) return <Loading />;
  return (
    <main className="w-full h-full bg-gray-100 p-4">
      <div className="h-full flex flex-col overflow-x-auto space-y-4">
        <div className="border-2 border-gray-200 bg-white rounded p-4 shadow">
          <div className="flex flex-col space-y-4">
            <div className="border-2 border-gray-200 bg-white rounded p-4 shadow h-auto">
              <LineChart />
            </div>
            <div className="bg-gray-200 rounded inline-block">
              <Heatmap data={data1.data} />
            </div>

            <Legend data={data1.data} />
          </div>
        </div>
      </div>
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
        .translate([width / 2 + 150, height / 2 + 100]);

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

  const urls = [
    `${process.env.NEXT_PUBLIC_API_URL}/timequota/gettimeseq/?eventid=${eventId}&mode=date`, // 时间热度
    `${process.env.NEXT_PUBLIC_API_URL}/SensitiveDataOverAll/?eventid=${eventId}`, // 内容敏感度
    `${process.env.NEXT_PUBLIC_API_URL}/UserQuotaOverAll/?eventid=${eventId}`, // 用户真实度
    `${process.env.NEXT_PUBLIC_API_URL}/EmotionQuotaOverAll/?eventid=${eventId}`, // 情感激烈性
    `${process.env.NEXT_PUBLIC_API_URL}/OpinionQuotaOverAll/?eventid=${eventId}`, // 观点对立性
    `${process.env.NEXT_PUBLIC_API_URL}/SummaryQuotaOverAll/?eventid=${eventId}`, // 总指标
  ];
  const fetcher = (urls) =>
    Promise.all(urls.map((url) => fetch(url).then((res) => res.json())));
  const { data, error } = useSWR(urls, fetcher);
  if (error) return <div>{error.message}Failed to load</div>;
  if (!data) return <Loading />;

  const labels = Object.keys(data[0].data); // Assuming all datasets have the same labels

  const datasetNames = [
    "时间热度",
    "内容敏感度",
    "用户真实度",
    "情感激烈性",
    "观点对立性",
    "总指标",
  ];

  const colors = [
    "rgba(255, 99, 132, 0.6)", // red
    "rgba(75, 192, 192, 0.6)", // green
    "rgba(153, 102, 255, 0.6)", // purple
    "rgba(255, 159, 64, 0.6)", // orange
    "rgba(255, 205, 86, 0.6)", // yellow
    "rgba(54, 162, 235, 0.6)", // blue
    // Add more colors if you have more datasets
  ];

  const chartData = {
    labels: labels,
    datasets: data.map((dataset, index) => ({
      label: datasetNames[index],
      data: Object.values(dataset.data),
      fill: false,
      backgroundColor: colors[index % colors.length],
      borderColor: colors[index % colors.length],
    })),
  };

  return <Line data={chartData} />;
};

const Legend = ({ data }) => {
  // 假设 data 是一个对象，其键是省份名称，值是该省份在轴上的位置（0-100）
  let provinces = Object.keys(data);
  let positions = Object.values(data);

  // 创建一个新的数组，包含省份和位置的信息
  let items = provinces.map((province, index) => ({
    province,
    position: positions[index],
  }));

  // 按位置对数组进行排序
  items.sort((a, b) => a.position - b.position);

  // 对相邻的省份进行错开
  for (let i = 1; i < items.length; i++) {
    if (items[i].position - items[i - 1].position < 3) {
      // 如果两个省份的位置相差小于10%，则将它们错开
      items[i].offset = 60; // 偏移量
    }
  }

  // 创建一个颜色渐变字符串
  const gradient = `linear-gradient(to right, ${colorScale(0)}, ${colorScale(
    100
  )})`;

  return (
    <div
      className="relative h-32 opacity-80 rounded-lg shadow-lg overflow-hidden"
      style={{ backgroundImage: gradient }}
    >
      {items.map((item, index) => (
        <div
          key={item.province}
          className="absolute transform -translate-x-1/2"
          style={{ left: `${item.position}%`, top: `${item.offset || 20}px` }} // 使用偏移量
        >
          <div className="w-4 h-4 bg-white rounded-full animate-pulse" />
          <span className="text-lg text-gray-800 mt-2 bg-white px-1 rounded-md shadow-md transition-all duration-500 ease-in-out transform hover:scale-125">
            {item.province}
          </span>
        </div>
      ))}
    </div>
  );
};
