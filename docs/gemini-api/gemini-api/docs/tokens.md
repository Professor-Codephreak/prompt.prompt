# Understand and count tokens

* On this page

  + [Count text tokens](#text-tokens)
  + [Count multi-turn (chat) tokens](#multi-turn-tokens)
  + [Count multimodal tokens](#multimodal-tokens)
  + [System instructions and tools](#system-instructions-and-tools)

Python
JavaScript
Go

Gemini and other generative AI models process input and output at a granularity
called a *token*.

## About tokens

Tokens can be single characters like `z` or whole words like `cat`. Long words
are broken up into several tokens. The set of all tokens used by the model is
called the vocabulary, and the process of splitting text into tokens is called
*tokenization*.

For Gemini models, a token is equivalent to about 4 characters.
100 tokens is equal to about 60-80 English words.

When billing is enabled, the [cost of a call to the Gemini API](/pricing) is
determined in part by the number of input and output tokens, so knowing how to
count tokens can be helpful.

## Try out counting tokens in a Colab

You can try out counting tokens by using a Colab.

|  |  |  |
| --- | --- | --- |
| [View on ai.google.dev](https://ai.google.dev/gemini-api/docs/tokens) | [Try a Colab notebook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb) | [View notebook on GitHub](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Counting_Tokens.ipynb) |

## Context windows

The models available through the Gemini API have context windows that are
measured in tokens. The context window defines how much input you can provide
and how much output the model can generate. You can determine the size of the
context window by calling the [getModels endpoint](/api/rest/v1/models/get) or
by looking in the [models documentation](/gemini-api/docs/models/gemini).

In the following example, you can see that the `gemini-1.5-flash` model has an
input limit of about 1,000,000 tokens and an output limit of about 8,000 tokens,
which means a context window is 1,000,000 tokens.

```
import google.generativeai as genai

model_info = genai.get_model("models/gemini-1.5-flash")

# Returns the "context window" for the model,

# which is the combined input and output token limits.

print(f"{model_info.input_token_limit=}")
print(f"{model_info.output_token_limit=}")

# ( input_token_limit=30720, output_token_limit=2048 )

count_tokens.py

```

## Count tokens

All input to and output from the Gemini API is tokenized, including text, image
files, and other non-text modalities.

You can count tokens in the following ways:

* **Call [`count_tokens`](/api/rest/v1/models/countTokens) with the input of the
  request.**  
  This returns the total number of tokens in
  *the input only*. You can make this call before sending the input to the model
  to check the size of your requests.
* **Use the `usage_metadata` attribute on the `response` object after calling
  `generate_content`.**  
  This returns the total number of tokens in *both the input and the output*:
  `total_token_count`.  
  It also returns the token counts of the input and output separately:
  `prompt_token_count` (input tokens) and
  `candidates_token_count` (output tokens).

### Count text tokens

If you call `count_tokens` with a text-only input, it returns the token count
of the text in *the input only* (`total_tokens`). You can make this call before
calling `generate_content` to check the size of your requests.

Another option is calling `generate_content` and then using the `usage_metadata`
attribute on the `response` object to get the following:

* The separate token counts of the input (`prompt_token_count`)
  and the output (`candidates_token_count`)
* The total number of tokens in *both the input and the output*
  (`total_token_count`)

```
import google.generativeai as genai

model = genai.GenerativeModel("models/gemini-1.5-flash")

prompt = "The quick brown fox jumps over the lazy dog."

# Call `count_tokens` to get the input token count (`total_tokens`).

print("total_tokens: ", model.count_tokens(prompt))

# ( total_tokens: 10 )

response = model.generate_content(prompt)

# On the response for `generate_content`, use `usage_metadata`

# to get separate input and output token counts

# (`prompt_token_count` and `candidates_token_count`, respectively),

# as well as the combined token count (`total_token_count`).

print(response.usage_metadata)

# ( prompt_token_count: 11, candidates_token_count: 73, total_token_count: 84 )

count_tokens.py

```

### Count multi-turn (chat) tokens

If you call `count_tokens` with the chat history, it returns the total token
count of the text from each role in the chat (`total_tokens`).

Another option is calling `send_message` and then using the `usage_metadata`
attribute on the `response` object to get the following:

* The separate token counts of the input (`prompt_token_count`)
  and the output (`candidates_token_count`)
* The total number of tokens in *both the input and the output*
  (`total_token_count`)

To understand how big your next conversational turn will be, you need to append
it to the history when you call `count_tokens`.

```
import google.generativeai as genai

model = genai.GenerativeModel("models/gemini-1.5-flash")

chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hi my name is Bob"},
        {"role": "model", "parts": "Hi Bob!"},
    ]
)

# Call `count_tokens` to get the input token count (`total_tokens`).

print(model.count_tokens(chat.history))

# ( total_tokens: 10 )

response = chat.send_message(
    "In one sentence, explain how a computer works to a young child."
)

# On the response for `send_message`, use `usage_metadata`

# to get separate input and output token counts

# (`prompt_token_count` and `candidates_token_count`, respectively),

# as well as the combined token count (`total_token_count`).

print(response.usage_metadata)

# ( prompt_token_count: 25, candidates_token_count: 21, total_token_count: 46 )

from google.generativeai.types.content_types import to_contents

# You can call `count_tokens` on the combined history and content of the next turn.

print(model.count_tokens(chat.history + to_contents("What is the meaning of life?")))

# ( total_tokens: 56 )

count_tokens.py

```

### Count multimodal tokens

All input to the Gemini API is tokenized, including text, image files, and other
non-text modalities. Note the following high-level key points about tokenization
of multimodal input during processing by the Gemini API:

* With Gemini 2.0, image inputs with both dimensions <=384 pixels are counted as
  258 tokens. Images larger in one or both dimensions are cropped and scaled as
  needed into tiles of 768x768 pixels, each counted as 258 tokens. Prior to Gemini
  2.0, images used a fixed 258 tokens.
* Video and audio files are converted to tokens at the following fixed rates:
  video at 263 tokens per second and audio at 32 tokens per second.

#### Image files

If you call `count_tokens` with a text-and-image input, it returns the combined
token count of the text and the image in *the input only* (`total_tokens`). You
can make this call before calling `generate_content` to check the size of your
requests. You can also optionally call `count_tokens` on the text and the file
separately.

Another option is calling `generate_content` and then using the `usage_metadata`
attribute on the `response` object to get the following:

* The separate token counts of the input (`prompt_token_count`)
  and the output (`candidates_token_count`)
* The total number of tokens in *both the input and the output*
  (`total_token_count`)

**Note:** You'll get the same token count if you use a file uploaded using the
File API or you provide the file as inline data.

Example that uses an uploaded image from the File API:

```
import google.generativeai as genai

model = genai.GenerativeModel("models/gemini-1.5-flash")

prompt = "Tell me about this image"
your_image_file = genai.upload_file(path=media / "organ.jpg")

# Call `count_tokens` to get the input token count

# of the combined text and file (`total_tokens`).

# An image's display or file size does not affect its token count.

# Optionally, you can call `count_tokens` for the text and file separately.

print(model.count_tokens([prompt, your_image_file]))

# ( total_tokens: 263 )

response = model.generate_content([prompt, your_image_file])
response.text

# On the response for `generate_content`, use `usage_metadata`

# to get separate input and output token counts

# (`prompt_token_count` and `candidates_token_count`, respectively),

# as well as the combined token count (`total_token_count`).

print(response.usage_metadata)

# ( prompt_token_count: 264, candidates_token_count: 80, total_token_count: 345 )

count_tokens.py

```

Example that provides the image as inline data:

```
import google.generativeai as genai

import PIL.Image

model = genai.GenerativeModel("models/gemini-1.5-flash")

prompt = "Tell me about this image"
your_image_file = PIL.Image.open(media / "organ.jpg")

# Call `count_tokens` to get the input token count

# of the combined text and file (`total_tokens`).

# An image's display or file size does not affect its token count.

# Optionally, you can call `count_tokens` for the text and file separately.

print(model.count_tokens([prompt, your_image_file]))

# ( total_tokens: 263 )

response = model.generate_content([prompt, your_image_file])

# On the response for `generate_content`, use `usage_metadata`

# to get separate input and output token counts

# (`prompt_token_count` and `candidates_token_count`, respectively),

# as well as the combined token count (`total_token_count`).

print(response.usage_metadata)

# ( prompt_token_count: 264, candidates_token_count: 80, total_token_count: 345 )

count_tokens.py

```

#### Video or audio files

Audio and video are each converted to tokens at the following fixed rates:

* Video: 263 tokens per second
* Audio: 32 tokens per second

If you call `count_tokens` with a text-and-video/audio input, it returns the
combined token count of the text and the video/audio file in *the input only*
(`total_tokens`). You can make this call before calling `generate_content` to
check the size of your requests. You can also optionally call `count_tokens` on
the text and the file separately.

Another option is calling `generate_content` and then using the `usage_metadata`
attribute on the `response` object to get the following:

* The separate token counts of the input (`prompt_token_count`)
  and the output (`candidates_token_count`)
* The total number of tokens in *both the input and the output*
  (`total_token_count`)

**Note:** You'll get the same token count if you use a file uploaded using the
File API or you provide the file as inline data.

```
import google.generativeai as genai

import time

model = genai.GenerativeModel("models/gemini-1.5-flash")

prompt = "Tell me about this video"
your_file = genai.upload_file(path=media / "Big_Buck_Bunny.mp4")

# Videos need to be processed before you can use them.

while your_file.state.name == "PROCESSING":
    print("processing video...")
    time.sleep(5)
    your_file = genai.get_file(your_file.name)

# Call `count_tokens` to get the input token count

# of the combined text and video/audio file (`total_tokens`).

# A video or audio file is converted to tokens at a fixed rate of tokens per second.

# Optionally, you can call `count_tokens` for the text and file separately.

print(model.count_tokens([prompt, your_file]))

# ( total_tokens: 300 )

response = model.generate_content([prompt, your_file])

# On the response for `generate_content`, use `usage_metadata`

# to get separate input and output token counts

# (`prompt_token_count` and `candidates_token_count`, respectively),

# as well as the combined token count (`total_token_count`).

print(response.usage_metadata)

# ( prompt_token_count: 301, candidates_token_count: 60, total_token_count: 361 )

count_tokens.py

```

### System instructions and tools

System instructions and tools also count towards the total token count for the
input.

If you use system instructions, the `total_tokens` count increases to reflect
the addition of `system_instruction`.

```
import google.generativeai as genai

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

prompt = "The quick brown fox jumps over the lazy dog."

print(model.count_tokens(prompt))

# total_tokens: 10

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", system_instruction="You are a cat. Your name is Neko."
)

# The total token count includes everything sent to the `generate_content` request.

# When you use system instructions, the total token count increases.

print(model.count_tokens(prompt))

# ( total_tokens: 21 )

count_tokens.py

```

If you use function calling, the `total_tokens` count increases to reflect the
addition of `tools`.

```
import google.generativeai as genai

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

prompt = "I have 57 cats, each owns 44 mittens, how many mittens is that in total?"

print(model.count_tokens(prompt))

# ( total_tokens: 22 )

def add(a: float, b: float):
    """returns a + b."""
    return a + b

def subtract(a: float, b: float):
    """returns a - b."""
    return a - b

def multiply(a: float, b: float):
    """returns a * b."""
    return a * b

def divide(a: float, b: float):
    """returns a / b."""
    return a / b

model = genai.GenerativeModel(
    "models/gemini-1.5-flash-001", tools=[add, subtract, multiply, divide]
)

# The total token count includes everything sent to the `generate_content` request.

# When you use tools (like function calling), the total token count increases.

print(model.count_tokens(prompt))

# ( total_tokens: 206 )

count_tokens.py

```

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-01 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-01 UTC."],[],[]]