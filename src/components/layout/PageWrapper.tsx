import { Sidebar } from "./Sidebar";
import { TopBar } from "./TopBar";

export function PageWrapper({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen">
      <Sidebar />
      <div className="pl-64">
        <TopBar />
        <main className="p-6">{children}</main>
      </div>
    </div>
  );
}
