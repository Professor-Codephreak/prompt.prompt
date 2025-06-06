# Explore document processing capabilities with the Gemini API

* On this page

  + [Technical details](#technical-details)

  + [As inline data](#inline_data)
  + [Locally stored PDFs](#local-pdfs)
  + [Large PDFs](#large-pdfs)
  + [Multiple PDFs](#prompt-multiple)
  + [List files](#list-files)
  + [Delete files](#delete-files)

  + [List caches](#list-caches)
  + [Update a cache](#update-cache)
  + [Delete a cache](#delete-cache)

Python
JavaScript
Go
REST

The Gemini API supports PDF input, including long documents (up to 3600 pages).
Gemini models process PDFs with native vision, and are therefore able to
understand both text and image contents inside documents. With native PDF
vision support, Gemini models are able to:

* Analyze diagrams, charts, and tables inside documents.
* Extract information into structured output formats.
* Answer questions about visual and text contents in documents.
* Summarize documents.
* Transcribe document content (e.g. to HTML) preserving layouts and formatting, for use in downstream applications (such as in RAG pipelines).

This tutorial demonstrates some possible ways to use the Gemini API with PDF
documents. All output is text-only.

### Before you begin

Before calling the Gemini API, ensure you have [your SDK of choice](/gemini-api/docs/downloads)
installed, and a [Gemini API key](/gemini-api/docs/api-key) configured and ready to use.

## Prompting with PDFs

This guide demonstrates how to upload and process PDFs
using the File API or by including them as inline data.

### Technical details

Gemini 1.5 Pro and 1.5 Flash support a maximum of 3,600 document pages. Document
pages must be in one of the following text data MIME types:

* PDF - `application/pdf`
* JavaScript - `application/x-javascript`, `text/javascript`
* Python - `application/x-python`, `text/x-python`
* TXT - `text/plain`
* HTML - `text/html`
* CSS - `text/css`
* Markdown - `text/md`
* CSV - `text/csv`
* XML - `text/xml`
* RTF - `text/rtf`

Each document page is equivalent to 258 tokens.

While there are no specific limits to the number of pixels in a document besides
the model's context window, larger pages are scaled down to a maximum resolution
of 3072x3072 while preserving their original aspect ratio, while smaller pages
are scaled up to 768x768 pixels. There is no cost reduction for pages at lower
sizes, other than bandwidth, or performance improvement for pages at higher
resolution.

For best results:

* Rotate pages to the correct orientation before uploading.
* Avoid blurry pages.
* If using a single page, place the text prompt after the page.

## PDF input

For PDF payloads under 20MB, you can choose between uploading base64
encoded documents or directly uploading locally stored files.

### As inline data

You can process PDF documents directly from URLs. Here's a code snippet
showing how to do this:

```
from google import genai
from google.genai import types
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"  # Replace with the actual URL of your PDF

# Retrieve and encode the PDF byte

doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-1.5-flash",
  contents=[
      types.Part.from_bytes(
        data=doc_data,
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)

```

### Locally stored PDFs

For locally stored PDFs, you can use the following approach:

```
from google import genai
from google.genai import types
import pathlib
import httpx

client = genai.Client()

doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"  # Replace with the actual URL of your PDF

# Retrieve and encode the PDF byte

filepath = pathlib.Path('file.pdf')
filepath.write_bytes(httpx.get(doc_url).content)

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-1.5-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)

```

### Large PDFs

You can use the File API to upload a document of any size. Always use the File
API when the total request size (including the files, text prompt, system
instructions, etc.) is larger than 20 MB.

**Note:** The File API lets you store up to 20 GB of files per project, with a
per-file maximum size of 2 GB. Files are stored for 48 hours. They can be
accessed in that period with your API key, but cannot be downloaded from the
API. The File API is available at no cost in all regions where the Gemini API is
available.

Call [`media.upload`](/api/rest/v1beta/media/upload) to upload a file using the
File API. The following code uploads a document file and then uses the file in a
call to
[`models.generateContent`](/api/generate-content#method:-models.generatecontent).

#### Large PDFs from URLs

Use the File API for large PDF files available from URLs,
simplifying the process of uploading and processing these documents directly
through their URLs:

```
from google import genai
from google.genai import types
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf" # Replace with the actual URL of your large PDF

# Retrieve and upload the PDF using the File API

doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

sample_doc = client.files.upload(
  # You can pass a path or a file-like object here

  file=doc_io, 
  config=dict(
    # It will guess the mime type from the file extension, but if you pass

    # a file-like object, you need to set the

    mime_type='application/pdf')
)

prompt = "Summarize this document"

response = client.models.generate_content(
  model="gemini-1.5-flash",
  contents=[sample_doc, prompt])
print(response.text)

```

#### Large PDFs stored locally

```
from google import genai
from google.genai import types
import pathlib
import httpx

client = genai.Client()

long_context_pdf_path = "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf" # Replace with the actual URL of your large PDF

# Retrieve the PDF

file_path = pathlib.Path('A17.pdf')
file_path.write_bytes(httpx.get(long_context_pdf_path).content)

# Upload the PDF using the File API

sample_file = client.files.upload(
  file=file_path,
)

prompt="Summarize this document"

response = client.models.generate_content(
  model="gemini-1.5-flash",
  contents=[sample_file, "Summarize this document"])
print(response.text)

```

You can verify the API successfully stored the uploaded file and get its
metadata by calling [`files.get`](/api/rest/v1beta/files/get). Only the `name`
(and by extension, the `uri`) are unique.

```
from google import genai
import pathlib

client = genai.Client()

fpath = pathlib.Path('example.txt')
fpath.write_text('hello')

file = client.files.upload('example.txt')

file_info = client.files.get(file.name)
print(file_info.model_dump_json(indent=4))

```

### Multiple PDFs

The Gemini API is capable of processing multiple PDF documents in a single
request, as long as the combined size of the documents and the text prompt
stays within the model's context window.

```
from google import genai
import io
import httpx

client = genai.Client()

doc_url_1 = "https://arxiv.org/pdf/2312.11805" # Replace with the URL to your first PDF

doc_url_2 = "https://arxiv.org/pdf/2403.05530" # Replace with the URL to your second PDF

# Retrieve and upload both PDFs using the File API

doc_data_1 = io.BytesIO(httpx.get(doc_url_1).content)
doc_data_2 = io.BytesIO(httpx.get(doc_url_2).content)

sample_pdf_1 = client.files.upload(
  file=doc_data_1,
  config=dict(mime_type='application/pdf')
)
sample_pdf_2 = client.files.upload(
  file=doc_data_2,
  config=dict(mime_type='application/pdf')
)

prompt = "What is the difference between each of the main benchmarks between these two papers? Output these in a table."

response = client.models.generate_content(
  model="gemini-1.5-flash",
  contents=[sample_pdf_1, sample_pdf_2, prompt])
print(response.text)

```

### List files

You can list all files uploaded using the File API and their URIs using
[`files.list`](/api/files#method:-files.list).

```
from google import genai

client = genai.Client()

print("My files:")
for f in client.files.list():
    print("  ", f.name)

```

### Delete files

Files uploaded using the File API are automatically deleted after 2 days. You
can also manually delete them using
[`files.delete`](/api/files#method:-files.delete).

```
from google import genai
import pathlib

client = genai.Client()

fpath = pathlib.Path('example.txt')
fpath.write_text('hello')

file = client.files.upload('example.txt')

client.files.delete(file.name)

```

## Context caching with PDFs

```
from google import genai
from google.genai import types
import io
import httpx

client = genai.Client()

long_context_pdf_path = "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf" # Replace with the actual URL of your large PDF

# Retrieve and upload the PDF using the File API

doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

document = client.files.upload(
  file=doc_io,
  config=dict(mime_type='application/pdf')
)

# Specify the model name and system instruction for caching

model_name = "gemini-1.5-flash-002" # Ensure this matches the model you intend to use

system_instruction = "You are an expert analyzing transcripts."

# Create a cached content object

cache = client.caches.create(
    model=model_name,
    config=types.CreateCachedContentConfig(
      system_instruction=system_instruction,
      contents=[document], # The document(s) and other content you wish to cache

    )
)

# Display the cache details

print(f'{cache=}')

# Generate content using the cached prompt and document

response = client.models.generate_content(
  model=model_name,
  contents="Please summarize this transcript",
  config=types.GenerateContentConfig(
    cached_content=cache.name
  ))

# (Optional) Print usage metadata for insights into the API call

print(f'{response.usage_metadata=}')

# Print the generated text

print('\n\n', response.text)

```

### List caches

It's not possible to retrieve or view cached content, but you can retrieve
cache metadata (`name`, `model`, `display_name`, `usage_metadata`,
`create_time`, `update_time`, and `expire_time`).

To list metadata for all uploaded caches, use `CachedContent.list()`:

```
from google import genai

client = genai.Client()
for c in client.caches.list():
  print(c)

```

### Update a cache

You can set a new `ttl` or `expire_time` for a cache. Changing anything else
about the cache isn't supported.

The following example shows how to update the `ttl` of a cache using
`CachedContent.update()`.

```
from google import genai
from google.genai import types
import datetime

client = genai.Client()

model_name = "models/gemini-1.5-flash-002" 

cache = client.caches.create(
    model=model_name,
    config=types.CreateCachedContentConfig(
      contents=['hello']
    )
)

client.caches.update(
  name = cache.name,
  config=types.UpdateCachedContentConfig(
    ttl=f'{datetime.timedelta(hours=2).total_seconds()}s'
  )
)

```

### Delete a cache

The caching service provides a delete operation for manually removing content
from the cache. The following example shows how to delete a cache using
`CachedContent.delete()`.

```
from google import genai
from google.genai import types
import datetime

client = genai.Client()

model_name = "models/gemini-1.5-flash-002" 

cache = client.caches.create(
    model=model_name,
    config=types.CreateCachedContentConfig(
      contents=['hello']
    )
)

client.caches.delete(name = cache.name)

```

## What's next

This guide shows how to use
[`generateContent`](/api/generate-content#method:-models.generatecontent) and
to generate text outputs from processed documents. To learn more,
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