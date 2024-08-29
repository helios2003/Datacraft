import { motion } from 'framer-motion'
import Upload from "@/components/Upload"
import Card from "@/components/Card"
import Topbar from "@/components/Topbar"

const pageVariants = {
  initial: {
    opacity: 0,
  },
  in: {
    opacity: 1,
  },
  out: {
    opacity: 0,
  },
}

const pageTransition = {
  type: 'tween',
  ease: 'anticipate',
  duration: 0.3,
}

export default function Dashboard() {
  return (
    <motion.div
      initial="initial"
      animate="in"
      exit="out"
      variants={pageVariants}
      transition={pageTransition}
    >
      <Topbar heading="hi bro"/>
      <Card title="Previous Month Order" value="534.09545" />
    </motion.div>
  )
}