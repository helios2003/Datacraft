"use client"

import { useRouter } from "next/navigation"

export default function Button() {
    const router = useRouter()
    return (
        <div>
        <button
            className="bg-purple-500 h-12 w-56 rounded-lg text-slate-100 font-semibold hover:text-gray-600"
            onClick={() => router.push('/upload')}
        >
            Start By Uploading Files
        </button>
        </div>
    );
}
