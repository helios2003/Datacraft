"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

interface ProcessbuttonProps {
  filesSize: number;
}

export default function Processbutton({ filesSize }: ProcessbuttonProps) {
  const [hover, setHover] = useState<boolean>(false);
  const router = useRouter();

  const isDisabled = filesSize !== 2;

  return (
    <div className="p-16">
      <button
        className={`
          bg-purple-500 h-12 w-full mt-6 rounded-md
          ${hover && !isDisabled ? 'bg-purple-700' : ''} 
          text-white 
          ${isDisabled ? 'opacity-50 cursor-not-allowed' : 'hover:bg-purple-700'}
        `}
        disabled={isDisabled}
        onMouseEnter={() => setHover(true)}
        onMouseLeave={() => setHover(false)}
        onClick={() => {
          
        }}
      >
        Start Processing
      </button>
    </div>
  );
}