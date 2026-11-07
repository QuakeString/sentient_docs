+++
title = "AI models"
description = "Connect SENTIENT to AI models from cloud providers or a local Ollama server, for the AI assistant, the AI rule node and script help."
aliases = ["/docs/ai-models/"]
weight = 156

[extra]
status = "checked"
checked = "4.3.0.57"
+++
An **AI model** entry tells SENTIENT how to reach a large language model: the provider, the model and the key. SENTIENT then uses it for the [AI assistant](/docs/ai/assistant/), the **AI request** rule node, and help with writing scripts.

Open **Settings > AI models** and click **+**.

## Where the model runs

| Choice | Data leaves the site | Use it when |
|---|---|---|
| **Ollama** on a server in your network | No | The plant must stay offline, or data must not leave the site |
| A cloud provider | Yes: the text of each request goes to the provider | The server reaches the internet and your company allows it |

For an offline plant, run [Ollama](https://ollama.com) on a PC with a suitable GPU inside the network and add it here. Small local models are less capable than large cloud models; test the tasks you need.

## Providers

| Provider | Enter |
|---|---|
| **OpenAI** | **API key**, **Model ID** such as `gpt-5-mini` |
| **Azure OpenAI** | **API key**, **Endpoint**, **Deployment name**, **Service version** |
| **Google AI Gemini** | **API key**, **Model ID** |
| **Mistral AI** | **API key**, **Model ID** |
| **Anthropic** | **API key**, **Model ID** |
| **GitHub Models** | **Personal access token**, **Model ID** |
| **Ollama** | **Base URL** such as `http://192.168.10.5:11434`, **Model ID** such as `llama3.1:8b`, and **Authentication**: **None**, **Basic** (user name and password) or **Token** |

> **Note for 4.3.0.57:** **Amazon Bedrock** and **Google Vertex AI Gemini** can be chosen but do not work yet: requests fail with a message saying so.

Keys are stored encrypted and shown masked after you save.

### Model settings

**Temperature**, **Top P**, **Top K**, **Presence penalty**, **Frequency penalty** and **Maximum output tokens** tune the answers; leave them empty for the provider's defaults. For Ollama, **Context length** sets how much text the model can take in at once: raise it for long conversations if the GPU has the memory.

Click **Check connectivity** to send a test request, then **Save**.

## System models and tenant models

- Models the **system administrator** adds are **system models**. Tenants can use them without seeing the key or the address, if their [tenant profile](/docs/user-guide/tenant-profiles/) allows **system AI models**. The profile can limit tokens per month and requests per minute.
- A **tenant administrator** can add the tenant's own models, if the tenant profile allows **own AI models**. Switch that off where data must not leave the site.

## Related

- [AI assistant](/docs/ai/assistant/)
- [Tenant profiles](/docs/user-guide/tenant-profiles/)
