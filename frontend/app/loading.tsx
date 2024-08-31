"use client"

import { CSSProperties } from "react"
import { RingLoader } from "react-spinners"

const override: CSSProperties = {
  display: "block",
  margin: "0 auto",
  borderColor: "purple",
}

export default function Loading() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <RingLoader
        loading={true}
        cssOverride={override}
        size={100}
        aria-label="Loading Spinner"
        data-testid="loader"
      />
      <p className="mt-4 text-xl text-purple-600">The data is loading</p>
    </div>
  );
}
