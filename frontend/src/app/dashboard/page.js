"use client";
import useSWR from "swr";
import Image from "next/image";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";

export default function Page() {
  const router = useRouter();
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data, error } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/eventList`,
    fetcher
  );

  if (error) return <div>Failed to load</div>;
  return (
    <main className="p-4 flex text-black overflow-auto overscroll-none">
      <div>
        <h2>Finished</h2>
        {data ? (
          Object.entries(data.data.finished).map(([id, keywords]) => (
            <div
              key={id}
              className="p-4 bg-white border rounded shadow w-64"
              onClick={() => router.push(`/dashboard/tasks?id=${id}`)}
            >
              <h3 className="text-xl font-bold">ID: {id}</h3>
              <ul className="flex flex-wrap">
                {keywords.map((keyword, index) => (
                  <li
                    key={index}
                    className="mr-2 mb-2 bg-blue-500 text-white rounded-full px-2 py-1 text-sm"
                  >
                    {keyword}
                  </li>
                ))}
              </ul>
            </div>
          ))
        ) : (
          <div className="p-4 bg-white border rounded shadow w-64 animate-pulse"></div>
        )}
      </div>
      <div>
        <h2>Processing</h2>
        {data ? (
          Object.entries(data.data.processing).map(([id, item]) => (
            <div
              key={id}
              className="p-4 bg-gray-400 border rounded shadow w-64"
              onClick={() => router.push(`/dashboard/tasks?id=${id}`)}
            >
              <h3 className="text-xl font-bold">ID: {id}</h3>
              <p>Schedule: {item.schedule}</p>
              <p>Start time: {item["start time"]}</p>
              <ul className="flex flex-wrap">
                {item.keyword.map((keyword, index) => (
                  <li
                    key={index}
                    className="mr-2 mb-2 bg-blue-500 text-white rounded-full px-2 py-1 text-sm"
                  >
                    {keyword}
                  </li>
                ))}
              </ul>
            </div>
          ))
        ) : (
          <div className="p-4 bg-white border rounded shadow w-64 animate-pulse"></div>
        )}
      </div>
    </main>
  );
}
