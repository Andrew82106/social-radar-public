import { useState } from "react";
import useSWR from "swr";
import * as Dialog from "@radix-ui/react-dialog";
import { X, Plus } from "lucide-react";
import PlatformSelect from "@/components/widgets/select/PlatformSelect";

const AddTaskButton = () => {
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data, error } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/supportedplatform`,
    fetcher
  );
  const [inputValue, setInputValue] = useState("");

  const handleAddEvent = async (event) => {
    event.preventDefault();

    const res = await fetch(`http://127.0.0.1:5000/addEvent/${inputValue}`, {
      method: "GET",
    });
    if (res.ok) {
      window.location.reload();
    }
  };

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
        <Dialog.Content className="data-[state=open]:animate-contentShow fixed top-[50%] left-[50%] max-h-[85vh] w-[90vw] max-w-[450px] translate-x-[-50%] translate-y-[-50%] rounded-[6px] bg-white p-[25px] shadow-[hsl(206_22%_7%_/_35%)_0px_10px_38px_-10px,_hsl(206_22%_7%_/_20%)_0px_10px_20px_-15px] focus:outline-none dark:bg-black">
          <Dialog.Title className="text-mauve12 m-0 text-[17px] font-medium">
            添加新任务
          </Dialog.Title>
          <Dialog.Description className="text-mauve11 mt-[10px] mb-5 text-[15px] leading-normal">
            请使用"|"分隔想要分析的关键词，例如"关键词1|关键词2|关键词3"，并选择想要分析的平台
          </Dialog.Description>
          <fieldset className="mb-[15px] flex flex-row items-center justify-between">
            <label
              className="text-violet11 text-right text-base"
              htmlFor="name"
            >
              关键词
            </label>
            <input
              className="text-violet11 shadow-violet7 focus:shadow-violet8 inline-flex h-[35px] w-80 items-center justify-center rounded-[4px] px-[10px] text-[15px] leading-none shadow-[0_0_0_1px] outline-none focus:shadow-[0_0_0_2px] dark:text-black"
              id="name"
              onChange={(e) => setInputValue(e.target.value)}
              value={inputValue}
            />
          </fieldset>
          <fieldset className="mb-[15px] flex flex-row items-center justify-between">
            <label
              className="text-violet11 text-right text-base"
              htmlFor="Platform"
            >
              平台
            </label>
            <div className="flex flex-col w-80">
              <PlatformSelect className="w-80 dark:text-black" data={data.data} />
            </div>
          </fieldset>
          <div className="mt-[25px] flex justify-end">
            <Dialog.Close asChild>
              <button
                className="bg-green4 text-green11 hover:bg-green5 focus:shadow-green7 inline-flex h-[35px] items-center justify-center rounded-[4px] px-[15px] font-medium leading-none focus:shadow-[0_0_0_2px] focus:outline-none"
                onClick={handleAddEvent}
              >
                提交
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

export default AddTaskButton;
