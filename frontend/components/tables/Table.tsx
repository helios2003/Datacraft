'use client'

import axios from 'axios'
import { useEffect, useState } from 'react'
import { CSSProperties } from 'react'
import { RingLoader } from 'react-spinners'

const override: CSSProperties = {
  display: 'block',
  margin: '0 auto',
  borderColor: 'purple',
}

interface tableProps {
  tableName: string
}

export default function Table({ tableName }: tableProps) {

  const [data, setData] = useState<any[]>([])
  const [loading, setLoading] = useState<Boolean>(true)

  async function getTable() {
    try {
      const response = await axios.get(
        `http://localhost:8000/table?table_name=${tableName}`
      )
      if (response.status === 200) {
        setLoading(false)
        setData(response.data.data)
      }
    } catch (error) {
      console.error(error)
    }
  }

  useEffect(() => {
    getTable()
  }, [tableName])

  return (
    <>
      <h2 className="text-xl pl-12 pt-4 font-semibold">{tableName}</h2>
      <div className="container mx-auto p-2">
        <div className="flex justify-between items-center mb-4"></div>
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
            {loading ? (
              <tbody>
                <tr>
                  <td colSpan={4} className="px-6 py-4 text-center">
                    <div className="flex flex-col items-center justify-center">
                      <RingLoader
                        loading={true}
                        cssOverride={override}
                        size={50}
                        aria-label="Loading Spinner"
                        data-testid="loader"
                      />
                      <p className="mt-4 text-xl text-purple-600">
                        The data is loading
                      </p>
                    </div>
                  </td>
                </tr>
              </tbody>
            ) : (
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
            )}
          </table>
        </div>
      </div>
    </>
  )
}
