"use client";
import useSWR from "swr";
import Image from "next/image";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import Loading from "@/components/common/Loading";
import ProgressBar from "@/components/widgets/progress/ProgressBar";
import DeleteTasks from "@/components/widgets/dialog/DeleteTaskButton";
import AddTaskButton from "@/components/widgets/dialog/AddTaskButton";

export default function Page() {
  window.addEventListener("popstate", function (event) {
    history.pushState(null, null, document.URL);
  });
  const router = useRouter();
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data, error, mutate } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/eventList`,
    fetcher
  );

  if (error) return <div>Failed to load</div>;
  if (!data) return <Loading />;

  return (
    <main className="flex flex-row justify-between h-full w-full flex-wrap text-black overflow-auto overscroll-none">
      <div>
        <div className="flex flex-row flex-nowrap">
          {Object.entries(data.data.finished).map(([id, keywords]) => (
            <div
              key={id}
              className="flex flex-col justify-between m-4 px-4 py-2 bg-white border border-gray-100 rounded-lg shadow-sm w-64 transform transition-transform duration-200 hover:scale-105 hover:shadow-lg"
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
              <div className="flex flex-row-reverse mt-2 mb-[-10]">
                <DeleteTasks taskId={id} className="h-2" />
              </div>
            </div>
          ))}
        </div>

        <div className="flex flex-row flex-nowrap">
          {Object.entries(data.data.processing).map(([id, item]) => (
            <div
              key={id}
              className="flex flex-col justify-between m-4 p-4 bg-white border border-gray-100 rounded-lg shadow-sm w-64 transform transition-transform duration-200 hover:scale-105 hover:shadow-lg"
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
              <div className="flex flex-row-reverse mt-2 mb-[-10]">
                <DeleteTasks taskId={id} className="h-2" />
              </div>
            </div>
          ))}
        </div>
      </div>
      <div className="flex p-2 h-full ml-4 ">
        <AddTaskButton className="" />
      </div>
    </main>
  );
}
