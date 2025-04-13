# Generate images

* On this page

  + [Image editing with Gemini](#gemini-image-editing)
  + [Limitations](#gemini-limitations)

  + [Imagen model parameters](#imagen-model)

The Gemini API supports image generation
using [Gemini 2.0 Flash Experimental](#gemini) and
using [Imagen 3](#imagen). This guide helps you get started with both models.

### Before you begin

Before calling the Gemini API, ensure you have [your SDK of choice](/gemini-api/docs/downloads)
installed, and a [Gemini API key](/gemini-api/docs/api-key) configured and ready to use.

## Generate images using Gemini

Gemini 2.0 Flash Experimental supports the ability to output text and inline
images. This lets you use Gemini to conversationally edit images or generate
outputs with interwoven text (for example, generating a blog post with text and
images in a single turn). All generated images include a
[SynthID watermark](/responsible/docs/safeguards/synthid), and images in Google AI
Studio include a visible watermark as well.

**Note:** Make sure to include `responseModalities`: ["Text", "Image"] in your generation
configuration for text and image output with `gemini-2.0-flash-exp-image-generation`.
Image only is not allowed.

The following example shows how to use Gemini 2.0 to generate text-and-image
output:

[Python](#python)[JavaScript](#javascript)[REST](#rest)
More

```
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64

client = genai.Client()

contents = ('Hi, can you create a 3d rendered image of a pig '
            'with wings and a top hat flying over a happy '
            'futuristic scifi city with lots of greenery?')

response = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=contents,
    config=types.GenerateContentConfig(
      response_modalities=['Text', 'Image']
    )
)

for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO((part.inline_data.data)))
    image.save('gemini-native-image.png')
    image.show()

```

**Note:** We've released the [Google SDK for TypeScript and JavaScript](https://www.npmjs.com/package/@google/genai)
in [preview launch stage](https://github.com/googleapis/js-genai?tab=readme-ov-file#preview-launch).
Use this SDK for image generation features.

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

  const contents =
    "Hi, can you create a 3d rendered image of a pig " +
    "with wings and a top hat flying over a happy " +
    "futuristic scifi city with lots of greenery?";

  // Set responseModalities to include "Image" so the model can generate  an image
  const response = await ai.models.generateContent({
    model: "gemini-2.0-flash-exp-image-generation",
    contents: contents,
    config: {
      responseModalities: ["Text", "Image"],
    },
  });
  for (const part of response.candidates[0].content.parts) {
    // Based on the part type, either show the text or save the image
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("gemini-native-image.png", buffer);
      console.log("Image saved as gemini-native-image.png");
    }
  }
}

main();

```
```
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp-image-generation:generateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Hi, can you create a 3d rendered image of a pig with wings and a top hat flying over a happy futuristic scifi city with lots of greenery?"}
      ]
    }],
    "generationConfig":{"responseModalities":["Text","Image"]}
  }' \
  | grep -o '"data": "[^"]*"' \
  | cut -d'"' -f4 \
  | base64 --decode > gemini-native-image.png

```

![AI-generated image of a fantastical flying pig](/static/gemini-api/docs/images/flying-pig.png)

AI-generated image of a fantastical flying pig

Depending on the prompt and context, Gemini will generate content in different
modes (text to image, text to image and text, etc.). Here are some examples:

* Text to image
  + **Example prompt:** "Generate an image of the Eiffel tower with fireworks in
    the background."
* Text to image(s) and text (interleaved)
  + **Example prompt:** "Generate an illustrated recipe for a paella."
* Image(s) and text to image(s) and text (interleaved)
  + **Example prompt:** (With an image of a furnished room) "What other color
    sofas would work in my space? can you update the image?"
* Image editing (text and image to image)
  + **Example prompt:** "Edit this image to make it look like a cartoon"
  + **Example prompt:** [image of a cat] + [image of a pillow] + "Create a
    cross stitch of my cat on this pillow."
* Multi-turn image editing (chat)
  + **Example prompts:** [upload an image of a blue car.] "Turn this car into
    a convertible." "Now change the color to yellow."

### Image editing with Gemini

To perform image editing, add an image as input. The following example
demonstrats uploading base64 encoded images. For multiple images and larger
payloads, check the [image input](/gemini-api/docs/vision#image-input) section.

[Python](#python)[JavaScript](#javascript)[REST](#rest)
More

```
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

import PIL.Image

image = PIL.Image.open('/path/to/image.png')

client = genai.Client()

text_input = ('Hi, This is a picture of me.'
            'Can you add a llama next to me?',)

response = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=[text_input, image],
    config=types.GenerateContentConfig(
      response_modalities=['Text', 'Image']
    )
)

for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO(part.inline_data.data))
    image.show()

```

**Note:** We've released the [Google SDK for TypeScript and JavaScript](https://www.npmjs.com/package/@google/genai)
in [preview launch stage](https://github.com/googleapis/js-genai?tab=readme-ov-file#preview-launch).
Use this SDK for image generation features.

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

  // Load the image from the local file system
  const imagePath = "path/to/image.png";
  const imageData = fs.readFileSync(imagePath);
  const base64Image = imageData.toString("base64");

  // Prepare the content parts
  const contents = [
    { text: "Can you add a llama next to the image?" },
    {
      inlineData: {
        mimeType: "image/png",
        data: base64Image,
      },
    },
  ];

  // Set responseModalities to include "Image" so the model can generate an image
  const response = await ai.models.generateContent({
    model: "gemini-2.0-flash-exp-image-generation",
    contents: contents,
    config: {
      responseModalities: ["Text", "Image"],
    },
  });
  for (const part of response.candidates[0].content.parts) {
    // Based on the part type, either show the text or save the image
    if (part.text) {
      console.log(part.text);
    } else if (part.inlineData) {
      const imageData = part.inlineData.data;
      const buffer = Buffer.from(imageData, "base64");
      fs.writeFileSync("gemini-native-image.png", buffer);
      console.log("Image saved as gemini-native-image.png");
    }
  }
}

main();

```
```
IMG_PATH=/path/to/your/image1.jpeg

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

IMG_BASE64=$(base64 "$B64FLAGS" "$IMG_PATH" 2>&1)

curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp-image-generation:generateContent?key=$GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d "{
      \"contents\": [{
        \"parts\":[
            {\"text\": \"'Hi, This is a picture of me. Can you add a llama next to me\"},
            {
              \"inline_data\": {
                \"mime_type\":\"image/jpeg\",
                \"data\": \"$IMG_BASE64\"
              }
            }
        ]
      }],
      \"generationConfig\": {\"responseModalities\": [\"Text\", \"Image\"]}
    }"  \
  | grep -o '"data": "[^"]*"' \
  | cut -d'"' -f4 \
  | base64 --decode > gemini-edited-image.png

```

### Limitations

* For best performance, use the following languages: EN, es-MX, ja-JP, zh-CN,
  hi-IN.
* Image generation does not support audio or video inputs.
* Image generation may not always trigger:
  + The model may output text only. Try asking for image outputs explicitly
    (e.g. "generate an image", "provide images as you go along", "update the
    image").
  + The model may stop generating partway through. Try again or try a different
    prompt.
* When generating text for an image, Gemini works best if you first generate the
  text and then ask for an image with the text.

## Choose a model

Which model should you use to generate images? It depends on your use case.

Gemini 2.0 is best for producing contextually relevant images, blending
text + images, incorporating world knowledge, and reasoning about images.
You can use it to create accurate, contextually relevant visuals embedded in
long text sequences. You can also edit images conversationally, using natural
language, while maintaining context throughout the conversation.

If image quality is your top priority, then Imagen 3 is a better choice.
Imagen 3 excels at photorealism, artistic detail, and specific artistic styles
like impressionism or anime. Imagen 3 is also a good choice for specialized
image editing tasks like updating product backgrounds, upscaling images, and
infusing branding and style into visuals. You can use Imagen 3 to create logos
or other branded product designs.

## Generate images using Imagen 3

The Gemini API provides access to
[Imagen 3](https://deepmind.google/technologies/imagen-3/), Google's highest
quality text-to-image model, featuring a number of new and improved
capabilities. Imagen 3 can do the following:

* Generate images with better detail, richer lighting, and fewer distracting
  artifacts than previous models
* Understand prompts written in natural language
* Generate images in a wide range of formats and styles
* Render text more effectively than previous models

**Note:** Imagen 3 is only available on the [Paid Tier](/gemini-api/docs/pricing)
and always includes a [SynthID](https://deepmind.google/technologies/synthid/)
watermark.

[Python](#python)[JavaScript](#javascript)[REST](#rest)
More

```
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client(api_key='GEMINI_API_KEY')

response = client.models.generate_images(
    model='imagen-3.0-generate-002',
    prompt='Robot holding a red skateboard',
    config=types.GenerateImagesConfig(
        number_of_images= 4,
    )
)
for generated_image in response.generated_images:
  image = Image.open(BytesIO(generated_image.image.image_bytes))
  image.show()

```
```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

async function main() {

  const ai = new GoogleGenAI({ apiKey: "GEMINI_API_KEY" });

  const response = await ai.models.generateImages({
    model: 'imagen-3.0-generate-002',
    prompt: 'Robot holding a red skateboard',
    config: {
      numberOfImages: 4,
    },
  });

  let idx = 1;
  for (const generatedImage of response.generatedImages) {
    let imgBytes = generatedImage.image.imageBytes;
    const buffer = Buffer.from(imgBytes, "base64");
    fs.writeFileSync(`imagen-${idx}.png`, buffer);
    idx++;
  }
}

main();

```
```
curl -X POST \
    "https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-002:predict?key=GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "instances": [
          {
            "prompt": "Robot holding a red skateboard"
          }
        ],
        "parameters": {
          "sampleCount": 4
        }
      }'

```

![AI-generated image of two fuzzy bunnies in the kitchen](/static/gemini-api/docs/images/fuzzy-bunnies.png)

AI-generated image of two fuzzy bunnies in the kitchen

Imagen supports English only prompts at this time and the following parameters:

### Imagen model parameters

(Naming conventions vary by programming language.)

* `numberOfImages`: The number of images to generate, from 1 to 4 (inclusive).
  The default is 4.
* `aspectRatio`: Changes the aspect ratio of the generated image. Supported
  values are `"1:1"`, `"3:4"`, `"4:3"`, `"9:16"`, and `"16:9"`. The default is
  `"1:1"`.
* `personGeneration`: Allow the model to generate images of people. The
  following values are supported:
  + `"DONT_ALLOW"`: Block generation of images of people.
  + `"ALLOW_ADULT"`: Generate images of adults, but not children. This is the
    default.

## What's next

* To learn more about prompt writing for Imagen, see the
  [Imagen prompt guide](/gemini-api/docs/imagen-prompt-guide).
* To learn more about Gemini 2.0 models, see
  [Gemini models](/gemini-api/docs/models/gemini) and
  [Experimental models](/gemini-api/docs/models/experimental-models).

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-03 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-03 UTC."],[],[]]