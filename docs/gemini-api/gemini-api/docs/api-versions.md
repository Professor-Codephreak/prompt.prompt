# API versions explained

* On this page

This document provides a high-level overview of the differences between the `v1`
and `v1beta` versions of the Gemini API.

* **v1**: Stable version of the API. Features in the stable version are
  fully-supported over the lifetime of the major version. If there are any
  breaking changes, then the next major version of the API will be created and
  the existing version will be deprecated after a reasonable period of time.
  Non-breaking changes may be introduced to the API without changing the major
  version.
* **v1beta**: This version includes early-access features that may be under
  development and is subject to rapid and breaking changes. There is also no
  guarantee that the features in the Beta version will move to the stable
  version. Due to this instability, you should consider not launching production
  applications with this version.

| Feature | v1 | v1beta |
| --- | --- | --- |
| Generate Content - Text-only input |  |  |
| Generate Content - Text-and-image input |  |  |
| Generate Content - Text output |  |  |
| Generate Content - Multi-turn conversations (chat) |  |  |
| Generate Content - Function calls |  |  |
| Generate Content - Streaming |  |  |
| Embed Content - Text-only input |  |  |
| Generate Answer |  |  |
| Semantic retriever |  |  |

* - Supported
* - Will never be supported

## Configure API version in an SDK

The Gemini API SDK's default to `v1beta`, but you can opt to use other versions
by setting the API version as shown in the following code sample:

[Python](#python)[JavaScript](#javascript)[REST](#rest)
More

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY",
                      http_options={'api_version': 'v1alpha'})

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents="Explain how AI works",
)

print(response.text)

```
```
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  apiKey: "YOUR_API_KEY",
  httpOptions: { apiVersion: "v1alpha" },
});

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
curl "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key=YOUR_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "Explain how AI works."}]
    }]
   }'

```

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-25 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-25 UTC."],[],[]]