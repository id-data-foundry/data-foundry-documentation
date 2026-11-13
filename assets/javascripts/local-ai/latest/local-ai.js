/*!
 * DF Local AI - a high-level library for Industrial Design education,
 * using Data Foundry Local AI functionalities.
 *
 * Copyright (c) 2024-2026 Jort Wiersma and Mathias Funk
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
const foundry = {
  resolveServer: function (server) {
    if (server && typeof server === "string" && server.trim().length > 0) {
      return server.trim().replace(/\/+$/, "");
    }
    return typeof document !== "undefined" && document.location ? document.location.origin : "";
  },
  textToText: async function (options) {
    const result = await foundry.textToTextWithUsage(options);
    return result ? result.text : undefined;
  },
  textToTextWithUsage: async function ({
    api_token,
    server = document.location.origin,
    model = "default",
    prompt,
    messages,
    temperature = 0.9,
    maxTokens = 1000,
    responseFormat,
    tools,
    toolChoice,
    stream = false,
    onChunk,
    logging = true,
    loadingElementSelector,
    resultElementSelector,
  }) {
    server = foundry.resolveServer(server);
    if (!api_token) {
      // Do not run the function when no API key is given
      console.error("No API key provided.");
      return;
    }

    if (logging) {
      console.log("Running text-to-text function");
    }

    // Create message for request
    if (!messages) {
      if (!prompt) {
        console.error("No prompt given. Empty message created.");
        prompt = "";
      }
      messages = [
        // Create a message for LocalAI
        {
          role: "user",
          content: prompt,
        },
      ];
    }

    // Start the loading indicator
    let loadingElement;
    if (loadingElementSelector) {
      loadingElement = document.querySelector(loadingElementSelector);
      if(!loadingElement) {
        console.warn("Element specified for loading indicator not found (using result element instead)");
        loadingElement = document.querySelector(resultElementSelector);
      }
      loadingElement && loadingElement.setAttribute("aria-busy", "true");
    }

    try {
      // Send messages to LocalAI
      const response = await fetch(
        `${server}/v1/chat/completions`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${api_token}`,
          },
          body: JSON.stringify({
            messages: messages,
            model: model,
            temperature: temperature,
            max_tokens: maxTokens,
            stream: stream,
            ...(responseFormat && { response_format: responseFormat }),
            ...(tools && { tools: tools }),
            ...(toolChoice && { tool_choice: toolChoice }),
          }),
        }
      );

      // check for error in response
      if(!response.ok) {
        const errorJson = await response.json();
        alert(errorJson.error || "An error occurred");
        if (loadingElement) {
          loadingElement.setAttribute("aria-busy", "false");
        }
        return;
      }

      let chatResponse = "";
      let toolCalls = undefined;
      let usage = undefined;

      if (stream) {
        const reader = response.body.getReader();
        const decoder = new TextDecoder("utf-8");
        let buffer = "";

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          buffer += decoder.decode(value, { stream: true });

          let parts = buffer.split(/\r?\n\r?\n/);
          buffer = parts.pop();

          for (const eventStr of parts) {
            if (!eventStr.trim()) continue;

            const lines = eventStr.split(/\r?\n/);
            let dataStr = "";
            for (const line of lines) {
              if (line.trim().startsWith("data:")) {
                dataStr += line.replace(/^data:\s*/, "") + "\n";
              }
            }
            dataStr = dataStr.trim();

            if (dataStr === "[DONE]") continue;
            if (!dataStr) continue;

            try {
              const data = JSON.parse(dataStr);
              const choice = data.choices && data.choices[0];
              const delta = choice && (choice.delta || choice.message);

              if (delta && delta.content !== undefined && delta.content !== null) {
                const content = delta.content;

                // Stop loading indicator on first chunk
                if (loadingElement) {
                  loadingElement.setAttribute("aria-busy", "false");
                  loadingElement = null;
                }

                chatResponse += content;
                if (onChunk) {
                  onChunk(content);
                }
                if (resultElementSelector) {
                  const el = document.querySelector(resultElementSelector);
                  if (el) el.insertAdjacentText('beforeend', content);
                }
              }
              if (data.usage) {
                usage = data.usage;
              }
            } catch (e) {
              console.error("SSE parse error", e, dataStr);
            }
          }
        }
      } else {
        // Wait for LocalAI response
        const json = await response.json();

        // check for error in response
        if(json.error) {
          // if so, display and return
          alert(json.error);
          if (loadingElement) {
            loadingElement.setAttribute("aria-busy", "false");
          }
          return;
        }

        // json.content contains the generated chat response
        let message = json.choices[0].message;
        chatResponse = message.content;
        toolCalls = message.tool_calls;
        usage = json.usage;
      }

      // Stop loading indicator
      if (loadingElement) {
        loadingElement.setAttribute("aria-busy", "false");
      }

      if (logging) {
        console.log("Result:", chatResponse);
        if (toolCalls) {
          console.log("Tool Calls:", toolCalls);
        }
      }

      // Place result on the page (only if not streaming, as streaming already handles this)
      if (!stream && resultElementSelector && chatResponse) {
        const el = document.querySelector(resultElementSelector);
        if (el) el.insertAdjacentText("beforeend", chatResponse);
      }

      // Return the AI response and usage
      return { text: chatResponse, toolCalls: toolCalls, usage: usage };
    } catch (error) {
      console.error("Error:", error);
    }
  },
  chatbot: async function ({
    api_token,
    server = document.location.origin,
    chatbotId,
    message,
    conversationId,
    logging = true,
    loadingElementSelector,
    resultElementSelector,
  }) {
    server = foundry.resolveServer(server);
    if (!api_token) {
      console.error("No API key provided.");
      return;
    }
    if (!chatbotId) {
      console.error("No chatbot ID provided.");
      return;
    }

    if (logging) {
      console.log("Running chatbot function for bot:", chatbotId);
    }

    // Start the loading indicator
    let loadingElement;
    if (loadingElementSelector) {
      loadingElement = document.querySelector(loadingElementSelector);
      if(!loadingElement) {
        console.warn("Element specified for loading indicator not found (using result element instead)");
        loadingElement = document.querySelector(resultElementSelector);
      }
      loadingElement && loadingElement.setAttribute("aria-busy", "true");
    }

    try {
      const response = await fetch(
        `${server}/api/v1/chatbots/${chatbotId}/chat`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${api_token}`,
          },
          body: JSON.stringify({
            message: message,
            conversationId: conversationId
          }),
        }
      );

      const json = await response.json();

      if (loadingElement) {
        loadingElement.setAttribute("aria-busy", "false");
      }

      if(json.error) {
        alert(json.error);
        return;
      }

      // json.choices[0].message.content contains the generated chat response
      let chatResponse = json.choices[0].message.content;
      if (logging) {
        console.log("Result:", chatResponse);
        console.log("Conversation ID:", json.conversationId);
      }

      // Place result on the page
      if (resultElementSelector && chatResponse) {
        const el = document.querySelector(resultElementSelector);
        if (el) el.insertAdjacentText("beforeend", chatResponse);
      }

      // Return an object with both the content and the conversationId
      // to allow for easy state management in subsequent calls.
      return {
        content: chatResponse,
        conversationId: json.conversationId
      };
    } catch (error) {
      console.error("Error:", error);
    }
  },
  textToImage: async function ({
    api_token,
    server = document.location.origin,
    model = "default",
    prompt,
    negativePrompt = '',
    cfgScale = 10,
    seed = -1,
    steps = 20,
    width = 512,
    height = 512,
    logging = true,
    loadingElementSelector,
    resultElementSelector
  }) {
    server = foundry.resolveServer(server);
    if (logging) {
      console.log("Running text-to-image function");
    }
    // Do not run the function when no API key is given
    if (!api_token) {
      console.error("No API key provided.");
      return;
    }

    // Start the loading indicator
    let loadingElement;
    if (loadingElementSelector) {
      loadingElement = document.querySelector(loadingElementSelector);
      if(!loadingElement) {
        console.warn("Element specified for loading indicator not found (using result element instead)");
        loadingElement = document.querySelector(resultElementSelector);
      }
      loadingElement && loadingElement.setAttribute("aria-busy", "true");
    }

    try {
      // Make AI request
      const response = await fetch(
        `${server}/v1/images/generations`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${api_token}`,
          },
          body: JSON.stringify({
            model: model,
            prompt: prompt,
            steps: steps,
            width: width,
            height: height,
            cfg: cfgScale,
            seed: seed,
            negativeprompt: negativePrompt
          }),
        }
      );

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const json = await response.json();

      // Stop loading indicator
      if (loadingElement) {
        loadingElement.setAttribute("aria-busy", "false");
      }

      // check for error in response
      if(json.error) {
        // if so, display and return
        alert(json.error);
        return;
      }

      if (logging) {
        console.log("Generated image:", json["image_url"]);
      }

      // If a result element has been provided (which should be an <img> element, place the result)
      if (resultElementSelector) {
        document.querySelector(resultElementSelector).src = json["image_url"].replace('http://', 'https://');
      }

      return json["image_url"];
    } catch (error) {
      console.error("There was a problem with the fetch operation:", error.message);
    }
  },
  imageToImage: async function ({
    api_token,
    server = document.location.origin,
    model = "default",
    image,
    prompt,
    negativePrompt = '',
    strength = 0.7,
    cfgScale = 10,
    seed = -1,
    steps = 20,
    width = 512,
    height = 512,
    logging = true,
    loadingElementSelector,
    resultElementSelector
  }) {
    server = foundry.resolveServer(server);
    if (logging) {
      console.log("Running image-to-image function");
    }
    if (!api_token) {
      console.error("No API key provided.");
      return;
    }
    if (!image) {
      console.error("No input image provided.");
      return;
    }

    let loadingElement;
    if (loadingElementSelector) {
      loadingElement = document.querySelector(loadingElementSelector);
      if (!loadingElement) {
        console.warn("Element specified for loading indicator not found (using result element instead)");
        loadingElement = document.querySelector(resultElementSelector);
      }
      loadingElement && loadingElement.setAttribute("aria-busy", "true");
    }

    try {
      const normalizedImage = await foundry.normalizeImageInput(image);
      const formData = new FormData();
      if (normalizedImage instanceof Blob) {
        formData.append("image", normalizedImage, "image.png");
      } else {
        formData.append("image", normalizedImage);
      }
      formData.append("model", model);
      if (prompt) formData.append("prompt", prompt);
      if (negativePrompt) formData.append("negativeprompt", negativePrompt);
      if (strength !== undefined) formData.append("strength", String(Math.max(0.0, Math.min(1.0, strength))));
      if (cfgScale !== undefined) formData.append("cfg", String(cfgScale));
      if (seed !== undefined) formData.append("seed", String(seed));
      if (steps !== undefined) formData.append("steps", String(Math.max(1, Math.min(50, steps))));
      if (width !== undefined) formData.append("width", String(Math.max(64, Math.min(2048, width))));
      if (height !== undefined) formData.append("height", String(Math.max(64, Math.min(2048, height))));

      const response = await fetch(`${server}/v1/images/edits`, {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${api_token}`,
        },
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const json = await response.json();

      if (loadingElement) {
        loadingElement.setAttribute("aria-busy", "false");
      }

      if (json.error) {
        alert(json.error);
        return;
      }

      if (logging) {
        console.log("Generated image:", json["image_url"]);
      }

      if (resultElementSelector) {
        document.querySelector(resultElementSelector).src = json["image_url"].replace('http://', 'https://');
      }

      return json["image_url"];
    } catch (error) {
      console.error("There was a problem with image-to-image operation:", error.message);
    } finally {
      if (loadingElement) {
        loadingElement.setAttribute("aria-busy", "false");
      }
    }
  },
  editImage: async function ({
    api_token,
    server = document.location.origin,
    model = "default",
    image,
    mask,
    prompt,
    negativePrompt = '',
    strength = 0.8,
    cfgScale = 10,
    seed = -1,
    steps = 20,
    width = 512,
    height = 512,
    logging = true,
    loadingElementSelector,
    resultElementSelector
  }) {
    server = foundry.resolveServer(server);
    if (logging) {
      console.log("Running edit-image (inpainting) function");
    }
    if (!api_token) {
      console.error("No API key provided.");
      return;
    }
    if (!image) {
      console.error("No base image provided.");
      return;
    }

    let loadingElement;
    if (loadingElementSelector) {
      loadingElement = document.querySelector(loadingElementSelector);
      if (!loadingElement) {
        console.warn("Element specified for loading indicator not found (using result element instead)");
        loadingElement = document.querySelector(resultElementSelector);
      }
      loadingElement && loadingElement.setAttribute("aria-busy", "true");
    }

    try {
      const normalizedImage = await foundry.normalizeImageInput(image);
      const formData = new FormData();
      if (normalizedImage instanceof Blob) {
        formData.append("image", normalizedImage, "image.png");
      } else {
        formData.append("image", normalizedImage);
      }
      if (mask) {
        const normalizedMask = await foundry.normalizeImageInput(mask);
        if (normalizedMask instanceof Blob) {
          formData.append("mask", normalizedMask, "mask.png");
        } else {
          formData.append("mask", normalizedMask);
        }
      }
      formData.append("model", model);
      if (prompt) formData.append("prompt", prompt);
      if (negativePrompt) formData.append("negativeprompt", negativePrompt);
      if (strength !== undefined) formData.append("strength", String(Math.max(0.0, Math.min(1.0, strength))));
      if (cfgScale !== undefined) formData.append("cfg", String(cfgScale));
      if (seed !== undefined) formData.append("seed", String(seed));
      if (steps !== undefined) formData.append("steps", String(Math.max(1, Math.min(50, steps))));
      if (width !== undefined) formData.append("width", String(Math.max(64, Math.min(2048, width))));
      if (height !== undefined) formData.append("height", String(Math.max(64, Math.min(2048, height))));

      const response = await fetch(`${server}/v1/images/edits`, {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${api_token}`,
        },
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const json = await response.json();

      if (loadingElement) {
        loadingElement.setAttribute("aria-busy", "false");
      }

      if (json.error) {
        alert(json.error);
        return;
      }

      if (logging) {
        console.log("Edited image:", json["image_url"]);
      }

      if (resultElementSelector) {
        document.querySelector(resultElementSelector).src = json["image_url"].replace('http://', 'https://');
      }

      return json["image_url"];
    } catch (error) {
      console.error("There was a problem with image edit operation:", error.message);
    } finally {
      if (loadingElement) {
        loadingElement.setAttribute("aria-busy", "false");
      }
    }
  },
  imageVariation: async function ({
    api_token,
    server = document.location.origin,
    model = "default",
    image,
    n = 1,
    logging = true,
    loadingElementSelector,
    resultElementSelector
  }) {
    server = foundry.resolveServer(server);
    if (logging) {
      console.log("Running image-variation function");
    }
    if (!api_token) {
      console.error("No API key provided.");
      return;
    }
    if (!image) {
      console.error("No input image provided.");
      return;
    }

    let loadingElement;
    if (loadingElementSelector) {
      loadingElement = document.querySelector(loadingElementSelector);
      if (!loadingElement) {
        console.warn("Element specified for loading indicator not found (using result element instead)");
        loadingElement = document.querySelector(resultElementSelector);
      }
      loadingElement && loadingElement.setAttribute("aria-busy", "true");
    }

    try {
      const normalizedImage = await foundry.normalizeImageInput(image);
      const formData = new FormData();
      if (normalizedImage instanceof Blob) {
        formData.append("image", normalizedImage, "image.png");
      } else {
        formData.append("image", normalizedImage);
      }
      formData.append("model", model);
      if (n !== undefined) formData.append("n", String(n));

      const response = await fetch(`${server}/v1/images/variations`, {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${api_token}`,
        },
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const json = await response.json();

      if (loadingElement) {
        loadingElement.setAttribute("aria-busy", "false");
      }

      if (json.error) {
        alert(json.error);
        return;
      }

      if (logging) {
        console.log("Variation image:", json["image_url"]);
      }

      if (resultElementSelector) {
        document.querySelector(resultElementSelector).src = json["image_url"].replace('http://', 'https://');
      }

      return json["image_url"];
    } catch (error) {
      console.error("There was a problem with image variation operation:", error.message);
    } finally {
      if (loadingElement) {
        loadingElement.setAttribute("aria-busy", "false");
      }
    }
  },
  textToSpeech: async function ({
    api_token,
    server = document.location.origin,
    prompt,
    language = "en",
    voice = "af_heart",
    model = "kokoro",
    speed = 1.0,
    loadingElementSelector,
    resultElementSelector,
    logging = true,
  }) {
    server = foundry.resolveServer(server);
    if (!api_token) {
      // Do not run the function when no API key has been provided
      console.error("No API key provided.");
      return;
    }

    if (logging) {
      console.log("Running text-to-sound function");
    }

    let loadingElement;
    if (loadingElementSelector) {
      loadingElement = document.querySelector(loadingElementSelector);
      if(!loadingElement) {
        console.warn("Element specified for loading indicator not found (using result element instead)");
        loadingElement = document.querySelector(resultElementSelector);
      }
      loadingElement && loadingElement.setAttribute("aria-busy", "true");
    }

    try {
      const response = await fetch(
        `${server}/v1/audio/speech`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${api_token}`,
          },
          body: JSON.stringify({
            model: model || "kokoro",
            // choose from: https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md
            voice: voice,
            lang: language,
            input: prompt,
            speed: speed,
          }),
        }
      );

      if (loadingElement) {
        loadingElement.setAttribute("aria-busy", "false");
      }

      if(!response.ok) {
        console.error("Problem occurred in generating speech.");
        return;
      }

      // note: we don't need to check for a json.error response,
      // because the response will either have a proper error code or contain the speech as MP3

      const blob = await response.blob();
      const objectURL = URL.createObjectURL(blob);

      if (resultElementSelector) {
        document.querySelector(resultElementSelector).src = objectURL;
        document.querySelector(resultElementSelector).play();
      }

      return objectURL;
    } catch (err) {
      console.error(err);
    }
  },
  textToRobot: async function ({
    api_token,
    server = document.location.origin,
    projectId,
    prompt,
    language = "en",
    voice = "retro",
    speed = 1.0,
    loadingElementSelector,
    resultElementSelector,
    logging = true,
  }) {
    server = foundry.resolveServer(server);
    if (!api_token) {
      // Do not run the function when no API key has been provided
      console.error("No API key provided.");
      return;
    }

    // Modern local AI route: /v1/audio/speech with model: "robot"
    if (!projectId) {
      return foundry.textToSpeech({
        api_token,
        server,
        prompt,
        language,
        voice,
        model: "robot",
        speed,
        loadingElementSelector,
        resultElementSelector,
        logging,
      });
    }

    if (logging) {
      console.log("Running text-to-sound function");
    }

    // Start the loading indicator
    let loadingElement;
    if (loadingElementSelector) {
      loadingElement = document.querySelector(loadingElementSelector);
      if(!loadingElement) {
        console.warn("Element specified for loading indicator not found (using result element instead)");
        loadingElement = document.querySelector(resultElementSelector);
      }
      loadingElement && loadingElement.setAttribute("aria-busy", "true");
    }

    try {
      const response = await fetch(
        `${server}/api/vendor/t2s/${projectId}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            api_token: api_token,
            lang: language,
            text: prompt,
          }),
        }
      );
      const json = await response.json();
      const audioLink = `${server}/api/vendor/t2s/${json.text}`;
      if (logging) {
        console.log("Generated audio:", audioLink);
      }
      if (json.text === undefined) {
        console.error(
          "No result. It is possible your API Key and project ID are not matching."
        );
      }
      if (loadingElement) {
        loadingElement.setAttribute("aria-busy", "false");
      }
      if (resultElementSelector) {
        document.querySelector(resultElementSelector).src = audioLink;
      }

      return audioLink;
    } catch (err) {
      console.error(err);
    }
  },
  imageToText: async function (options) {
    const result = await foundry.imageToTextWithUsage(options);
    return result ? result.text : undefined;
  },
  imageToTextWithUsage: async function ({
    api_token,
    server = document.location.origin,
    model = "vision",
    prompt = '',
    systemPrompt = '',
    image,
    messages,
    temperature = 0.8,
    maxTokens = 1000,
    responseFormat,
    tools,
    toolChoice,
    stream = false,
    onChunk,
    logging = true,
    loadingElementSelector,
    resultElementSelector,
  }) {
    server = foundry.resolveServer(server);
    if (!api_token) {
      // Do not run the function when no API key has been provided
      console.error("No API key provided.");
      return;
    }

    // if no image or image url is given
    if (!image && !messages) {
      console.error("No image provided!");
      return;
    }

    if (logging) {
      console.log("Running image-to-text function");
    }
    if(image) {
      image = await foundry.processImage(image);
    }
    messages = messages || [
      {
        role: "system",
        content: systemPrompt,
      },
      {
        role: "user",
        content: [
          { type: "text", text: prompt },
          { type: "image_url", image_url: { url: image }},
        ],
      },
    ];

    // Start the loading indicator
    let loadingElement;
    if (loadingElementSelector) {
      loadingElement = document.querySelector(loadingElementSelector);
      if(!loadingElement) {
        console.warn("Element specified for loading indicator not found (using result element instead)");
        loadingElement = document.querySelector(resultElementSelector);
      }
      loadingElement && loadingElement.setAttribute("aria-busy", "true");
    }

    try {
      // Send messages to LocalAI
      const response = await fetch(
        `${server}/v1/chat/completions`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${api_token}`,
          },
          body: JSON.stringify({
            messages: messages,
            model: model,
            temperature: temperature,
            max_tokens: maxTokens,
            stream: stream,
            ...(responseFormat && { response_format: responseFormat }),
            ...(tools && { tools: tools }),
            ...(toolChoice && { tool_choice: toolChoice }),
          }),
        }
      );

      // check for error in response
      if(!response.ok) {
        const errorJson = await response.json();
        alert(errorJson.error || "An error occurred");
        if (loadingElement) {
          loadingElement.setAttribute("aria-busy", "false");
        }
        return;
      }

      let chatResponse = "";
      let toolCalls = undefined;
      let usage = undefined;

      if (stream) {
        const reader = response.body.getReader();
        const decoder = new TextDecoder("utf-8");
        let buffer = "";

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          buffer += decoder.decode(value, { stream: true });

          let parts = buffer.split(/\r?\n\r?\n/);
          buffer = parts.pop();

          for (const eventStr of parts) {
            if (!eventStr.trim()) continue;

            const lines = eventStr.split(/\r?\n/);
            let dataStr = "";
            for (const line of lines) {
              if (line.trim().startsWith("data:")) {
                dataStr += line.replace(/^data:\s*/, "") + "\n";
              }
            }
            dataStr = dataStr.trim();

            if (dataStr === "[DONE]") continue;
            if (!dataStr) continue;

            try {
              const data = JSON.parse(dataStr);
              const choice = data.choices && data.choices[0];
              const delta = choice && (choice.delta || choice.message);

              if (delta && delta.content !== undefined && delta.content !== null) {
                const content = delta.content;

                // Stop loading indicator on first chunk
                if (loadingElement) {
                  loadingElement.setAttribute("aria-busy", "false");
                  loadingElement = null;
                }

                chatResponse += content;
                if (onChunk) {
                  onChunk(content);
                }
                if (resultElementSelector) {
                  const el = document.querySelector(resultElementSelector);
                  if (el) el.insertAdjacentText('beforeend', content);
                }
              }
              if (data.usage) {
                usage = data.usage;
              }
            } catch (e) {
              console.error("SSE parse error", e, dataStr);
            }
          }
        }
      } else {
        // Wait for LocalAI response
        const json = await response.json();

        // check for error in response
        if (json.error) {
          console.error("Error:", json);
          // if so, display and return
          alert(json.error);
          if (loadingElement) {
            loadingElement.setAttribute("aria-busy", "false");
          }
          return;
        }

        // json.content contains the generated chat response
        let message = json.choices[0].message;
        chatResponse = message.content;
        toolCalls = message.tool_calls;
        usage = json.usage;
      }

      // Stop loading indicator
      if (loadingElement) {
        loadingElement.setAttribute("aria-busy", "false");
      }

      if (logging) {
        console.log("Result:", chatResponse);
        if (toolCalls) {
          console.log("Tool Calls:", toolCalls);
        }
      }

      // Place result on the page
      if (!stream && resultElementSelector && chatResponse) {
        const el = document.querySelector(resultElementSelector);
        if (el) el.insertAdjacentText("beforeend", chatResponse);
      }

      return { text: chatResponse, toolCalls: toolCalls, usage: usage };
    } catch (error) {
      console.error("Error:", error);
    }
  },
  transcribeFile: async function ({
    api_token,
    server = document.location.origin,
    file,
    model = "whisper-base",
    lang = "",
    timestamps = false,
    diarization = false,
    num_speakers = null,
    resultElementSelector,
    loadingElementSelector,
    onTranscribe = (text) => {},
    logging = true,
  }) {
    server = foundry.resolveServer(server);
    if (!api_token) {
      console.error("No API key provided for transcribeFile.");
      return;
    }
    if (!file) {
      console.error("No audio file provided to transcribeFile.");
      return;
    }

    let loadingElement;
    if (loadingElementSelector) {
      loadingElement = document.querySelector(loadingElementSelector);
      if (!loadingElement && resultElementSelector) {
        loadingElement = document.querySelector(resultElementSelector);
      }
      loadingElement && loadingElement.setAttribute("aria-busy", "true");
    }

    const formData = new FormData();
    formData.append("model", model);
    formData.append("file", file, file.name || "audio.webm");
    if (lang) formData.append("lang", lang);
    if (timestamps) formData.append("timestamps", "true");
    if (diarization) formData.append("diarization", "true");
    if (num_speakers) formData.append("num_speakers", String(num_speakers));

    try {
      if (logging) console.log("transcribeFile: Uploading audio to longform STT service...");
      const response = await fetch(`${server}/v1/audio/transcriptions`, {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${api_token}`,
        },
        body: formData,
      });

      const result = await response.json();
      const text = result && result.text ? result.text : "";
      if (logging) console.log("transcribeFile result:", text);

      onTranscribe(text);
      if (resultElementSelector && text) {
        const target = document.querySelector(resultElementSelector);
        if (target) target.insertAdjacentText("beforeend", text + " ");
      }
      return text;
    } catch (error) {
      console.error("transcribeFile error:", error);
    } finally {
      loadingElement && loadingElement.setAttribute("aria-busy", "false");
    }
  },

  transcribeLive: async function ({
    api_token,
    server = document.location.origin,
    sampleRate = 16000,
    resultElementSelector,
    partialElementSelector,
    loadingElementSelector,
    onPartial = (text) => {},
    onFinal = (text) => {},
    logging = true,
  }) {
    server = foundry.resolveServer(server);
    if (!api_token) {
      console.error("No API key provided for transcribeLive.");
      return;
    }

    let loadingElement;
    if (loadingElementSelector) {
      loadingElement = document.querySelector(loadingElementSelector);
      loadingElement && loadingElement.setAttribute("aria-busy", "true");
    }

    let wsProto = "ws:";
    if (typeof location !== "undefined" && location.protocol === "https:") {
      wsProto = "wss:";
    }
    const host = server.replace(/^https?:\/\//, "");
    const wsUrl = `${wsProto}//${host}/v1/audio/transcriptions/stream?token=${encodeURIComponent(api_token)}`;

    let ws = null;
    let audioContext = null;
    let mediaStream = null;
    let processor = null;
    let fullTranscription = "";

    try {
      if (logging) console.log("transcribeLive: Connecting to real-time STT WebSocket:", wsUrl);
      ws = new WebSocket(wsUrl);

      const sessionPromise = new Promise((resolve, reject) => {
        ws.onopen = async () => {
          if (logging) console.log("transcribeLive: WebSocket connected. Starting mic capture...");
          try {
            mediaStream = await navigator.mediaDevices.getUserMedia({
              audio: {
                channelCount: 1,
                sampleRate: sampleRate,
                echoCancellation: true,
                noiseSuppression: true,
              },
            });

            audioContext = new (window.AudioContext || window.webkitAudioContext)({ sampleRate: sampleRate });
            const source = audioContext.createMediaStreamSource(mediaStream);
            processor = audioContext.createScriptProcessor(2048, 1, 1);

            processor.onaudioprocess = (e) => {
              if (ws.readyState !== WebSocket.OPEN) return;
              const inputData = e.inputBuffer.getChannelData(0);

              // Convert Float32 to 16-bit linear PCM
              const pcm16 = new Int16Array(inputData.length);
              for (let i = 0; i < inputData.length; i++) {
                const s = Math.max(-1, Math.min(1, inputData[i]));
                pcm16[i] = s < 0 ? s * 0x8000 : s * 0x7FFF;
              }

              // Base64 encode PCM frame for JSON WebSocket
              let binary = "";
              const bytes = new Uint8Array(pcm16.buffer);
              const len = bytes.byteLength;
              for (let i = 0; i < len; i++) {
                binary += String.fromCharCode(bytes[i]);
              }
              const base64Audio = btoa(binary);

              ws.send(JSON.stringify({
                audio: base64Audio,
                sample_rate: sampleRate,
              }));
            };

            source.connect(processor);
            processor.connect(audioContext.destination);

            window.df_liveSession = {
              stop: stopLiveInternal,
            };
            resolve(window.df_liveSession);
          } catch (micErr) {
            console.error("Microphone access failed:", micErr);
            reject(micErr);
          }
        };

        ws.onmessage = (event) => {
          try {
            const data = JSON.parse(event.data);
            if (data.type === "partial") {
              if (logging) console.log("Live STT partial:", data.text);
              onPartial(data.text);
              if (partialElementSelector) {
                const pEl = document.querySelector(partialElementSelector);
                if (pEl) pEl.textContent = data.text;
              }
            } else if (data.type === "final") {
              if (logging) console.log("Live STT final:", data.text);
              fullTranscription += (fullTranscription ? " " : "") + data.text;
              onFinal(data.text);
              if (partialElementSelector) {
                const pEl = document.querySelector(partialElementSelector);
                if (pEl) pEl.textContent = "";
              }
              if (resultElementSelector) {
                const rEl = document.querySelector(resultElementSelector);
                if (rEl) rEl.insertAdjacentText("beforeend", data.text + " ");
              }
            }
          } catch (err) {
            console.error("Error parsing live STT message:", err);
          }
        };

        ws.onerror = (err) => {
          console.error("Live STT WebSocket error:", err);
          reject(err);
        };
      });

      function stopLiveInternal() {
        if (processor) {
          try { processor.disconnect(); } catch (e) {}
          processor = null;
        }
        if (audioContext) {
          try { audioContext.close(); } catch (e) {}
          audioContext = null;
        }
        if (mediaStream) {
          mediaStream.getTracks().forEach((t) => t.stop());
          mediaStream = null;
        }
        if (ws && ws.readyState === WebSocket.OPEN) {
          try {
            ws.send(JSON.stringify({ action: "stop" }));
            ws.close();
          } catch (e) {}
        }
        ws = null;
        loadingElement && loadingElement.setAttribute("aria-busy", "false");
        window.df_liveSession = null;
        return fullTranscription;
      }

      window.df_stopLive = stopLiveInternal;
      return await sessionPromise;
    } catch (err) {
      loadingElement && loadingElement.setAttribute("aria-busy", "false");
      console.error("transcribeLive error:", err);
    }
  },

  stopLive: function () {
    if (window.df_stopLive) {
      return window.df_stopLive();
    }
    return "";
  },

  soundToText: async function ({
    api_token,
    server = document.location.origin,
    type = "file", //'file' or 'record'
    file, // The audio file that needs to be transcribed
    resultElementSelector,
    partialElementSelector,
    loadingElementSelector,
    onTranscribe = (text) => {},
    logging = true,
    stopRec = false,
  }) {
    if (stopRec) {
      if (window.df_stopLive) {
        return window.df_stopLive();
      }
      return "";
    }

    // 1. File mode: delegate to dedicated transcribeFile
    if (type === "file" || file) {
      return await foundry.transcribeFile({
        api_token,
        server,
        file,
        resultElementSelector,
        loadingElementSelector,
        onTranscribe,
        logging,
      });
    }

    // 2. Record mode: delegate to real-time streaming transcribeLive
    if (type === "record") {
      return await foundry.transcribeLive({
        api_token,
        server,
        resultElementSelector,
        partialElementSelector,
        loadingElementSelector,
        onPartial: onTranscribe,
        onFinal: onTranscribe,
        logging,
      });
    }
  },
  stopRec: async function ({
    logging = true,
    loadingElementSelector,
    resultElementSelector,
  }) {
    return await foundry.soundToText({
      stopRec: true,
      logging: logging,
      loadingElementSelector,
      resultElementSelector,
    });
  },
  models: async function (api_token, server = document.location.origin) {
    server = foundry.resolveServer(server);
    if (!api_token) {
      console.error("No api token provided!");
      return "No api token provided!";
    }
    try {
      const response = await fetch(`${server}/v1/models`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${api_token}`,
        },
      });
      // Wait for LocalAI response
      return await response.json();
    } catch (err) {
      console.error(err);
    }
  },
  popup: async function (type, logging = true) {
    // If not file input had already been created, create a new one
    if (!document.querySelector("#df_hiddenFileInput")) {
      const hiddenInput = document.createElement("input");
      hiddenInput.type = "file";
      hiddenInput.id = "df_hiddenFileInput";
      hiddenInput.style.display = "none";
      document.body.appendChild(hiddenInput);
    }

    // If types audio / image have been selected, add 'accept' attribute and set to the correct value
    // If no type has been provided, remove this attribute, as it may have been set previously
    if (type === "audio" || type === "sound") {
      document
        .querySelector("#df_hiddenFileInput")
        .setAttribute("accept", "audio/*");
    } else if (type === "image") {
      document
        .querySelector("#df_hiddenFileInput")
        .setAttribute("accept", "image/*");
    } else {
      document.querySelector("#df_hiddenFileInput").removeAttribute("accept");
    }

    // Activate the file input.
    document.querySelector("#df_hiddenFileInput").click();

    try {
      let file = await df_waitForFileSelection();
      return file;
    } catch (err) {
      console.error(err);
    }

    function df_waitForFileSelection() {
      return new Promise((resolve, reject) => {
        const fileInput = document.querySelector("#df_hiddenFileInput");

        // Check if file input exists
        if (!fileInput) {
          reject(new Error("File input element not found"));
          return;
        }

        // Event listener for file selection
        fileInput.onchange = async function (event) {
          const files = event.target.files;

          if (files && files.length > 0) {
            const selectedFile = files[0];
            if (logging) {
              console.log("File selected:", selectedFile);
            }

            if (selectedFile.type.startsWith("image/")) {
              try {
                let image = await foundry.processImage(selectedFile, logging);
                resolve(image);
              } catch (error) {
                reject(new Error("Error during image processing"));
              }
            } else {
              resolve(selectedFile);
            }
          }
        };
      });
    }
  },
  processImage: async function (source, logging = true) {
    return new Promise((resolve, reject) => {
      // if the source is a File (Blob), use FileReader
      if (source instanceof File) {
        const reader = new FileReader();

        reader.onload = function (e) {
          const img = new Image();
          img.src = e.target.result;

          img.onload = async function () {
            let processedImage = await df_processImageLogic(img);
            resolve(processedImage);
          };

          img.onerror = function () {
            reject(new Error("Error loading image from file"));
          };
        };

        reader.onerror = function () {
          reject(new Error("Error reading the image file"));
        };

        // Start reading the file as a Data URL
        reader.readAsDataURL(source);
      }
      // if the source is a URL, directly process the image
      else if (typeof source === "string") {
        const img = new Image();
        img.crossOrigin = "Anonymous"; // Handle CORS if necessary
        img.src = source;

        img.onload = async function () {
          let processedImage = await df_processImageLogic(img);
          resolve(processedImage);
        };

        img.onerror = function () {
          reject(new Error("Error loading image from URL"));
        };
      } else {
        reject(new Error("Invalid image source"));
      }
    });

    function df_processImageLogic(img) {
      return new Promise((resolve) => {
        const canvas = document.createElement("canvas");
        const ctx = canvas.getContext("2d");

        // Reduce the image size
        const maxWidth = 800;
        const maxHeight = 800;

        let width = img.width;
        let height = img.height;

        // Maintain aspect ratio
        if (width > height) {
          if (width > maxWidth) {
            height *= maxWidth / width;
            width = maxWidth;
          }
        } else {
          if (height > maxHeight) {
            width *= maxHeight / height;
            height = maxHeight;
          }
        }

        canvas.width = width;
        canvas.height = height;

        ctx.drawImage(img, 0, 0, width, height); // Draw the image onto the canvas

        // Get the data URL
        const processedImage = canvas.toDataURL("image/jpeg", 0.5); // 0.5 reduces image quality to decrease the prompt length
        if (logging) {
          console.log("Image processed.");
        }
        resolve(processedImage);
      });
    }
  },
  normalizeImageInput: async function (source) {
    if (!source) return null;
    if (typeof HTMLCanvasElement !== "undefined" && source instanceof HTMLCanvasElement) {
      return new Promise((resolve) => {
        source.toBlob((blob) => resolve(blob), "image/png");
      });
    }
    if (typeof HTMLImageElement !== "undefined" && source instanceof HTMLImageElement) {
      const canvas = document.createElement("canvas");
      canvas.width = source.naturalWidth || source.width;
      canvas.height = source.naturalHeight || source.height;
      const ctx = canvas.getContext("2d");
      ctx.drawImage(source, 0, 0);
      return new Promise((resolve) => {
        canvas.toBlob((blob) => resolve(blob), "image/png");
      });
    }
    if (typeof Blob !== "undefined" && source instanceof Blob) {
      return source;
    }
    if (typeof source === "string") {
      if (source.startsWith("data:")) {
        const parts = source.split(",");
        const mimeMatch = parts[0].match(/:(.*?);/);
        const mime = (mimeMatch && mimeMatch[1]) ? mimeMatch[1] : "image/png";
        const bstr = atob(parts[1]);
        let n = bstr.length;
        const u8arr = new Uint8Array(n);
        while (n--) {
          u8arr[n] = bstr.charCodeAt(n);
        }
        return new Blob([u8arr], { type: mime });
      } else {
        try {
          const res = await fetch(source);
          return await res.blob();
        } catch (e) {
          console.warn("Could not fetch image URL as Blob, returning original string:", e);
          return source;
        }
      }
    }
    return source;
  }
};