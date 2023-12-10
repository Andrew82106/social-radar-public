"use client";
import React, { useEffect, useRef } from "react";
import useSWR from "swr";
import { useEventId } from "@/components/hooks/EventIdContext";
import * as d3 from "d3";
import Loading from "@/components/common/Loading";

export default function Page() {
  const { eventId, setEventId } = useEventId();
  const fetcher = (...args) => fetch(...args).then((res) => res.json());
  const { data: data1, error: error1 } = useSWR(
    `${process.env.NEXT_PUBLIC_API_URL}/summaryLocationall/?eventID=${eventId}`,
    fetcher
  );
  if (error1) return <div>Failed to load</div>;
  if (!data1) return <Loading />;
  return (
    <main className="w-full h-full">
      <Heatmap data={data1.data} />
    </main>
  );
}

const Heatmap = ({ data }) => {
  const ref = useRef();

  useEffect(() => {
    d3.json("/china_simplify.json").then((topology) => {
      console.log(JSON.stringify(topology));
      const geoData = topology;

      const width = 1000;
      const height = 800;

      const projection = d3
        .geoMercator()
        .center([107, 31])
        .scale(750)
        .translate([width / 2, height / 2 + 50]);

      const path = d3.geoPath().projection(projection);

      const color = d3
        .scaleQuantize()
        .domain([0, d3.max(Object.values(data))])
        .range(d3.schemeBlues[9]);

      const svg = d3
        .select(ref.current)
        .attr("width", width)
        .attr("height", height);

      svg
        .selectAll("path")
        .data(geoData.features)
        .enter()
        .append("path")
        .attr("d", path)
        .attr("fill", (d) => color(data[d.properties.name]))
        .attr("stroke", "#fff")
        .attr("stroke-width", 1);
    });
  }, []);

  return (
    <main className="w-full h-full">
      <svg ref={ref} />
    </main>
  );
};
