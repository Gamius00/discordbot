"use client";

import Link from "next/link";
import Image from "next/image";

const Projects = () => {
  const Projects = [
    {
      name: "Weather.io",
      picture: "/Images/weatherio.png",
      link: "https://weatherio1.vercel.app/de/home?cityId=j578kecpb8an217c6w7c01nh256pzw1g",
    },
    {
      name: "Chat.io",
      picture: "/Images/chatio.png",
      link: "https://chat-io.roessner.tech/",
    },
  ];

  return (
    <div className="flex min-h-screen w-full items-center justify-around">
      <div className="flex w-full flex-wrap justify-center gap-10">
        {Projects.map((item, index) => {
          return (
            <div
              key={index}
              onClick={() => {
                window.location.href = item.link;
              }}
              style={{
                backgroundColor: "#1E1E1E",
                border: "1px solid #383838",
              }}
              className="flex cursor-pointer flex-col items-center rounded-lg p-5 px-7"
            >
              <Image
                width={200}
                height={30}
                className="rounded-lg"
                src={item.picture}
                alt={item.name}
              />
              <Link href={item.link} className="flex cursor-pointer rounded-md">
                {" "}
                <p className="mt-4 text-lg font-semibold">{item.name}</p>
              </Link>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Projects;
