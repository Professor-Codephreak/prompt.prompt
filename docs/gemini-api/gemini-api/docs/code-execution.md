# Code execution

* On this page

  + [Enable code execution on the model](#enable-on-model)
  + [Use code execution in chat](#code-in-chat)

  + [I/O pricing](#input-output-pricing)
  + [I/O details](#input-output-details)

Python
JavaScript
Go
REST

The Gemini API code execution feature enables the model to generate and run
Python code and learn iteratively from the results until it arrives at a
final output. You can use this code execution capability to build applications
that benefit from code-based reasoning and that produce text output. For
example, you could use code execution in an application that solves equations or
processes text.

**Note:** Gemini is only able to execute code in Python. You can still ask Gemini
to generate code in another language, but the model can't use the
code execution tool to run it.

Code execution is available in both AI Studio and the Gemini API. In AI Studio,
you can enable code execution in the right panel under **Tools**. The Gemini API
provides code execution as a tool, similar to
[function calling](/gemini-api/docs/function-calling). After you add
code execution as a tool, the model decides when to use it.

The code execution environment includes the following libraries:
`altair`, `chess`, `cv2`, `matplotlib`, `mpmath`, `numpy`, `pandas`,
`pdfminer`, `reportlab`, `seaborn`, `sklearn`, `statsmodels`, `striprtf`,
`sympy`, and `tabulate`. You can't install your own libraries.

**Note:** Only `matplotlib` is supported for graph rendering using code execution.

### Before you begin

Before calling the Gemini API, ensure you have [your SDK of choice](/gemini-api/docs/downloads)
installed, and a [Gemini API key](/gemini-api/docs/api-key) configured and ready to use.

## Get started with code execution

You can also try the code execution tutorial in a notebook:

|  |  |  |
| --- | --- | --- |
| [View on ai.google.dev](https://ai.google.dev/gemini-api/docs/code-execution) | [Try a Colab notebook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Code_Execution.ipynb) | [View notebook on GitHub](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Code_Execution.ipynb) |

### Enable code execution on the model

You can enable code execution on the model, as shown here:

```
from google import genai
from google.genai import types

client = genai.Client(api_key="GEMINI_API_KEY")

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents='What is the sum of the first 50 prime numbers? '
           'Generate and run code for the calculation, and make sure you get all 50.',
  config=types.GenerateContentConfig(
    tools=[types.Tool(
      code_execution=types.ToolCodeExecution
    )]
  )
)

```

In a notebook you can display everything in Markdown format with this helper function:

```
def display_code_execution_result(response):
  for part in response.candidates[0].content.parts:
    if part.text is not None:
      display(Markdown(part.text))
    if part.executable_code is not None:
      code_html = f'<pre style="background-color: #BBBBEE;">{part.executable_code.code}</pre>' # Change code color

      display(HTML(code_html))
    if part.code_execution_result is not None:
      display(Markdown(part.code_execution_result.output))
    if part.inline_data is not None:
      display(Image(data=part.inline_data.data, format="png"))
    display(Markdown("---"))

display_code_execution_result(response)

```

The output might look something like this:

Okay, I need to calculate the sum of the first 50 prime numbers. I will use a python script to generate the first 50 primes and then sum them up.

```
```python
def is_prime(n):
  """Checks if a number is prime."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def sum_of_primes(n):
  """Calculates the sum of the first n prime numbers."""
  primes = []
  i = 2
  while len(primes) < n:
    if is_prime(i):
      primes.append(i)
    i += 1
  return sum(primes)

# Calculate the sum of the first 50 prime numbers

sum_of_first_50_primes = sum_of_primes(50)

print(f"The sum of the first 50 prime numbers is: {sum_of_first_50_primes}")
```

**Output:**

```
The sum of the first 50 prime numbers is: 5117
```
```

### Use code execution in chat

You can also use code execution as part of a chat.

```
from google import genai
from google.genai import types

client = genai.Client(api_key="GEMINI_API_KEY")

chat = client.chats.create(
    model='gemini-2.0-flash',
    config=types.GenerateContentConfig(
      tools=[types.Tool(
        code_execution=types.ToolCodeExecution
      )]
    )
)

response = chat.send_message("Can you run some code to bogo-sort this list of numbers?: [2,34,1,65,4]")
display_code_execution_result(response)

```

The conversation could continue like this:

I understand that you want me to bogo-sort the list [2, 34, 1, 65, 4]. Bogo-sort is a notoriously inefficient sorting algorithm. It works by repeatedly shuffling the list until it happens to be sorted. Due to its extremely poor performance, it's impractical for lists of any significant size.

However, for demonstration purposes, I can run a simplified version for a very limited number of iterations, just to show the process. Should I go ahead?

```
response = chat.send_message("Yes, please create the code.")
display_code_execution_result(response)

```

Okay,I will proceed with a function that shuffles the list and checks if it's sorted. I'll run it for a maximum of 10 iterations.
...

## Input/output (I/O)

Starting with
[Gemini 2.0 Flash](/gemini-api/docs/models/gemini#gemini-2.0-flash), code
execution supports file input and graph output. Using these new input and output
capabilities, you can upload CSV and text files, ask questions about the
files, and have [Matplotlib](https://matplotlib.org/) graphs generated as part
of the response.

### I/O pricing

When using code execution I/O, you're charged for input tokens and output
tokens:

**Input tokens:**

* User prompt

**Output tokens:**

* Code generated by the model
* Code execution output in the code environment
* Summary generated by the model

### I/O details

When you're working with code execution I/O, be aware of the following technical
details:

* The maximum runtime of the code environment is 30 seconds.
* If the code environment generates an error, the model may decide to
  regenerate the code output. This can happen up to 5 times.
* The maximum file input size is limited by the model token window. In
  AI Studio, using Gemini Flash 2.0, the maximum input file size is 1 million
  tokens (roughly 2MB for text files of the supported input types). If you
  upload a file that's too large, AI Studio won't let you send it.

|  | Single turn | Bidirectional (Multimodal Live API) |
| --- | --- | --- |
| Models supported | All Gemini 2.0 models | Only Flash experimental models |
| File input types supported | .png, .jpeg, .csv, .xml, .cpp, .java, .py, .js, .ts | .png, .jpeg, .csv, .xml, .cpp, .java, .py, .js, .ts |
| Plotting libraries supported | Matplotlib | Matplotlib |
| [Multi-tool use](/gemini-api/docs/function-calling#multi-tool-use) | No | Yes |

## Billing

There's no additional charge for enabling code execution from the Gemini API.
You'll be billed at the current rate of input and output tokens based on the
Gemini model you're using.

Here are a few other things to know about billing for code execution:

* You're only billed once for the input tokens you pass to the model, and you're
  billed for the final output tokens returned to you by the model.
* Tokens representing generated code are counted as output tokens. Generated
  code can include text and multimodal output like images.
* Code execution results are also counted as output tokens.

The billing model is shown in the following diagram:

![code execution billing model](/static/gemini-api/docs/images/code-execution-diagram.png)

* You're billed at the current rate of input and output tokens based on the
  Gemini model you're using.
* If Gemini uses code execution when generating your response, the original
  prompt, the generated code, and the result of the executed code are labeled
  *intermediate tokens* and are billed as *input tokens*.
* Gemini then generates a summary and returns the generated code, the result of
  the executed code, and the final summary. These are billed as *output tokens*.
* The Gemini API includes an intermediate token count in the API response, so
  you know why you're getting additional input tokens beyond your initial
  prompt.

## Limitations

* The model can only generate and execute code. It can't return other artifacts
  like media files.
* In some cases, enabling code execution can lead to regressions in other areas
  of model output (for example, writing a story).
* There is some variation in the ability of the different models to use code
  execution successfully.

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-03 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-03 UTC."],[],[]]