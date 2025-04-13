# Gemini API reference

* On this page

The Gemini API lets you access the latest generative models from Google. This
API reference provides detailed information for the classes and methods
available in the Gemini API SDKs. Pick a language and follow the setup steps
to get started building.

Python
JavaScript
Go
Apps Script

## Install the Gemini API library

**Note:** We're rolling out a new set of Gemini API libraries, the
[Google Gen AI SDK](/gemini-api/docs/sdks).

Using [Python 3.9+](https://www.python.org/downloads/), install the
[`google-genai` package](https://pypi.org/project/google-genai/)
using the following [pip command](https://packaging.python.org/en/latest/tutorials/installing-packages/):

```
pip install -q -U google-genai

```

## Make your first request

Use the
[`generateContent`](/api/generate-content#method:-models.generatecontent) method
to send a request to the Gemini API.

```
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)

```

## What's next

If you're just getting started, check out the following guides, which will help
you understand the Gemini API programming model:

You might also want to check out the capabilities guides, which introduce different
Gemini API features and provide code examples:

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-04 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-04 UTC."],[],[]]