# Audio understanding

* On this page

  + [Upload an audio file](#upload-audio)
  + [Pass audio data inline](#inline-audio)

Gemini can analyze and understand audio input, enabling use cases like the
following:

* Describe, summarize, or answer questions about audio content.
* Provide a transcription of the audio.
* Analyze specific segments of the audio.

This guide shows you how to use the Gemini API to generate a text response to
audio input.

### Before you begin

Before calling the Gemini API, ensure you have [your SDK of choice](/gemini-api/docs/downloads)
installed, and a [Gemini API key](/gemini-api/docs/api-key) configured and ready to use.

## Input audio

You can provide audio data to Gemini in the following ways:

* [Upload an audio file](#upload-audio) before making a request to
  `generateContent`.
* [Pass inline audio data](#inline-audio) with the request to
  `generateContent`.

### Upload an audio file

You can use the [Files API](/gemini-api/docs/files) to upload an audio file.
Always use the Files API when the total request size (including the files, text
prompt, system instructions, etc.) is larger than 20 MB.

The following code uploads an audio file and then uses the file in a call to
`generateContent`.

[Python](#python)[JavaScript](#javascript)[Go](#go)[REST](#rest)
More

```
from google import genai

client = genai.Client(api_key="GOOGLE_API_KEY")

myfile = client.files.upload(file="path/to/sample.mp3")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=["Describe this audio clip", myfile]
)

print(response.text)

```
```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GOOGLE_API_KEY" });

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp3",
    config: { mimeType: "audio/mp3" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-2.0-flash",
    contents: createUserContent([
      createPartFromUri(myfile.uri, myfile.mimeType),
      "Describe this audio clip",
    ]),
  });
  console.log(response.text);
}

await main();

```
```
file, err := client.UploadFileFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}
defer client.DeleteFile(ctx, file.Name)

model := client.GenerativeModel("gemini-2.0-flash")
resp, err := model.GenerateContent(ctx,
    genai.FileData{URI: file.URI},
    genai.Text("Describe this audio clip"))
if err != nil {
    log.Fatal(err)
}

printResponse(resp)

```
```
AUDIO_PATH="path/to/sample.mp3"
MIME_TYPE=$(file -b --mime-type "${AUDIO_PATH}")
NUM_BYTES=$(wc -c < "${AUDIO_PATH}")
DISPLAY_NAME=AUDIO

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.

# The upload url is in the response headers dump them to a file.

curl "https://generativelanguage.googleapis.com/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.

curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${AUDIO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[
          {"text": "Describe this audio clip"},
          {"file_data":{"mime_type": "${MIME_TYPE}", "file_uri": '$file_uri'}}]
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json

```

To learn more about working with media files, see
[Files API](/gemini-api/docs/files).

### Pass audio data inline

Instead of uploading an audio file, you can pass inline audio data in the
request to `generateContent`:

[Python](#python)[JavaScript](#javascript)[Go](#go)
More

```
from google.genai import types

with open('path/to/small-sample.mp3', 'rb') as f:
    audio_bytes = f.read()

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents=[
    'Describe this audio clip',
    types.Part.from_bytes(
      data=audio_bytes,
      mime_type='audio/mp3',
    )
  ]
)

print(response.text)

```
```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({ apiKey: "GOOGLE_API_KEY" });
const base64AudioFile = fs.readFileSync("path/to/small-sample.mp3", {
  encoding: "base64",
});

const contents = [
  { text: "Please summarize the audio." },
  {
    inlineData: {
      mimeType: "audio/mp3",
      data: base64AudioFile,
    },
  },
];

const response = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: contents,
});
console.log(response.text);

```
```
// Initialize a Gemini model appropriate for your use case.
model := client.GenerativeModel("gemini-2.0-flash")

bytes, err := os.ReadFile("path/to/small-sample.mp3")
if err != nil {
  log.Fatal(err)
}

prompt := []genai.Part{
  genai.Blob{MIMEType: "audio/mp3", Data: bytes},
  genai.Text("Please summarize the audio."),
}

// Generate content using the prompt.
resp, err := model.GenerateContent(ctx, prompt...)
if err != nil {
  log.Fatal(err)
}

// Handle the response of generated text
for _, c := range resp.Candidates {
  if c.Content != nil {
    fmt.Println(*c.Content)
  }
}

```

A few things to keep in mind about inline audio data:

* The maximum request size is 20 MB, which includes text prompts,
  system instructions, and files provided inline. If your file's
  size will make the *total request size* exceed 20 MB, then
  use the Files API to [upload an audio file](#upload-audio) for use in
  the request.
* If you're using an audio sample multiple times, it's more efficient
  to [upload an audio file](#upload-audio).

## Get a transcript

To get a transcript of audio data, just ask for it in the prompt:

[Python](#python)[JavaScript](#javascript)[Go](#go)
More

```
myfile = client.files.upload(file='path/to/sample.mp3')
prompt = 'Generate a transcript of the speech.'

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents=[prompt, myfile]
)

print(response.text)

```
```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GOOGLE_API_KEY" });
const myfile = await ai.files.upload({
  file: "path/to/sample.mp3",
  config: { mimeType: "audio/mpeg" },
});

const result = await ai.models.generateContent({
  model: "gemini-2.0-flash",
  contents: createUserContent([
    createPartFromUri(myfile.uri, myfile.mimeType),
    "Generate a transcript of the speech.",
  ]),
});
console.log("result.text=", result.text);

```
```
// Initialize a Gemini model appropriate for your use case.
model := client.GenerativeModel("gemini-2.0-flash")

// Create a prompt using text and the URI reference for the uploaded file.
prompt := []genai.Part{
  genai.FileData{URI: sampleAudio.URI},
  genai.Text("Generate a transcript of the speech."),
}

// Generate content using the prompt.
resp, err := model.GenerateContent(ctx, prompt...)
if err != nil {
  log.Fatal(err)
}

// Handle the response of generated text
for _, c := range resp.Candidates {
  if c.Content != nil {
    fmt.Println(*c.Content)
  }
}

```

## Refer to timestamps

You can refer to specific sections of an audio file using timestamps of the form
`MM:SS`. For example, the following prompt requests a transcript that

* Starts at 2 minutes 30 seconds from the beginning of the file.
* Ends at 3 minutes 29 seconds from the beginning of the file.

[Python](#python)[JavaScript](#javascript)[Go](#go)
More

```

# Create a prompt containing timestamps.

prompt = "Provide a transcript of the speech from 02:30 to 03:29."

```
```
// Create a prompt containing timestamps.
const prompt = "Provide a transcript of the speech from 02:30 to 03:29."

```
```
// Create a prompt containing timestamps.
prompt := []genai.Part{
    genai.FileData{URI: sampleAudio.URI},
    genai.Text("Provide a transcript of the speech from 02:30 to 03:29."),
}

```

## Count tokens

Call the `countTokens` method to get a count of the number of tokens in an
audio file. For example:

[Python](#python)[JavaScript](#javascript)[Go](#go)
More

```
response = client.models.count_tokens(
  model='gemini-2.0-flash',
  contents=[myfile]
)

print(response)

```
```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({ apiKey: "GOOGLE_API_KEY" });
const myfile = await ai.files.upload({
  file: "path/to/sample.mp3",
  config: { mimeType: "audio/mpeg" },
});

const countTokensResponse = await ai.models.countTokens({
  model: "gemini-2.0-flash",
  contents: createUserContent([
    createPartFromUri(myfile.uri, myfile.mimeType),
  ]),
});
console.log(countTokensResponse.totalTokens);

```
```
tokens, err := model.CountTokens(ctx, genai.FileData{URI: sampleAudio.URI})
if err != nil {
    log.Fatal(err)
}
fmt.Printf("File %s is %d tokens", sampleAudio.DisplayName, tokens.TotalTokens)

```

## Supported audio formats

Gemini supports the following audio format MIME types:

* WAV - `audio/wav`
* MP3 - `audio/mp3`
* AIFF - `audio/aiff`
* AAC - `audio/aac`
* OGG Vorbis - `audio/ogg`
* FLAC - `audio/flac`

## Technical details about audio

* Gemini represents each second of audio as 32 tokens; for example,
  one minute of audio is represented as 1,920 tokens.
* Gemini can only infer responses to English-language speech.
* Gemini can "understand" non-speech components, such as birdsong or sirens.
* The maximum supported length of audio data in a single prompt is 9.5 hours.
  Gemini doesn't limit the *number* of audio files in a single prompt; however,
  the total combined length of all audio files in a single prompt can't exceed
  9.5 hours.
* Gemini downsamples audio files to a 16 Kbps data resolution.
* If the audio source contains multiple channels, Gemini combines those channels
  into a single channel.

## What's next

This guide shows how to generate text in response to audio data. To learn more,
see the following resources:

* [File prompting strategies](/gemini-api/docs/file-prompting-strategies): The
  Gemini API supports prompting with text, image, audio, and video data, also
  known as multimodal prompting.
* [System instructions](/gemini-api/docs/system-instructions): System
  instructions let you steer the behavior of the model based on your specific
  needs and use cases.
* [Safety guidance](/gemini-api/docs/safety-guidance): Sometimes generative AI
  models produce unexpected outputs, such as outputs that are inaccurate,
  biased, or offensive. Post-processing and human evaluation are essential to
  limit the risk of harm from such outputs.

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-10 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-10 UTC."],[],[]]