"use client"

import Card from "@/components/utils/Card"
import Navbar from "@/components/utils/Navbar"
import axios from "axios"
import { useEffect, useState } from "react"

interface dataProps {
  distinct_count: string,
  order_payment_received: string,
  payment_pending: string,
  tolerance_breached: string,
  return_sheet: string,
  negative_payout: string
}

export default function Dashboard() {
  const [data, setData] = useState<dataProps>()

  async function getData() {
    try {

      const dataURL = 'http://localhost:8000/data/summary'
      const response = await axios.get(dataURL)

      if (response.status === 200) {
        console.log(response)
        setData(response.data)
      } else {
        console.error("Sorry, the server is not responding")
      }
    } catch (error) {
      console.error("Oops!!, error fetching data")
    }
  }

  useEffect(() => {
    getData()
  }, [])

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar heading="Dashboard"/>
      <div className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <Card title="Previous Month Order" value={data?.distinct_count!} />
          <Card title="Order & Payment Received" value={data?.order_payment_received!} />
          <Card title="Payment Pending" value={data?.payment_pending!} />
          <Card title="Tolerance Rate Breached" value={data?.tolerance_breached!} />
          <Card title="Return" value={data?.return_sheet!} />
          <Card title="Negative Payout" value={data?.negative_payout!} />
        </div>
      </div>
    </div>
  )
}