"use client";

import Link from "next/link";
import Image from "next/image";

const Team = () => {
  const Team = [
    {
      name: "Fabius Schurig",
      picture: "/Images/fabius-schurig.png",
      description: "CO-Founder / Software Developer",
      link: "https://schurig.tech",
    },
    {
      name: "Jakob Rössner",
      picture: "/Images/jakob-roessner.png",
      description: "Founder / Software Developer",
      link: "https://roessner.tech",
    },
    {
      name: "Murtaza Noori",
      picture: "/Images/murtaza-noori.png",
      description: "Developer of Finance.io",
      link: "https://github.com/murtazanoori",
    },
    {
      name: "Iqbal Rahman",
      picture: "/Images/iqbalrahman.png",
      description: "Designer of Weather.io",
      link: "https://www.notion.so/iqbalrh/Hello-I-m-Iqbal-c8e26a91f13b464cb88a89eb1cb1082d?pvs=4",
    },
  ];

  return (
    <div className="flex min-h-screen w-full items-center justify-around">
      <div className="mt-32 flex w-full flex-wrap justify-center gap-10 lg:mt-12 xl:mt-0">
        {Team.map((item, index) => {
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
                <p className="mt-4 text-lg font-semibold">{item.name}</p>
              </Link>
              <div className="text-sm">{item.description}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Team;
