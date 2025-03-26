import { defineEnt, defineEntSchema, getEntDefinitions } from "convex-ents";
import { v } from "convex/values";


const schema = defineEntSchema({
    tasks: defineEnt({})
        .field("text", v.string())
    ,
    serverInformations: defineEnt({})
        .field("MemberCount", v.number())
})


export default schema;

export const entDefinitions = getEntDefinitions(schema);