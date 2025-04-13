# Files API

* On this page

You can use the Files API to upload and interact with media files. The Files API
lets you store up to 20 GB of files per project, with a per-file maximum
size of 2 GB. Files are stored for 48 hours. During that time, you can
use the API to get metadata about the files, but you can't download the files.
The Files API is available at no cost in all regions where the Gemini API is
available.

This guide shows you how to work with media files using the Files API. The
basic operations are the same for audio files, images, videos, documents, and
other supported file types.

### Upload a file

You can use the Files API to upload a media file. Always use the Files API when
the total request size (including the files, text prompt, system instructions,
etc.) is larger than 20 MB.

The following code uploads a file and then uses the file in a call to
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
    config: { mimeType: "audio/mpeg" },
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

curl "${BASE_URL}/upload/v1beta/files?key=${GOOGLE_API_KEY}" \
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

## Get metadata for a file

You can verify that the API successfully stored the uploaded file and get its
metadata by calling `files.get`.

[Python](#python)[JavaScript](#javascript)[Go](#go)[REST](#rest)
More

```
myfile = client.files.upload(file='path/to/sample.mp3')
file_name = myfile.name
myfile = client.files.get(name=file_name)
print(myfile)

```
```
const myfile = await ai.files.upload({
  file: "path/to/sample.mp3",
  config: { mimeType: "audio/mpeg" },
});

const fileName = myfile.name;
const fetchedFile = await ai.files.get({ name: fileName });
console.log(fetchedFile);

```
```
file, err := client.UploadFileFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}

gotFile, err := client.GetFile(ctx, file.Name)
if err != nil {
    log.Fatal(err)
}
fmt.Println("Got file:", gotFile.Name)

```
```

# file_info.json was created in the upload example

name=$(jq ".file.name" file_info.json)

# Get the file of interest to check state

curl https://generativelanguage.googleapis.com/v1beta/files/$name > file_info.json

# Print some information about the file you got

name=$(jq ".file.name" file_info.json)
echo name=$name
file_uri=$(jq ".file.uri" file_info.json)
echo file_uri=$file_uri

```

## List uploaded files

You can upload multiple files using the Files API. The following code gets
a list of all the files uploaded:

[Python](#python)[JavaScript](#javascript)[Go](#go)[REST](#rest)
More

```
print('My files:')
for f in client.files.list():
    print(' ', f.name)

```
```
const listResponse = await ai.files.list({ config: { pageSize: 10 } });
for await (const file of listResponse) {
  console.log(file.name);
}

```
```
iter := client.ListFiles(ctx)
for {
    ifile, err := iter.Next()
    if err == iterator.Done {
        break
    }
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(ifile.Name)
}

```
```
echo "My files: "

curl "https://generativelanguage.googleapis.com/v1beta/files?key=$GOOGLE_API_KEY"

```

## Delete uploaded files

Files are automatically deleted after 48 hours. You can also manually delete an
uploaded file:

[Python](#python)[JavaScript](#javascript)[Go](#go)[REST](#rest)
More

```
myfile = client.files.upload(file='path/to/sample.mp3')
client.files.delete(name=myfile.name)

```
```
const myfile = await ai.files.upload({
  file: "path/to/sample.mp3",
  config: { mimeType: "audio/mpeg" },
});

const fileName = myfile.name;
await ai.files.delete({ name: fileName });

```
```
file, err := client.UploadFileFromPath(ctx, "path/to/sample.mp3", nil)
if err != nil {
    log.Fatal(err)
}
client.DeleteFile(ctx, file.Name)

```
```
curl --request "DELETE" https://generativelanguage.googleapis.com/v1beta/files/$name?key=$GOOGLE_API_KEY

```

## What's next

This guide shows how to work with files using the Files API. To learn more about
prompting with files, see
[File prompting strategies](/gemini-api/docs/file-prompting-strategies).

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-09 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-09 UTC."],[],[]]