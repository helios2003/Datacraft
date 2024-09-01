"use client"

import { MdNavigateNext } from "react-icons/md"
import { useRouter } from "next/navigation"

interface CardProps {
  title: string
  value: string
}

function CommaSeparation(value: string) {
  let formattedString = ""
  let counter = 0;
  const num = value.split(".")[0];
  const fraction = value.split(".")[1] === undefined ? "" : value.split(".")[1];

  if (num.length <= 3) {
    return num + "." + fraction
  }

  for (let i = num.length - 1; i >= 1; i--) {
    formattedString += num[i];
    if (counter % 3 == 2) {
      formattedString += ","
    }
    counter++
  }

  formattedString += num[0]
  let finalValue = ""

  if (fraction) {
    finalValue = formattedString.split("").reverse().join("") + "." + fraction
  } else {
    finalValue = formattedString.split("").reverse().join("")
  }
  return finalValue
}

export default function Card({ title, value }: CardProps) {
  const router = useRouter();
  //const finalValue = CommaSeparation(value);

  return (
    <div className="w-72 h-30 grid grid-cols-5 p-2 rounded-lg border border-gray-400">
      <div className="col-span-4 flex flex-col justify-center space-y-2">
        <div className="text-md font-semibold text-purple-500">{title}</div>
        <div className="font-semibold text-4xl">{value}</div>
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
  );
}
