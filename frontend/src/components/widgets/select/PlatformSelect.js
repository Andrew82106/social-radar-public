import React from "react";
import * as Select from "@radix-ui/react-select";
import classnames from "classnames";
import {
  CheckIcon,
  ChevronDownIcon,
  ChevronUpIcon,
} from "@radix-ui/react-icons";
import { useEventId } from "@/components/hooks/EventIdContext";
import useSWR from "swr";
import Loading from "@/components/common/Loading";

const PlatformSelect = () => {
  const { eventId, platform, activePlatform, setEventId, setActivePlatform } =
    useEventId();
  const data = platform;

  return (
    <div className="flex">
      {data.map((platform, index) => (
        <button
          key={index}
          value={platform}
          onClick={() => setActivePlatform(platform)}
          className={classnames(
            "p-3", // padding
            "m-2", // margin
            "rounded-lg", // large rounded corners
            "text-base", // base text size
            "font-semibold", // semi-bold font weight
            "transition-colors", // smooth color transitions
            "duration-200", // transition duration
            "ease-in-out", // transition timing function
            "hover:bg-gray-400", // hover background color
            "hover:text-white", // hover text color
            {
              "bg-gray-300 text-black": activePlatform === platform,
              "bg-gray-200 text-gray-500": activePlatform !== platform,
            }
          )}
        >
          {platform}
        </button>
      ))}
    </div>
  );
};

const SelectItem = React.forwardRef(
  ({ children, className, ...props }, forwardedRef) => {
    return (
      <Select.Item
        className={classnames(
          "text-[13px] leading-none text-violet11 rounded-[3px] flex items-center h-[25px] pr-[35px] pl-[25px] relative select-none data-[disabled]:text-mauve8 data-[disabled]:pointer-events-none data-[highlighted]:outline-none data-[highlighted]:bg-violet9 data-[highlighted]:text-violet1",
          className
        )}
        {...props}
        ref={forwardedRef}
      >
        <Select.ItemText>{children}</Select.ItemText>
        <Select.ItemIndicator className="absolute left-0 w-[25px] inline-flex items-center justify-center">
          <CheckIcon />
        </Select.ItemIndicator>
      </Select.Item>
    );
  }
);

export default PlatformSelect;
