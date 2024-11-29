import { Outlet } from "react-router-dom";

export default function Layout() {
    return (
      <div className="content container mt-3">
        <Outlet />
    </div>
    );
}