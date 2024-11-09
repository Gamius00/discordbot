"use client";

import React from "react";
import { useMutation } from "convex/react";
import {api} from "convex/_generated/api";


export default function HomePage() {

    const [CurrentValue, setCurrentValue] = React.useState("");

    const handleInput = (event: React.ChangeEvent<HTMLInputElement>) => {
        setCurrentValue(event.target.value)
    };

    const mutateSomething = useMutation(api.setData.createEntry);

    return (
    <main>
        <h1>Welcome to the Discord Bot Dashboard!</h1>
        <p>A dashboard for managing the Creativo Bot.</p>
        <input value={CurrentValue} onChange={handleInput}/>
        <button onClick={() => mutateSomething({ text: CurrentValue })}>Submit</button>
    </main>
  );
}
