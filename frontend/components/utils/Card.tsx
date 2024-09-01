'use client'

import { MdNavigateNext } from 'react-icons/md'
import { useRouter } from 'next/navigation'

interface CardProps {
  title: string
  value: number
}

function CommaSeparation(value: number) {
  const stat = value.toString()
  if (typeof stat !== 'string' || stat.trim() === '') {
    return stat
  }

  let formattedString = ''
  let counter = 0
  const num = stat.split('.')[0]
  const fraction = stat.split('.')[1] === undefined ? '' : stat.split('.')[1]

  if (num.length <= 3) {
    if (fraction) {
      return num + '.' + fraction
    } else {
      return num
    }
  }

  for (let i = num.length - 1; i >= 1; i--) {
    formattedString += num[i]
    if (counter % 3 === 2) {
      formattedString += ','
    }
    counter++
  }

  formattedString += num[0]
  let finalValue = ''

  if (fraction) {
    finalValue = formattedString.split('').reverse().join('') + '.' + fraction
  } else {
    finalValue = formattedString.split('').reverse().join('')
  }
  return finalValue
}

export default function Card({ title, value }: CardProps) {
  const router = useRouter()
  const finalValue = CommaSeparation(value)

  return (
    <div className="w-72 h-30 grid grid-cols-5 p-2 rounded-lg border border-gray-400">
      <div className="col-span-4 flex flex-col justify-center space-y-2">
        <div className="text-md font-semibold text-purple-500">{title}</div>
        <div className="font-semibold text-4xl">{finalValue}</div>
      </div>
      <div className="flex items-center justify-center">
        <MdNavigateNext
          className="text-black cursor-pointer h-8 w-8 hover:text-gray-600"
          onClick={() => {
            router.push(`/table?table_name=${title}`)
          }}
        />
      </div>
    </div>
  )
}
