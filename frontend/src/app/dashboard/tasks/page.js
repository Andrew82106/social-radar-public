"use client";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { useEffect, useState } from "react";
import useSWR from "swr";
import Loading from "@/components/common/Loading";

export default function Page() {
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data, error } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/fetchcomment/bilibili`,
    fetcher
  );

  const [page, setPage] = useState(1);
  const [pagedData, setPagedData] = useState([]);
  const [totalPages, setTotalPages] = useState(0);
  const [searchQuery, setSearchQuery] = useState("");
  const [filteredData, setFilteredData] = useState([]);

  const handleSearch = (event) => {
    setSearchQuery(event.target.value);
    setFilteredData(
      data.data.filter((item) => item.comment.includes(searchQuery))
    );
  };

  useEffect(() => {
    if (data) {
      const perPage = 12;
      const start = (page - 1) * perPage;
      const end = start + perPage;
      setPagedData(data.data.slice(start, end));
      const total = data.length;
      setTotalPages(Math.ceil(total / perPage));
    }
  }, [data, page]);

  const loadPrevious = () => {
    setPage(page - 1);
  };

  const loadNext = () => {
    setPage(page + 1);
  };

  if (error) return <div>Failed to load</div>;
  if (!data) return <Loading />;
  return (
    <main className="flex h-full flex-col">
      <div className="w-full flex mb-2 items-center justify-between">
        <button
          onClick={loadPrevious}
          disabled={page === 1}
          className="rounded-md flex items-center p-3 transition-transform duration-200 ease-in-out transform active:scale-90 hover:shadow-lg hover:bg-gray-400"
        >
          <ChevronLeft />
          Previous
        </button>
        <div className="flex">
          <input
            type="text"
            placeholder="Search..."
            className="border-2 border-gray-300 border-blue-400 rounded-md p-2 mr-5"
            value={searchQuery}
            onChange={handleSearch}
          />
          <button
            onClick={loadNext}
            disabled={page === totalPages}
            className="rounded-md flex items-center p-3 transition-transform duration-200 ease-in-out transform active:scale-90 hover:shadow-lg hover:bg-gray-400"
          >
            Next
            <ChevronRight />
          </button>
        </div>
      </div>
      <div className="flex flex-wrap p-2 justify-center space-x-4 space-y-4 overflow-auto">
        {pagedData.map((item, index) => (
          <div
            key={index}
            className="p-4 bg-white border-2 border-blue-400 rounded-lg shadow-lg w-64"
          >
            <h2 className="text-xl font-bold text-blue-500">{item.username}</h2>
            <p className="text-gray-500">{item.time}</p>
            <p className="mt-2 text-gray-700">{item.comment}</p>
            <p className="mt-2 text-blue-500">Likes: {item.like}</p>
          </div>
        ))}
      </div>
    </main>
  );
}
