'use client'

import { Bar } from 'react-chartjs-2'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(
  Title, 
  Tooltip, 
  Legend, 
  BarElement, 
  CategoryScale, 
  LinearScale
)

interface BarChartData {
  labels: string[],
  datasets: {
    label: string,
    data: number[],
    backgroundColor: string[],
    borderColor: string[],
    borderWidth: number
  }[]
}

interface BarChartProps {
  data: BarChartData
}

export default function BarChart({ data }: BarChartProps) {
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        align: 'start' as const,
      },
      title: {
        display: true,
        text: 'Reimbursements bar chart'
      },
    },
    scales: {
      x: {
        beginAtZero: true,
      },
      y: {
        beginAtZero: true,
      },
    },
  }

  return (
    <div className="h-full w-96 ml-32">
      <Bar data={data} options={options} />
    </div>
  )
}
