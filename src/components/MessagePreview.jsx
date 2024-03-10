import Image from "next/image";
import styles from "@/app/styles/messages.module.css";

function MessagePreview() {
  return (
    <section>
      <div className="grid grid-cols-8 gap-x-4">
        <div className="col-start-1 col-end-2">
          <Image src="/images/profile.svg" width="50" height="50"></Image>
        </div>
        <div className="col-start-2 col-end-9">
          <p className={styles.contact}>Contact Name</p>
          <div className="w-full">
            <p className={styles.messagecontent}>sldkfjsdjf</p>
          </div>
        </div>
      </div>
    </section>
  );
}

export default MessagePreview;
