"use client"

import { Pie } from "react-chartjs-2"
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
                label: "Statistics Chart",
                data: data.map(item => item.value),
                backgroundColor: data.map(item => item.color),
                borderColor: data.map(item => item.color),
                borderWidth: 1,
            }
        ]
    }

    return (
        <>
            <Pie data={chartData} />
        </>
    )
}