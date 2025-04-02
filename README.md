# prompt.prompt

#  The `.prompt` Language Project

## Overview

`.prompt` is a programming language designed specifically for the art and science of **advanced prompt engineering** and **AI interaction management**. Recognizing that interacting with increasingly sophisticated AI models (LLMs multimodal models agentic systems) requires more than simple text strings or general purpose glue code `.prompt` aims provide a dedicated robust and developer friendly environment.

It originates from the need handle complex multi step AI workflows manage prompt variations define agent behaviors integrate diverse logical reasoning mechanisms and ensure secure reliable interactions all within a single coherent structure. We are building `.prompt` iteratively exploring features needed bridge human intent complex AI capabilities effectively.

## Core Philosophy & Design Principles

The design of `.prompt` is guided by several key principles we have established:

1.  **Pythonic Foundation:** Leverages familiar Python like syntax for core programming constructs (`class` `def` control flow data structures) reducing learning curve.
2.  **Object Oriented Structure:** Fundamentally OOP enabling encapsulation modularity and reusability through classes objects conceptual base classes (`BasePrompt` `BaseAgent`).
3.  **Markdown Like Prompt Readability:** Employs triple quoted strings (`"""..."""` `````...`````) for defining core prompt text minimizing escape characters prioritizing human readability editing natural language instructions.
4.  **Simple Templating:** Integrates basic `{{ expression }}` syntax seamlessly within prompt text blocks dynamic content injection.
5.  **Loose Typing:** Adopts dynamic typing runtime flexibility rapid development common AI related tasks where data structures vary.
6.  **Async Native:** Built with `async` `await` core handle I O bound operations especially AI model API calls efficiently.
7.  **AI Readable Documentation Style:** Features unique convention documentation elements (`#` comments metadata `description`) avoiding standard punctuation numerals favouring word numerals promote direct machine readability processing potential AI tools analyzing extending code itself.

## Key Features (Conceptual)

Based on our iterative development `.prompt` conceptually supports:

* **Structured Prompt Definition:** Define prompts complex objects bundling text parameters context metadata logic.
* **Agent Framework:** Define autonomous agents state perception planning action loops tool usage (`agent.prompt` `prompt.agent`).
* **Logic Module Integration:** Incorporate various reasoning paradigms propositional logic (`logic.prompt`) default logic (`nonmonotonic.prompt`) epistemic logic belief revision (`epistemic.prompt`) Socratic dialogue (`socratic.prompt`) BDI structures (`bdi.prompt`).
* **Specialized Utilities:** Implement specific tasks like ML prediction workflows (`prediction.prompt`) secure strategy marketplaces (`aion.prompt`).
* **Meta Programming:** Create prompts agents generate refine other `.prompt` code files (`prompt.agent` generating templates specs `prompt.prompt` generating spec).
* **Configuration Management:** Standardized YAML metadata header file level defaults context (`--- ... ---`).
* **Abstracted AI Interaction:** Conceptual layer `AI_Interaction` handle communication diverse AI backends modalities.
* **Multimodality Components Constraints:** Conceptual syntax elements support image audio generation component based design reward driven optimization.
* **Interactivity:** Conceptual `input()` function enable user interaction during execution.

## Language Structure (`.prompt` File)

A typical `.prompt` file presents hybrid `.md` `.json` feel combining structure readability:

1.  **Metadata Block (YAML):** `---` enclosed header defines `version` `description` `tags` `defaultModelConfig` etc.
2.  **Conceptual Imports:** Section import other `.prompt` modules standard libraries tools.
3.  **Logic Block:** Core code definitions classes functions execution logic Pythonic syntax. Contains embedded Markdown like prompt text blocks.

## Examples Created So Far

During conceptualization we have designed several example `.prompt` files illustrating capabilities:

* `encapsulation.prompt`: Demonstrates OOP encapsulation principle.
* `logic.prompt`: Shows conditional logic shortcode truth table utility context broader logic systems.
* `bdi.prompt`: Defines core Belief Desire Intention components agent cognition.
* `socratic.prompt`: Implements Socratic dialogue reasoning structure.
* `nonmonotonic.prompt`: Provides Default Logic implementation handling uncertainty.
* `epistemic.prompt`: Focuses belief revision knowledge representation autoepistemic concepts.
* `reasoning.prompt`: Outlines general purpose reasoning engine concept.
* `aion.prompt`: Represents complex secure strategy marketplace agent.
* `prediction.prompt`: Defines standard ML prediction workflow.
* `agent.prompt`: Example autonomous research agent structure tool use.
* `prompt.agent`: Meta agent specialized generating refining `.prompt` files itself.
* `prompt.prompt`: Meta prompt generates language specification document.
* `rules.prompt`: Self documenting file listing language rules data structure.

## Unique Documentation Style Explained

A distinctive feature `.prompt` is its internal documentation style applied `#` comments metadata `description` fields. This style intentionally omits standard punctuation most numerals using word equivalents instead eg `five` not `5`. The goal enhance direct machine readability allowing AI tools more easily parse analyze utilize documentation context refactoring explanation code generation tasks. This rule does *not* apply code syntax YAML structure string literal content error messages or procedural prompts intended direct LLM execution. The README you are reading uses standard Markdown clarity general audience.

## Status

`.prompt` is currently a **conceptual language project**. All examples syntax features described exist design documents explorations based this iterative process. No compiler interpreter or formal specification exists yet.

## Future Directions

Potential next steps building upon this conceptual foundation include:

* Developing formal grammar specification EBNF.
* Defining standard library modules `AI_Interaction` `FileSystem` `Crypto` `HTTP` `JSON` etc.
* Prototyping simple interpreter parser.
* Refining syntax error handling module system.
* Building tooling IDE support syntax highlighting linting debugging.
* Exploring deeper integration specific AI model capabilities backend frameworks.
