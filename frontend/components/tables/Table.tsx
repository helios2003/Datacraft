'use client'

import axios from 'axios'
import { useEffect, useState, useCallback } from 'react'
import { CSSProperties } from 'react'
import { RingLoader } from 'react-spinners'

const override: CSSProperties = {
  display: 'block',
  margin: '0 auto',
  borderColor: 'purple',
}

interface TableProps {
  tableName: string
}

export default function Table({ tableName }: TableProps) {

  const [data, setData] = useState<any[]>([])
  const [loading, setLoading] = useState<boolean>(true)
  const [error, setError] = useState<boolean>(false)

  const getTable = useCallback(async () => {
    setLoading(true)
    try {
      const response = await axios.get(
        `http://localhost:8000/table?table_name=${tableName}`
      )
      if (response.status === 200) {
        setData(response.data.data)
        setError(false)
      } else if (response.status === 404) {
        setError(true)
      }
    } catch (error) {
      console.error(error)
      setError(true)
    } finally {
      setLoading(false)
    }
  }, [tableName])

  useEffect(() => {
    getTable()
  }, [getTable])

  return (
    <>
      <h2 className="text-xl pl-12 pt-4 font-semibold">{tableName}</h2>
      <div className="container mx-auto p-2">
        <div className="flex justify-between items-center mb-4"></div>
        {loading ? (
          <div className="flex flex-col items-center justify-center">
            <RingLoader
              loading={true}
              cssOverride={override}
              size={50}
              aria-label="Loading Spinner"
              data-testid="loader"
            />
            <p className="mt-4 text-xl text-purple-600">The data is loading</p>
          </div>
        ) : error ? (
          <div className="text-center text-red-600">
            <p className="text-xl">Table not found or an error occurred</p>
          </div>
        ) : (
          <div className="overflow-x-auto">
            <table className="min-w-full bg-white">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                    Order ID
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                    Net Amount
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                    Invoice Amount
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">
                    Transaction Type
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {data.map((order) => (
                  <tr key={order.id} className="hover:bg-gray-50">
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                      {order.order_id}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-700">
                      {order.total}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-700">
                      {order.invoice_amt}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-700">
                      {order.transaction_type}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </>
  )
}
