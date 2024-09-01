'use client'

import { Pie } from 'react-chartjs-2'
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, ArcElement)

interface chartInput {
  label: string,
  value: number,
  color: string
}

interface chartInputProps {
  data: chartInput[]
}

export default function PieChart({ data }: chartInputProps) {
  const chartData = {
    labels: data.map(item => item.label),
    datasets: [
      {
        label: 'Statistics Chart',
        data: data.map(item => item.value),
        backgroundColor: data.map(item => item.color),
        borderColor: data.map(item => item.color),
        borderWidth: 1,
      },
    ],
  }

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'right' as const,
        align: 'center' as const,
        labels: {
          boxWidth: 10,
          padding: 10,
          font: {
            size: 12,
          },
        },
      },
      tooltip: {
        callbacks: {
          label: function (tooltipItem: any) {
            return `${tooltipItem.label}: ${tooltipItem.raw}`
          },
        },
      },
    },
    layout: {
      padding: 10,
    },
  }

  return (
    <div style={{ width: '100%', height: '270px' }}>
      <div className="text-xs text-gray-500 font-semibold flex justify-center">Reimbursement Data as Percentage</div>
      <Pie data={chartData} options={options} />
    </div>
  )
}