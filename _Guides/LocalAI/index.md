---
layout: default
title: Local AI
nav_order: 6
has_children: true
has_toc: true
---

# Local AI How-To Guides

This section contains task-oriented guides for working with the AI features of Data Foundry. These guides assume you have a basic understanding of the platform. For a more conceptual overview and details on available models, check out the [Local AI learning section]({% link _Learning/LocalAI/index.md %}).


{% if site.external_base_urls.datafoundry == null %}
{: .warning}
The Local AI functionality in the examples only works *live* with a Data Foundry instance that is configured with API keys and a gateway to a local AI runtime server. Otherwise, you can still browse the example and check their source code, but the AI requests will not work.
{% endif %}


## Getting Started with Local AI

The Local AI functionality on the Data Foundry platform is based on large language models (LLM) that commonly are text-to-text. However, there are also other modalities available; examples show you can work with images and speech. 

You can find an overview of all the examples [here]({% link _Guides/LocalAI/examples/index.md %}){:.btn}.


several examples for you to explore and play with! You can try them out directly to see what the different AI features can do. We encourage you to experiment by typing in your own prompts and tweaking settings like "temperature" to see how the AI's personality and responses change. If you find something you like, you are more than welcome to copy the code and use it as a starting point for your own wonderful projects. If you would like to use the examples in your prototyping, make a copy and upload them to a new Data Foundry project (see [tutorial](https://miro.com/app/board/uXjVIajSnpo=/?share_link_id=802305677504)). Or take the AI tour to learn how to get started with the examples:
{% include df-link.html text="AI tour" path="/tour/ai-tour" %} 


## Working with Chatbots

Local AI often means using chatbots for interaction. In Data Foundry, we offer to paths to a chatbot, the first being high-level and mainly about prompting and steering a LLM with knowledge context, the second being more explicit in conversation design.

* **[Designing Custom Chatbots]({% link _Guides/LocalAI/Chatbots.md %})**: Learn how to create and configure your own LLM-based AI chatbot using system prompt and a custom knowledge base.
* **[Scripting Conversational Experiences]({% link _Guides/LocalAI/convoscript/index.md %})**: Work with the ConvoScript tools integrated in Data Foundry to create scripted chatbots. You start with a clear conversational design, then extend it with dynamic features, LLMs and context.

