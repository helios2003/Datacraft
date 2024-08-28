interface headingProps {
    heading: string
}
export default function Topbar({ heading }: headingProps) {
    return (
        <div className="h-16 flex flex-col items-center justify-center border border-gray-500 text-2xl">
            {heading}
        </div>
    )
}