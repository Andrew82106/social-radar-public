"use client";
import Link from "next/link";
import { useEventId } from "@/components/hooks/EventIdContext";
import { usePathname, useRouter } from "next/navigation";
import {
  CheckCircle,
  Settings,
  BarChartBig,
  Database,
  LineChart,
  ArrowLeft,
} from "lucide-react";
import { EventIdProvider } from "@/components/hooks/EventIdContext";

function DashboardLink({ href, children, isActive }) {
  return (
    <li
      className={`${
        isActive ? "text-blue-500" : ""
      } transition duration-300 ease-in-out transform-gpu hover:scale-105`}
    >
      <Link href={href}>
        <div className="flex items-center space-x-2">{children}</div>
      </Link>
    </li>
  );
}

export default function DashboardLayout({ children }) {
  const pathname = usePathname();
  const layoutdashboard = ["/dashboard", "/dashboard/status"];
  const layouttasks = ["/dashboard/tasks"];
  const isPathInLayoutTasks = pathname.startsWith("/dashboard/tasks");

  return (
    <EventIdProvider>
      <div className="flex h-screen bg-gray-200 dark:bg-gray-700">
        <div className="grow-0 p-6 bg-white dark:bg-black whitespace-nowrap">
          {!isPathInLayoutTasks ? (
            <ul className="text-lg font-semibold font-sans space-y-4 text-black dark:text-white">
              <DashboardLink
                href="/dashboard"
                isActive={pathname == "/dashboard"}
              >
                <CheckCircle size={24} />
                <span>任务</span>
              </DashboardLink>
              <DashboardLink
                href="/dashboard/status"
                isActive={pathname == "/dashboard/status"}
              >
                <BarChartBig size={24} />
                <span>系统状态</span>
              </DashboardLink>
              <DashboardLink
                href="/dashboard/settings"
                isActive={pathname == "/dashboard/settings"}
              >
                <Settings size={24} />
                <span>设置</span>
              </DashboardLink>
            </ul>
          ) : (
            <ul className="text-lg font-semibold font-sans space-y-4 text-black dark:text-white">
              <DashboardLink
                href="/dashboard"
                isActive={false}
              >
                <ArrowLeft size={24} />
                <span>返回</span>
              </DashboardLink>
              <DashboardLink
                href="/dashboard/tasks"
                isActive={pathname == "/dashboard/tasks"}
              >
                <CheckCircle size={24} />
                <span>事件概览</span>
              </DashboardLink>
              <DashboardLink
                href="/dashboard/tasks/analysis"
                isActive={pathname == "/dashboard/tasks/analysis"}
              >
                <LineChart size={24} />
                <span>平台分析</span>
              </DashboardLink>
              <DashboardLink
                href="/dashboard/tasks/data"
                isActive={pathname == "/dashboard/tasks/data"}
              >
                <Database size={24} />
                <span>数据</span>
              </DashboardLink>
            </ul>
          )}
        </div>
        <div className="p-4 w-full h-screen">{children}</div>
      </div>
    </EventIdProvider>
  );
}
