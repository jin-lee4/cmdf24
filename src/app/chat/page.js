"use client";

import Sidebar from "@/components/Sidebar";
import styles from "@/app/styles/messages.module.css";
import MessagePreview from "@/components/MessagePreview";
import Image from "next/image";
import React from "react";

export default function Chat() {

  return (
    <section>
      <Sidebar />
      <div className={styles.panel}>
        <div className="grid grid-cols-2 divide-x">
          <div className="pt-20 pl-12 pr-12">
            <h1 className={styles.heading}>Messages</h1>
            <form className="flex items-center max-w-sm mt-3">
              <label for="simple-search" className="sr-only">
                Search
              </label>
              <div className="relative w-full">
                <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none"></div>
                <input
                  type="text"
                  id="simple-search"
                  className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Search..."
                  required
                />
              </div>
            </form>
            <div className="mt-10 grid grid-rows-5 gap-10">
              <div>
                <MessagePreview />
              </div>
              <div>
                <MessagePreview />
              </div>
              <div>
                <MessagePreview />
              </div>
              <div>
                <MessagePreview />
              </div>
            </div>
          </div>
          <div className="px-5 mb-20">
            <div className="flex justify-end space-x-4 mt-10 mx-10">
              <div className="space-y-2">
                <h3 className={styles.name}>Josh Cheng</h3>
                <p className={styles.viewprofile}>View profile</p>
              </div>
              <div className="">
                <Image
                  src="/images/profile.png"
                  width="48"
                  height="48"
                />
              </div>
            </div>
            <div className="mt-5">
            <Image src="/images/chat.png" width="500" height="600" unoptimized={true}></Image>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
