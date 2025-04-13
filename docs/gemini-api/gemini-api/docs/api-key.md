# Get a Gemini API key

* On this page

To use the Gemini API, you need an API key.
You can create a key with a few clicks in Google AI Studio.

[Get a Gemini API key in Google AI Studio](https://aistudio.google.com/app/apikey)

## Set up your API key

For initial testing, you can hard code an API key, but this should only be
temporary since it is not secure. The rest of this section goes through how to
set up your API key locally as an environment variable with different operating
systems.

[Linux/macOS - Bash](#linuxmacos---bash)[macOS - Zsh](#macos---zsh)[Windows](#windows)
More

Bash is a common Linux and macOS terminal configuration. You can check if
you have a configuration file for it by running the following command:

```
~/.bashrc
```

If the response is "No such file or directory", you will need to create this
file and open it by running the following commands, or use `zsh`:

```
touch ~/.bashrc
open ~/.bashrc
```

Next, you need to set your API key by adding the following export command:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

After saving the file, apply the changes by running:

```
source ~/.bashrc
```

Zsh is a common Linux and macOS terminal configuration. You can check if
you have a configuration file for it by running the following command:

```
~/.zshrc
```

If the response is "No such file or directory", you will need to create this
file and open it by running the following commands, or use `bash`:

```
touch ~/.zshrc
open ~/.zshrc
```

Next, you need to set your API key by adding the following export command:

```
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>
```

After saving the file, apply the changes by running:

```
source ~/.zshrc
```

1. Search for "Environment Variables" in the system settings
2. Edit either "User variables" (for current user) or "System variables"
   (for all users - use with caution).
3. Create the variable and add `export GEMINI_API_KEY=your_key_here`
4. Apply the changes

## Send your first Gemini API request

You can use a curl command to verify your setup:

```
  curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${GEMINI_API_KEY}" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{
        "parts":[{"text": "Write a story about a magic backpack."}]
        }]
       }'
```

## Keep your API key secure

It's important to keep your Gemini API key secure. Here are a few things to keep
in mind when using your Gemini API key:

* The Google AI Gemini API uses API keys for authorization. If others get access
  to your Gemini API key, they can make calls using your project's quota,
  which could result in lost quota or additional charges for billed projects,
  in addition to accessing tuned models and files.
* Adding
  [API key restrictions](https://cloud.google.com/api-keys/docs/add-restrictions-api-keys#add-api-restrictions)
  can help limit the surface area usable through each API key.
* You're responsible for keeping your Gemini API key secure.

  + Do NOT check Gemini API keys into source control.
  + Client-side applications (Android, Swift, web, and Dart/Flutter) risk
    exposing API keys. We don't recommend using the Google AI client SDKs
    in production apps to call the Google AI Gemini API directly from your
    mobile and web apps.

For some general best practices, you can also review this
[support article](https://support.google.com/googleapi/answer/6310037).

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-17 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-17 UTC."],[],[]]