export default function Loading() {
  return (
    <main className="flex w-full h-full">
      <div className="flex w-full items-center justify-center">
        <svg
          viewBox="0 0 25 25"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          className="animate-spin h-16 w-16 mr-5"
        >
          <path
            d="M4.5 12.5C4.5 16.9183 8.08172 20.5 12.5 20.5C16.9183 20.5 20.5 16.9183 20.5 12.5C20.5 8.08172 16.9183 4.5 12.5 4.5"
            stroke="#121923"
            stroke-width="1.2"
          />
        </svg>
        <p className="font-mono text-3xl">加载中...</p>
      </div>
    </main>
  );
}
