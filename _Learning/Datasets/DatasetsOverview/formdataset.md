---
layout: default
title: Form Dataset
parent: Datasets
has_children: true
has_toc: false
---

# Form Dataset

The Form Dataset is a versatile tool for creating and distributing web-based forms to collect data from a wide audience, particularly anonymous or external participants. This is the perfect tool for running public surveys, collecting feedback, or gathering any kind of information from people who are not registered participants in your project. Its ease of use and powerful features make it a staple for many research activities. You can have several different items in a form, from single and multi-select items to text inputs, continuous numerical sliders and grids. The creation of such forms is very straight-forward, just copy your prepared form items into the source box and add the items. There is a preview box next to it that shows how the form will render.

Creating a form is a remarkably simple and interactive process. You design the entire form using a straightforward Markdown-based syntax directly within the dataset's view page. As you type, a live preview is rendered on the same page, so you can see exactly what your form will look like. The editor supports a rich variety of input types, including single-choice questions (radio buttons), multiple-choice questions (check-boxes), numerical scales, single- and multi-line text inputs, and even complex grid questions.

Once your form is designed, Data Foundry generates a unique, shareable URL. Anyone with this link can access and submit the form, and each submission is securely stored as a single JSON object. To help you make sense of the incoming data, the dataset includes a built-in visualization tool that provides a quick overview and generates charts from the responses. For more detailed analysis, the data can be downloaded in two formats: as a raw log of JSON objects, or as a "projected" CSV file, where Data Foundry intelligently converts each form field into its own column, making it instantly ready for statistical software.

## Configuring a Form Dataset

For the Form Dataset, the primary "configuration" is the creative process of building your form. The dataset's main page is a powerful, interactive editor where you define the form's content and structure using a specialized Markdown syntax. A live preview is rendered as you type. Once you save your design, the system generates a unique, public URL for you to distribute.

Beyond the form editor, standard configuration tabs are available for managing the data you collect:

*   **CSV/JSON Download:** This tab allows you to generate a public URL (with an access token) to download your collected responses. Data can be exported as a raw JSON log or as a "projected" CSV file where each form field has its own column.
*   **Forward data to OOCSI:** This tab allows you to specify an OOCSI channel to forward all new form submissions to, enabling real-time integrations.
