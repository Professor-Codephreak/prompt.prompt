# About generative models

* On this page

  + [Generate a poem](#generate-poem)
  + [Generate a list](#generate-list)

  + [Prompting versus traditional software development](#prompting-versus)

  + [Zero-shot prompts](#zero-shot-prompts)
  + [One-shot prompts](#one-shot-prompts)
  + [Few-shot prompts](#few-shot-prompts)

Generative artificial intelligence (AI) models such as the Gemini family of
models are able to create content from varying types of data input, including
text, images, and audio. At their most basic level, these models operate like
sophisticated autocomplete applications. Given input text ("You can lead a horse
to water,"), a generative model can predict that the output text that's
statistically likely to follow ("but you can't make it drink"), based on
patterns learned from their training data. You can use this basic property of
generative models for various applications:

* Generate creative writing such as poetry, short stories, metaphors, and
  blog posts
* Convert structured data to freeform text
* Extract and summarize information from freeform text
* Generate code
* Translate between languages

Using generative models to build these features doesn't require any machine
learning (ML) expertise. You don't need to collect a large dataset or train a
model. All it takes to start your first prototype is to describe what you want
the model to do in a few sentences.

Generative models that only handle text input and output are also known as
*large language models* (LLMs). The Gemini family of models can process more
than text data, and while they can perform the functions of an LLM, they are
more properly known as *generative models*.

## Example applications

The following examples show typical text inputs to, and outputs from, a
generative model.

### Generate a poem

User input: `Write me a four-line poem about puppies and Android phones. Make
sure it rhymes.`

Model output:

```
Puppies are cute,
Android phones are neat,
They both bring joy,
And make life complete.

```

### Generate a list

User input: `Generate a bulleted list of items I need to pack for a three-day
camping trip.`

Model output:

```
*   Tent
*   Sleeping bag
*   Sleeping pad
*   Camp stove
*   Pots and pans
*   Utensils
*   Food
*   Water
*   First-aid kit
*   Sunscreen
*   Insect repellent
*   ...

```

You can get generative models to produce all sorts of useful behaviors like
this, just by crafting the right input text, also called a **prompt**. The art
and science of figuring out the right wording to get generative models to do
what you want is called **prompt design** (also called "prompt engineering" or
simply "prompting").

## Prompt design 101

The previous section showed some examples of prompts that contain an
instruction, like 'Write me a poem'. This kind of instruction may work well for
certain types of tasks. However, for other applications, another prompting
technique called **few-shot prompting** may work better. Few-shot prompts take
advantage of the fact that large language models are incredibly good at
recognizing and replicating patterns in text data. The idea is to send the
generative model a text pattern that it learns to complete. For example, say you
want to build an application that takes as input a country name and outputs its
capital city. Here's a text prompt designed to do just that:

```
Italy : Rome
France : Paris
Germany :

```

In this prompt, you establish a pattern: `[country] : [capital]`. If you send
this prompt to a large language model, it will autocomplete the pattern and
return something like this:

```
     Berlin
Turkey : Ankara
Greece : Athens

```

This model response may look a little strange. The model returned not only the
capital of Germany (the last country in your hand-written prompt), but also a
whole list of additional country and capital pairs. That's because the
generative model is "continuing the pattern." If all you're trying to do is
build a function that tells you the capital of an input country ("Germany :
Berlin"), you probably don't really care about any of the text the model
generates after "Berlin." Indeed, as application designers, you'd probably want
to truncate those extraneous examples. What's more, you'd probably want to
**parameterize** the input, so that Germany is not a fixed string but a variable
that the end user provides:

```
Italy : Rome
France : Paris
<user input here> :

```

You have just written a few-shot prompt for generating country capitals.

You can accomplish a large number of tasks by following this **few-shot prompt**
template. Here's a few-shot prompt with a slightly different format that
converts Python to JavaScript:

```
Convert Python to JavaScript.
Python: print("hello world")
JavaScript: console.log("hello world")
Python: for x in range(0, 100):
JavaScript: for(var i = 0; i < 100; i++) {
Python: ${USER INPUT HERE}
JavaScript:

```

Or, take this "reverse dictionary" prompt. Given a definition, it returns the
word that fits that definition:

```
Given a definition, return the word it defines.
Definition: When you're happy that other people are also sad.
Word: schadenfreude
Definition: existing purely in the mind, but not in physical reality
Word: abstract
Definition: ${USER INPUT HERE}
Word:

```

You might have noticed that the exact pattern of these few-shot prompts varies
slightly. In addition to containing examples, providing instructions in your
prompts is an additional strategy to consider when writing your own prompts, as
it helps to communicate your intent to the model.

### Prompting versus traditional software development

Unlike traditional software that's designed to a carefully written spec, the
behavior of generative models is largely opaque even to the model trainers. As a
result, you often can't predict in advance what types of prompt structures will
work best for a particular model. What's more, the behavior of a generative
model is determined in large part by its training data, and since models are
continually tuned on new datasets, sometimes the model changes enough that it
inadvertently changes which prompt structures work best. What does this mean for
you? Experiment! Try different prompt formats.

## Model parameters

Every prompt you send to the model includes parameter values that control how
the model generates a response. The model can generate different results for
different parameter values. The most common model parameters are:

1. **Max output tokens:** Specifies the maximum number of tokens that can be
   generated in the response. A token is approximately four characters. 100
   tokens correspond to roughly 60-80 words.
2. **Temperature:** The temperature controls the degree of randomness in token
   selection. The temperature is used for sampling during response generation,
   which occurs when `topP` and `topK` are applied. Lower temperatures are good
   for prompts that require a more deterministic or less open-ended response,
   while higher temperatures can lead to more diverse or creative results. A
   temperature of 0 is deterministic, meaning that the highest probability
   response is always selected.
3. **`topK`:** The `topK` parameter changes how the model selects tokens for
   output. A `topK` of 1 means the selected token is the most probable among
   all the tokens in the model's vocabulary (also called greedy decoding),
   while a `topK` of 3 means that the next token is selected from among the 3
   most probable using the temperature. For each token selection step, the
   `topK` tokens with the highest probabilities are sampled. Tokens are then
   further filtered based on `topP` with the final token selected using
   temperature sampling.
4. **`topP`:** The `topP` parameter changes how the model selects tokens for
   output. Tokens are selected from the most to least probable until the sum of
   their probabilities equals the `topP` value. For example, if tokens A, B,
   and C have a probability of 0.3, 0.2, and 0.1 and the `topP` value is 0.5,
   then the model will select either A or B as the next token by using the
   temperature and exclude C as a candidate. The default `topP` value is 0.95.
5. **`stop_sequences`:** Set a stop sequence to
   tell the model to stop generating content. A stop sequence can be any
   sequence of characters. Try to avoid using a sequence of characters that
   may appear in the generated content.

## Types of prompts

Depending on the level of contextual information contained in them, prompts are
broadly classified into three types.

### Zero-shot prompts

These prompts don't contain examples for the model to replicate. Zero-shot
prompts essentially show the model's ability to complete the prompt without any
additional examples or information. It means the model has to rely on its
pre-existing knowledge to generate a plausible answer.

Some commonly used zero-shot prompt patterns are:

* Instruction-content

```
<Overall instruction>
<Content to operate on>

```

For example,

```
Summarize the following into two sentences at the third-grade level:

Hummingbirds are the smallest birds in the world, and they are also one of the
most fascinating. They are found in North and South America, and they are known
for their long, thin beaks and their ability to fly at high speeds.

Hummingbirds are made up of three main parts: the head, the body, and the tail.
The head is small and round, and it contains the eyes, the beak, and the brain.
The body is long and slender, and it contains the wings, the legs, and the
heart. The tail is long and forked, and it helps the hummingbird to balance
while it is flying.

Hummingbirds are also known for their coloration. They come in a variety of
colors, including green, blue, red, and purple. Some hummingbirds are even able
to change their color!

Hummingbirds are very active creatures. They spend most of their time flying,
and they are also very good at hovering. Hummingbirds need to eat a lot of food
in order to maintain their energy, and they often visit flowers to drink nectar.

Hummingbirds are amazing creatures. They are small, but they are also very
powerful. They are beautiful, and they are very important to the ecosystem.

```

* Instruction-content-instruction

```
<Overall instruction or context setting>
<Content to operate on>
<Final instruction>

```

For example,

```
Here is some text I'd like you to summarize:

Hummingbirds are the smallest birds in the world, and they are also one of the
most fascinating. They are found in North and South America, and they are known
for their long, thin beaks and their ability to fly at high speeds. Hummingbirds
are made up of three main parts: the head, the body, and the tail. The head is
small and round, and it contains the eyes, the beak, and the brain. The body is
long and slender, and it contains the wings, the legs, and the heart. The tail
is long and forked, and it helps the hummingbird to balance while it is flying.
Hummingbirds are also known for their coloration. They come in a variety of
colors, including green, blue, red, and purple. Some hummingbirds are even able
to change their color! Hummingbirds are very active creatures. They spend most
of their time flying, and they are also very good at hovering. Hummingbirds need
to eat a lot of food in order to maintain their energy, and they often visit
flowers to drink nectar. Hummingbirds are amazing creatures. They are small, but
they are also very powerful. They are beautiful, and they are very important to
the ecosystem.

Summarize it in two sentences at the third-grade reading level.

```

* Continuation. Sometimes, you can have the model continue text without any
  instructions. For example, here is a zero-shot prompt where the model is
  intended to continue the input provided:

```
Once upon a time, there was a little sparrow building a nest in a farmer's
barn. This sparrow

```

Use zero-shot prompts to generate creative text formats, such as poems, code,
scripts, musical pieces, email, or letters.

### One-shot prompts

These prompts provide the model with a single example to replicate and continue
the pattern. This allows for the generation of predictable responses from the
model.

For example, you can generate food pairings like:

```
Food: Apple
Pairs with: Cheese
Food: Pear
Pairs with:

```

### Few-shot prompts

These prompts provide the model with multiple examples to replicate. Use
few-shot prompts to complete complicated tasks, such as synthesizing data based
on a pattern.

An example prompt may be:

```
Generate a grocery shopping list for a week for one person. Use the JSON format
given below.
{"item": "eggs", "quantity": "6"}
{"item": "bread", "quantity": "one loaf"}

```

## Generative models under the hood

This section aims to answer the question - ***Is there randomness in generative
models' responses, or are they deterministic?***

The short answer - yes to both. When you prompt a generative model, a text
response is generated in two stages. In the first stage, the generative model
processes the input prompt and generates a **probability distribution** over
possible tokens (words) that are likely to come next. For example, if you prompt
with the input text "The dog jumped over the ... ", the generative model will
produce an array of probable next words:

```
[("fence", 0.77), ("ledge", 0.12), ("blanket", 0.03), ...]

```

This process is deterministic; a generative model will produce this same
distribution every time it's input the same prompt text.

In the second stage, the generative model converts these distributions into
actual text responses through one of several decoding strategies. A simple
decoding strategy might select the most likely token at every timestep. This
process would always be deterministic. However, you could instead choose to
generate a response by *randomly sampling* over the distribution returned by the
model. This process would be stochastic (random). Control the degree of
randomness allowed in this decoding process by setting the temperature. A
temperature of 0 means only the most likely tokens are selected, and there's no
randomness. Conversely, a high temperature injects a high degree of randomness
into the tokens selected by the model, leading to more unexpected, surprising
model responses.

## Further reading

* Now that you have a deeper understanding of prompts and generative models,
  try writing your own prompts using
  [Google AI Studio](https://aistudio.google.com).
* Refer to the [Prompt guidelines](/gemini-api/docs/prompting-intro) to learn
  more about best practices for creating prompts.

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-02-25 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-25 UTC."],[],[]]