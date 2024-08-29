import Navbar from "@/components/Navbar";
import Button from "@/components/Button";
import Image from "next/image";
import { PT_Serif_Caption } from "next/font/google";
import Link from "next/link";

const pt_serif = PT_Serif_Caption({
  weight: "400",
  subsets: ["latin"],
  display: "swap",
});

export default function Home() {
  return (
    <>
      <Navbar />
      <div className="flex flex-col items-center justify-center">
        <div>
          <Image src="/home.png" height={500} width={500} alt="Home Page" className="drop-shadow"/>
        </div>
        <div
          className={`${pt_serif.className}`}
        >
          <h1 className="text-purple-500 text-5xl font-extrabold">
            Quick and Efficient Way to <br />
            Visualize Your Transactions
          </h1>
          <br />
        </div>
          <Button />
      </div>
    </>
  );
}
