interface HeadingProps {
  heading: string;
  className?: string;
}

export default function Topbar({ heading, className = "" }: HeadingProps) {
  return (
    <>
      <div className={`h-16 flex flex-col items-center justify-center border border-gray-500 ${className}`}>
        {heading}
      </div>
    </>
  );
}
