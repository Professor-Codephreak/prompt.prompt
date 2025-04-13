# Billing

* On this page

  + [Why use the paid tier?](#paid-tier)
  + [Cloud Billing](#cloud-billing)

  + [What am I billed for?](#what-am-i-billed-for)
  + [Where can I view my quota?](#where-can-i-view-my-quota)
  + [How do I request more quota?](#how-do-i-request-more-quota)
  + [Can I use the Gemini API for free in EEA (including EU), the UK, and CH?](#is-Gemini-free-in-EEA-UK-CH)
  + [If I set up billing with the Gemini API, will I be charged for my Google AI Studio usage?](#is-AI-Studio-free)
  + [Can I use 1M tokens in the free tier?](#can-i-use-1m-tokens-for-free)
  + [How can I calculate the number of tokens I'm using?](#count-tokens)
  + [Can I use my Google Cloud credits with the Gemini API?](#cloud-credits)
  + [How is billing handled?](#how-is-billing-handled)
  + [Am I charged for failed requests?](#am-i-charged-for-failed-requests)
  + [Is there a charge for fine-tuning the models?](#is-fine-tuning-free)
  + [Is GetTokens billed?](#is-gettokens-billed)
  + [How is my Google AI Studio data handled if I have a paid API account?](#paid-api-ai-studio)
  + [Where can I get help with billing?](#get-help)

This guide provides an overview of different Gemini API billing options,
explains how to enable billing and monitor usage, and provides answers to
frequently asked questions (FAQs) about billing.

[Upgrade to the Gemini API paid tier](https://aistudio.google.com/plan_information)

## About billing

Billing for the Gemini API is based on two pricing tiers: *free of charge*
(or *free*) and *pay-as-you-go* (or *paid*). Pricing and rate limits differ
between these tiers and also vary by model. You can check out the [rate limits](/gemini-api/docs/rate-limits)
and [pricing](/gemini-api/docs/pricing) pages for more into. For a model-by-model
breakdown of capabilities, see the [Gemini models page](/gemini-api/docs/models/gemini).

#### How to request an upgrade

The Gemini API uses Cloud Billing for all billing services. To transition from
the Free tier to a paid tier, you must first
[enable Cloud Billing](#enable-cloud-billing) for your Google Cloud project.

When your project meets the specified criteria, it becomes eligible for an
upgrade to the next tier. To request an upgrade, follow these steps:

1. Go to the [AI Studio API keys page](https://aistudio.google.com/app/apikey).
2. Find the project you want to upgrade and click **Upgrade**.
3. The system will automatically verify your project's eligibility. This process
   takes a few seconds.
4. If your project meets all the requirements, it will be instantly upgraded to
   the next tier.

### Why use the paid tier?

When you enable billing and use the paid tier, you benefit from [higher rate limits](/gemini-api/docs/rate-limits),
and your prompts and responses aren't used to improve Google products.
For more information on data use for paid services, see the
[terms of service](/gemini-api/terms#data-use-paid).

### Cloud Billing

The Gemini API uses
[Cloud Billing](https://cloud.google.com/billing/docs/concepts)
for billing services. To use the paid tier, you must set up Cloud Billing on
your cloud project. After you've enabled Cloud Billing, you can use Cloud
Billing tools to track spending, understand costs, make payments, and access
Cloud Billing support.

## Enable billing

You can enable Cloud Billing starting from Google AI Studio:

1. Open [Google AI Studio](https://aistudio.google.com/).
2. In the bottom of the left sidebar, select **Settings** >
   **Plan information**.
3. Click **Set up Billing** for your chosen project to enable Cloud Billing.

## Monitor usage

After you enable Cloud Billing, you can monitor your usage of the Gemini API in
the
[Google Cloud console](https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com).
The service name for the API is `generativelanguage.googleapis.com`, and in the
console the Gemini API is also referred to as the **Generative Language API**.

![Cloud console](/static/gemini-api/docs/images/console-apis-services.png)

To learn more, see the Google Cloud documentation on
[monitoring API usage](https://cloud.google.com/apis/docs/monitoring).

## Frequently asked questions

This section provides answers to frequently asked questions.

### What am I billed for?

Gemini API pricing is based on the following:

* Input token count
* Output token count
* Cached token count
* Cached token storage duration

For pricing information, see the [pricing page](/pricing).

### Where can I view my quota?

You can view your quota and system limits in the
[Google Cloud console](https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas).

### How do I request more quota?

To request more quota, follow the instructions at
[How to request an upgrade](#request-an-upgrade).

### Can I use the Gemini API for free in EEA (including EU), the UK, and CH?

Yes, we make the free tier and paid tier available in
[many regions](/gemini-api/docs/available-regions).

### If I set up billing with the Gemini API, will I be charged for my Google AI Studio usage?

No, Google AI Studio usage remains free of charge regardless of if you set up
billing across all supported regions.

### Can I use 1M tokens in the free tier?

The free tier for Gemini API differs based on the model selected. For now, you
can try the 1M token context window in the following ways:

* In Google AI Studio
* With pay-as-you-go plans
* With free-of-charge plans for select models

See the latest free-of-charge rate limits per model on [rate limits page](/gemini-api/docs/rate-limits).

### How can I calculate the number of tokens I'm using?

Use the
[`GenerativeModel.count_tokens`](/api/python/google/generativeai/GenerativeModel#count_tokens)
method to count the number of tokens. Refer to the
[Tokens guide](/gemini-api/docs/tokens) to learn more about tokens.

### Can I use my Google Cloud credits with the Gemini API?

Yes, Google Cloud credits can be used towards Gemini API usage.

### How is billing handled?

Billing for the Gemini API is handled by the
[Cloud Billing](https://cloud.google.com/billing/docs/concepts) system.

### Am I charged for failed requests?

If your request fails with a 400 or 500 error, you won't be charged for the
tokens used. However, the request will still count against your quota.

### Is there a charge for fine-tuning the models?

[Model tuning](/gemini-api/docs/model-tuning) is free, but inference on tuned
models is charged at the same rate as the base models.

### Is GetTokens billed?

Requests to the GetTokens API are not billed, and they don't count against
inference quota.

### How is my Google AI Studio data handled if I have a paid API account?

Refer to the [terms](/gemini-api/terms#paid-services) for details on how data is
handled when Cloud billing is enabled (see "How Google Uses Your Data" under
"Paid Services"). Note that your Google AI Studio prompts are treated under the
same "Paid Services" terms so long as at least 1 API project has billing enabled,
which you can validate on the [Gemini API Key page](https://aistudio.google.com/apikey)
if you see any projects marked as "Paid" under "Plan".

### Where can I get help with billing?

To get help with billing, see
[Get Cloud Billing support](https://cloud.google.com/support/billing).

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-25 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-25 UTC."],[],[]]