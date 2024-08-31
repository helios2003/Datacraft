"use client"

import { useState } from "react"

interface ProcessbuttonProps {
  filesSize: number
  onClick: () => void
  uploadStatus: boolean
}

export default function Processbutton({ filesSize, onClick, uploadStatus }: ProcessbuttonProps) {
  const [hover, setHover] = useState<boolean>(false)

  const isDisabled = filesSize !== 2;

  return (
    <div className="p-16">
      <button
        className={`
          bg-purple-500 h-12 w-full mt-6 rounded-md text-xl
          ${hover && !isDisabled ? 'bg-purple-700' : ''} 
          text-white 
          ${isDisabled ? 'opacity-50 cursor-not-allowed' : 'hover:bg-purple-700'}
        `}
        disabled={isDisabled}
        onMouseEnter={() => setHover(true)}
        onMouseLeave={() => setHover(false)}
        onClick={onClick}
      >
        {uploadStatus ? "Start Processing" : "Start Uploading"}
      </button>
    </div>
  );
}