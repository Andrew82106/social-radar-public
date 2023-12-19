"use client";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { useEffect, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { useEventId } from "@/components/hooks/EventIdContext";
import useSWR from "swr";
import Loading from "@/components/common/Loading";
import CommentList from "@/components/widgets/list/CommentList";
import PlatformSelect from "@/components/widgets/select/PlatformSelect";

export default function Page() {
  const [searchTerm, setSearchTerm] = useState("");
  const [newSearchTerm, setNewSearchTerm] = useState("");
  const [comments, setComments] = useState([]);
  const [maximumPage, setMaximumPage] = useState(1);
  const [page, setPage] = useState(1);
  const [inputValue, setInputValue] = useState(page);
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

  const handleSubmit = (event) => {
    event.preventDefault();
    let finalPage = inputValue;

    if (inputValue < 1) {
      finalPage = 1;
    } else if (inputValue > maximumPage) {
      finalPage = maximumPage;
    }
  
    setPage(finalPage);
    setInputValue(finalPage);
  };

  const handleOnBlur = (event) => {
    event.preventDefault();
    let finalPage = inputValue;

    if (inputValue < 1) {
      finalPage = 1;
    } else if (inputValue > maximumPage) {
      finalPage = maximumPage;
    }
  
    setPage(finalPage);
    setInputValue(finalPage);
  };


  useEffect(() => {
    if (newSearchTerm == "" && data1 && data1.data && data1.data.maximumPage) {
      setMaximumPage(data1.data.maximumPage);
    }
    if (newSearchTerm !== "" && data2 && data2.data && data2.data.maximumPage) {
      setMaximumPage(data2.data.maximumPage);
    }
  }, [data1, data2]);

  useEffect(() => {
    setPage(1);
    setInputValue(1);
    setSearchTerm("");
    setNewSearchTerm("");
  }, [activePlatform]);

  if (error2) return <div>Failed to load</div>;
  return (
    <main className="flex h-full flex-col">
      <div className="w-full flex mb-2 items-center justify-between bg-gray-100 rounded">
        <button
          onClick={() => setPage((prevPage) => Math.max(prevPage - 1, 1))}
          disabled={page === 1}
          className="rounded-md flex items-center p-3 transition-transform duration-200 ease-in-out transform active:scale-90 hover:shadow-lg hover:bg-gray-400"
        >
          <ChevronLeft />
          上一页
        </button>
        <div className="flex flex-row space-x-2">
          <div>页面</div>
          <form onSubmit={handleSubmit}>
            <input
              type="number"
              value={inputValue}
              onBlur={handleOnBlur}
              onChange={(e) => {
                const newPage = e.target.value === "" ? "" : Number(e.target.value);
                setInputValue(newPage);
              }}
              className="w-12 bg-gray-100"
            />
          </form>
          <div>/ {maximumPage}</div>
        </div>
        <PlatformSelect />
        <div className="flex">
          <input
            type="text"
            placeholder="关键词"
            className="border-2 border-gray-300 border-blue-400 rounded-md p-2 mr-5"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <button
            onClick={() => {
              setNewSearchTerm(searchTerm);
              setPage(1);
              setInputValue(1);
            }}
          >
            搜索
          </button>
          <button
            onClick={() => {
              if (page < maximumPage) {
                setPage((prevPage) => prevPage + 1);
              }
            }}
            disabled={page === maximumPage}
            className="rounded-md flex items-center p-3 transition-transform duration-200 ease-in-out transform active:scale-90 hover:shadow-lg hover:bg-gray-400"
          >
            下一页
            <ChevronRight />
          </button>
        </div>
      </div>
      {!data1 || (newSearchTerm && !data2) ? (
        <Loading />
      ) : (
        <CommentList
          data={newSearchTerm == "" ? data1.data : data2.data}
          className="max-w-full"
        />
      )}
    </main>
  );
}
