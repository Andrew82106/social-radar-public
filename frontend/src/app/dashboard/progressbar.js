import { useEffect, useState } from "react";
import * as Progress from "@radix-ui/react-progress";

const ProgressBar = ({ item }) => {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setProgress((prevProgress) =>
        prevProgress >= item.schedule ? item.schedule : prevProgress + 0.01
      );
    }, 5);
    return () => {
      clearInterval(timer);
    };
  }, [item.schedule]);

  return (
    <Progress.Root
      className="mt-2 mb-4 relative overflow-hidden bg-rose-200 rounded-full w-full h-4"
      style={{
        transform: "translateZ(0)",
      }}
      value={progress}
    >
      <Progress.Indicator
        className="bg-rose-400 w-full h-full transition-transform duration-[660ms] ease-[cubic-bezier(0.65, 0, 0.35, 1)]"
        style={{
          transform: `translateX(-${100 - progress * 100}%)`,
        }}
      />
    </Progress.Root>
  );
};

export default ProgressBar;
