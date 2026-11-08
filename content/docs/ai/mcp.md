+++
title = "MCP server"
description = "Let AI tools such as Claude Code work on SENTIENT through the Model Context Protocol, with the permissions of the user whose API key they use."
weight = 158

[extra]
status = "checked"
checked = "4.3.0.57"
+++
SENTIENT has a **Model Context Protocol (MCP) server**. With it, an AI tool on an engineer's computer, such as Claude Code or Cursor, can read and change SENTIENT the way the [AI assistant](/docs/ai/assistant/) does: build dashboards, rule chains, calculated fields, or check a setup.

Every request runs as the owner of the API key, with exactly that user's permissions, and is recorded in the audit log. MCP cannot do anything the user could not do in the browser.

## Turn it on

MCP is off until the system administrator enables it.

1. Sign in as the system administrator and open **Settings > MCP server**.
2. Tick **Enable MCP server**.
3. Under **Tenant profiles allowed to use MCP**, choose the tenant profiles whose tenant administrators may connect. System administrators can always connect while MCP is enabled; customer users never can.
4. **Save**.

## Connect an AI tool

1. Open **Settings > MCP server** as the user the tool should act as. It shows the **Endpoint URL**, `https://<your server>/api/mcp`.
2. Under **API keys**, create a key and copy it. You see its value only once.
3. Run the command shown under **Connect an MCP client**, with your key in place of the placeholder. For Claude Code:

   ```sh
   claude mcp add --transport http sentient https://<your server>/api/mcp --header "Authorization: ApiKey <your key>"
   ```

Other MCP clients take the same URL and the header `Authorization: ApiKey <your key>`.

> An API key can do exactly what you can do. Keep it like a password, give each tool its own key, and delete keys you no longer use. Use HTTPS: over plain HTTP the key travels unencrypted.

The keys are also listed under your user's **API keys** tab, with their **Status** and when they were **Last used**.

If the page says **MCP is not available to this tenant**, ask the system administrator to add your tenant profile.

## Related

- [AI assistant](/docs/ai/assistant/)
- [AI models](/docs/ai/models/)
