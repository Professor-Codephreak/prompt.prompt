# Rate limits

* On this page

  + [Live API rate limits](#live-api)

Rate limits regulate the number of requests you can make to the Gemini API
within a given timeframe. These limits help ensure fair usage, protect against
abuse, and help maintain system performance for all users.

## How rate limits work

Rate limits are measured across three dimensions:

* Requests per minute (**RPM**)
* Requests per day (**RPD**)
* Tokens per minute (**TPM**)

Your usage is evaluated against each limit, and exceeding any of them will
trigger a rate limit error. For example, if your RPM limit is 20, making 21
requests within a minute will result in an error, even if you haven't exceeded
your TPM or other limits.

Rate limits are applied per project, not per API key.

Limits vary depending on the specific model being used, and some limits only
apply to specific models. For example, Images per minute, or IPM, is only
calculated for models capable of generating images (Imagen 3), but is
conceptually similar to TPM.

## Usage tiers

Rate limits are tied to the projects usage tier (which we will soon be rolling
out). As your API usage and spending increase, you'll have an option to upgrade
to a higher tier with increased rate limits.

| Tier | Qualifications |
| --- | --- |
| Free | Users in [eligible countries](/gemini-api/docs/available-regions) |
| Tier 1 | Billing account [linked to the project](/gemini-api/docs/billing#enable-cloud-billing) |
| Tier 2 | Total spend: $250 + at least 30 days since successful payment |
| Tier 3 | Total spend: $1,000 + at least 30 days since successful payment |

When you request an upgrade, our automated abuse protection system performs
additional checks. While meeting the stated qualification criteria is generally
sufficient for approval, in rare cases an upgrade request may be denied based on
other factors identified during the review process.

This system helps ensure the security and integrity of the Gemini API platform
for all users.

## Current rate limits

[Free Tier](#free-tier)[Tier 1](#tier-1)[Tier 2](#tier-2)[Tier 3](#tier-3)
More

| Model | RPM | TPM | RPD |
| --- | --- | --- | --- |
| Gemini 2.5 Pro Experimental | 5 | 1,000,000 | 25 |
| Gemini 2.5 Pro Preview | -- | -- | -- |
| Gemini 2.0 Flash | 15 | 1,000,000 | 1,500 |
| Gemini 2.0 Flash Experimental (including image generation) | 10 | 1,000,000 | 1,500 |
| Gemini 2.0 Flash-Lite | 30 | 1,000,000 | 1,500 |
| Gemini 2.0 Flash Thinking Experimental 01-21 | 10 | 4,000,000 | 1,500 |
| Gemini 1.5 Flash | 15 | 1,000,000 | 1,500 |
| Gemini 1.5 Flash-8B | 15 | 1,000,000 | 1,500 |
| Gemini 1.5 Pro | 2 | 32,000 | 50 |
| Veo 2 | -- | -- | -- |
| Imagen 3 | -- | -- | -- |
| Gemma 3 | 30 | 15,000 | 14,400 |
| Gemini Embedding Experimental 03-07 | 5 | -- | 100 |

| Model | RPM | TPM | RPD |
| --- | --- | --- | --- |
| Gemini 2.5 Pro Experimental | -- | -- | -- |
| Gemini 2.5 Pro Preview | 150 | 2,000,000 | 1,000 |
| Gemini 2.0 Flash | 2,000 | 4,000,000 | -- |
| Gemini 2.0 Flash Experimental (including image generation) | 10 | 4,000,000 | -- |
| Gemini 2.0 Flash-Lite | 4,000 | 4,000,000 | -- |
| Gemini 2.0 Flash Thinking Experimental 01-21 | 10 | 4,000,000 | -- |
| Gemini 1.5 Flash | 2,000 | 4,000,000 | -- |
| Gemini 1.5 Flash-8B | 4,000 | 4,000,000 | -- |
| Gemini 1.5 Pro | 1,000 | 4,000,000 | -- |
| Imagen 3 | -- | 20 images per minute (IPM) | -- |
| Veo 2 | 2 | -- | 50 |
| Gemma 3 | 30 | 15,000 | 14,400 |
| Gemini Embedding Experimental 03-07 | 10 | -- | 1,000 |

| Model | RPM | TPM | RPD |
| --- | --- | --- | --- |
| Gemini 2.5 Pro Experimental | -- | -- | -- |
| Gemini 2.5 Pro Preview | 1,000 | 5,000,000 | 50,000 |
| Gemini 2.0 Flash | 10,000 | 10,000,000 | -- |
| Gemini 2.0 Flash Experimental (including image generation) | 10 | 4,000,000 | -- |
| Gemini 2.0 Flash-Lite | 4,000 | 4,000,000 | -- |
| Gemini 2.0 Flash Thinking Experimental 01-21 | 10 | 4,000,000 | -- |
| Gemini 1.5 Flash | 2,000 | 4,000,000 | -- |
| Gemini 1.5 Flash-8B | 4,000 | 4,000,000 | -- |
| Gemini 1.5 Pro | 1,000 | 4,000,000 | -- |
| Imagen 3 | -- | 20 images per minute (IPM) | -- |
| Veo 2 | -- | -- | -- |
| Gemma 3 | 30 | 15,000 | 14,400 |
| Gemini Embedding Experimental 03-07 | 10 | -- | 1,000 |

| Model | RPM | TPM | RPD |
| --- | --- | --- | --- |
| Gemini 2.5 Pro Preview | 2,000 | 8,000,000 | -- |

Specified rate limits are not guaranteed and actual capacity may vary.

### Live API rate limits

[Free Tier](#free-tier)[Tier 1](#tier-1)[Tier 2](#tier-2)[Tier 3](#tier-3)
More

| Number of concurrent sessions | TPM |
| --- | --- |
| 3 | 1,000,000 |

| Number of concurrent sessions | TPM |
| --- | --- |
| 50 | 4,000,000 |

| Number of concurrent sessions | TPM |
| --- | --- |
| 1000 | 10,000,000 |

| Number of concurrent sessions | TPM |
| --- | --- |
| Not yet available | Not yet available |

Specified rate limits are not guaranteed and actual capacity may vary.

## How to upgrade to the next tier

The Gemini API uses Cloud Billing for all billing services. To transition from
the Free tier to a paid tier, you must first enable Cloud Billing for your
Google Cloud project.

Once your project meets the specified criteria, it becomes eligible for an
upgrade to the next tier. To request an upgrade, follow these steps:

* Navigate to the [API keys page](https://aistudio.google.com/app/apikey) in AI Studio.
* Locate the project you want to upgrade and click "Upgrade". The "Upgrade" option
  will only show up for projects that meet [next tier qualifications](/gemini-api/docs/rate-limits#usage-tiers).

After a quick validation, the project will be upgraded to the next tier.

## Request a rate limit increase

Each model variation has an associated rate limit (requests per minute, RPM).
For details on those rate limits, see [Gemini models](/models/gemini).

[Request paid tier rate limit increase](https://forms.gle/ETzX94k8jf7iSotH9)

We offer no guarantees about increasing your rate limit, but we'll do our best
to review your request and reach out to you if we're able to accommodate your
capacity needs.

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-08 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-08 UTC."],[],[]]