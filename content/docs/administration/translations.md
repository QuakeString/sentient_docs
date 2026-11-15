+++
title = "Translations"
description = "Show SENTIENT and your own dashboards in your users' languages: translation engines, the offline translator, the glossary, and changing the UI's own texts."
weight = 173

[extra]
status = "checked"
checked = "4.3.0.57"
+++
SENTIENT translates two kinds of text:

- **The UI's own texts**, such as menu items, buttons and messages. They ship in 63 languages. The system administrator can change any of them and add languages.
- **Your content**: dashboard titles, widget titles and labels, alarm types, notification and report templates. A tenant chooses its languages, and SENTIENT translates new and changed texts in the background with the translation engines you set up.

Each user picks a language in their profile: the user menu at the top right, then **Account**, then **Language**. Dashboards, alarms and notifications then show in that language wherever a translation exists, and in the original text where none does.

Open **Settings > Translations** in the left menu. A tenant administrator sees the tabs **Languages**, **Texts**, **Glossary** and **Engines**; the system administrator sees **Languages**, **App texts** and **Engines**.

## Translate your content (tenant)

### 1. Choose the languages

On **Languages**, click **Add language** for each language your users read. The table shows how much of your content is **Translated** in each; **Show texts** opens that language's texts. The **Default source language** is used when a text's script fits several languages.

### 2. Add a translation engine

On **Engines**, click **Add engine**. Engines are tried from the top: a text one engine cannot translate goes to the next. Use **Try earlier** and **Try later** to change the order, and **Use only for** to limit an engine to some languages.

| Engine | Use it when |
|---|---|
| **SENTIENT translator** | You want translation without the internet. It runs on any machine that reaches the server. See below |
| **Google Cloud Translation** | You have a Google Cloud API key. Covers every language |
| **Google Gemini**, **Claude (Anthropic)**, **OpenAI/Compatible** | You have an API key for one of these, or a local model through Ollama, vLLM or LM Studio |
| **AI model** | You already added a chat model under [AI models](/docs/ai/models/). Requests count toward your AI usage |
| **LibreTranslate/Compatible** | You run a LibreTranslate server |
| **DeepL** | Strong for European and East Asian languages. Free keys end in `:fx` |

**Test** sends a sample text through the engine before you save. Engines the system administrator shares show as **Shared by system**: you can switch them off or put another engine before them, but you do not see their settings.

Placeholders such as `${value}`, codes such as `PLC-002-xyz` and glossary terms are kept as written in every translation.

### 3. Translate

With **Translate new texts automatically when a dashboard is saved** on, only new and changed texts are translated, in the background, after each save. To translate everything that already exists:

1. On **Texts**, click **Scan existing content** once. It finds the texts of dashboards, alarm types, notification and report templates saved before translation was turned on.
2. Click **Translate missing**. A progress bar shows the language being translated and the time left. From its menu you can translate one language only, or **Translate again** to replace machine translations.

Viewers see new translations the next time they open the page.

### 4. Review

**Texts** lists every source text with its translation, its **Status** and where it is **Used in** (dashboard title, widget title, data key label, alarm type, and so on). Click a translation to type your own.

| Status | Meaning |
|---|---|
| **Machine** | Translated by an engine |
| **Reviewed** | Checked by a person (**Mark reviewed**) |
| **Manual** | Typed by a person |
| **Missing** | No translation yet |
| **Changed** / **Outdated** | The source text changed after it was translated |
| **Don't translate** | Kept as written in every language (**Don't translate** on the row) |

Reviewed and manual translations are never replaced by machine translation. **Export** and **Import JSON** move translations to and from a file, for one language or all of them, for example to send them to a translator.

### While you edit

In a widget's settings and in the alarm rule dialog, a **Translations** section shows how many of the item's texts are missing, **Translate now**, and an **Add translation** field per language. In the dashboard editor, **Preview in** shows the dashboard in another language without saving anything.

## The glossary

**Glossary** holds words that need a fixed treatment in every translation:

| Treatment | Example |
|---|---|
| **Keep** | `PLC`, `VFD`, `HH` stay exactly as written |
| **Fixed translation** | `Kiln` is always translated the way your plant says it. Languages left empty keep the term as written |
| **Expand** | `brg` is replaced by `bearing` before translating |

Turn on **Match case** for terms where case matters. A changed glossary applies to texts translated from then on; existing translations stay as they are.

## The SENTIENT translator

The SENTIENT translator is an offline translation service you install yourself, like a gateway. Add it from **Engines > Add engine > SENTIENT translator**:

1. **Configure**: give it a name and choose how SENTIENT reaches it.
   - **The translator connects to SENTIENT** (recommended): it opens the connection, so no port or firewall change is needed.
   - **SENTIENT connects to the translator**: for the same machine or local network, at an address such as `http://127.0.0.1:5100`.
2. Choose the **Language packs**. Each shows its download size, memory use and languages. Some packs allow non-commercial use only; you must accept their licence.
3. **Install**: copy the Docker Compose file or the Linux install command shown, with its **Access token**, and run it on the translator machine. The dialog shows **Connected** once it starts.

The access token is shown only once. **New access token** on the engine replaces it; the old one stops working.

The engine then shows its state (**Online**, **Offline**, **Waiting for connection**), host, CPU and memory, queue and speed, and which of your languages its packs cover. Languages it often gets wrong are marked **weak offline**: use an online engine for them if you can, and review the results.

A system administrator can add a translator with **Share with all tenants**, so tenants can use it without setting up their own.

## Change the UI's own texts (system administrator)

**App texts** lists every UI text by key, with the English text and the text in the chosen language. Click a text to change it; Enter saves, Esc cancels. Changed texts replace the shipped ones for every user and can be **Reset** at any time. Filter by **Changed**, **Not translated** or **Outdated**, the last meaning the English text changed after yours was saved.

- **Translate missing** machine-translates the texts not yet translated in that language, with the engines on the **Engines** tab.
- **More > Export changes** and **Import JSON** move your changes between servers.
- **Reset** returns the whole language to the shipped texts.

**Languages** lists every UI language with its coverage. **Add language** adds one the UI does not ship: a language code such as `ha_NG`, its name in the language itself, its English name, whether it is written right to left, and whether to show numbers in its **Native digits** (on screen only; exported data keeps 0-9). Texts not translated in an added language show in English.

## Related

- [AI models](/docs/ai/models/)
- [Dashboards](/docs/user-guide/dashboards/)
