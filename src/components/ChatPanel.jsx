import styles from "@/app/styles/chatpanel.module.css";
import Image from "next/image";
import ChatPreview from "@/components/ChatPreview";

function ChatPanel() {
  return (
    <section className="py-10 fixed top-0 right-0">
      <div className="flex justify-end px-10 space-x-4">
        <div className="space-y-2">
          <h3 className={styles.profilename}>Josh Cheng</h3>
          <p className={styles.profile}>VIew Profile</p>
        </div>
        <div className={styles.profileimage}>
          <Image
            src={"/images/profile.png"}
            width="32"
            height="32"
          ></Image>
        </div>
      </div>
      <div className="my-5 space-y-7 justify-start px-5 w-80">
        <h2 className={styles.heading}>Recent Chats</h2>
        <div className="">
          <div className="space-y-4">
            <div className="flex space-x-56">
              <h3 className={styles.secondaryheading}>Mentors</h3>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="25"
                height="23"
                viewBox="0 0 25 23"
                fill="none"
              >
                <path
                  d="M9.47966 6.43045C9.38527 6.51911 9.31038 6.62442 9.25928 6.74035C9.20819 6.85628 9.18188 6.98056 9.18188 7.10607C9.18188 7.23158 9.20819 7.35586 9.25928 7.4718C9.31038 7.58773 9.38527 7.69304 9.47966 7.7817L13.4304 11.5L9.47966 15.2184C9.28927 15.3976 9.18232 15.6406 9.18232 15.894C9.18232 16.1474 9.28927 16.3904 9.47966 16.5696C9.67005 16.7488 9.92826 16.8495 10.1975 16.8495C10.4668 16.8495 10.725 16.7488 10.9154 16.5696L15.589 12.1709C15.6834 12.0822 15.7583 11.9769 15.8094 11.861C15.8605 11.745 15.8868 11.6208 15.8868 11.4952C15.8868 11.3697 15.8605 11.2454 15.8094 11.1295C15.7583 11.0136 15.6834 10.9083 15.589 10.8196L10.9154 6.42086C10.5284 6.0567 9.87677 6.0567 9.47966 6.43045Z"
                  fill="white"
                />
              </svg>
            </div>
            <ChatPreview />
          </div>
        </div>
        <div className="space-y-4">
          <div className="flex space-x-56">
            <h3 className={styles.secondaryheading}>Mentees</h3>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="25"
              height="23"
              viewBox="0 0 25 23"
              fill="none"
            >
              <path
                d="M9.47966 6.43045C9.38527 6.51911 9.31038 6.62442 9.25928 6.74035C9.20819 6.85628 9.18188 6.98056 9.18188 7.10607C9.18188 7.23158 9.20819 7.35586 9.25928 7.4718C9.31038 7.58773 9.38527 7.69304 9.47966 7.7817L13.4304 11.5L9.47966 15.2184C9.28927 15.3976 9.18232 15.6406 9.18232 15.894C9.18232 16.1474 9.28927 16.3904 9.47966 16.5696C9.67005 16.7488 9.92826 16.8495 10.1975 16.8495C10.4668 16.8495 10.725 16.7488 10.9154 16.5696L15.589 12.1709C15.6834 12.0822 15.7583 11.9769 15.8094 11.861C15.8605 11.745 15.8868 11.6208 15.8868 11.4952C15.8868 11.3697 15.8605 11.2454 15.8094 11.1295C15.7583 11.0136 15.6834 10.9083 15.589 10.8196L10.9154 6.42086C10.5284 6.0567 9.87677 6.0567 9.47966 6.43045Z"
                fill="white"
              />
            </svg>
          </div>
          <ChatPreview />
        </div>
      </div>
    </section>
  );
}

export default ChatPanel;
