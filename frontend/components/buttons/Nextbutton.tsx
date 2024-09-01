'use client'

import { useRouter } from 'next/navigation'
import { useState } from 'react'
import { FaArrowAltCircleRight } from 'react-icons/fa'

export default function Uploadbutton() {
  const [hover, setHover] = useState<Boolean>(false)
  const router = useRouter()
  return (
    <div>
      <button
        className="bg-purple-500 h-12 w-56 rounded-lg text-slate-100 font-semibold flex items-center justify-center "
        onClick={() => router.push('/upload')}
        onMouseEnter={() => setHover(true)}
        onMouseLeave={() => setHover(false)}
      >
        {hover ? <FaArrowAltCircleRight className="items-center text-slate-100 h-8 w-8"/> : 'Start By Uploading Files'}
      </button>
    </div>
  )
}
