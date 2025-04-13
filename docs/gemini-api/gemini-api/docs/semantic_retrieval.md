# Gemini Developer API

[Get a Gemini API Key](https://aistudio.google.com/apikey)

Get a Gemini API key and make your first API request in minutes.

[Python](#python)[JavaScript](#javascript)[REST](#rest)
More

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)

```
```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "YOUR_API_KEY" });

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.0-flash",
    contents: "Explain how AI works",
  });
  console.log(response.text);
}

await main();

```
```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=YOUR_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'

```

## Meet the models

[Use Gemini in Google AI Studio](https://aistudio.google.com)

2.5 Pro
experiment

Our most powerful thinking model with features for complex reasoning and much more

2.0 Flash
spark

Our newest multimodal model, with next generation features and improved
capabilities

2.0 Flash-Lite
bolt

Our fastest and most cost-efficient multimodal model with great performance
for high-frequency tasks

## Explore the API

![](/static/site-assets/images/image-generation-index.png)

### Native Image Generation

Generate and edit highly contextual images natively with Gemini 2.0 Flash.

![](/static/site-assets/images/long-context-overview.png)

### Explore long context

Input millions of tokens to Gemini models and derive understanding from unstructured images, videos, and documents.

![](/static/site-assets/images/structured-outputs-index.png)

### Generate structured outputs

Constrain Gemini to respond with JSON, a structured data format suitable for automated processing.

### Start building with the Gemini API

[Get started](/gemini-api/docs/quickstart)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-04 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-04 UTC."],[],[]]