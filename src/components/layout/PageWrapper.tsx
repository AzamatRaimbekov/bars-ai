import { Sidebar } from "./Sidebar";
import { TopBar } from "./TopBar";
import { TabBar } from "./TabBar";

export function PageWrapper({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen min-h-[100dvh] bg-black">
      <Sidebar />
      <TabBar />
      <div className="lg:pl-64">
        <TopBar />
        <main className="px-4 pt-4 pb-[88px] lg:px-6 lg:pt-6 lg:pb-6">{children}</main>
      </div>
    </div>
  );
}
