"use client";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { CheckCircle, Settings, BarChartBig } from "lucide-react";

export default function DashboardLayout({ children }) {
  const pathname = usePathname();

  return (
    <div className="flex h-screen bg-gray-200">
      <div className="p-6 w-64 bg-white">
        {pathname === "/dashboard" && (
          <ul className="text-lg font-semibold font-sans space-y-4 text-black">
            <li className={pathname == "/dashboard" ? "text-blue-500 " : ""}>
              <Link href="/dashboard">
                <div className="flex items-center space-x-2">
                  <CheckCircle size={24} />
                  <span>Tasks</span>
                </div>
              </Link>
            </li>
            <li
              className={
                pathname == "/dashboard/status" ? "text-blue-500" : ""
              }
            >
              <Link href="/dashboard/status">
                <div className="flex items-center space-x-2">
                  <BarChartBig size={24} />
                  <span>Status</span>
                </div>
              </Link>
            </li>

            <li
              className={
                pathname == "/dashboard/settings" ? "text-blue-500" : ""
              }
            >
              <Link href="/dashboard/settings">
                <div className="flex items-center space-x-2">
                  <Settings size={24} />
                  <span>Settings</span>
                </div>
              </Link>
            </li>
          </ul>
        )}
        {pathname === "/dashboard/tasks" && <></>}
      </div>
      <div className="flex-grow p-6">{children}</div>
    </div>
  );
}
