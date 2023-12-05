"use client";

import useSWR from "swr";
import Loading from "../loading";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Doughnut } from "react-chartjs-2";

ChartJS.register(ArcElement, Tooltip, Legend);

export default function Page() {
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data, error } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/serverstatus`,
    fetcher
  );

  if (!data) return <Loading />;

  const filesystems = data.data.filesystems;
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

  return (
    <main className="flex flex-row space-x-2 flag-warp h-full w-full">
      <div className="flex flex-col space-y-2 basis-1/2 h-auto">
        <div className="flex h-60 bg-white shadow-lg rounded-xl p-4 items-center justify-center">
          <Doughnut data={chartData} options={options} />
        </div>
      </div>
      <div className="flex flex-col space-y-2 basis-1/2 h-auto">
        <div className="col-span-2 flex flex-col bg-white shadow-lg rounded-xl p-4 justify-center">
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
        <div className="col-span-2 flex flex-col bg-white shadow-lg rounded-xl p-4 justify-center">
          {data.data.top.split("\n").map((line, index) => {
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