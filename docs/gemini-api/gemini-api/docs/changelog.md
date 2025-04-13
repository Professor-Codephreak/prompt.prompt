# Release notes

* On this page

This page documents updates to the Gemini API.

## April 9, 2025

**Model updates:**

* Released `veo-2.0-generate-001`, a generally available (GA) text- and
  image-to-video model, capable of generating detailed and artistically
  nuanced videos. To learn more, see the [Veo docs](/gemini-api/docs/video).
* Released `gemini-2.0-flash-live-001`, a public preview version of the
  [Live API](/gemini-api/docs/live) model with billing enabled.

## April 4, 2025

* Released `gemini-2.5-pro-preview-03-25`, a public preview Gemini 2.5 Pro version
  with billing enabled. You can continue to use `gemini-2.5-pro-exp-03-25` on
  the free tier.

## March 25, 2025

* Released `gemini-2.5-pro-exp-03-25`, a public experimental Gemini model
  with thinking mode always on by default.
  To learn more, see
  [Gemini 2.5 Pro Experimental](/gemini-api/docs/models#gemini-2.5-pro-preview-03-25).

## March 12, 2025

**Model updates:**

* Launched an experimental [Gemini 2.0 Flash](/gemini-api/docs/image-generation#gemini)
  model capable of image generation and editing.
* Released `gemma-3-27b-it`, available on
  [AI Studio](https://aistudio.google.com) and through the Gemini API,
  as part of the [Gemma 3](https://ai.google.dev/gemma/docs/core) launch.

**API updates:**

* Added support for
  [YouTube URLs](/gemini-api/docs/vision#youtube) as a media source.
* Added support for including an
  [inline video](/gemini-api/docs/vision#inline-video) of less than 20MB.

## March 11, 2025

**SDK updates:**

* Released the
  [Google Gen AI SDK for TypeScript and JavaScript](https://googleapis.github.io/js-genai)
  to public preview.

## March 7, 2025

**Model updates:**

* Released `gemini-embedding-exp-03-07`, an
  [experimental](/gemini-api/docs/models/experimental-models)
  Gemini-based embeddings model in public preview.

## February 28, 2025

**API updates:**

* Support for [Search as a tool](/gemini-api/docs/grounding)
  added to `gemini-2.0-pro-exp-02-05`, an experimental model based on
  Gemini 2.0 Pro.

## February 25, 2025

**Model updates:**

* Released `gemini-2.0-flash-lite`, a generally available (GA) version of
  [Gemini 2.0 Flash-Lite](/gemini-api/docs/models/gemini#gemini-2.0-flash-lite),
  which is optimized for speed, scale, and cost efficiency.

## February 18, 2025

**Model updates:**

* Gemini 1.0 Pro is no longer supported. For the list of supported models, see
  [Gemini models](/gemini-api/docs/models/gemini).

## February 19, 2025

**AI Studio updates:**

* Support for
  [additional regions](https://ai.google.dev/gemini-api/docs/available-regions)
  (Kosovo, Greenland and Faroe Islands).

**API updates:**

* Support for
  [additional regions](https://ai.google.dev/gemini-api/docs/available-regions)
  (Kosovo, Greenland and Faroe Islands).

## February 11, 2025

**API updates:**

* Updates on the
  [OpenAI libraries compatibility](https://ai.google.dev/gemini-api/docs/openai).

## February 6, 2025

**Model updates:**

* Released `imagen-3.0-generate-002`, a generally available (GA) version of
  [Imagen 3 in the Gemini API](/gemini-api/docs/imagen).

**SDK updates:**

* Released the [Google Gen AI SDK for Java](https://github.com/googleapis/java-genai)
  for public preview.

## February 5, 2025

**Model updates:**

* Released `gemini-2.0-flash-001`, a generally available (GA) version of
  [Gemini 2.0 Flash](/gemini-api/docs/models/gemini#gemini-2.0-flash) that
  supports text-only output.
* Released `gemini-2.0-pro-exp-02-05`,
  an [experimental](/gemini-api/docs/models/experimental-models) public
  preview version of Gemini 2.0 Pro.
* Released `gemini-2.0-flash-lite-preview-02-05`, an experimental public
  preview [model](/gemini-api/docs/models/gemini#gemini-2.0-flash-lite)
  optimized for cost efficiency.

**API updates:**

* Added
  [file input and graph output](/gemini-api/docs/code-execution#input-output)
  support to code execution.

**SDK updates:**

* Released the
  [Google Gen AI SDK for Python](https://googleapis.github.io/python-genai/)
  to general availability (GA).

## January 21, 2025

**Model updates:**

* Released `gemini-2.0-flash-thinking-exp-01-21`, the latest preview version of
  the model behind the
  [Gemini 2.0 Flash Thinking Model](/gemini-api/docs/thinking).

## December 19, 2024

**Model updates:**

* Released Gemini 2.0 Flash Thinking Mode for public preview. Thinking Mode is
  a test-time compute model that lets you see the model's thought process
  while it generates a response, and produces responses with stronger
  reasoning capabilities.

  Read more about Gemini 2.0 Flash Thinking Mode in our [overview
  page](/gemini-api/docs/thinking-mode).

## December 11, 2024

**Model updates:**

* Released [Gemini 2.0 Flash Experimental](/gemini-api/docs/models/gemini#gemini-2.0-flash)
  for public preview. Gemini 2.0 Flash Experimental's partial list of features includes:
  + Twice as fast as Gemini 1.5 Pro
  + Bidirectional streaming with our Live API
  + Multimodal response generation in the form of text, images, and speech
  + Built-in tool use with multi-turn reasoning to use features like code
    execution, Search, function calling, and more

Read more about Gemini 2.0 Flash in our [overview
page](/gemini-api/docs/models/gemini-v2).

## November 21, 2024

**Model updates:**

* Released `gemini-exp-1121`, an even more powerful experimental Gemini API model.

**Model updates:**

* Updated the `gemini-1.5-flash-latest` and `gemini-1.5-flash` model aliases
  to use `gemini-1.5-flash-002`.
  + Change to `top_k` parameter: The `gemini-1.5-flash-002`
    model supports `top_k` values between 1 and 41 (exclusive).
    Values greater than 40 will be changed to 40.

## November 14, 2024

**Model updates:**

* Released `gemini-exp-1114`, a powerful experimental Gemini API model.

## November 8, 2024

**API updates:**

* Added [support for Gemini](/gemini-api/docs/openai) in the OpenAI libraries / REST API.

## October 31, 2024

**API updates:**

* Added [support for Grounding with Google Search](/gemini-api/docs/grounding).

## October 3, 2024

**Model updates:**

* Released `gemini-1.5-flash-8b-001`, a stable version of our smallest Gemini
  API model.

## September 24, 2024

**Model updates:**

* Released `gemini-1.5-pro-002` and `gemini-1.5-flash-002`, two new stable
  versions of Gemini 1.5 Pro and 1.5 Flash, for general availability.
* Updated the `gemini-1.5-pro-latest` model code to use `gemini-1.5-pro-002`
  and the `gemini-1.5-flash-latest` model code to use `gemini-1.5-flash-002`.
* Released `gemini-1.5-flash-8b-exp-0924` to replace `gemini-1.5-flash-8b-exp-0827`.
* Released the [civic integrity safety filter](/gemini-api/docs/safety-settings#safety-filters)
  for the Gemini API and AI Studio.
* Released support for two new parameters for Gemini 1.5 Pro and 1.5 Flash in
  Python and NodeJS:
  [`frequencyPenalty`](/api/generate-content#FIELDS.frequency_penalty) and
  [`presencePenalty`](/api/generate-content#FIELDS.presence_penalty).

## September 19, 2024

**AI Studio updates:**

* Added thumb-up and thumb-down buttons to model responses, to enable users to
  provide feedback on the quality of a response.

**API updates:**

* Added support for Google Cloud credits, which can now be used towards
  Gemini API usage.

## September 17, 2024

**AI Studio updates:**

* Added an **Open in Colab** button that exports a prompt – and the
  code to run it – to a Colab notebook. The feature doesn't yet support
  prompting with tools (JSON mode, function calling, or code execution).

## September 13, 2024

**AI Studio updates:**

* Added support for compare mode, which lets you compare responses across
  models and prompts to find the best fit for your use case.

## August 30, 2024

**Model updates:**

* Gemini 1.5 Flash supports
  [supplying JSON schema through model configuration](/gemini-api/docs/json-mode#supply-schema-in-config).

## August 27, 2024

**Model updates:**

* Released the following
  [experimental models](/gemini-api/docs/models/experimental-models):
  + `gemini-1.5-pro-exp-0827`
  + `gemini-1.5-flash-exp-0827`
  + `gemini-1.5-flash-8b-exp-0827`

## August 9, 2024

**API updates:**

* Added support for [PDF processing](/gemini-api/docs/document-processing).

## August 5, 2024

**Model updates:**

* Fine-tuning support released for Gemini 1.5 Flash.

## August 1, 2024

**Model updates:**

* Released `gemini-1.5-pro-exp-0801`, a new experimental version of
  [Gemini 1.5 Pro](/gemini-api/docs/models/gemini#gemini-1.5-pro).

## July 12, 2024

**Model updates:**

* Support for Gemini 1.0 Pro Vision removed from Google AI services and tools.

## June 27, 2024

**Model updates:**

* General availability release for Gemini 1.5 Pro's 2M context window.

**API updates:**

* Added support for [code execution](/gemini-api/docs/code-execution).

## June 18, 2024

**API updates:**

* Added support for [context caching](/gemini-api/docs/caching).

## June 12, 2024

**Model updates:**

* Gemini 1.0 Pro Vision deprecated.

## May 23, 2024

**Model updates:**

  (`gemini-1.5-pro-001`) is generally available (GA).

  (`gemini-1.5-flash-001`) is generally available (GA).

## May 14, 2024

**API updates:**

* Introduced a 2M context window for Gemini 1.5 Pro (waitlist).
* Introduced pay-as-you-go [billing](/gemini-api/docs/billing) for Gemini 1.0
  Pro, with Gemini 1.5 Pro and Gemini 1.5 Flash billing coming soon.
* Introduced increased rate limits for the upcoming paid tier of Gemini 1.5
  Pro.
* Added built-in video support to the [File API](/api/rest/v1beta/files).
* Added plain text support to the [File API](/api/rest/v1beta/files).
* Added support for parallel function calling, which returns more than one
  call at a time.

## May 10, 2024

**Model updates:**

* Released [Gemini 1.5 Flash](/gemini-api/docs/models/gemini#gemini-1.5-flash)
  (`gemini-1.5-flash-latest`) in preview.

## April 9, 2024

**Model updates:**

* Released [Gemini 1.5 Pro](/gemini-api/docs/models/gemini#gemini-1.5-pro)
  (`gemini-1.5-pro-latest`) in preview.
* Released a new text embedding model, `text-embeddings-004`, which supports
  [elastic embedding](/gemini-api/docs/embeddings#elastic-embedding)
  sizes under 768.

**API updates:**

* Released the [File API](/api/rest/v1beta/files) for temporarily storing
  media files for use in prompting.
* Added support for prompting with text, image, and audio data, also
  known as *multimodal* prompting. To learn more, see
  [Prompting with media](/gemini-api/docs/prompting_with_media).
* Released [System instructions](/gemini-api/docs/system-instructions) in
  beta.
* Added
  [Function calling mode](/gemini-api/docs/function-calling#function_calling_mode),
  which defines the execution behavior for function calling.
* Added support for the `response_mime_type` configuration option, which lets
  you request responses in
  [JSON format](/gemini-api/docs/api-overview#json).

## March 19, 2024

**Model updates:**

* Added support for
  [tuning Gemini 1.0 Pro](https://developers.googleblog.com/en/tune-gemini-pro-in-google-ai-studio-or-with-the-gemini-api/)
  in Google AI Studio or with the Gemini API.

## December 13 2023

**Model updates:**

* gemini-pro: New text model for a wide variety of tasks. Balances capability
  and efficiency.
* gemini-pro-vision: New multimodal model for a wide variety of tasks.
  Balances capability and efficiency.
* embedding-001: New embeddings model.
* aqa: A new specially tuned model that is trained to answer questions
  using text passages for grounding generated answers.

See [Gemini models](/gemini-api/docs/models/gemini) for more details.

**API version updates:**

* v1: The stable API channel.
* v1beta: Beta channel. This channel has features that may be under
  development.

See [the API versions topic](/gemini-api/docs/api-versions) for more details.

**API updates:**

* `GenerateContent` is a single unified endpoint for chat and text.
* Streaming available through the `StreamGenerateContent` method.
* Multimodal capability: Image is a new supported modality
* New beta features:
  + [Function Calling](/gemini-api/docs/function-calling)
  + [Semantic Retriever](/gemini-api/docs/semantic_retrieval)
  + Attributed Question Answering (AQA)
* Updated candidate count: Gemini models only return 1 candidate.
* Different Safety Settings and SafetyRating categories. See
  [safety settings](/gemini-api/docs/safety-settings) for more details.
* Tuning models is not yet supported for Gemini models (Work in progress).

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-09 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-09 UTC."],[],[]]