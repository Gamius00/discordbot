
import { v } from "convex/values";
import {mutation} from "./_generated/server";

export const createEntry = mutation({
    args: { count: v.number() },
    handler: async (ctx, args) => {
        await ctx.db.insert("serverInformations", { MemberCount: args.count });
    },
});