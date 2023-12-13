"use client";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { useEffect, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { useEventId } from "@/components/hooks/EventIdContext";
import useSWR from "swr";
import Loading from "@/components/common/Loading";
import CommentList from "@/components/widgets/list/CommentList";

export default function Page() {
  const [page, setPage] = useState(1);
  const { eventId, setEventId } = useEventId();

  const router = useRouter();

  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data: data1, error: error1 } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/summaryPlatformByEvent`,
    fetcher
  );

  const { data: data2, error: error2 } = useSWR(
    data1
      ? `${process.env.NEXT_PUBLIC_API_URL}/fetchdetailcomment/?id=${"1"}&platform=${"bilibili"}&count=${40}&page=${page}`
      : null,
    fetcher
  );

  if (error1 || error2) return <div>Failed to load</div>;
  if (!data1 || !data2) return <Loading />;
  return (
    <main className="flex h-full flex-col">
      <div className="w-full flex mb-2 items-center justify-between">
        <button
          onClick={null}
          disabled={null}
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
            value={null}
            onChange={null}
          />
          <button
            onClick={null}
            className="rounded-md flex items-center p-3 transition-transform duration-200 ease-in-out transform active:scale-90 hover:shadow-lg hover:bg-gray-400"
          >
            Next
            <ChevronRight />
          </button>
        </div>
      </div>
      {JSON.stringify(data1, null, 2)}

      {JSON.stringify(data1.data[eventId], null, 2)}

      {JSON.stringify(data2, null, 2)}
      <CommentList data={data2.data} />
    </main>
  );
}