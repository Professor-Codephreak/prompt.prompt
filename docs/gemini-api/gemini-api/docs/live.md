# Live API

* On this page

  + [Send and receive text](#send-receive-text)
  + [Receive audio](#receive-audio)
  + [Stream audio and video](#stream-audio-video)
  + [System instructions](#system-instructions)
  + [Incremental content updates](#incremental-updates)
  + [Change voices](#change-voices)
  + [Use function calling](#function-calling)
  + [Handle interruptions](#interruptions)
  + [Configure voice activity detection (VAD)](#voice-activity-detection)
  + [Get the token count](#token-count)
  + [Configure session resumption](#session-resumption)
  + [Receive a message before the session disconnects](#goaway-message)
  + [Receive a message when the generation is complete](#generation-complete-message)
  + [Enable context window compression](#context-window-compression)
  + [Change the media resolution](#media-resolution)

  + [Client authentication](#client-authentication)
  + [Session duration](#maximum-session-duration)
  + [Context window](#context-window)

**Preview:** The Live API is in preview.

The Live API enables low-latency bidirectional voice and
video interactions with Gemini. Using the Live API, you can
provide end users with the experience of natural, human-like voice
conversations, and with the ability to interrupt the model's responses using
voice commands. The model can process text, audio, and video input, and it can
provide text and audio output.

You can try the Live API in
[Google AI Studio](https://aistudio.google.com/app/live).

To try a tutorial that lets you use your voice and camera to talk to Gemini
through the Live API, see the [`Web Console Demo`
project](https://github.com/google-gemini/live-api-web-console).

## What's new

The Live API has new features and capabilities!

**New capabilities:**

* Two new voices and 30 new languages, with configurable output language
* Configurable image resolutions 66/256 tokens
* Configurable turn coverage: Send all inputs all the time or only when the user
  is speaking
* Configure if input should interrupt the model or not
* Configurable Voice Activity Detection and new client events for end of turn
  signaling
* Token counts
* A client event for signaling end of stream
* Text streaming
* Configurable session resumption, with session data stored on the server for
  24 hours
* Longer session support with a sliding context window

**New client events:**

* End of audio stream / mic closed
* Activity start/end events for manually controlling turn transition

**New server events:**

* Go away notification signaling a need to restart a session
* Generation complete

## Use the Live API

This section describes how to use the Live API with one of
our SDKs. For more information about the underlying WebSockets API, see the
[WebSockets API reference](/api/live).

### Send and receive text

```
import asyncio
from google import genai

client = genai.Client(api_key="GEMINI_API_KEY")
model = "gemini-2.0-flash-live-001"

config = {"response_modalities": ["TEXT"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        while True:
            message = input("User> ")
            if message.lower() == "exit":
                break
            await session.send_client_content(
                turns={"role": "user", "parts": [{"text": message}]}, turn_complete=True
            )

            async for response in session.receive():
                if response.text is not None:
                    print(response.text, end="")

if __name__ == "__main__":
    asyncio.run(main())

```

### Receive audio

The following example shows how to receive audio data and write it to a `.wav` file.

```
import asyncio
import wave
from google import genai

client = genai.Client(api_key="GEMINI_API_KEY", http_options={'api_version': 'v1alpha'})
model = "gemini-2.0-flash-live-001"

config = {"response_modalities": ["AUDIO"]}

async def main():
    async with client.aio.live.connect(model=model, config=config) as session:
        wf = wave.open("audio.wav", "wb")
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)

        message = "Hello? Gemini are you there?"
        await session.send_client_content(
            turns={"role": "user", "parts": [{"text": message}]}, turn_complete=True
        )

        async for idx,response in async_enumerate(session.receive()):
            if response.data is not None:
                wf.writeframes(response.data)

            # Un-comment this code to print audio data info

            # if response.server_content.model_turn is not None:

            #      print(response.server_content.model_turn.parts[0].inline_data.mime_type)

        wf.close()

if __name__ == "__main__":
    asyncio.run(main())

```

#### Audio formats

The Live API supports the following audio formats:

* Input audio format: Raw 16 bit PCM audio at 16kHz little-endian
* Output audio format: Raw 16 bit PCM audio at 24kHz little-endian

### Stream audio and video

To see an example of how to use
the Live API in a streaming audio and video format,
run the "Live API - Quickstart" file in the cookbooks repository:

[View
on GitHub](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI.py)

### System instructions

System instructions let you steer the behavior of a model based on your specific
needs and use cases. System instructions can be set in the setup configuration
and will remain in effect for the entire session.

```
from google.genai import types

config = {
    "system_instruction": types.Content(
        parts=[
            types.Part(
                text="You are a helpful assistant and answer in a friendly tone."
            )
        ]
    ),
    "response_modalities": ["TEXT"],
}

```

### Incremental content updates

Use incremental updates to send text input, establish session context, or
restore session context. For short contexts you can send turn-by-turn
interactions to represent the exact sequence of events:

[Python](#python)[JSON](#json)
More

```
turns = [
    {"role": "user", "parts": [{"text": "What is the capital of France?"}]},
    {"role": "model", "parts": [{"text": "Paris"}]},
]

await session.send_client_content(turns=turns, turn_complete=False)

turns = [{"role": "user", "parts": [{"text": "What is the capital of Germany?"}]}]

await session.send_client_content(turns=turns, turn_complete=True)

```
```
{
  "clientContent": {
    "turns": [
      {
        "parts":[
          {
            "text": ""
          }
        ],
        "role":"user"
      },
      {
        "parts":[
          {
            "text": ""
          }
        ],
        "role":"model"
      }
    ],
    "turnComplete": true
  }
}

```

For longer contexts it's recommended to provide a single message summary to free
up the context window for subsequent interactions.

### Change voices

The Live API supports the following voices: Puck, Charon,
Kore, Fenrir, Aoede, Leda, Orus, and Zephyr.

To specify a voice, set the voice name within the `speechConfig` object as part
of the session configuration:

[Python](#python)[JSON](#json)
More

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    speech_config=types.SpeechConfig(
        voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Kore")
        )
    )
)

```
```
{
  "voiceConfig": {
    "prebuiltVoiceConfig": {
      "voiceName": "Kore"
    }
  }
}

```

### Use function calling

You can define tools with the Live API. See the [Function calling
tutorial](https://ai.google.dev/gemini-api/docs/function-calling) to
learn more about function calling.

Tools must be defined as part of the session configuration:

```
config = types.LiveConnectConfig(
    response_modalities=["TEXT"],
    tools=[set_light_values]
)

async with client.aio.live.connect(model=model, config=config) as session:
    await session.send_client_content(
        turns={
            "role": "user",
            "parts": [{"text": "Turn the lights down to a romantic level"}],
        },
        turn_complete=True,
    )

    async for response in session.receive():
        print(response.tool_call)

```

From a single prompt, the model can generate multiple function calls and the
code necessary to chain their outputs. This code executes in a sandbox
environment, generating subsequent [BidiGenerateContentToolCall](/api/live#bidigeneratecontenttoolcall)
messages. The execution pauses until the results of each function call are
available, which ensures sequential processing.

The client should respond with [BidiGenerateContentToolResponse](/api/live#bidigeneratecontenttoolresponse).

Audio inputs and audio outputs negatively impact the model's ability to use
function calling.

### Handle interruptions

Users can interrupt the model's output at any time. When [Voice activity
detection](/api/live#voice-activity-detection) (VAD) detects an interruption, the ongoing
generation is canceled and discarded. Only the information already sent to the
client is retained in the session history. The server then sends a
[BidiGenerateContentServerContent](/api/live#bidigeneratecontentservercontent) message to
report the interruption.

In addition, the Gemini server discards any pending function calls and sends
a `BidiGenerateContentServerContent` message with the IDs of the canceled calls.

```
async for response in session.receive():
    if response.server_content.interrupted is not None:
        # The generation was interrupted

```

### Configure voice activity detection (VAD)

By default, the model automatically performs voice activity detection (VAD) on
a continuous audio input stream. VAD can be configured with the
[`realtimeInputConfig.automaticActivityDetection`](/api/live#RealtimeInputConfig.AutomaticActivityDetection)
field of the [setup configuration](/api/live#BidiGenerateContentSetup).

When the audio stream is paused for more than a second (for example,
because the user switched off the microphone), an
[`audioStreamEnd`](/api/live#BidiGenerateContentRealtimeInput.FIELDS.bool.BidiGenerateContentRealtimeInput.audio_stream_end)
event should be sent to flush any cached audio. The client can resume sending
audio data at any time.

Alternatively, the automatic VAD can be disabled by setting
`realtimeInputConfig.automaticActivityDetection.disabled` to `true` in the setup
message. In this configuration the client is responsible for detecting user
speech and sending
[`activityStart`](/api/live#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityStart.BidiGenerateContentRealtimeInput.activity_start)
and [`activityEnd`](/api/live#BidiGenerateContentRealtimeInput.FIELDS.BidiGenerateContentRealtimeInput.ActivityEnd.BidiGenerateContentRealtimeInput.activity_end)
messages at the appropriate times. An `audioStreamEnd` isn't sent in
this configuration. Instead, any interruption of the stream is marked by
an `activityEnd` message.

*SDK support for this feature will be available in the coming weeks.*

### Get the token count

You can find the total number of consumed tokens in the
[usageMetadata](/api/live#usagemetadata) field of the returned server message.

```
from google.genai import types

async with client.aio.live.connect(
    model='gemini-2.0-flash-live-001',
    config=types.LiveConnectConfig(
        response_modalities=['AUDIO'],
    ),
) as session:
    # Session connected

    while True:
        await session.send_client_content(
            turns=types.Content(role='user', parts=[types.Part(text='Hello world!')])
        )
        async for message in session.receive():
            # The server will periodically send messages that include

            # UsageMetadata.

            if message.usage_metadata:
                usage = message.usage_metadata
                print(
                    f'Used {usage.total_token_count} tokens in total. Response token'
                    ' breakdown:'
                )
            for detail in usage.response_tokens_details:
                match detail:
                  case types.ModalityTokenCount(modality=modality, token_count=count):
                      print(f'{modality}: {count}')

            # For the purposes of this example, placeholder input is continually fed

            # to the model. In non-sample code, the model inputs would come from

            # the user.

            if message.server_content and message.server_content.turn_complete:
                break

```

### Configure session resumption

To prevent session termination when the server periodically resets the WebSocket
connection, configure the [sessionResumption](/api/live#BidiGenerateContentSetup.FIELDS.SessionResumptionConfig.BidiGenerateContentSetup.session_resumption)
field within the [setup configuration](/api/live#BidiGenerateContentSetup).

Passing this configuration causes the
server to send [SessionResumptionUpdate](/api/live#SessionResumptionUpdate)
messages, which can be used to resume the session by passing the last resumption
token as the [`SessionResumptionConfig.handle`](/api/liveSessionResumptionConfig.FIELDS.string.SessionResumptionConfig.handle)
of the subsequent connection.

```
from google.genai import types

print(f"Connecting to the service with handle {previous_session_handle}...")
async with client.aio.live.connect(
    model="gemini-2.0-flash-live-001",
    config=types.LiveConnectConfig(
        response_modalities=["AUDIO"],
        session_resumption=types.SessionResumptionConfig(
            # The handle of the session to resume is passed here,

            # or else None to start a new session.

            handle=previous_session_handle
        ),
    ),
) as session:
    # Session connected

    while True:
        await session.send_client_content(
            turns=types.Content(
                role="user", parts=[types.Part(text="Hello world!")]
            )
        )
        async for message in session.receive():
            # Periodically, the server will send update messages that may

            # contain a handle for the current state of the session.

            if message.session_resumption_update:
                update = message.session_resumption_update
                if update.resumable and update.new_handle:
                    # The handle should be retained and linked to the session.

                    return update.new_handle

            # For the purposes of this example, placeholder input is continually fed

            # to the model. In non-sample code, the model inputs would come from

            # the user.

            if message.server_content and message.server_content.turn_complete:
                break

```

### Receive a message before the session disconnects

The server sends a [GoAway](/api/live#GoAway) message that signals that the current
connection will soon be terminated. This message includes the [timeLeft](/api/live#GoAway.FIELDS.google.protobuf.Duration.GoAway.time_left),
indicating the remaining time and lets you take further action before the
connection will be terminated as ABORTED.

### Receive a message when the generation is complete

The server sends a [generationComplete](/api/live#BidiGenerateContentServerContent.FIELDS.bool.BidiGenerateContentServerContent.generation_complete)
message that signals that the model finished generating the response.

### Enable context window compression

To enable longer sessions, and avoid abrupt connection termination, you can
enable context window compression by setting the [contextWindowCompression](/api/live#BidiGenerateContentSetup.FIELDS.ContextWindowCompressionConfig.BidiGenerateContentSetup.context_window_compression)
field as part of the session configuration.

In the [ContextWindowCompressionConfig](/api/live#contextwindowcompressionconfig), you
can configure a [sliding-window mechanism](/api/live#ContextWindowCompressionConfig.FIELDS.ContextWindowCompressionConfig.SlidingWindow.ContextWindowCompressionConfig.sliding_window)
and the [number of tokens](/api/live#ContextWindowCompressionConfig.FIELDS.int64.ContextWindowCompressionConfig.trigger_tokens)
that triggers compression.

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    context_window_compression=(
        # Configures compression with default parameters.

        types.ContextWindowCompressionConfig(
            sliding_window=types.SlidingWindow(),
        )
    ),
)

```

### Change the media resolution

You can specify the media resolution for the input media by setting the
`mediaResolution` field as part of the session configuration:

```
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    media_resolution=types.MediaResolution.MEDIA_RESOLUTION_LOW,
)

```

## Limitations

Consider the following limitations of the Live API and
Gemini 2.0 when you plan your project.

### Client authentication

The Live API only provides server to server authentication
and isn't recommended for direct client use. Client input should be routed
through an intermediate application server for secure authentication with
the Live API.

### Session duration

Session duration can be extended to unlimited by enabling session [compression](/gemini-api/docs/live#context-window-compression).
Without compression, audio-only sessions are limited to 15 minutes,
and audio plus video sessions are limited to 2 minutes. Exceeding these limits
without compression will terminate the connection.

### Context window

A session has a context window limit of 32k tokens.

## Third-party integrations

For web and mobile app deployments, you can explore options from:

Was this helpful?

Send feedback

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-11 UTC.

Need to tell us more?

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Missing the information I need","missingTheInformationINeed","thumb-down"],["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"],["Out of date","outOfDate","thumb-down"],["Samples / code issue","samplesCodeIssue","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-11 UTC."],[],[]]