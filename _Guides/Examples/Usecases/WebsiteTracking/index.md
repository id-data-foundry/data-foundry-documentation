---
layout: default
title: Website Tracking
parent: Usecases
nav_order: 6
---

# Use Case: Website Tracking

Sometimes you need to Log actions on a website to gain a clear understanding how your website or tool is being used. The example allows you to track and log scroll behavior, mouse movement, and browser characteristics to Data Foundry.

## Context

For digital design, there are numerous methods to conduct UX research on the interaction flow of a UI (e.g., website, app, or dashboard). One such method is customer journey logging. You can program your UI to track visitor actions (e.g., scroll behavior, mouse movement, browser characteristics) to identify optimal user flows and improve user satisfaction or marketing effectiveness.

Collecting this data is often just the first step. Using Data Foundry's tools, you can visualize data streams and apply sampling where needed. Furthermore, data mining and AI techniques can be applied for supervised and unsupervised learning to discover deeper correlations. The helps you gain a better understanding of your users through analytics.

## Example

Customer journey logging is frequently used to analyze the flow of users through e-commerce sites. By collecting data on which pages users visit and how long they stay, companies can build profiles to recommend products aligned with individual tastes.

## Requirements

A project created in Data Foundry and inside the project an new IoT dataset with openParticipation switched on (edit project, see bottom of form). The IoT dataset needs to be configured to get input data from an OOCSI stream (dataset page, see second configuration tab). The channel that you have configured in the OOCSI stream of the dataset, needs to be inserted also in the code below.

## Implementation Guide

### 1. Collect Web Page Visitor Data

Use the OOCSI network to send data items to your IoT dataset. This is available across many platforms. [You can find an overview of all OOCSI clients here](https://oocsi.net/about/oocsi-clients/)

### 2. Connect to the OOCSI API

Configure your channel name in the Data Foundry IoT dataset settings. Copy and paste the following code into the HTML of the pages you wish to track:

**Add to HTML header:**
```html
<script type="text/javascript" src="https://{{ site.external_base_urls.oocsi }}/assets/js/oocsi-web.min.js"></script>
```

**Add to HTML body:**
```javascript
<script type="text/javascript">
	// Connect to the OOCSI network
	OOCSI.connect("wss://{{ site.external_base_urls.oocsi }}/ws");

	// Store identifier of this browser
	var myname = '';
	if(navigator) {
		myname = navigator.appName + "_" + navigator.platform + '_' + navigator.language;
	}

	// Log click events
	document.addEventListener('click', function (event) {
		// send the X and Y values of the mouse point relative to page
		// TODO: change "CHANNEL NAME" to the channel you want to receive this data from
		OOCSI.send("CHANNEL NAME",
			{
				device_id: myname,
				x: event.pageX,
				y: event.pageY
			}
		);
	});
</script>
```

In the part that starts with `OOCSI.send("CHANNEL NAME",`, you first need to change the CHANNEL NAME to the one provided in the Data Foundry configuration of the IoT dataset. Then you can determine what type of web tracking data you want to log into the IoT dataset. Right now it only focuses on mouse position when the visitor clicks somewhere on the page. This can be further extended, for instance, with browser characteristics, time that a visitor spends on a single page, user interaction flow, etc. You can change these things in this line to make it send the right type of data to Data Foundry.

## Exporting Data

<!--todo: needs to be updated, we dont have a Data Tool}-->

There are two ways to export your data. If you want a simple export without any preprocessing, visualization or annotation, you can use the download button in the dataset screen. If you want a more advanced export, you can use the Data Tool to export your data.

[Open Data Tool]({% link _Guides/Tools/index.md %}){: .btn .btn-purple }

## Next Steps

A useful next step for this application is using data mining and machine learning techniques in order to make actual sense of the data. There are various tools and platforms for doing this, that can connect to Data Foundry to retrieve the data locally. One example is already given in the platform: if you go to a dataset page and open the CSV token link tab under configuration, you will find a code example in Python to download and visualise the dataset contents. You can use similar code to work with the dataset in Python for machine-learning purposes. This will only work if you generate a token link first.
