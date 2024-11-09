import { query } from "./_generated/server.js";

export const get = query({
  handler: async ({ db }) => {
    return await db.query("tasks").collect();
  },
});