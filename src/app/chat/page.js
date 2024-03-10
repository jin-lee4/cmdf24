'use client';

import Sidebar from "@/components/Sidebar";
import styles from "@/app/styles/messages.module.css";
import MessagePreview from "@/components/MessagePreview";
import Image from "next/image";
import React, { useState, useEffect, useContext } from "react";
import dynamic from "next/dynamic";
import { getOrCreateChat } from 'react-chat-engine'



const ChatEngine = dynamic(() =>
  import("react-chat-engine").then((module) => module.ChatEngine)
);
const MessageFormSocial = dynamic(() =>
  import("react-chat-engine").then((module) => module.MessageFormSocial)
);


export default function Chat() {
  const [username, setUsername] = useState('')


  function createDirectChat(creds) {
		getOrCreateChat(
			creds,
			{ is_direct_chat: true, usernames: [username] },
			() => setUsername('')
		)
	}
  
  function renderChatForm(creds) {
		return (
			<div>
				<input 
					placeholder='Username' 
					value={username} 
					onChange={(e) => setUsername(e.target.value)} 
				/>
				<button onClick={() => createDirectChat(creds)}>
					Create
				</button>
			</div>
		)
	}

  return (
    <section>
      <Sidebar />
      
      <div className={styles.panel}>
        <div className="grid grid-cols-2 divide-x">
          <div className="pt-20 pl-12 pr-12">
            <h1 className={styles.heading}>Messages</h1>
            <form className="flex items-center max-w-sm">
              <label for="simple-search" class="sr-only">
                Search
              </label>
              <div className="relative w-full">
                <div className="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none"></div>
                <input
                  type="text"
                  id="simple-search"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Search..."
                  required
                />
              </div>
              <button
                type="submit"
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
              >
                <svg
                  className="w-4 h-4"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 20 20"
                >
                  <path
                    stroke="currentColor"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
                  />
                </svg>
                <span class="sr-only">Search</span>
              </button>
            </form>
            <div className="mt-10 grid grid-rows-5 gap-10 divide-y">
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
          <div>
            <div className="flex justify-end space-x-4 mt-10 mx-10">
              <div className="space-y-2">
                <h3 className={styles.name}>Josh Cheng</h3>
                <p className={styles.viewprofile}>View profile</p>
              </div>
              <div className="">
                <Image
                  src="./../../../public/images/profile.svg"
                  width="48"
                  height="48"
                />
                {/* <Image
            src={"/public/images/profile.png"}
            width="32"
            height="32"
          ></Image> */}
              </div>
            </div>
            <div className="px-5">
              <div className={styles.chatbox}>
                <p className={styles.chatdetails}>
                  This is the start of your conversation with Marvin James.
                </p>
                <div className="background">
      <div className="shadow">
        <ChatEngine
          projectID="0546f576-dc48-4bda-8a2b-3d1084135888"
          userName="marianeolivan"
          userSecret="chocolate"
          renderNewChatForm={(creds) => renderChatForm(creds)}
          />
      </div>
    </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
