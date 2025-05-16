"use client";

import { IoIosInformationCircle } from "react-icons/io";
import { GoFileDirectoryFill } from "react-icons/go";
import Link from "next/link";
import Image from "next/image";
import { FaUserGroup } from "react-icons/fa6";
import { IoNewspaper } from "react-icons/io5";
import { Kaushan_Script } from "next/font/google";
import { Menu, X } from "lucide-react";
import { useState } from "react";

const kaushanScript = Kaushan_Script({
  subsets: ["latin"],
  weight: ["400"], // Kaushan Script hat nur 400
  display: "swap",
});

const Navbar = () => {
  const Navbar_Items = [
    {
      name: "About",
      Icon: <IoIosInformationCircle />,
      link: "/",
    },
    {
      name: "Projects",
      Icon: <GoFileDirectoryFill />,
      link: "/projects",
    },
    {
      name: "Team",
      Icon: <FaUserGroup />,
      link: "/team",
    },
  ];

  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <div className="fixed flex w-full bg-background">
      <div className="align-center ml-5 flex p-4 lg:ml-7">
        <Image
          className="h-9 w-9 rounded-lg"
          src={"/Images/creativeProgrammersLogo.png"}
          alt={"Creative Programmers"}
          width="55"
          height="35"
        />{" "}
        <div className={kaushanScript.className}>
          <p className="ml-3 mt-1 w-60 text-lg">Creative Programmers</p>
        </div>
      </div>
      <div className="flex w-11/12 justify-end lg:hidden">
        <p className="mr-6 mt-6">
          {!menuOpen ? (
            <Menu
              className="flex lg:hidden"
              onClick={() => {
                setMenuOpen(!menuOpen);
              }}
            />
          ) : (
            <X
              className="flex lg:hidden"
              onClick={() => {
                setMenuOpen(!menuOpen);
              }}
            />
          )}
        </p>
      </div>

      {menuOpen ? (
        <div
          style={{ borderBottom: "1px solid #383838" }}
          className="absolute mt-16 flex w-full flex-col items-center bg-background pb-7 pt-4 lg:hidden"
        >
          {Navbar_Items.map((item, index) => {
            return (
              <Link
                href={item.link}
                onClick={() => {
                  setMenuOpen(!menuOpen);
                }}
                key={index}
                className="flex cursor-pointer rounded-md p-1.5 px-5"
              >
                {" "}
                <p className={"mr-1.5 mt-1.5 text-lg"}>{item.Icon}</p>{" "}
                <p className="text-lg">{item.name}</p>
              </Link>
            );
          })}
        </div>
      ) : null}
      <div className="hidden w-11/12 justify-end lg:flex">
        <div className="flex w-[600px] justify-around p-5">
          {Navbar_Items.map((item, index) => {
            return (
              <Link
                href={item.link}
                key={index}
                className="flex cursor-pointer rounded-md p-1.5 px-5"
              >
                {" "}
                <p className={"mr-1.5 mt-1.5 text-lg"}>{item.Icon}</p>{" "}
                <p className="text-lg">{item.name}</p>
              </Link>
            );
          })}
        </div>
      </div>
    </div>
  );
};

export default Navbar;
