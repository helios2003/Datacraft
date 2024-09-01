"use client"

import Table from "@/components/tables/Table"
import Navbar from "@/components/utils/Navbar"
import { useSearchParams } from 'next/navigation'

export default function Home() {
    const searchParams = useSearchParams()
 
    const tableName = searchParams.get('table_name')!

    return (
        <>
            <Navbar heading="Datacraft"/>
            <Table tableName={tableName} />
        </>
    )
}