'use client'
import useSWR from 'swr'
import Image from 'next/image'
import { useState, useEffect } from 'react';

export default function Page() {
  const fetcher = (...args) => fetch(...args).then(res => res.json())
  const { data, error } = useSWR(`${process.env.NEXT_PUBLIC_API_URL}/fetchcomment/bilibili`, fetcher)

  const [page, setPage] = useState(1);
  const [pagedData, setPagedData] = useState([]);

  useEffect(() => {
    if (data) {
      const perPage = 10;
      const start = (page - 1) * perPage;
      const end = start + perPage;
      setPagedData(data.data.slice(start, end));
    }
  }, [data, page]);

  const loadMore = () => {
    setPage(page + 1);
  };

  if (error) return <div>Failed to load</div>
  if (!data) return <div>Loading...</div>
  return (
    <main className="p-4 flex flex-wrap items-stretch justify-around space-x-4 space-y-4 overflow-auto overscroll-none h-screen">
      {pagedData.map((item, index) => (
        <div key={index} className="p-4 bg-blue-400 border rounded shadow w-64">
          <h2 className="text-xl font-bold">{item.username}</h2>
          <p className="text-gray-500">{item.time}</p>
          <p className="mt-2">{item.comment}</p>
          <p className="mt-2 text-blue-500">Likes: {item.like}</p>
        </div>
      ))}
      <button onClick={loadMore}>Load more</button>
    </main>
  )
}