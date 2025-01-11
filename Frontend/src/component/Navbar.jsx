import React, { useState } from "react";
import {
  AppstoreOutlined,
  BgColorsOutlined,
  ContainerOutlined,
  DesktopOutlined,
  MailOutlined,
  MenuFoldOutlined,
  MenuUnfoldOutlined,
  PieChartOutlined,
} from "@ant-design/icons";
import { Menu } from "antd";
import { Link } from "react-router-dom";

const items = [
  {
    key: "1",
    icon: <PieChartOutlined />,
    label: <Link to="/home">Home</Link>,
  },
  {
    key: "2",
    icon: <DesktopOutlined />,
    label: <Link to="/bg">BackGround</Link>,
  },
  {
    key: "3",
    icon: <ContainerOutlined />,
    label: <Link to="/qr">Generate QR</Link>,
  },
  {
    key: "4",
    icon: <ContainerOutlined />,
    label: <Link to="/bg-remove">Remove BackGround</Link>,
  },
  {
    key: "sub1",
    label: "Navigation One",
    icon: <MailOutlined />,
    children: [
      { key: "5", label: "Option 5" },
      { key: "6", label: "Option 6" },
      { key: "7", label: "Option 7" },
      { key: "8", label: "Option 8" },
    ],
  },
  {
    key: "sub2",
    label: "Navigation Two",
    icon: <AppstoreOutlined />,
    children: [
      { key: "9", label: "Option 9" },
      {
        key: "sub3",
        label: "Submenu",
        children: [{ key: "12", label: "Option 12" }],
      },
    ],
  },
];

const Navbar = () => {
  const [collapsed, setCollapsed] = useState(false);

  const toggleCollapsed = () => {
    setCollapsed(!collapsed);
  };

  return (
    <div>
      <div className="w-full">
        <button
          type="button"
          onClick={toggleCollapsed}
          className="bg-cyan-800 p-2 w-full text-white"
        >
          {collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
        </button>
      </div>
      <Menu
        defaultSelectedKeys={["1"]}
        defaultOpenKeys={["sub1"]}
        mode="inline"
        inlineCollapsed={collapsed}
        items={items}
        className="bg-cyan-500 transition-all duration-300"
      />
    </div>
  );
};

export default Navbar;
