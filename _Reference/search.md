---
layout: default
title: Search reference
nav_order: 2
parent: Reference
has_children: false
has_toc: false
---

# How to search Data Foundry?

We are using the <a href="https://lucene.apache.org" target="_blank">Apache Lucene</a> search engine which allows for search queries that you probably also know from web search with Google, Bing, Baidu and Yandex. Let's go through a few possibilities:


## Search basics

Ok, so you can search for individual search terms, keywords. You can also use multiple together to extend the search results. Our search engine will find then projects that match any of the search terms, and ranks the ones with multiple hits higher. You can put entire phrases into quotes to ensure that search results contain the phrase, not just individual terms.

Sometimes, you would like to have more control over the matching. For instance, you want to find all projects that match both `"movement"` and `"health"`. Just add `AND` in-between the search terms to ensure that results match all terms. `AND`, `+` and also `NOT` and `-` are Boolean operators and they can be combined with search terms freely. With `+` the following search term must be included, with `NOT` and `-` the following search term must not appear in search results.

You can use parenthese to group search terms and Boolean operators: `("movement" AND "health") OR "movement behavior"`


## Searching in specific fields

You can search in specific fields of projects, such as the title, abstract, description, keyword, organization and remarks.

So, instead of searching in all fields with `"movement behavior"` you can search all project titles with `title:"movement behavior"`. Similar for all other fields. So, you can search for projects that have specific keywords with `keyword:automotive keyword:car`. You can even combine this field-specific search with Boolean expressions. For instance, search for project with a specific keyword that should not be present in the title of the project `keyword:diabetes NOT title: diabetes`. It's as easy as that.


## More information (fuzzy search, boosting, etc.)

You can find more information on the <a href="https://lucene.apache.org/core/2_9_4/queryparsersyntax.html" target="_blank">Lucene Query Parser page</a>.
