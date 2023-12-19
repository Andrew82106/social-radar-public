import React, { useState } from "react";
import useSWR from "swr";
import { useEventId } from "@/components/hooks/EventIdContext";
import Loading from "@/components/common/Loading";

const fetcher = (url) => fetch(url).then((res) => res.json());

export default function CommentList({ data }) {
  const { eventId, platform, activePlatform, setEventId, setActivePlatform } =
    useEventId();
  const [selectedUserId, setSelectedUserId] = useState(null);
  const [selectedUsername, setSelectedUsername] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const { data: userInfo } = useSWR(
    selectedUserId
      ? `${process.env.NEXT_PUBLIC_API_URL}/fetchdetailuserinfo/?id=${selectedUserId}&platform=${activePlatform}`
      : null,
    fetcher
  );
  const { data: userQuota } = useSWR(
    selectedUserId
      ? `${process.env.NEXT_PUBLIC_API_URL}/fetchuserquota/?id=${selectedUserId}&platform=${activePlatform}`
      : null,
    fetcher
  );

  const { data: searchResults } = useSWR(
    selectedUsername
      ? `${process.env.NEXT_PUBLIC_API_URL}/searchuser/${selectedUsername}`
      : null,
    fetcher
  );

  const openModal = (username) => {
    setIsModalOpen(true);
    setSelectedUsername(username);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  if (!data || !data.datalist) return null;

  return (
    <div className="space-y-4 overflow-auto bg-gray-100 p-4">
      {Array.isArray(data.datalist) &&
        data.datalist.map((item, index) => (
          <div
            key={index}
            className="p-4 border border-gray-300 rounded shadow bg-white"
          >
            <h2
              className="text-xl font-bold text-gray-700"
              onClick={() => {
                setSelectedUserId(item.UserID);
                openModal(item.Username);
              }}
            >
              {item.Username}
            </h2>
            <p className="text-gray-600">{item.comment}</p>
            <p className="text-sm text-gray-500">Likes: {item.like}</p>
            <p className="text-sm text-gray-500">Time: {item.time}</p>
          </div>
        ))}
      {isModalOpen && (
        <div className="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-black bg-opacity-50">
          <div className="w-1/3 bg-white p-4 rounded shadow-lg max-w-lg mx-auto">
            {/* {JSON.stringify(userInfo)} */}
            {userInfo &&
            userInfo.data &&
            userInfo.data[0] &&
            userInfo.data[0].Username ? (
              <div className="border-b pb-4 mb-4">
                <h2 className="text-2xl font-bold text-gray-700 mb-2">
                  {userInfo.data[0].Username}
                </h2>
                <p className="text-gray-600">
                  <strong>IP地址:</strong> {userInfo.data[0]["IP location"]}
                </p>
                <p className="text-gray-600">
                  <strong>Level:</strong> {userInfo.data[0].Level}
                </p>
                {/* 显示其他用户信息 */}
              </div>
            ) : (
              <Loading />
            )}
            {userQuota ? (
              <div className="mb-4">
                <h3 className="text-xl font-bold text-gray-700 mb-2">
                  用户指标
                </h3>
                <p className="text-gray-600">
                  <strong>Quota 1:</strong> {userQuota.data.quta1}
                </p>
                <p className="text-gray-600">
                  <strong>Quota 2:</strong> {userQuota.data.quta2}
                </p>
                {/* 显示其他用户指标 */}
              </div>
            ) : null}
            {searchResults ? (
              <div>
                <h3 className="text-xl font-bold text-gray-700 mb-2">
                  跨平台用户搜索结果
                </h3>
                {Object.entries(searchResults.data).map(([platform, users]) => (
                  <div key={platform}>
                    <h4 className="text-lg font-bold text-gray-600 mb-2">
                      {platform}
                    </h4>
                    {users &&
                      users.map((user) => (
                        <div key={user.IDIndex} className="mb-2">
                          <p>
                            <strong>用户名:</strong> {user.Username}
                          </p>
                          <p>
                            <strong>IP地址:</strong> {user["IP location"]}
                          </p>
                          <p>
                            <strong>Level:</strong> {user.Level}
                          </p>
                          <p>
                            <strong>注册时间:</strong> {user["register time"]}
                          </p>
                          <p>
                            <strong>相关事件:</strong> {user.relatedEvent}
                          </p>
                        </div>
                      ))}
                  </div>
                ))}
              </div>
            ) : null}
            <button
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
              onClick={closeModal}
            >
              关闭
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
