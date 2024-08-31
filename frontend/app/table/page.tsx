import Table from "@/components/tables/Table"
import Navbar from "@/components/utils/Navbar"

export default function Home() {
    return (
        <>
            <Navbar heading="Datacraft"/>
            <Table tableName="orderpaymentreceivedsheet" />
        </>
    )
}