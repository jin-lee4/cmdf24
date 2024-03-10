import Sidebar from "@/components/Sidebar";
import DashboardContent from "@/components/Dashboard";
import ChatPanel from "@/components/ChatPanel";

export default function Dashboard() {
  return (
    <section>
      <Sidebar />
      <DashboardContent />
      <ChatPanel />
    </section>
  );
}
