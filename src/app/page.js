'use client';

import Image from "next/image";
import Logo from '../components/Logo';

export default function Home() {
  return (

    <div style={{ 
      backgroundImage: `url('/images/landing-bg.jpg')`,
      height: '100vh', // Adjust the height as needed
      backgroundSize: 'cover', // Cover the entire page
      backgroundPosition: 'center' // Center the background image
    }}>
      <main className="min-h-screen">

<div className="header min-w-screen flex justify-between my-5 mx-5">
  <Logo />
  <span className="">
    <button>Log In</button>
  </span>
</div>
<div className="landing-content">
  <h1 className="landing-title">Welcome to Orbit</h1>
  <p className="landing-description py-5">your community for growth</p>
  <button>Join Now</button>
  {/* <div className="landing-images">
    <Image src="C:\Users\jjin_\github\cmdf24\public\images\landing-1.png"
    width={484.167}
    height={463.836}/>
  </div> */}
</div>
</main>
    </div>
    
    
  );
}
