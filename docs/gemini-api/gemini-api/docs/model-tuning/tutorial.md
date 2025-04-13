# Fine-tuning tutorial

* On this page

  + [Fine-tuning datasets](#fine-tuning-datasets)
  + [Tuned models](#tuned-models)

Python
REST

This tutorial will help you get started with the Gemini API tuning service
using either the Python SDK or the REST API using
[curl](https://curl.se/). The examples show how to tune the text model behind
the Gemini API text generation service.

### Before you begin

Before calling the Gemini API, ensure you have [your SDK of choice](/gemini-api/docs/downloads)
installed, and a [Gemini API key](/gemini-api/docs/api-key) configured and ready to use.

|  |  |  |
| --- | --- | --- |
| [View on ai.google.dev](https://ai.google.dev/gemini-api/docs/model-tuning/python) | [Try a Colab notebook](https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/model-tuning/python.ipynb) | [View notebook on GitHub](https://github.com/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/model-tuning/python.ipynb) |

## Limitations

Before tuning a model, you should be aware of the following limitations:

### Fine-tuning datasets

Fine-tuning datasets for Gemini 1.5 Flash have the following limitations:

* The maximum input size per example is 40,000 characters.
* The maximum output size per example is 5,000 characters.
* Only input-output pair examples are supported. Chat-style multi-turn
  conversations are not supported.

### Tuned models

Tuned models have the following limitations:

* The input limit of a tuned Gemini 1.5 Flash model is 40,000 characters.
* JSON mode is not supported with tuned models.
* Only text input is supported.

## List tuned models

You can check your existing tuned models with the
[`tunedModels.list`](/api/tuning#method:-tunedmodels.list) method.

```
from google import genai
from google.genai import types
client = genai.Client() # Get the key from the GOOGLE_API_KEY env variable

for model_info in client.models.list():
    print(model_info.name)

```

## Create a tuned model

To create a tuned model, you need to pass your [dataset](/api/tuning#Dataset) to
the model in the [`tunedModels.create`](/api/tuning#method:-tunedmodels.create)
method.

For this example, you will tune a model to generate the next number in the
sequence. For example, if the input is `1`, the model should output `2`. If the
input is `one hundred`, the output should be `one hundred one`.

```

# create tuning model

training_dataset =  [
    ["1", "2"],
    ["3", "4"],
    ["-3", "-2"],
    ["twenty two", "twenty three"],
    ["two hundred", "two hundred one"],
    ["ninety nine", "one hundred"],
    ["8", "9"],
    ["-98", "-97"],
    ["1,000", "1,001"],
    ["10,100,000", "10,100,001"],
    ["thirteen", "fourteen"],
    ["eighty", "eighty one"],
    ["one", "two"],
    ["three", "four"],
    ["seven", "eight"],
]
training_dataset=types.TuningDataset(
        examples=[
            types.TuningExample(
                text_input=i,
                output=o,
            )
            for i,o in training_dataset
        ],
    )
tuning_job = client.tunings.tune(
    base_model='models/gemini-1.5-flash-001-tuning',
    training_dataset=training_dataset,
    config=types.CreateTuningJobConfig(
        epoch_count= 5,
        batch_size=4,
        learning_rate=0.001,
        tuned_model_display_name="test tuned model"
    )
)

# generate content with the tuned model

response = client.models.generate_content(
    model=tuning_job.tuned_model.model,
    contents='III',
)

print(response.text)

```

The optimal values for epoch count, batch size, and learning rate are dependent
on your dataset and other constraints of your use case. To learn more about
these values, see
[Advanced tuning settings](/gemini-api/docs/model-tuning#advanced-settings) and
[Hyperparameters](/api/tuning#Hyperparameters).

**Tip:** For a more general introduction to these hyperparameters, see
[Linear regression: Hyperparameters](https://developers.google.com/machine-learning/crash-course/linear-regression/hyperparameters)
in the
[Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course).

## Try the model

You can use the
[`tunedModels.generateContent`](/api/tuning#method:-tunedmodels.generatecontent)
method and specify the name of the tuned model to test its performance.

```
response = client.models.generate_content(
    model=tuning_job.tuned_model.model,
    contents='III'
)

```

## Not implemented

Some features (progress reporting, updating the description, and
deleting tuned models) has not yet been implemented in the new SDK.

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-03 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-03 UTC."],[],[]]