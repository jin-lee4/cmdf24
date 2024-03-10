import styles from "@/app/styles/insights.module.css";
import Sidebar from "@/components/Sidebar"

export default function Insights() {
  return (
    <section>
        <Sidebar />
    <div className={styles.panel}>
      <div className="items-center">
        <h1 className={styles.heading}>Insights Hub</h1>
        <div className="grid grid-cols-2 gap-5 pr-10">
          <div className={styles.box}>
          <p className={styles.title}>Marvin's Insights</p>
            <p className={styles.insights}></p>
                <ol>
                    <li>Marvin's Insights: Offered deep industry knowledge, focusing on emerging trends Josh could leverage.</li>
                    <li>Professional Goals: Josh outlined his career aspirations with Marvin suggesting a tailored action plan for growth.</li>
                    <li>Networking Advice: Marvin provided specific strategies for Josh to expand his professional network effectively.</li>
                </ol>
          </div>
          <div className={styles.box}></div>
        </div>
      </div>
      </div>
    </section>
  );
}
