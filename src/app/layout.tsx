import "~/styles/globals.css";

import { GeistSans } from "geist/font/sans";
import { type Metadata } from "next";
import { ConvexClientProvider } from "./ConvexClientProvider";
import Navbar from "~/app/components/navbar";
import React from "react";
import { Inter, Kaushan_Script } from "next/font/google";

export const metadata: Metadata = {
  title: "Creative Programmers",
  description: "The official Website of the Creative Programmer Group.",
  icons: [{ rel: "icon", url: "/public/Images/creativeProgrammersLogo.png" }],
};

const Inter_Font = Inter({
  subsets: ["latin"],
  weight: ["400"], // Kaushan Script hat nur 400
  display: "swap",
});

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en" className={Inter_Font.className}>
      <body className={"bg-background text-white"}>
        <Navbar />
        <ConvexClientProvider>{children}</ConvexClientProvider>
      </body>
    </html>
  );
}
