# Get started with Gemini Nano on Android (on-device)

* On this page

Gemini Nano, the smallest version of the Gemini model family, can be executed
on-device on capable Android devices starting with Google Pixel 8 Pro and
Samsung S24 Series.

To execute the Gemini Nano model on Android, you need to use the
Google AI Edge SDK for Android, which provides APIs to:

* Determine if the underlying Android-powered device is supported.
* Get access to Gemini Nano model.
* Tune safety settings.
* Run inference at high performance and implement fallbacks.
* Optionally, provide a LoRA fine-tuning block to improve performance of the
  model for your use case.

The APIs for accessing Gemini Nano support text-to-text modality, with more
modalities coming in the future.

## Benefits of on-device execution

On-device execution enables the following:

* **Local processing of sensitive data**: Processing data locally can help you
  avoid sending user data to the cloud. This is important for apps that handle
  sensitive data, such as messaging apps with end-to-end encryption.
* **Offline access**: Users can access AI features even when there is no
  internet connection. This is useful for applications that need to work
  offline or with variable connectivity.
* **Cost savings**: You can reduce inference costs by offloading execution to
  consumer hardware. This can produce significant savings for frequently used
  user flows.

On-device execution of Gemini has many benefits; however, for use cases that
require larger Gemini models, and to support a wide range of devices, you may
want to consider using the Gemini API for accessing Gemini on the server. You
can do this either through backend integration (with [Python](/tutorials/python_quickstart),
[Go](/tutorials/go_quickstart), [Node.js](/tutorials/node_quickstart), or [REST](/tutorials/rest_quickstart)) or directly from
your Android app through the new
[Google AI client SDK for Android](/tutorials/android_quickstart).

## How it works

On-device execution of Gemini Nano is powered by **Android AICore**, a new
system-level capability that provides access to foundation models for on-device
execution, introduced in Android 14. Foundation models are pre-installed using
AICore, so you don't need to download or distribute them within your app. You
can fine-tune these models for downstream tasks using LoRa. Android AICore is
now available in production on Google Pixel 8 Pro and Samsung S24 Series devices
and is already powering innovative features in Google apps.

For more information, see [Android AICore](https://developer.android.com/ml/aicore).

![AICore architecture](/static/tutorials/images/gemini-architecture-google-ai-edge-sdk-for-android.png)

**Figure 1.** AICore architecture

## What's next

* To learn how to take advantage of Gemini Pro inference on Google's servers
  in your Android app, read the [quickstart for
  the Google AI client SDK for Android](/tutorials/android_quickstart).

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-02-25 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-25 UTC."],[],[]]