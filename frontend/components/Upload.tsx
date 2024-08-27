"use client"

import { useState } from "react"
import axios from 'axios'

export default function Upload() {
    const [files, setFiles] = useState<File[]>([])

    function handleFileChange(e: React.ChangeEvent<HTMLInputElement>) {
        if (e.target.files) {
          setFiles(Array.from(e.target.files));
        }
    }

    async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault()
        const formdata = new FormData()
        files.forEach(file => formdata.append("files", file))
        try {
            const uploadURL = 'http://localhost:8000/upload'
            const response = await axios.post(uploadURL, formdata,{
                headers: {
                    'Content-Type': 'multipart/form-data', 
                }
            })
            if (response.status === 200) {
                alert("Files uploaded successfully")
            }
        } catch (error) {
            console.error(error)
            alert("Files could not be uploaded, please try again")
        }
    }

    return (
        <>
        <form onSubmit={handleSubmit}>
            <div>Upload the merchant and the payment file</div>
            <input type="file" onChange={handleFileChange}/>
            <button type="submit">Upload</button>
        </form>
        </>
    )
}