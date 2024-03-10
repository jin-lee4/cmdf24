import styles from "@/app/styles/connectionspotlight.module.css";
import Image from "next/image";

function ConnectionSpotlight() {
  return (
    <section>
      <div className={styles.box}>
        <div className="justify-center">
        <div className="flex">
          <div>
            <h1 className={styles.name}>Marvin James</h1>
            <p className={styles.occupation}>Software Engineer</p>
          </div>
        </div>
        <div className="justify-center">
        <button className={styles.match}>Send Match Request</button>
        </div>
        </div>
      </div>
    </section>
  );
}

export default ConnectionSpotlight;
