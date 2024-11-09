
import { v } from "convex/values";
import {mutation} from "./_generated/server";

export const createEntry = mutation({
    args: { text: v.string() },
    handler: async (ctx, args) => {
        await ctx.db.insert("tasks", { text: args.text });
    },
});