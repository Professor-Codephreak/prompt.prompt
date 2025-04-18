# Gemini models

* On this page

  + [Gemini 2.5 Pro Preview](#gemini-2.5-pro-preview-03-25)
  + [Gemini 2.0 Flash](#gemini-2.0-flash)
  + [Gemini 2.0 Flash-Lite](#gemini-2.0-flash-lite)
  + [Gemini 1.5 Flash](#gemini-1.5-flash)
  + [Gemini 1.5 Flash-8B](#gemini-1.5-flash-8b)
  + [Gemini 1.5 Pro](#gemini-1.5-pro)
  + [Imagen 3](#imagen-3)
  + [Veo 2](#veo-2)
  + [Gemini 2.0 Flash Live](#live-api)
  + [Gemini Embedding Experimental](#gemini-embedding)
  + [Text Embedding and Embedding](#text-embedding-and-embedding)
  + [AQA](#aqa)

  + [Previous experimental models](#previous-experimental-models)

2.5 Pro
experiment

Our most powerful thinking model with maximum response accuracy and state-of-the-art performance

* Input audio, images, video, and text, get text responses
* Tackle difficult problems, analyze large databases, and more
* Best for complex coding, reasoning, and multimodal understanding

2.0 Flash
spark

Our newest multimodal model, with next generation features and improved
capabilities

* Input audio, images, video, and text, get text responses
* Generate code and images, extract data, analyze files, generate graphs, and more
* Low latency, enhanced performance, built to power agentic experiences

2.0 Flash-Lite

A Gemini 2.0 Flash model optimized for cost efficiency and low latency

* Input audio, images, video, and text, get text responses
* Outperforms 1.5 Flash on the majority of benchmarks
* A 1 million token context window and multimodal input, like Flash 2.0

## Model variants

The Gemini API offers different models that are optimized for specific use
cases. Here's a brief overview of Gemini variants that are available:

| Model variant | Input(s) | Output | Optimized for |
| --- | --- | --- | --- |
| [Gemini 2.5 Pro Preview](#gemini-2.5-pro-preview-03-25)  `gemini-2.5-pro-preview-03-25` | Audio, images, videos, and text | Text | Enhanced thinking and reasoning, multimodal understanding, advanced coding, and more |
| [Gemini 2.0 Flash](#gemini-2.0-flash)  `gemini-2.0-flash` | Audio, images, videos, and text | Text, images (experimental), and audio (coming soon) | Next generation features, speed, thinking, realtime streaming, and multimodal generation |
| [Gemini 2.0 Flash-Lite](#gemini-2.0-flash-lite)  `gemini-2.0-flash-lite` | Audio, images, videos, and text | Text | Cost efficiency and low latency |
| [Gemini 1.5 Flash](#gemini-1.5-flash)  `gemini-1.5-flash` | Audio, images, videos, and text | Text | Fast and versatile performance across a diverse variety of tasks |
| [Gemini 1.5 Flash-8B](#gemini-1.5-flash-8b)  `gemini-1.5-flash-8b` | Audio, images, videos, and text | Text | High volume and lower intelligence tasks |
| [Gemini 1.5 Pro](#gemini-1.5-pro)  `gemini-1.5-pro` | Audio, images, videos, and text | Text | Complex reasoning tasks requiring more intelligence |
| [Gemini Embedding](#gemini-embedding)  `gemini-embedding-exp` | Text | Text embeddings | Measuring the relatedness of text strings |
| [Imagen 3](#imagen-3)  `imagen-3.0-generate-002` | Text | Images | Our most advanced image generation model |
| [Veo 2](#veo-2)  `veo-2.0-generate-001` | Text, images | Video | High quality video generation |
| [Gemini 2.0 Flash Live](#live-api)  `gemini-2.0-flash-live-001` | Audio, video, and text | Text, audio | Low-latency bidirectional voice and video interactions |

You can view the rate limits for each model on the [rate limits page](/gemini-api/docs/rate-limits).

### Gemini 2.5 Pro Preview

Gemini 2.5 Pro is our state-of-the-art thinking model,
capable of reasoning over complex problems in code, math, and STEM, as well
as analyzing large datasets, codebases, and documents using long context.

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-2.5-pro-preview-03-25)

#### Model details

| Property | Description |
| --- | --- |
| id\_cardModel code | Paid: `gemini-2.5-pro-preview-03-25`, Experimental: `gemini-2.5-pro-exp-03-25` |
| saveSupported data types | **Inputs**  Audio, images, video, and text  **Output**  Text |
| token\_autoToken limits[[\*]](#token-size) | **Input token limit**  1,048,576  **Output token limit**  65,536 |
| handymanCapabilities | **Structured outputs**  Supported  **Caching**  Not supported  **Tuning**  Not supported  **Function calling**  Supported  **Code execution**  Supported  **Search grounding**  Supported  **Image generation**  Not supported  **Native tool use**  Supported  **Audio generation**  Not supported  **Live API**  Not supported  **Thinking**  Supported |
| 123Versions | Read the [model version patterns](/gemini-api/docs/models/gemini#model-versions) for more details.  * Preview: `gemini-2.5-pro-preview-03-25` * Experimental: `gemini-2.5-pro-exp-03-25` |
| calendar\_monthLatest update | March 2025 |
| cognition\_2Knowledge cutoff | January 2025 |

### Gemini 2.0 Flash

Gemini 2.0 Flash delivers next-gen features and improved capabilities,
including superior speed, native tool use, multimodal generation, and a 1M token
context window.

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-2.0-flash-001)

#### Model details

| Property | Description |
| --- | --- |
| id\_cardModel code | `models/gemini-2.0-flash` |
| saveSupported data types | **Inputs**  Audio, images, video, and text  **Output**  Text, images (experimental), and audio(coming soon) |
| token\_autoToken limits[[\*]](#token-size) | **Input token limit**  1,048,576  **Output token limit**  8,192 |
| handymanCapabilities | **Structured outputs**  Supported  **Caching**  Coming soon  **Tuning**  Not supported  **Function calling**  Supported  **Code execution**  Supported  **Search**  Supported  **Image generation**  Experimental  **Native tool use**  Supported  **Audio generation**  Coming soon  **Live API**  Experimental  **Thinking**  Experimental |
| 123Versions | Read the [model version patterns](/gemini-api/docs/models/gemini#model-versions) for more details.  * Latest: `gemini-2.0-flash` * Stable: `gemini-2.0-flash-001` * Experimental: `gemini-2.0-flash-exp` and `gemini-2.0-flash-exp-image-generation` point to the same underlying model * Experimental: `gemini-2.0-flash-thinking-exp-01-21` |
| calendar\_monthLatest update | February 2025 |
| cognition\_2Knowledge cutoff | August 2024 |

### Gemini 2.0 Flash-Lite

A Gemini 2.0 Flash model optimized for cost efficiency and low latency.

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-2.0-flash-lite)

#### Model details

| Property | Description |
| --- | --- |
| id\_cardModel code | `models/gemini-2.0-flash-lite` |
| saveSupported data types | **Inputs**  Audio, images, video, and text  **Output**  Text |
| token\_autoToken limits[[\*]](#token-size) | **Input token limit**  1,048,576  **Output token limit**  8,192 |
| handymanCapabilities | **Structured outputs**  Supported  **Caching**  Not supported  **Tuning**  Not supported  **Function calling**  Not supported  **Code execution**  Not supported  **Search**  Not supported  **Image generation**  Not supported  **Native tool use**  Not supported  **Audio generation**  Not supported  **Live API**  Not supported |
| 123Versions | Read the [model version patterns](/gemini-api/docs/models/gemini#model-versions) for more details.  * Latest: `gemini-2.0-flash-lite` * Stable: `gemini-2.0-flash-lite-001` |
| calendar\_monthLatest update | February 2025 |
| cognition\_2Knowledge cutoff | August 2024 |

### Gemini 1.5 Flash

Gemini 1.5 Flash is a fast and versatile multimodal model for scaling across
diverse tasks.

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-1.5-flash)

#### Model details

| Property | Description |
| --- | --- |
| id\_cardModel code | `models/gemini-1.5-flash` |
| saveSupported data types | **Inputs**  Audio, images, video, and text  **Output**  Text |
| token\_autoToken limits[[\*]](#token-size) | **Input token limit**  1,048,576  **Output token limit**  8,192 |
| movie\_infoAudio/visual specs | **Maximum number of images per prompt**  3,600  **Maximum video length**  1 hour  **Maximum audio length**  Approximately 9.5 hours |
| handymanCapabilities | **System instructions**  Supported  **JSON mode**  Supported  **JSON schema**  Supported  **Adjustable safety settings**  Supported  **Caching**  Supported  **Tuning**  Supported  **Function calling**  Supported  **Code execution**  Supported  **Live API**  Not supported |
| 123Versions | Read the [model version patterns](/gemini-api/docs/models/gemini#model-versions) for more details.  * Latest: `gemini-1.5-flash-latest` * Latest stable: `gemini-1.5-flash` * Stable:  + `gemini-1.5-flash-001` + `gemini-1.5-flash-002` |
| calendar\_monthLatest update | September 2024 |

### Gemini 1.5 Flash-8B

Gemini 1.5 Flash-8B is a small model designed for lower intelligence tasks.

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-1.5-flash)

#### Model details

| Property | Description |
| --- | --- |
| id\_cardModel code | `models/gemini-1.5-flash-8b` |
| saveSupported data types | **Inputs**  Audio, images, video, and text  **Output**  Text |
| token\_autoToken limits[[\*]](#token-size) | **Input token limit**  1,048,576  **Output token limit**  8,192 |
| movie\_infoAudio/visual specs | **Maximum number of images per prompt**  3,600  **Maximum video length**  1 hour  **Maximum audio length**  Approximately 9.5 hours |
| handymanCapabilities | **System instructions**  Supported  **JSON mode**  Supported  **JSON schema**  Supported  **Adjustable safety settings**  Supported  **Caching**  Supported  **Tuning**  Supported  **Function calling**  Supported  **Code execution**  Supported  **Live API**  Not supported |
| 123Versions | Read the [model version patterns](/gemini-api/docs/models/gemini#model-versions) for more details.  * Latest: `gemini-1.5-flash-8b-latest` * Latest stable: `gemini-1.5-flash-8b` * Stable:  + `gemini-1.5-flash-8b-001` |
| calendar\_monthLatest update | October 2024 |

### Gemini 1.5 Pro

Try [Gemini 2.0 Pro Experimental](/gemini-api/docs/models/experimental-models#available-models), our most advanced Gemini model to date.

Gemini 1.5 Pro is a mid-size multimodal model that is optimized for
a wide-range of reasoning tasks. 1.5 Pro can process large amounts of data
at once, including 2 hours of video, 19 hours of audio, codebases with
60,000 lines of code, or 2,000 pages of text.

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-1.5-pro)

#### Model details

| Property | Description |
| --- | --- |
| id\_cardModel code | `models/gemini-1.5-pro` |
| saveSupported data types | **Inputs**  Audio, images, video, and text  **Output**  Text |
| token\_autoToken limits[[\*]](#token-size) | **Input token limit**  2,097,152  **Output token limit**  8,192 |
| movie\_infoAudio/visual specs | **Maximum number of images per prompt**  7,200  **Maximum video length**  2 hours  **Maximum audio length**  Approximately 19 hours |
| handymanCapabilities | **System instructions**  Supported  **JSON mode**  Supported  **JSON schema**  Supported  **Adjustable safety settings**  Supported  **Caching**  Supported  **Tuning**  Not supported  **Function calling**  Supported  **Code execution**  Supported  **Live API**  Not supported |
| 123Versions | Read the [model version patterns](/gemini-api/docs/models/gemini#model-versions) for more details.  * Latest: `gemini-1.5-pro-latest` * Latest stable: `gemini-1.5-pro` * Stable:  + `gemini-1.5-pro-001` + `gemini-1.5-pro-002` |
| calendar\_monthLatest update | September 2024 |

### Imagen 3

Imagen 3 is our highest quality text-to-image model, capable of generating
images with even better detail, richer lighting and fewer distracting artifacts
than our previous models.

##### Model details

| Property | Description |
| --- | --- |
| id\_cardModel code | **Gemini API**  `imagen-3.0-generate-002` |
| saveSupported data types | **Input**  Text  **Output**  Images |
| token\_autoToken limits[[\*]](#token-size) | **Input token limit**  N/A  **Output images**  Up to to 4 |
| calendar\_monthLatest update | February 2025 |

### Veo 2

Veo 2 is our high quality text- and image-to-video model, capable of generating
detailed videos, capturing the artistic nuance in your prompts.

##### Model details

| Property | Description |
| --- | --- |
| id\_cardModel code | **Gemini API**  `veo-2.0-generate-001` |
| saveSupported data types | **Input**  Text, image  **Output**  Video |
| token\_autoLimits | **Text input**  N/A  **Image input**  Any image resolution and aspect ratio up to 20MB file size  **Output video**  Up to 2 |
| calendar\_monthLatest update | April 2025 |

### Gemini 2.0 Flash Live

The Gemini 2.0 Flash Live model works with the Live API to enable low-latency
bidirectional voice and video interactions
with Gemini. The model can process text, audio, and video input, and it can
provide text and audio output.

[Try in Google AI Studio](https://aistudio.google.com?model=gemini-2.0-flash-live-001)

#### Model details

| Property | Description |
| --- | --- |
| id\_cardModel code | `models/gemini-2.0-flash-live-001` |
| saveSupported data types | **Inputs**  Audio, video, and text  **Output**  Text, and audio |
| token\_autoToken limits[[\*]](#token-size) | **Input token limit**  1,048,576  **Output token limit**  8,192 |
| handymanCapabilities | **Structured outputs**  Supported  **Caching**  Not supported  **Tuning**  Not supported  **Function calling**  Supported  **Code execution**  Supported  **Search**  Supported  **Image generation**  Not supported  **Native tool use**  Supported  **Audio generation**  Supported  **Thinking**  Not supported |
| 123Versions | Read the [model version patterns](/gemini-api/docs/models/gemini#model-versions) for more details.  * Preview: `gemini-2.0-flash-live-001` |
| calendar\_monthLatest update | April 2025 |
| cognition\_2Knowledge cutoff | August 2024 |

### Gemini Embedding Experimental

`Gemini embedding` achieves a [SOTA performance](https://deepmind.google/research/publications/157741/)
across many key dimensions including code, multi-lingual, and retrieval.

##### Model details

| Property | Description |
| --- | --- |
| id\_cardModel code | **Gemini API**  `gemini-embedding-exp-03-07` |
| saveSupported data types | **Input**  Text  **Output**  Text embeddings |
| token\_autoToken limits[[\*]](#token-size) | **Input token limit**  8,192  **Output dimension size**  Elastic, supports: 3072, 1536, or 768 |
| calendar\_monthLatest update | March 2025 |

### Text Embedding and Embedding

#### Text Embedding

Try our new [experimental Gemini embedding model](https://developers.googleblog.com/en/gemini-embedding-text-model-now-available-gemini-api/)
which achieves state-of-the-art performance.

[Text embeddings](/gemini-api/docs/embeddings) are used to measure the relatedness of strings and are widely used in
many AI applications.

`text-embedding-004` achieves a [stronger retrieval performance and outperforms existing models](https://arxiv.org/pdf/2403.20327)
with comparable dimensions, on the standard MTEB embedding benchmarks.

##### Model details

| Property | Description |
| --- | --- |
| id\_cardModel code | **Gemini API**  `models/text-embedding-004` |
| saveSupported data types | **Input**  Text  **Output**  Text embeddings |
| token\_autoToken limits[[\*]](#token-size) | **Input token limit**  2,048  **Output dimension size**  768 |
| swap\_driving\_apps\_wheelRate limits[[\*\*]](#rate-limits) | 1,500 requests per minute |
| encryptedAdjustable safety settings | Not supported |
| calendar\_monthLatest update | April 2024 |

#### Embedding

**Note:** Text Embedding is the newer version of the Embedding model. If
you're creating a new project, use Text Embedding.

You can use the Embedding model to generate
[text embeddings](/gemini-api/docs/embeddings) for
input text.

The Embedding model is optimized for creating embeddings with 768 dimensions
for text of up to 2,048 tokens.

##### Embedding model details

| Property | Description |
| --- | --- |
| id\_cardModel code | `models/embedding-001` |
| saveSupported data types | **Input**  Text  **Output**  Text embeddings |
| token\_autoToken limits[[\*]](#token-size) | **Input token limit**  2,048  **Output dimension size**  768 |
| swap\_driving\_apps\_wheelRate limits[[\*\*]](#rate-limits) | 1,500 requests per minute |
| encryptedAdjustable safety settings | Not supported |
| calendar\_monthLatest update | December 2023 |

### AQA

You can use the AQA model to perform
[Attributed Question-Answering](/gemini-api/docs/semantic_retrieval)
(AQA)–related tasks over a document, corpus, or a set of passages. The AQA
model returns answers to questions that are grounded in provided sources,
along with estimating answerable probability.

#### Model details

| Property | Description |
| --- | --- |
| id\_cardModel code | `models/aqa` |
| saveSupported data types | **Input**  Text  **Output**  Text |
| languageSupported language | English |
| token\_autoToken limits[[\*]](#token-size) | **Input token limit**  7,168  **Output token limit**  1,024 |
| swap\_driving\_apps\_wheelRate limits[[\*\*]](#rate-limits) | 1,500 requests per minute |
| encryptedAdjustable safety settings | Supported |
| calendar\_monthLatest update | December 2023 |

See the [examples](/examples) to explore the capabilities of these model
variations.

[\*] A token is equivalent to about 4 characters for Gemini models. 100 tokens
are about 60-80 English words.

## Model version name patterns

Gemini models are available in either *preview* or *stable* versions. In your
code, you can use one of the following model name formats to specify which model
and version you want to use.

* **Latest:** Points to the cutting-edge version of the model for a specified
  generation and variation. The underlying model is updated regularly and might
  be a preview version. Only exploratory testing apps and prototypes should
  use this alias.

  To specify the latest version, use the following pattern:
  `<model>-<generation>-<variation>-latest`. For example,
  `gemini-1.0-pro-latest`.
* **Latest stable:** Points to the most recent stable version released for the
  specified model generation and variation.

  To specify the latest stable version, use the following pattern:
  `<model>-<generation>-<variation>`. For example, `gemini-1.0-pro`.
* **Stable:** Points to a specific stable model. Stable models usually don't change.
  Most production apps should use a specific stable model.

  To specify a stable version, use the following pattern:
  `<model>-<generation>-<variation>-<version>`. For example,
  `gemini-1.0-pro-001`.
* **Experimental:** Points to an experimental model which may not be suitable for
  production use. We release experimental models to gather feedback and get our
  latest updates into the hands of developers quickly.

  To specify an experimental version, use the following pattern:
  `<model>-<generation>-<variation>-<version>`. For example,
  `gemini-2.0-pro-exp-02-05`.

## Experimental models

In addition to the production ready models,
the Gemini API offers experimental models which may not be suitable for
production use.

We release experimental models to gather feedback, get our
latest updates into the hands of developers quickly, and highlight the pace of
innovation happening at Google. What we learn from experimental launches informs
how we release models more widely. An experimental model can be swapped for
another without prior notice. We don't guarantee that an experimental model will
become a stable model in the future.

### Previous experimental models

As new versions or stable releases become available, we remove and replace
experimental models. You can find the previous experimental models we released
in the following section along with the replacement version:

| Model code | Base model | Replacement version |
| --- | --- | --- |
| `gemini-2.0-pro-exp-02-05` | Gemini 2.0 Pro Experimental | `gemini-2.5-pro-exp-03-25` |
| `gemini-2.0-flash-exp` | Gemini 2.0 Flash | `gemini-2.0-flash` |
| `gemini-exp-1206` | Gemini 2.0 Pro | `gemini-2.0-pro-exp-02-05` |
| `gemini-2.0-flash-thinking-exp-1219` | Gemini 2.0 Flash Thinking | `gemini-2.0-flash-thinking-exp-01-21` |
| `gemini-exp-1121` | Gemini | `gemini-exp-1206` |
| `gemini-exp-1114` | Gemini | `gemini-exp-1206` |
| `gemini-1.5-pro-exp-0827` | Gemini 1.5 Pro | `gemini-exp-1206` |
| `gemini-1.5-pro-exp-0801` | Gemini 1.5 Pro | `gemini-exp-1206` |
| `gemini-1.5-flash-8b-exp-0924` | Gemini 1.5 Flash-8B | `gemini-1.5-flash-8b` |
| `gemini-1.5-flash-8b-exp-0827` | Gemini 1.5 Flash-8B | `gemini-1.5-flash-8b` |

## Supported languages

Gemini models are trained to work with the following languages:

* Arabic (`ar`)
* Bengali (`bn`)
* Bulgarian (`bg`)
* Chinese simplified and traditional (`zh`)
* Croatian (`hr`)
* Czech (`cs`)
* Danish (`da`)
* Dutch (`nl`)
* English (`en`)
* Estonian (`et`)
* Finnish (`fi`)
* French (`fr`)
* German (`de`)
* Greek (`el`)
* Hebrew (`iw`)
* Hindi (`hi`)
* Hungarian (`hu`)
* Indonesian (`id`)
* Italian (`it`)
* Japanese (`ja`)
* Korean (`ko`)
* Latvian (`lv`)
* Lithuanian (`lt`)
* Norwegian (`no`)
* Polish (`pl`)
* Portuguese (`pt`)
* Romanian (`ro`)
* Russian (`ru`)
* Serbian (`sr`)
* Slovak (`sk`)
* Slovenian (`sl`)
* Spanish (`es`)
* Swahili (`sw`)
* Swedish (`sv`)
* Thai (`th`)
* Turkish (`tr`)
* Ukrainian (`uk`)
* Vietnamese (`vi`)

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-08 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-08 UTC."],[],[]]