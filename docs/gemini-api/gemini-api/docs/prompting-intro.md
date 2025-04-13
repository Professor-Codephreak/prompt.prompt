# Introduction to prompt design

* On this page

  + [Prompt content types](#prompt-content-types)

*Prompt design* is the process of creating prompts that elicit the desired
response from language models. Writing well structured prompts is an essential
part of ensuring accurate, high quality responses from a language model. This
page introduces some basic concepts, strategies, and best practices to get you
started in designing prompts.

## What is a prompt

A prompt is a natural language request submitted to a language model to receive
a response back. Prompts can contain questions, instructions, contextual
information, examples, and partial input for the model to complete or continue.
After the model receives a prompt, depending on the type of model being used, it
can generate text, embeddings, code, images, videos, music, and more.

### Prompt content types

Prompts can include one or more of the following types of content:

#### Input

An input is the text in the prompt that you want the model to provide a response
for, and it's a required content type. Inputs can be a question that the model
answers (question input), a task the model performs (task input), an entity the
model operates on (entity input), or partial input that the model completes or
continues (completion input).

##### Question input

A question input is a question that you ask the model that the
model provides an answer to.

|  |
| --- |
| **Prompt:**    ``` What's a good name for a flower shop that specializes in selling bouquets of dried flowers? Create a list of 10 options with just the names.    ```  **Response:**    ```     Here are 10 names for a flower shop specializing in dried flowers:      1.  Everlasting Blooms     2.  Dried & Delightful     3.  The Petal Preserve     4.  Whispers of Wildflowers     5.  Forever Blooms     6.  The Botanical Muse     7.  Timeless Blooms     8.  Dried Flower Co.     9.  Bloom & Co.     10.  The Sun-Kissed Petals        ```  (gemini-1.5-flash) |

##### Task input

A task input is a task that you want the model to perform. For
example, you can tell the model to give you ideas or suggestions for something.

|  |
| --- |
| **Prompt:**    ``` Give me a simple list of just the things that I must bring on a camping trip. The list should have 10 items.    ```  **Response:**    ```     Here's a list of 10 essential items for a camping trip:      1. **Tent:** Your shelter from the elements.     2. **Sleeping Bag:** Stay warm and comfortable.     3. **Sleeping Pad:** Insulation and cushioning for a good night's sleep.     4. **Headlamp or Flashlight:** Light for nighttime activities.     5. **First Aid Kit:** Be prepared for minor injuries.     6. **Water Bottle/Hydration Pack:** Stay hydrated.     7. **Food and Snacks:** Fuel for your adventures.     8. **Cooking Gear:** Camp stove, fuel, utensils, etc.     9. **Knife and Multitool:** Essential for various tasks.     10. **Camp Chair:** Enjoy your campfire and meals comfortably.         ```  (gemini-1.5-flash) |

##### Entity input

An entity input is what the model performs an action on, such as
classify or summarize. This type of input can benefit from the inclusion of
instructions.

|  |
| --- |
| **Prompt:**    ``` Classify the following items as [large, small]. Elephant Mouse Snail    ```  **Response:**    ```     Here's the classification:      * **Elephant:** Large     * **Mouse:** Small     * **Snail:** Small         ```  (gemini-1.5-flash) |

##### Completion input

A completion input is text that the model is expected to complete or
continue.

|  |
| --- |
| **Prompt:**    ```     Complete the following prompt: Some simple strategies for overcoming writer's block include...    ```  **Response:**    ```     Some simple strategies for overcoming writer's block include:      * **Freewriting:** Write non-stop for a set amount of time (5-10 minutes) without worrying about grammar, spelling, or even making sense. Just keep your pen moving and let your thoughts flow freely. This can help you loosen up and access ideas you might not have considered otherwise.     * **Brainstorming:**  Make a list of everything that comes to mind related to your topic, no matter how silly or unrelated it seems. You can also use mind mapping or other visual brainstorming techniques.     * **Changing your environment:**  Sometimes a change of scenery can be all you need to get the creative juices flowing. Go for a walk, work in a coffee shop, or even just move to a different room in your house.      * **Reading:**  Immerse yourself in the work of other writers, especially those who inspire you. Pay attention to their style, their structure, and their use of language.      * **Taking a break:** Sometimes the best way to overcome writer's block is to simply step away from the project for a while. Go for a walk, watch a movie, listen to music, or do something else that you enjoy. You might be surprised at how much clearer your head feels when you return to your writing.      * **Focusing on a single element:**  Instead of tackling the entire project, focus on a single sentence, paragraph, or scene. Once you get something down on paper, it can be easier to build from there.     * **Starting with the ending:**  If you're stuck on the beginning, try writing the ending first. This can help you to clarify your overall vision for the project and provide a framework for your ideas.     * **Talking it out:** Share your ideas and challenges with a friend, a writing group, or a writing coach. Discussing your project with someone else can help you to see it from a new perspective and find solutions to your writing problems.          Remember, writer's block is a common experience, and it's not a sign that you're a bad writer. Just be patient with yourself, try some of these strategies, and keep writing!         ```  (gemini-1.5-flash) |

#### Context

Context can be one of the following:

* Instructions that specify how the model should behave.
* Information that the model uses or references to generate a response.

Add contextual information in your prompt when you need to give information to
the model, or restrict the boundaries of the responses to only what's within the
prompt.

|  |
| --- |
| **Prompt:**    ``` Marbles: Color: red Number: 12 Color: blue Number: 28 Color: yellow Number: 15 Color: green Number: 17  How many green marbles are there?    ```  **Response:**    ``` There are 17 green marbles.    ```  (gemini-1.5-flash) |

#### Examples

Examples are input-output pairs that you include in the prompt to give the
model an example of an ideal response. Including examples in
the prompt is an effective strategy for customizing the response format.

|  |
| --- |
| **Prompt:**    ``` Classify the following. Options: - red wine - white wine  Text: Chardonnay The answer is: white wine Text: Cabernet The answer is: red wine Text: Moscato The answer is: white wine  Text: Riesling The answer is:    ```  **Response:**    ``` The answer is: white wine    ```  (gemini-1.5-flash) |

## Next steps

* Now that you have an understanding of prompt design, try writing your
  own prompts using [Google AI Studio](http://aistudio.google.com).
* For a deeper understanding of prompt design, see the
  [prompt strategies](/gemini-api/docs/prompting-strategies) topic.
* To learn about multimodal prompting, see
  [Prompting with media files](/gemini-api/docs/prompting_with_media).

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-02-25 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-25 UTC."],[],[]]