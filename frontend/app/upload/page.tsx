"use client"

import Navbar from "@/components/Navbar"
import { useDropzone } from "react-dropzone"
import { useCallback, useState } from "react"
import { PT_Serif_Caption } from "next/font/google"
import Processbutton from "@/components/Processbutton"
import { FaUpload } from "react-icons/fa6"

const pt_serif = PT_Serif_Caption({
  weight: "400",
  subsets: ["latin"],
  display: "swap",
})

export default function Upload() {
  const [files, setFiles] = useState<File[]>([])

  const onDrop = useCallback((acceptedFiles: File[]) => {
    setFiles((prevFiles: File[]) => {
      const newFiles = [...prevFiles, ...acceptedFiles]
      return newFiles.slice(0, 2)
    })
  }, [])

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'text/csv': ['.csv'],
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ['.xlsx']
    },
    maxFiles: 2,
  })

  const removeFile = (fileRemoved: File) => {
    setFiles(files.filter((file: File) => file != fileRemoved))
  }

  return (
    <>
      <div
        className={`flex flex-col items-center justify-center space-y-12 ${pt_serif.className}`}
      >
        <Navbar />
        <div className="mt-12 text-5xl font-extrabold text-purple-500">
          Upload Your Transaction Sheets Here
        </div>
        <div className="w-full max-w-md">
          <div
            {...getRootProps()}
            className={`border-2 border-dashed rounded-lg p-8 text-center cursor-pointer transition-colors h-40 flex flex-col justify-center items-center ${
              isDragActive
                ? "border-purple-600 bg-purple-50"
                : "border-gray-300 hover:border-purple-400"
            } ${files.length >= 2 ? "opacity-50 cursor-not-allowed" : ""}`}
          >
            <FaUpload className="text-gray-500 h-10 w-10 m-2"/>
            <input {...getInputProps()} disabled={files.length >= 2} />
            <p className="text-sm text-gray-600">
              {files.length >= 2
                ? "Maximum files reached"
                : "Drag 'n' drop some files here, or click to select files"}
            </p>
            <p className="text-xs text-gray-500 mt-2">
              (Only *.csv, and *.xlsx files will be accepted)
            </p>
          </div>
          {files.length > 0 && (
            <div className="mt-4">
              <div className="text-sm font-semibold mb-2">Uploaded Files:</div>
              {files.map((file, index) => (
                <div key={index} className="flex items-center justify-between mb-2">
                  <span className="text-sm truncate">{file.name}</span>
                  <button
                    onClick={() => removeFile(file)}
                    className="text-red-500 text-xs hover:text-red-700"
                  >
                    Remove
                  </button>
                </div>
              ))}
              <div className="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
                <div
                  className="bg-purple-600 h-2.5 rounded-full"
                  style={{ width: `${(files.length / 2) * 100}%` }}
                ></div>
              </div>
            </div>
          )}
        </div>
      </div>
      <Processbutton filesSize={files.length} />
    </>
  )
}