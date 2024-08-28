"use client"

import { MdNavigateNext } from "react-icons/md"

interface CardProps {
  title: string;
  value: string;
}

function CommaSeparation(value: string) {
    let formattedString = ""
    let counter = 0
    const num = value.split('.')[0]
    const fraction = value.split('.')[1] === undefined ? '' : value.split('.')[1] 

    if (num.length <= 3) {
        return num + '.' + fraction
    }

    for (let i = num.length - 1; i >= 0; i--) {
        formattedString += num[i];
        if (counter % 3 == 2) {
            formattedString += ','
        }
        counter++;
    }
    
    const finalValue = formattedString.split('').reverse().join('') + '.' + fraction
    return finalValue
}

export default function Card({ title, value }: CardProps) {
    const finalValue = CommaSeparation(value)
  return (
    <div className="m-8 flex flex-col justify-center space-y-4 p-4 w-72 h-24 border border-gray-400 rounded-md">
      <div className="text-md font-semibold pt-3">{title}</div>
      <div className="font-bold text-4xl">{finalValue}</div>
      <MdNavigateNext />
    </div>
  );
}
