---
layout: default
title: Connecting Max
parent: Clients
nav_order: 5
---

# Connecting Max

https://github.com/edenchiang/PlayWithDataFoundry/tree/master/examples/Save_from_MAX

## Description

This is an example for MAX users to save data to an IoT dataset of Data Foundry.

[What is Max?](https://cycling74.com/)

## Requirements

* Active project and dataset on Data Foundry:
  * IoT dataset - here I use an IoT dataset as an example, but this may also be able to be applied to some other datasets.
* You must have Max software installed


## Settings

### IoT dataset

Set up an IoT dataset to store the data into and also configure the HTTP POST option with a new token.

## How to send data from Max

1. Open your project, or start a new project, then search "maxurl" by the telescope on the nav bar on the right side of the window. Then, double click the first (usually) option -- **"maxurl -- Make HTTP requests"** under the Objects column. ![search maxurl]({% link _Guides/Clients/images/max/search-maxurl_w800_search-mark.png %})
2. The window of maxurl library will show up, then switch to the **"XMLHttpRequest"** tab. ![open XMLHttpRequest tab]({% link _Guides/Clients/images/max/maxurl-XMLHttpRequest_w800_tab-mark.png %})
3. The "headertest" function in the **"js_xhr_example.js"** is the target we are going to use. So, double click the **"js_xhr_example.js"** object in the chart, the content will be showed up in an editor. ![update code and trigger with button]({% link _Guides/Clients/images/max/maxurl-XMLHttpRequest_w800_button-script-mark.png %})
4. Find the "headertest" function and replace it with the following code, save it. Then, the data included in the code will be sent to Data Foundry as the **"headertest"** button is clicked.


```js
  function headertest()
  {
    // the data to send to Data Foundry
    var data = {
        "someint" : 23,
        "somefloat" : 3.045,
        "somestring" : "blah"
      }
    // Json object with data to send to Data Foundry
    var jsonBody = {
      activity: "ACTIVITY",
      source_id: "dc0046f6309644c56",
      data: JSON.stringify(data)
    }
    // make Json string object
    var dataToSend = JSON.stringify(jsonBody);

    // send request with XMLHttpRequest
    // update request content according to the target dataset in Data Foundry
    ajaxreq = new XMLHttpRequest();
    // set specific URL for sending
    ajaxreq.open("POST","https:/<YOUR-DF-INSTANCE>/datasets/ts/record/929/Q2R4eXlGVHgvdkExTFlYcUJrL01XeklLVEdIKy9BNlZxVTZTc2Z2dWFNTT0=");
    ajaxreq.setRequestHeader("Content-Type" , "application/json");
    ajaxreq.setRequestHeader("mode","cors");
    ajaxreq.setRequestHeader("cache","no-cache");
    ajaxreq.setRequestHeader("redirect","follow");
    ajaxreq.setRequestHeader("referrerPolicy","no-referrer");
    ajaxreq.onreadystatechange = readystatechange;
    // the Json data object has to be added to the last, otherwise it won't work properly
    ajaxreq.send(dataToSend);
  }
```

## Check data

1. The point in the chart on the IoT dataset page would show the summary of events according to the X-axis of the chart if the point is hovered by your mouse. ![event summary check on dataset page]({% link _Guides/Clients/images/max/quick_summary_on_chart_w800.png %})

2. Click "VIEW DATA" on the IoT dataset page, the data will be showed up in detail, and which will be updated by every refresh of the page. 
![button to view data]({% link _Guides/Clients/images/max/btn_view_data_w800.png %}) 
![data table]({% link _Guides/Clients/images/max/data_table_w800.png %})


## Troubleshooting

Q. How to open **"js_xhr_example.js"**? Or nothing happened after double clicking the **"js_xhr_example.js"** object?

A. Double click the **"js_xhr_example.js"** object on the diagram as the **lock** icon is activate, which means the diagram has to be locked. Then the editor window will popup on the screen.
![lock diagram and open script editor]({% link _Guides/Clients/images/max/maxurl-XMLHttpRequest_w800_script-lock-mark.png %})


## Source

All screenshots are sourced from Data Foundry and [Max](https://cycling74.com/products/max)
