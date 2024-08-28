import Navbar from "@/components/Navbar";
import Button from "@/components/Button";
import Image from "next/image";
import { PT_Serif_Caption } from "next/font/google";
import Link from 'next/link'

const pt_serif = PT_Serif_Caption({
  weight: "400",
  subsets: ["latin"],
  display: "swap",
});

export default function Home() {
  return (
    <>
      <Navbar />
      <div className="flex items-center justify-center">
        <Image src="/home.png" height={500} width={500} alt="Home Page" />
        <div
          className={`space-y-4 ${pt_serif.className}`}
        >
          <div className="text-purple-500 text-5xl font-extrabold">Quick and Efficient Way to </div>
          <div className="text-purple-500 text-5xl font-extrabold">Visualize Your Transactions </div>
          <Button />
        </div>
      </div>
    </>
  );
}
