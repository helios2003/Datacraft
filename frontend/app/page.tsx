import Navbar from "@/components/utils/Navbar"
import Nextbutton from "@/components/buttons/Nextbutton"
import Image from "next/image"
import { PT_Serif_Caption } from "next/font/google"

const pt_serif = PT_Serif_Caption({
  weight: "400",
  subsets: ["latin"],
  display: "swap",
});

export default async function Home() {
  
  return (
    <div className={`${pt_serif.className}`}>
      <Navbar heading="Datacraft"/>
      <div className="flex flex-col items-center justify-center text-center ">
        <div>
          <Image src="/home.png" height={400} width={400} alt="Home Page"/>
        </div>
        <div>
          <h1 className="text-purple-500 text-5xl font-extrabold">
            Quick and Efficient Way to <br />
            Visualize Your Transactions
          </h1>
          <br />
          <h2 className="text-purple-400 text-xl">
              Upload your CSV and Excel transaction sheets here and let us do the heavylifting <br /> to provide you with meaningful stats
          </h2>
          <br />
        </div>
          <Nextbutton />
      </div>
    </div>
  );
}
