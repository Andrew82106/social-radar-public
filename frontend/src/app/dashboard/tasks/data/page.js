"use client";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { useEffect, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { useEventId } from "@/components/hooks/EventIdContext";
import useSWR from "swr";
import Loading from "@/components/common/Loading";
import CommentList from "@/components/widgets/list/CommentList";

export default function Page() {
  const [searchTerm, setSearchTerm] = useState("");
  const [newSearchTerm, setNewSearchTerm] = useState("");
  const [comments, setComments] = useState([]);
  const [page, setPage] = useState(1);
  const { eventId, platform, setEventId, activePlatform } = useEventId();

  const router = useRouter();

  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data: data2, error: error2 } = useSWR(
    newSearchTerm !== ""
      ? `${process.env.NEXT_PUBLIC_API_URL}/searcheventdetail/?eventid=${eventId}&platform=${activePlatform}&keyword=${newSearchTerm}&count=40&page=${page}`
      : null,
    fetcher
  );

  const { data: data1, error: error1 } = useSWR(
    `${
      process.env.NEXT_PUBLIC_API_URL
    }/fetchdetailcomment/?id=${eventId}&platform=${activePlatform}&count=${40}&page=${page}`,
    fetcher
  );

  if (error1 || error2) return <div>Failed to load</div>;
  if (!data1 || (newSearchTerm && !data2)) return <Loading />;
  return (
    <main className="flex h-full flex-col">
      <div className="w-full flex mb-2 items-center justify-between">
        <button
          onClick={() => setPage((prevPage) => Math.max(prevPage - 1, 1))}
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
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <button
            onClick={() => {
              setNewSearchTerm(searchTerm);
              setPage(1);
            }}
          >
            搜索
          </button>
          <button
            onClick={() => setPage((prevPage) => prevPage + 1)}
            className="rounded-md flex items-center p-3 transition-transform duration-200 ease-in-out transform active:scale-90 hover:shadow-lg hover:bg-gray-400"
          >
            Next
            <ChevronRight />
          </button>
        </div>
      </div>
      <CommentList data={newSearchTerm == "" ? data1.data : data2.data} />
    </main>
  );
}
