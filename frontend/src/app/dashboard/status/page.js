"use client";

import useSWR from "swr";
import Loading from "../../../components/common/Loading";
import { Chart as ChartJS, registerables } from "chart.js";
import { Doughnut, Bar } from "react-chartjs-2";

ChartJS.register(...registerables);

export default function Page() {
  const urls = [
    `${process.env.NEXT_PUBLIC_API_URL}/serverstatus`,
    `${process.env.NEXT_PUBLIC_API_URL}/dataoverview`,
    `${process.env.NEXT_PUBLIC_API_URL}/supportedplatform`,
  ];
  const fetcher = (urls) =>
    Promise.all(urls.map((url) => fetch(url).then((res) => res.json())));
  const { data, error } = useSWR(urls, fetcher);
  if (error) return <div>Failed to load</div>;
  if (!data) return <Loading />;

  const filesystems = data[0].data.filesystems;
  const labels = Object.keys(filesystems);
  const usageData = labels.map((label) =>
    filesystems[label].usage.slice(0, -1)
  );
  const sizeData = labels.map((label) =>
    Number(filesystems[label].size.slice(0, -1))
  );

  const chartData = {
    labels: labels,
    datasets: [
      {
        data: sizeData,
        backgroundColor: [
          "#FF6384",
          "#36A2EB",
          "#FFCE56",
          "#FF6384", // bright pink
          "#36A2EB", // bright blue
          "#FFCE56", // bright yellow
          "#4BC0C0", // turquoise
          "#9966FF", // purple
          "#FF9F40", // orange
          "#E6C200", // gold
          "#5F4B8B", // indigo
          "#E71D36", // red
          "#2EC4B6", // teal
          "#011627", // dark blue
          "#FF1654", // neon pink
          "#F71735", // bright red
          "#C5D86D", // lime green
          "#6B4226", // dark brown
          "#1A535C", // dark cyan
          "#FF6B6B", // salmon
          "#4ECDC4", // light turquoise
          "#1DD3B0", // bright turquoise
          "#FF9F1C", // bright orange
        ],
      },
    ],
  };

  const options = {
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: "right",
        rtl: true,
        labels: {
          usePointStyle: true,
          pointStyle: "circle",
          padding: 10,
        },
      },
      tooltip: {
        enabled: true,
      },
    },
  };

  const barData = {
    labels: Object.keys(data[1].data["用户信息"]),
    datasets: [
      {
        label: "用户信息",
        axis: "y",
        data: Object.values(data[1].data["用户信息"]),
        backgroundColor: "rgba(255, 105, 180, 0.2)", // 粉色
        borderColor: "rgba(255, 105, 180, 1)", // 粉色
        borderWidth: 1,
      },
      {
        label: "评论信息",
        axis: "y",
        data: Object.values(data[1].data["评论信息"]),
        backgroundColor: "rgba(255, 165, 0, 0.2)", // 橙色
        borderColor: "rgba(255, 165, 0, 1)", // 橙色
        borderWidth: 1,
      },
    ],
  };

  return (
    <main className="flex flex-row space-x-2 flag-warp h-full w-full">
      <div className="flex flex-col space-y-2 basis-1/2 h-auto">
        <div className="flex h-60 bg-white shadow-lg rounded-xl p-4 items-center justify-center dark:bg-black">
          <Doughnut data={chartData} options={options} />
        </div>
        <div className="flex flex-col bg-white shadow-lg rounded-xl p-4 justify-center dark:bg-black">
          <Bar data={barData} options={{ indexAxis: "y" }} />
        </div>
        <div className="flex flex-col bg-white shadow-lg rounded-xl p-4 justify-center dark:bg-black">
          {Object.entries(data[2].data).map(([category, platforms]) => (
            <div key={category}>
              <h2 className="text-lg font-bold mb-2">{category}</h2>
              <div className="flex flex-wrap">
                {platforms.map((platform) => (
                  <div
                    key={platform}
                    className="mb-2 mx-1 px-4 py-2 bg-rose-200 text-rose-400 font-serif rounded-md"
                  >
                    {platform}
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>

      <div className="flex flex-col space-y-2 basis-1/2 h-auto">
        <div className="col-span-2 flex flex-col bg-white shadow-lg rounded-xl p-4 justify-center dark:bg-black">
          {labels.map((label) => {
            const used = Number(filesystems[label].used);
            const free = Number(filesystems[label].free);
            const total = used + free;

            return (
              <div className="flex items-center justify-between" key={label}>
                <label className="text-sm">{label}</label>
                <div className="h-2 w-48 bg-gray-200 rounded-full overflow-hidden">
                  <div
                    style={{ width: `${(used / total) * 100}%` }}
                    className="h-full bg-orange-300"
                  ></div>
                </div>
              </div>
            );
          })}
        </div>
        <div className="col-span-2 flex flex-col bg-white shadow-lg rounded-xl p-4 justify-center dark:bg-black">
          {data[0].data.top.split("\n").map((line, index) => {
            const parts = line.split(":");
            return (
              <p key={index} className="text-base">
                <strong>{parts[0]}</strong>:{parts.slice(1).join(":")}
                {line}
              </p>
            );
          })}
        </div>
      </div>
    </main>
  );
}
