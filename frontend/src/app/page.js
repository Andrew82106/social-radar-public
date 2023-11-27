'use client'
import useSWR from 'swr'
import Image from 'next/image'

export default function Page() {
  const fetcher = (...args) => fetch(...args).then(res => res.json())
  const { data, error } = useSWR(`${process.env.NEXT_PUBLIC_API_URL}/fetchcomment/bilibili`, fetcher)

  if (error) return <div>Failed to load</div>
  if (!data) return <div>Loading...</div>

  return (
    <main>

      <p>{JSON.stringify(data, null, 2)}</p>
    </main>
  )
}