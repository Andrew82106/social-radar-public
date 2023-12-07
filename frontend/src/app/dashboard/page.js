"use client";
import useSWR from "swr";
import Image from "next/image";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import Loading from "./loading";
import * as Dialog from "@radix-ui/react-dialog";
import { X, Plus } from "lucide-react";
import PlatformSelect from "./platformselect";
import ProgressBar from "./progressbar";
import DeleteTasks from "../../components/widgets/dialog/DeleteTasksButton";

export default function Page() {
  const router = useRouter();
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data, error, mutate } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/eventList`,
    fetcher
  );

  if (error) return <div>Failed to load</div>;
  if (!data) return <Loading />;

  return (
    <main className="flex flex-row justify-between flex-wrap text-black overflow-auto overscroll-none">
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
                  <DeleteTasks className="h-2" />
                </div>
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
      </div>
      <div className="flex p-2 h-full ml-4">
        <DialogDemo className="" />
      </div>
    </main>
  );
}

const DialogDemo = () => {
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data, error } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/supportedplatform`,
    fetcher
  );

  if (error) return <div>Failed to load</div>;
  if (!data) return <div>No data</div>;

  return (
    <Dialog.Root>
      <Dialog.Trigger asChild>
        <button className="text-violet11 shadow-blackA4 hover:bg-mauve3 inline-flex h-[35px] items-center justify-center rounded-lg bg-white px-[15px] font-medium leading-none shadow-[0_2px_10px] focus:shadow-[0_0_0_2px] focus:shadow-black focus:outline-none">
          <Plus />
        </button>
      </Dialog.Trigger>
      <Dialog.Portal>
        <Dialog.Overlay className="bg-blackA6 data-[state=open]:animate-overlayShow fixed inset-0" />
        <Dialog.Content className="data-[state=open]:animate-contentShow fixed top-[50%] left-[50%] max-h-[85vh] w-[90vw] max-w-[450px] translate-x-[-50%] translate-y-[-50%] rounded-[6px] bg-white p-[25px] shadow-[hsl(206_22%_7%_/_35%)_0px_10px_38px_-10px,_hsl(206_22%_7%_/_20%)_0px_10px_20px_-15px] focus:outline-none">
          <Dialog.Title className="text-mauve12 m-0 text-[17px] font-medium">
            Add a new task
          </Dialog.Title>
          <Dialog.Description className="text-mauve11 mt-[10px] mb-5 text-[15px] leading-normal">
            Make changes to your profile here. Click save when you're done.
          </Dialog.Description>
          <fieldset className="mb-[15px] flex items-center gap-5">
            <label
              className="text-violet11 text-right text-base"
              htmlFor="name"
            >
              Keywords
            </label>
            <input
              className="text-violet11 shadow-violet7 focus:shadow-violet8 inline-flex h-[35px] w-full flex-1 items-center justify-center rounded-[4px] px-[10px] text-[15px] leading-none shadow-[0_0_0_1px] outline-none focus:shadow-[0_0_0_2px]"
              id="name"
            />
          </fieldset>
          <fieldset className="mb-[15px] flex items-start gap-5">
            <label
              className="text-violet11 text-right text-base"
              htmlFor="Platform"
            >
              Platform
            </label>
            <div className="flex flex-col space-y-2 w-full">
              <PlatformSelect className="" data={data.data} />
            </div>
          </fieldset>
          <div className="mt-[25px] flex justify-end">
            <Dialog.Close asChild>
              <button className="bg-green4 text-green11 hover:bg-green5 focus:shadow-green7 inline-flex h-[35px] items-center justify-center rounded-[4px] px-[15px] font-medium leading-none focus:shadow-[0_0_0_2px] focus:outline-none">
                Save changes
              </button>
            </Dialog.Close>
          </div>
          <Dialog.Close asChild>
            <button
              className="text-violet11 hover:bg-violet4 focus:shadow-violet7 absolute top-[10px] right-[10px] inline-flex h-[25px] w-[25px] appearance-none items-center justify-center rounded-full focus:shadow-[0_0_0_2px] focus:outline-none"
              aria-label="Close"
            >
              <X />
            </button>
          </Dialog.Close>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
};
