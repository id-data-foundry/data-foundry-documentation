---
layout: default
parent: Configuration
title: Fitbit Setup
nav_order: 3
---

# Setting up Fitbit support

To get started with fitbit functionalities, you first will need to request an API token. The following guide will help you through registering and collecting this token.

## Step 1. Navigate to the fitbit api website
[Take me to the Fitbit API website](https://dev.fitbit.com/apps/new){: .btn }

## Step 2. Create an account / Login
Now to log in to fitbit youll need a google account, as google has deprecated fitbit accounts. Hence using a google account is easiest.

## Step 3. Register a new application
To register a new app, make sure you're logged in and then press the register an app button at the top. This will take you to a form where you can request API access. Below lists a reference of what you need to fill in for all prompts

### Form:
This is a small reference for what to fill in for all of the prompts.

#### Application Website URL
`https://<your-instance>.com`

#### Organization Link
`Your Organization name`

#### Organization URL
`https://<your-organization>.nl`

#### Terms of Service URL
`https://<Terms-of-Service>`

#### Privacy Policy URL
`https://<your-organization-privacy-policy>`

#### Redirect URL

{: .warning }
>This one is the most important to get right

your instance url + /wearables/signup/fitbit

`https://<your-instance.com>/wearables/signup/fitbit`

#### OAuth 2.0 Application Type
`Personal`

#### Default Access Type
`Read-Only`

## Step 4. Copy and Insert api key