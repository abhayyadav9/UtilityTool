import React, { useEffect, useRef } from "react";
import Navbar from "./Navbar";
import * as THREE from "three"; // Required for Vanta.js
import BIRDS from "vanta/dist/vanta.birds.min";
import QrGenerator from "./Page/QrGeneratoer";

const VantaBirdsBackground = () => {
  const vantaRef = useRef(null);

  useEffect(() => {
    const vantaEffect = BIRDS({
      el: vantaRef.current,
      mouseControls: true,
      touchControls: true,
      gyroControls: false,
      minHeight: 200.0,
      minWidth: 200.0,
      scale: 1.0,
      scaleMobile: 1.0,
      backgroundColor: 0x1a65c0,
      color2: 0x0,
    });

    return () => {
      // Clean up the Vanta effect when the component unmounts
      if (vantaEffect) vantaEffect.destroy();
    };
  }, []);

  return <div ref={vantaRef} style={{ height: "100vh", width: "100%" }} />;
};

const Home = () => {
  return (
    <div className="flex min-h-screen">
      <div style={{ position: "relative", flex: 1 }}>
        <VantaBirdsBackground />
        <div style={{ position: "absolute", top: 0, left: 0, zIndex: 1 }}>
        </div>
      </div>
    </div>
  );
};

export default Home;
