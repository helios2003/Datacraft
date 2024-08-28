import { FaGithub } from "react-icons/fa";
import { IoMdMail } from "react-icons/io";
import { FaPhoneAlt } from "react-icons/fa";

export default function Navbar() {
  return (
    <div className="w-full h-14 border border-gray-700 text-purple-500 p-2 flex items-center">
      <div className="text-3xl pl-6 font-semibold">DATACRAFT</div>
      <div className="ml-auto flex space-x-8 pr-6">
        <a
          href="https://github.com/helios2003/Interface-Labs"
          target="_blank"
          rel="noopener noreferrer"
          className="hover:text-gray-600 transition-colors duration-300"
        >
          <FaGithub className="h-10 w-10 cursor-pointer" />
        </a>
        <a
          href="mailto:ankitdash2019@gmail.com"
          className="hover:text-gray-600 transition-colors duration-300"
        >
          <IoMdMail className="h-10 w-10 cursor-pointer" />
        </a>
        <a
          href="tel:+91xxxxxx"
          className="hover:text-gray-600 transition-colors duration-300"
        >
          <FaPhoneAlt className="h-9 w-9 cursor-pointer" />
        </a>
      </div>
    </div>
  );
}
