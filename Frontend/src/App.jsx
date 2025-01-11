import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./component/Home";
import Navbar from "./component/Navbar";
import Background from "./component/Page/BackGround";
import QrGenerator from "./component/Page/QrGeneratoer";
import BackgroundRemover from "./component/Page/BackgroundRemover";

const App = () => {
  return (
    <div className="flex min-h-screen">
      {/* Navbar on the left side */}
      <div className=" bg-cyan-600 text-white">
        <Navbar />
      </div>
      {/* Main content takes the remaining width */}
      <div className="flex-1 bg-gray-100 ">
        <Routes>
          <Route path="/home" element={<Home />} />
          <Route path="/bg" element={<Background />} />
          <Route path="/qr" element={<QrGenerator />} />
          <Route path="/bg-remove" element={<BackgroundRemover />} />



        </Routes>
      </div>
    </div>
  );
};

export default App;
