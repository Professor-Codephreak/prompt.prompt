# Troubleshooting guide

* On this page

Python
Go

Use this guide to help you diagnose and resolve common issues that arise when
you call the Gemini API. You may encounter issues from either
the Gemini API backend service or the client SDKs. Our client SDKs are
open sourced in the following repositories:

If you encounter API key issues, ensure you have set up
your API key correctly per the [API key setup guide](/tutorials/setup).

## Gemini API backend service error codes

The following table lists common backend error codes you may encounter, along
with explanations for their causes and troubleshooting steps:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **HTTP Code** | **Status** | **Description** | **Example** | **Solution** |
| 400 | INVALID\_ARGUMENT | The request body is malformed. | There is a typo, or a missing required field in your request. | Check the [API reference](/api) for request format, examples, and supported versions. Using features from a newer API version with an older endpoint can cause errors. |
| 400 | FAILED\_PRECONDITION | Gemini API free tier is not available in your country. Please enable billing on your project in Google AI Studio. | You are making a request in a region where the free tier is not supported, and you have not enabled billing on your project in Google AI Studio. | To use the Gemini API, you will need to setup a paid plan using [Google AI Studio](https://aistudio.google.com/app/plan_information). |
| 403 | PERMISSION\_DENIED | Your API key doesn't have the required permissions. | You are using the wrong API key; you are trying to use a tuned model without going through [proper authentication](/docs/model-tuning/tutorial?lang=python#set_up_authentication). | Check that your API key is set and has the right access. And make sure to go through proper authentication to use tuned models. |
| 404 | NOT\_FOUND | The requested resource wasn't found. | An image, audio, or video file referenced in your request was not found. | Check if all [parameters in your request are valid](/docs/troubleshooting#check-api) for your API version. |
| 429 | RESOURCE\_EXHAUSTED | You've exceeded the rate limit. | You are sending too many requests per minute with the free tier Gemini API. | Ensure you're within the model's [rate limit](/models/gemini#model-variations). [Request a quota increase](/docs/increase_quota) if needed. |
| 500 | INTERNAL | An unexpected error occurred on Google's side. | Your input context is too long. | Reduce your input context or temporarily switch to another model (e.g. from Gemini 1.5 Pro to Gemini 1.5 Flash) and see if it works. Or wait a bit and retry your request. If the issue persists after retrying, please report it using the **Send feedback** button in Google AI Studio. |
| 503 | UNAVAILABLE | The service may be temporarily overloaded or down. | The service is temporarily running out of capacity. | Temporarily switch to another model (e.g. from Gemini 1.5 Pro to Gemini 1.5 Flash) and see if it works. Or wait a bit and retry your request. If the issue persists after retrying, please report it using the **Send feedback** button in Google AI Studio. |
| 504 | DEADLINE\_EXCEEDED | The service is unable to finish processing within the deadline. | Your prompt (or context) is too large to be processed in time. | Set a larger 'timeout' in your client request to avoid this error. |

## Client SDK error codes

The following table lists common
[Python client SDK](https://github.com/googleapis/python-genai) error
codes you may encounter, along with explanations for their causes:

| Exception/Error Type | Class | Description |
| --- | --- | --- |
| APIError | google.genai.errors.APIError | General errors raised by the GenAI API. |
| ClientError | google.genai.errors.ClientError | Client error raised by the GenAI API. |
| ServerError | google.genai.errors.ServerError | Server error raised by the GenAI API. |
| UnknownFunctionCallArgumentError | google.genai.errors.UnknownFunctionCallArgumentError | Raised when the function call argument cannot be converted to the parameter annotation. |
| UnsupportedFunctionError | google.genai.errors.UnsupportedFunctionError | Raised when the function is not supported. |
| FunctionInvocationError | google.genai.errors.FunctionInvocationError | Raised when the function cannot be invoked with the given arguments. |
| ValidationError | pydantic.ValidationError | Raised by [Pydantic](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) whenever it finds an error in the data it's validating. See [Pydantic error handling](https://docs.pydantic.dev/latest/errors/errors/). |

You'll also find all errors in the [errors class](https://github.com/googleapis/python-genai/blob/main/google/genai/errors.py).

To handle errors raised by the SDK, you can use a `try-except` block:

```
from google.genai import errors

try:
    client.models.generate_content(
        model="invalid-model-name",
        contents="What is your name?",
    )
except errors.APIError as e:
    print(e.code) # 404

    print(e.message)

```

## Check your API calls for model parameter errors

Ensure your model parameters are within the following values:

|  |  |
| --- | --- |
| **Model parameter** | **Values (range)** |
| Candidate count | 1-8 (integer) |
| Temperature | 0.0-1.0 |
| Max output tokens | Use `get_model` ([Python](/api/python/google/generativeai/get_model)) to determine the maximum number of tokens for the model you are using. |
| TopP | 0.0-1.0 |

In addition to checking parameter values, make sure you're using the correct
[API version](/gemini-api/docs/api-versions) (e.g., `/v1` or `/v1beta`) and
model that supports the features you need. For example, if a feature is in Beta
release, it will only be available in the `/v1beta` API version.

## Check if you have the right model

Ensure you are using a supported model listed on our
[models page](/gemini-api/docs/models/gemini).

## Safety issues

If you see a prompt was blocked because of a safety setting in your API call,
review the prompt with respect to the filters you set in the API call.

If you see `BlockedReason.OTHER`, the query or response may violate the [terms
of service](/terms) or be otherwise unsupported.

## Recitation issue

If you see the model stops generating output due to the RECITATION reason, this
means the model output may resemble certain data. To fix this, try to make
prompt / context as unique as possible and use a higher temperature.

## Improve model output

For higher quality model outputs, explore writing more structured prompts. The
[introduction to prompt design](/docs/prompt_best_practices) page introduces
some basic concepts, strategies, and best practices to get you started.

If you have hundreds of examples of good input/output pairs, you can also
consider [model tuning](/docs/model_tuning_guidance).

## Understand token limits

Read through our [Token guide](/gemini-api/docs/tokens) to better understand how
to count tokens and their limits.

## Known issues

* The API supports only a number of select languages. Submitting prompts in
  unsupported languages can produce unexpected or even blocked responses. See
  [available languages](/models/gemini#available-languages) for updates.

## File a bug

Join the discussion on the [Google AI developer forum](https://discuss.ai.google.dev)
if you have questions.

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-24 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-24 UTC."],[],[]]