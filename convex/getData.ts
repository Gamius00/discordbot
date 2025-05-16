import { query } from "./_generated/server.js";

export const getTasks = query({
  handler: async ({ db }) => {
    const data = await db.query("tasks").collect()
    return await db.query("tasks").collect();
  },
});

export const getMemberCount = query({
  handler: async ({ db }) => {
    const [last] = await db.query("serverInformations").order("desc").take(1);
    return last ?? null;
  }
})

export const getInfo = query({
  handler: async ({ db }) => {
    const data = await db.query("serverInformations").collect()

    if (!data) {return}

    const groupedByDay = data.reduce<Record<string, any>>((acc, entry) => {
      const date = new Date(entry._creationTime).toISOString().split("T")[0];

      if (!acc[date!] || acc[date!]._creationTime < entry._creationTime) {
        acc[date!] = entry;
      }

      return acc;
}, {});

const latestEntries = Object.values(groupedByDay);
    return latestEntries;
  },
});