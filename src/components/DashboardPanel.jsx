import Logo from "./Logo";
import Image from "next/image";
import styles from '../app/styles/sidebar.module.css'

function DashboardPanel() {
  return (
    <section>
      <aside
        id="sidebar"
        className="flex fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0"
        aria-label="Sidebar"
      >
        <div className="h-full px-3 py-4 overflow-y-auto">
          <a href="/" className="flex items-center ps-2.5 mb-5">
            <Logo />
          </a>
          <ul className="space-y-2 font-medium">
            <li>
              <a
                href="#"
                className="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="26"
                  height="25"
                  viewBox="0 0 26 25"
                  fill="none"
                >
                  <path
                    d="M24.8809 12.358L13.618 0.65568C13.5369 0.571194 13.4406 0.504166 13.3345 0.458433C13.2285 0.4127 13.1148 0.38916 13 0.38916C12.8852 0.38916 12.7716 0.4127 12.6655 0.458433C12.5595 0.504166 12.4632 0.571194 12.3821 0.65568L1.11917 12.358C0.79104 12.6992 0.605103 13.1626 0.605103 13.6459C0.605103 14.6496 1.38987 15.4655 2.3551 15.4655H3.54182V23.8158C3.54182 24.319 3.93284 24.7256 4.41682 24.7256H11.25V18.357H14.3125V24.7256H21.5832C22.0672 24.7256 22.4582 24.319 22.4582 23.8158V15.4655H23.6449C24.1098 15.4655 24.5555 15.275 24.8836 14.931C25.5645 14.2202 25.5645 13.0688 24.8809 12.358Z"
                    fill="#F5F5F8"
                  />
                </svg>
                <span className="ms-3">Dashboard</span>
              </a>
            </li>
          </ul>
        </div>
      </aside>
      <div className="p-4 sm:ml-64">
        <div className="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700">
          <div className="grid grid-cols-3 gap-4 mb-4">
            <div className="flex items-center justify-center h-24 rounded bg-gray-50 dark:bg-gray-800">
              <p className="text-2xl text-gray-400 dark:text-gray-500">
                <svg
                  className="w-3.5 h-3.5"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 18 18"
                >
                  <path
                    stroke="currentColor"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M9 1v16M1 9h16"
                  />
                </svg>
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default DashboardPanel;
