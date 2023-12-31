import React from "react";
import * as AlertDialog from "@radix-ui/react-alert-dialog";
import { Delete, Trash2 } from "lucide-react";

const DeleteTaskButton = ({ taskId }) => {
  const handleDelete = async () => {
    const res = await fetch(`http://127.0.0.1:5000/delEvent/${taskId}`, {
      method: "GET",
    });
    if (res.ok) {
      window.location.reload();
    }
  };

  return (
    <AlertDialog.Root>
      <AlertDialog.Trigger asChild onClick={(event) => event.stopPropagation()}>
        <button className="text-violet11 py-1 hover:bg-mauve3 shadow-blackA4 inline-flex items-center justify-center rounded-[4px] bg-red-400 text-white px-[15px] font-medium leading-none shadow-[0_2px_10px] outline-none focus:shadow-[0_0_0_2px] focus:shadow-red-200   ">
          <Trash2 size={20} />
        </button>
      </AlertDialog.Trigger>
      <AlertDialog.Portal>
        <AlertDialog.Overlay className="bg-blackA6 data-[state=open]:animate-overlayShow fixed inset-0" />
        <AlertDialog.Content className="data-[state=open]:animate-contentShow fixed top-[50%] left-[50%] max-h-[85vh] w-[90vw] max-w-[500px] translate-x-[-50%] translate-y-[-50%] rounded-[6px] bg-white p-[25px] shadow-[hsl(206_22%_7%_/_35%)_0px_10px_38px_-10px,_hsl(206_22%_7%_/_20%)_0px_10px_20px_-15px] focus:outline-none dark:bg-black">
          <AlertDialog.Title className="text-mauve12 m-0 text-[17px] font-medium">
            删除任务
          </AlertDialog.Title>
          <AlertDialog.Description className="text-mauve11 mt-4 mb-5 text-[15px] leading-normal">
            这个任务将会被永久删除，您确定吗
          </AlertDialog.Description>
          <div className="flex justify-end gap-[25px]">
            <AlertDialog.Cancel asChild onClick={(event) => event.stopPropagation()}>
              <button className="text-mauve11 bg-mauve4 hover:bg-mauve5 focus:shadow-mauve7 inline-flex h-[35px] items-center justify-center rounded-[4px] px-[15px] font-medium leading-none outline-none focus:shadow-[0_0_0_2px]">
                取消
              </button>
            </AlertDialog.Cancel>
            <AlertDialog.Action asChild onClick={(event) => event.stopPropagation()}>
              <button
                onClick={handleDelete}
                className="text-red11 bg-red4 hover:bg-red5 focus:shadow-red7 inline-flex h-[35px] items-center justify-center rounded-[4px] px-[15px] font-medium leading-none outline-none focus:shadow-[0_0_0_2px]"
              >
                是的，删除任务
              </button>
            </AlertDialog.Action>
          </div>
        </AlertDialog.Content>
      </AlertDialog.Portal>
    </AlertDialog.Root>
  );
};

export default DeleteTaskButton;
