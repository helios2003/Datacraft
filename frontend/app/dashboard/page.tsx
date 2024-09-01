'use client'

import { useEffect, useState } from 'react'
import axios from 'axios'
import Card from '@/components/utils/Card'
import Navbar from '@/components/utils/Navbar'
import PieChart from '@/components/charts/PieChart'
import BarChart from '@/components/charts/BarChart'

interface DataProps {
  distinct_count: number;
  order_payment_received: number;
  payment_pending: number;
  tolerance_breached: number;
  return_sheet: number;
  negative_payout: number;
}

interface ChartData {
  [key: string]: number;
}

export default function Dashboard() {
  const [data, setData] = useState<DataProps>()
  const [chartData, setChartData] = useState<ChartData>({})

  async function getData() {
    try {
      const dataURL = 'http://localhost:8000/generate/summary'
      const response = await axios.get(dataURL)
      if (response.status === 200) {
        setData(response.data)
      } else {
        console.error('Sorry, the server is not responding')
      }
    } catch (error) {
      console.error('Oops!!, error fetching data')
    }
  }

  async function getChartData() {
    try {
      const chartURL = 'http://localhost:8000/generate/charts'
      const response = await axios.get(chartURL)
      if (response.status === 200) {
        setChartData(response.data)
      } else {
        console.error('Sorry, the server is not responding')
      }
    } catch (error) {
      console.error('Oops!!, error fetching data')
    }
  }

  useEffect(() => {
    getData()
    getChartData()
  }, [])

  const pieChartData = Object.entries(chartData).map(
    ([label, value], index) => {
      const itemCount = Object.keys(chartData).length
      const lightness = 80 - (index / (itemCount - 2.5)) * 50
      return {
        label,
        value,
        color: `hsl(270, 70%, ${lightness}%)`,
      }
    }
  )

  const generateData = (chartData: ChartData) => {
    const itemCount = Object.keys(chartData).length

    const colors = Object.entries(chartData).map(([label, value], index) => {
      const lightness = 80 - (index / (itemCount - 1)) * 50
      return `hsl(270, 70%, ${lightness}%)`
    })

    return {
      labels: Object.keys(chartData),
      datasets: [
        {
          label: 'Customer Data',
          data: Object.values(chartData),
          backgroundColor: colors,
          borderColor: colors,
          borderWidth: 1,
        },
      ],
    }
  }

  const barGraphData = generateData(chartData)
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col overflow-hidden">
      <Navbar />
      {data ? 
        <div className="flex-grow flex flex-col p-4 overflow-hidden">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
            <Card title="Previous Month Order" value={data?.distinct_count} />
            <Card title="Order & Payment Received" value={data?.order_payment_received} />
            <Card title="Payment Pending" value={data?.payment_pending} />
            <Card title="Tolerance Rate Breached" value={data?.tolerance_breached} />
            <Card title="Return" value={data?.return_sheet} />
            <Card title="Negative Payout" value={data?.negative_payout} />
          </div>
          <div className="flex flex-col lg:flex-row gap-2 flex-grow">
            <div className="w-full lg:w-1/2 h-80">
              <PieChart data={pieChartData} />
            </div>
            <div className="w-full lg:w-1/2 h-96">
              <BarChart data={barGraphData} />
            </div>
          </div>
        </div> : null}
    </div>
  )
}
