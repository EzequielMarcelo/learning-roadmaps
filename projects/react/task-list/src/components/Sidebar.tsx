import { useState } from "react";
import { FaHome, FaUser, FaCog, FaBars } from "react-icons/fa";

import "./Sidebar.css";

interface sidebarProps {
  title: string;
  start_expanded: boolean;
}

export function Sidebar({ title, start_expanded }: sidebarProps) {
  const [expanded, setExpanded] = useState(start_expanded);

  return (
    <aside className={`sidebar ${expanded ? "expanded" : "collapsed"}`}>
      <button className="toggle-btn" onClick={() => setExpanded(!expanded)}>
        <span className="icon">
          <FaBars />
        </span>
        {expanded && <span className="fs-4">{title}</span>}
      </button>

      {expanded && <hr className="sidebar-divider" />}

      <nav className="menu d-flex flex-column flex-grow-1">
        <SidebarItem icon={<FaHome />} label="Home" expanded={expanded} />
        <SidebarItem icon={<FaUser />} label="Users" expanded={expanded} />
        <div className="mt-auto d-flex flex-column user-login">
          {expanded && <hr className="sidebar-divider" />}
          <SidebarItem icon={<FaCog />} label="Settings" expanded={expanded} />
          <SidebarItem icon={<FaUser />} label="Login" expanded={expanded} />
        </div>
      </nav>
    </aside>
  );
}

interface itemProps {
  icon: React.ReactNode;
  label: string;
  expanded: boolean;
}

function SidebarItem({ icon, label, expanded }: itemProps) {
  return (
    <div className="menu-item">
      <span className="icon">{icon}</span>
      {expanded && <span className="text">{label}</span>}
    </div>
  );
}
