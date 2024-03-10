import Sidebar from "@/components/Sidebar";
import styles from "@/app/styles/messages.module.css";
import MessagePreview from "@/components/MessagePreview";

export default function Chat() {
  return (
    <section>
      <Sidebar />
      <div className={styles.panel}>
        <div className="grid grid-cols-2 divide-x">
          <div className="pt-20 pl-12">
            <h1 className={styles.heading}>Messages</h1>
            <form class="flex items-center max-w-sm">
              <label for="simple-search" class="sr-only">
                Search
              </label>
              <div class="relative w-full">
                <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none"></div>
                <input
                  type="text"
                  id="simple-search"
                  class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                  placeholder="Search branch name..."
                  required
                />
              </div>
              <button
                type="submit"
                class="p-2.5 ms-2 text-sm font-medium text-white bg-blue-700 rounded-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300"
              >
                <svg
                  class="w-4 h-4"
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
                <h3 className="">Your Name</h3>
                <p className="">Your Profile</p>
              </div>
              <div className="">
                {/* <Image
            src={"/public/images/profile.png"}
            width="32"
            height="32"
          ></Image> */}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
