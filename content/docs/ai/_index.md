+++
title = "AI features"
description = "Where SENTIENT uses AI models: the AI assistant, script help, the AI request rule node, asset health questions and MCP for AI tools, and how to keep data on site."
sort_by = "weight"

[extra]
status = "checked"
checked = "4.3.0.57"
+++
SENTIENT can use a large language model to help you build and understand your plant's setup. Nothing AI is switched on until an administrator connects a model.

| Feature | What it does |
|---|---|
| [AI assistant](/docs/ai/assistant/) | A chat panel on every page. It reads what exists, answers questions about your data, and builds dashboards, calculated fields, alarm rules, reports and whole solutions, asking before it changes anything |
| Script help | The ✨ button in script editors writes a script from a description, fixes errors, explains or simplifies it, and can suggest while you type |
| **AI request** rule node | Sends a message's data to a model from a rule chain, for example to summarise an alarm or classify a fault text |
| [Asset health](/docs/asset-health/#ask-the-ai-assistant) | Explains why a machine's health dropped, what changed this week, and drafts work orders |
| [MCP server](/docs/ai/mcp/) | Lets AI tools on an engineer's computer, such as Claude Code, work on SENTIENT with that engineer's permissions |

## Set it up

1. Connect a model under **Settings > AI models**. See [AI models](/docs/ai/models/).
2. The system administrator decides, per tenant profile, which tenants may use the system's models and how much.
3. Open the assistant with the ✨ button at the top right.

## Your data

- With a model on a server in your own network (for example **Ollama**), no data leaves the site. This is the choice for plants that must stay offline.
- With a cloud model, the text of each request, including the data the assistant reads to answer, goes to that provider.
- The assistant and MCP always act **as the signed-in user**: they see and change only what that user may, and every change is in the [audit log](/docs/user-guide/audit-log/).

## In this section

- [AI models](/docs/ai/models/)
- [AI assistant](/docs/ai/assistant/)
- [MCP server](/docs/ai/mcp/)
