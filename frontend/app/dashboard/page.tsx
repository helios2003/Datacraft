import Card from "@/components/utils/Card"
import Navbar from "@/components/utils/Navbar"

export default function Dashboard({}) {
  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar heading="Dashboard"/>
      <div className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <Card title="Total Revenue" value="345678" />
          <Card title="Monthly Sales" value="87654" />
          <Card title="Active Users" value="12345" />
          <Card title="New Customers" value="5678" />
          <Card title="Conversion Rate" value="23.45" />
          <Card title="Average Order Value" value="789.12" />
        </div>
      </div>
    </div>
  )
}