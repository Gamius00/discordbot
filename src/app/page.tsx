"use client";

import React from "react";
import { useQuery } from "convex/react";
import "~/styles/globals.css";
import { api } from "convex/_generated/api";
import Image from "next/image";

export default function HomePage() {
  const getMemberCount = useQuery(api.getData.getMemberCount);

  return (
    <main className="flex min-h-screen flex-1 items-center justify-center">
      <div className="mt-32 flex flex-col items-center lg:mt-12 xl:mt-0">
        <div className="ml-5 flex w-10/12 items-center justify-center gap-3 lg:ml-0 lg:w-full">
          <Image
            className="rounded-xl"
            src="/Images/creativeProgrammersLogo.png"
            alt="Creative Programmers"
            width={55}
            height={55}
          />
          <div>
            <p className="w-10/12 truncate text-lg font-semibold lg:w-full lg:text-xl">
              The Creative Programmer Group
            </p>
            <div className={"mt-1 flex"}>
              <div className="mr-1.5 mt-1 h-2.5 w-2.5 rounded-full bg-gray-500"></div>
              <p className="text-sm font-medium text-gray-500">
                Membercount: {getMemberCount?.MemberCount}
              </p>
            </div>
          </div>
        </div>
        <div className="mt-12 flex w-full justify-center">
          <button
            onClick={() => {
              window.location.href = "https://discord.gg/PxAaKhUS6a";
            }}
            style={{ backgroundColor: "#44447C" }}
            className="rounded-lg p-2 px-6"
          >
            Join
          </button>
        </div>
        <div className="mt-14 flex w-full flex-col items-center justify-center">
          <p className="w-10/12 font-semibold italic lg:w-auto">
            The Story about the Creative Programmers Group?
          </p>
          <p className="mt-3 w-10/12 lg:w-1/3">
            The Creative Programmer Group was founded in February 2023 by Jakob
            Roessner. Fabius Schurig joined the group in March 2023. That same
            month, the team began working on its first project, Weather.io. The
            Creative Programmer Group actively developed the application for
            over nine months. In January 2024, the idea for Chat.io, a
            post-quantum secure messenger, was conceived. More than 11 months of
            intensive design and development went into the application. The
            applications are using more than 30+ people every day.{" "}
          </p>
        </div>
        <div className="mt-14 flex w-full flex-col items-center justify-center">
          <p className="w-10/12 font-semibold italic lg:w-auto">
            Why is the Creative Programmer Group better thann others?
          </p>
          <p className="mt-3 w-10/12 lg:w-1/3">
            The Creative Programmer Group is a team of young and talented
            individuals. With years of experience and a large Discord community,
            it stands out as unique.
          </p>
        </div>
      </div>
    </main>
  );
}
