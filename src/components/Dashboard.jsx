import panel from "@/app/styles/panel.module.css";
import styles from "../app/styles/dashboardpanel.module.css";
import Image from "next/image";
import MatchSpotlight from '@/components/ConnectionSpotlight'

function Dashboard() {
  return (
    <section className={panel.panel}>
      <div className="p-9 grid grid-cols-2 gap-7">
        <div className="col-start-1 col-end-3">
          <div className={styles.box}>
            <h2 className="text-2xl w-100">Welcome Back,</h2>
            <h2 className="text-2xl">Your Name</h2>
            <p>Let's thrive together.</p>
          </div>
        </div>
        <div className="col-start-1 col-end-2">
          <div className={styles.box}>
            <h2 className="top-0 right-0 text-base w-100">Connection Spotlight</h2>
            <div className="items-center">
            </div>
          </div>
        </div>
        <div className="col-start-2">
          <div className={styles.box}>
            <h2 className="text-base w-100">Insights</h2>
          </div>
        </div>
        <div className="col-start-1 col-end-3">
          <div className={styles.box}>
            <h2 className="text-base w-100">Upcoming Meetings</h2>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Dashboard;
