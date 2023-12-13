import React from "react";

export default function CommentList({ data }) {
  if (!data || !data.datalist) return null;

  return (
    <div className="space-y-4 overflow-auto">
      {data.datalist.map((item, index) => (
        <div key={index} className="p-4 border rounded shadow">
          <h2 className="text-xl font-bold">{item.Username}</h2>
          <p className="text-gray-700">{item.comment}</p>
          <p className="text-sm text-gray-500">Likes: {item.like}</p>
          <p className="text-sm text-gray-500">Time: {item.time}</p>
        </div>
      ))}
    </div>
  );
}
