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

import { scaleSequential } from 'd3-scale';
import { interpolateViridis } from 'd3-scale-chromatic';

// 定义颜色比例尺
const colorScale = scaleSequential(interpolateViridis).domain([0, 100]);

export default function Page() {
  const { eventId, platform, activePlatform, setEventId, setActivePlatform } =
    useEventId();
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data: data1, error: error1 } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/summaryLocationByPlatform/?eventid=${eventId}&Platform=${activePlatform}`,
    fetcher
  );

  const { data: data2, error: error2 } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/fetcheventquota/?id=${eventId}&platform=${activePlatform}`,
    fetcher
  );

  if (error1) return <div>Failed to load</div>;
  if (!data1 || !data2) return <Loading />;
  return (
    <main className="w-full h-full flex flex-col items-center justify-center space-y-4 bg-gray-100 p-4">
      <PlatformSelect />
      <div className="flex flex-col items-center max-w-6xl overflow-auto w-full space-y-4">
        <div className="h-1/2 p-8 bg-white rounded shadow w-full">
          <h2 className="text-xl font-bold mb-2">指标数据</h2>
          <div className="flex flex-wrap justify-between space-x-2">
            <DataCard title="时间热度" value={data2.data["时间热度指标"]} />
            <DataCard title="内容敏感度" value={data2.data["敏感度热度指标"]} />
            <DataCard
              title="用户真实度"
              value={data2.data["用户可性度热度指标"]}
            />
            <DataCard
              title="情感激烈性"
              value={data2.data["情感激烈性热度指标"]}
            />
            <DataCard
              title="观点对立性"
              value={data2.data["观点对立性热度指标"]}
            />
            <DataCard title="总指标" value={data2.data["总热度指标"]} />
          </div>
        </div>
        <div className="w-full h-2xl p-4 bg-white rounded shadow">
          <LineChart />
        </div>
        <div className="flex flex-row w-full p-4 space-x-2 bg-white rounded shadow">
          <div className="bg-gray-200 rounded inline-block">
            <Heatmap data={data1.data} />
          </div>
          <Legend data={data1.data} />
        </div>
        <SensitiveDataOverview />
      </div>
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
        .translate([width / 2 + 50, height / 2 + 100]);

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
  const { eventId, platform, activePlatform, setEventId, setActivePlatform } =
    useEventId();

  const urls = [
    `${process.env.NEXT_PUBLIC_API_URL}/timequota/gettimeseqdetail/?eventid=${eventId}&platform=${activePlatform}`, // 时间热度
    `${process.env.NEXT_PUBLIC_API_URL}/SensitiveDataDetail/?eventid=${eventId}&Platform=${activePlatform}`, // 内容敏感度
    `${process.env.NEXT_PUBLIC_API_URL}/UserDataByDate/?eventid=${eventId}&platform=${activePlatform}`, // 用户真实度
    `${process.env.NEXT_PUBLIC_API_URL}/EmotionDataDetail/?eventid=${eventId}&Platform=${activePlatform}&mode=date`, // 情感激烈性
    `${process.env.NEXT_PUBLIC_API_URL}/OpinionDataDetail/?eventid=${eventId}&Platform=${activePlatform}`, // 观点对立性
    `${process.env.NEXT_PUBLIC_API_URL}/SummaryQuota/?eventid=${eventId}&platform=${activePlatform}`, // 总指标
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

const DataCard = ({ title, value }) => (
  <div className="p-4 bg-gray-100 rounded shadow">
    <h3 className="text-lg font-semibold mb-1">{title}</h3>
    <p className="text-gray-600">{value}</p>
  </div>
);

const SensitiveDataOverview = () => {
  const { eventId, platform, activePlatform, setEventId, setActivePlatform } =
    useEventId();
  const fetcher = (...args) => fetch(...args).then((res) => res.json());

  const { data, error } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/sensitivedataOverviewDetail/?eventid=${eventId}&Platform=${activePlatform}`,
    fetcher
  );

  if (error) return <div>Failed to load</div>;
  if (!data) return <Loading />;

  return (
    <div className="w-full p-6 mx-auto bg-white rounded-xl shadow-md flex flex-col space-x-4">
      <h1 className=" text-3xl font-bold mb-4">敏感词频统计</h1>
      <div>
        {Object.entries(data.data).map(([category, words]) => (
          <div
            key={category}
            className="flex flex-row text-xl font-bold mb-4 flex-wrap"
          >
            <h2>{category}</h2>
            {Object.entries(words).map(([word, count]) => (
              <p key={word} className="text-gray-500 mx-2">
                {word}: {count}
              </p>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
};

const Legend = ({ data }) => {
  // 假设 data 是一个对象，其键是省份名称，值是该省份在轴上的位置（0-100）
  let provinces = Object.keys(data);
  let positions = Object.values(data);

  // 创建一个新的数组，包含省份和位置的信息
  let items = provinces.map((province, index) => ({ province, position: positions[index] }));

  // 按位置对数组进行排序
  items.sort((a, b) => a.position - b.position);

  // 对相邻的省份进行错开
  for (let i = 1; i < items.length; i++) {
    if (items[i].position - items[i - 1].position < 3) { // 如果两个省份的位置相差小于10%，则将它们错开
      items[i].offset = 60; // 偏移量
    }
  }

  // 创建一个颜色渐变字符串
  const gradient = `linear-gradient(to bottom, ${colorScale(0)}, ${colorScale(100)})`; // 修改为从上到下的渐变

  return (
    <div className="relative w-32 h-full opacity-80 rounded-lg shadow-lg overflow-hidden" style={{ backgroundImage: gradient }}>
      {items.map((item, index) => (
        <div
          key={item.province}
          className="absolute left-0 transform -translate-y-1/2"
          style={{ top: `${item.position}%`, left: `${item.offset || 0}px` }} // 修改为顶部偏移
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
