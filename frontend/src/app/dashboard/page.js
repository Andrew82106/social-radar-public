"use client";
import useSWR from "swr";
import Image from "next/image";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import Loading from "./loading";
import * as Progress from "@radix-ui/react-progress";

export default function Page() {
  const router = useRouter();
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data, error } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/eventList`,
    fetcher
  );

  if (error) return <div>Failed to load</div>;
  if (!data) return <Loading />;

  return (
    <main className="flex flex-col text-black overflow-auto overscroll-none">
      <div className="flex flex-row flex-nowrap">
        {Object.entries(data.data.finished).map(([id, keywords]) => (
          <div
            key={id}
            className="flex flex-col justify-between m-4 p-4 bg-white border border-gray-100 rounded-lg shadow-sm w-64 transform transition-transform duration-200 hover:scale-105 hover:shadow-lg"
            onClick={() => router.push(`/dashboard/tasks?id=${id}`)}
          >
            <ul className="mt-2 flex flex-wrap">
              {keywords.map((keyword, index) => (
                <li
                  key={index}
                  className="mr-2 mb-2 bg-blue-500 text-white rounded-full px-2 py-1 text-sm hover:bg-blue-600 transition-colors duration-200"
                >
                  {keyword}
                </li>
              ))}
            </ul>

            <span className="bg-green-200 text-sm text-green-500 rounded pl-2 p-1">
              Complete
            </span>
          </div>
        ))}
      </div>
      <div className="flex flex-row flex-nowrap">
        {Object.entries(data.data.processing).map(([id, item]) => (
          <div
            key={id}
            className="flex flex-col justify-between m-4 p-4 bg-white border border-gray-100 rounded-lg shadow-sm w-64 transform transition-transform duration-200 hover:scale-105 hover:shadow-lg"
            onClick={() => router.push(`/dashboard/tasks?id=${id}`)}
          >
            <ul className="mt-2 flex flex-wrap">
              {item.keyword.map((keyword, index) => (
                <li
                  key={index}
                  className="mr-2 mb-2 bg-blue-500 text-white rounded-full px-2 py-1 text-sm hover:bg-blue-600 transition-colors duration-200"
                >
                  {keyword}
                </li>
              ))}
            </ul>
            <ProgressBar item={item} />
            <span className="bg-orange-200 text-sm text-orange-500 rounded pl-2 p-1">
              Processing
            </span>
          </div>
        ))}
      </div>
    </main>
  );
}

function ProgressBar({ item }) {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setProgress((prevProgress) =>
        prevProgress >= item.schedule ? item.schedule : prevProgress + 0.01
      );
    }, 5);
    return () => {
      clearInterval(timer);
    };
  }, [item.schedule]);

  return (
    <Progress.Root
      className="mt-2 mb-4 relative overflow-hidden bg-rose-200 rounded-full w-full h-4"
      style={{
        transform: "translateZ(0)",
      }}
      value={progress}
    >
      <Progress.Indicator
        className="bg-rose-400 w-full h-full transition-transform duration-[660ms] ease-[cubic-bezier(0.65, 0, 0.35, 1)]"
        style={{
          transform: `translateX(-${100 - progress * 100}%)`,
        }}
      />
    </Progress.Root>
  );
}
