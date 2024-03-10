import logo from './../../public/logo.svg'
import Image from "next/image";

export default function Logo() {
    return (
        <div className="logo flex">
          <Image src={logo}></Image>
          <h1 className="logo-text">rbit</h1>
        </div>
    )
}