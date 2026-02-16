---
layout: default
title: Notebooks
parent: Tools
nav_order: 3
has_children: true
---

# Starboard Notebooks

Starboard is an in-browser notebook environment (similar to Jupyter) that allows you to write Javascript and Python code to analyze your data directly within Data Foundry. To get started with starboard notebooks, you first need to add an existing dataset to your design project.

## Creating a Notebook

1.  Go to the data tools tab.
2.  In the data tools section open the **Notebook** tool.
3.  Here you'll have to click **add a new notebook** after which youll get a pop-up
4. In this popup youll have to **select a project and dataset combination** from the dropdown menu and insert a name for your new notebook.
5. After selecting a project and inserting a notebook name you can click on submit query which will create a new notebook for you.
6. To open your newly generated notebook you can you **select it from the list of notebooks** within the notebook tools section, *or* **open the file from the existing dataset** the notebook resides in. This will take you to starboard.

Alternatively you can follow this tutorial:
{% include df-link.html text="Take the tour" path="/tour/starboard-tour" %}

## Analyzing Data

In your notebook, you have direct access to your project's data without needing to download CSVs or manage API keys manually. You can acces the data through the access your datasets button. This will show all your projects and datasets and is able to generate code snippets to access this data by pressing the javascript or python button. These snippets are the same as the code below, but have important information like the `Data_Foundry_URL` and `Dataset_ID` already filled in!

## Importing data from DF

### JavaScript Example

```javascript
// The 'df' object is automatically available
var data
await fetch("/datasets/download/json/<Dataset_ID>")
	.then(response => response.json())
	.then(text => json = text)

// Use a library like Chart.js or Plotly
plot(data, { x: 'ts', y: 'value' });
```

### Python (Pyodide)

You can also run Python code directly in the browser:

```python
# import libraries (needed only once in the notebook)
import pandas as pd
import matplotlib.pyplot as plt
import pyodide

# download from this url
url = "http://DATAFOUNDRYBASEURL/datasets/download/<Dataset_ID>"

# download and parse CSV into Pandas DataFrame
df = pd.read_csv(pyodide.open_url(url))

# work with the DataFrame and print results
print(df.groupby('activity').max())

df.plot(x='ts', y='value')
plt.show()
```

This allows for powerful, reproducible data analysis and documentation that stays with your project.