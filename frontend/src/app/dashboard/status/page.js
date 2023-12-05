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
    <main className="grid grid-cols-4 grid-rows-4 gap-2 flag-warp h-full w-full">
      <div className="col-span-2 flex bg-white shadow-lg rounded-xl p-4 items-center justify-center">
        <Doughnut data={chartData} options={options} />
      </div>
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
    </main>
  );
}

const data1 = {
  filesystems: {
    "/System/Volumes/Data": {
      free: "120835000",
      size: "98%",
      usage: "4%",
      used: "4564971",
    },
    "/System/Volumes/Hardware": {
      free: "4905640",
      size: "1%",
      usage: "0%",
      used: "53",
    },
    "/System/Volumes/Preboot": {
      free: "120835000",
      size: "28%",
      usage: "0%",
      used: "840",
    },
    "/System/Volumes/Update": {
      free: "120835000",
      size: "1%",
      usage: "0%",
      used: "43",
    },
    "/System/Volumes/VM": {
      free: "120835000",
      size: "54%",
      usage: "0%",
      used: "13",
    },
    "/System/Volumes/iSCPreboot": {
      free: "4905640",
      size: "2%",
      usage: "0%",
      used: "38",
    },
    "/Users/chriswhite/OrbStack": {
      free: "672079",
      size: "1%",
      usage: "0%",
      used: "38",
    },
    "/private/tmp/KSInstallAction.KZr3UN1Wnz/m": {
      free: "4294967248",
      size: "100%",
      usage: "0%",
      used: "31",
    },
  },
  top: "Processes: 571 total, 14 running, 557 sleeping, 4568 threads \n2023/12/05 12:47:58\nLoad Avg: 12.67, 9.92, 8.44 \nCPU usage: 22.42% user, 33.99% sys, 43.58% idle \nSharedLibs: 388M resident, 81M data, 27M linkedit.\nMemRegions: 1029082 total, 3034M resident, 139M private, 2400M shared.\nPhysMem: 15G used (4076M wired, 6109M compressor), 73M unused.\nVM: 301T vsize, 4283M framework vsize, 268760837(0) swapins, 278474706(0) swapouts.\nNetworks: packets: 166812665/190G in, 78005225/51G out.\nDisks: 429099490/7853G read, 159883229/5434G written.",
  uptime: "12:47 up 32 days, 2:39, 10 users, load averages: 12.67 9.92 8.44",
};
