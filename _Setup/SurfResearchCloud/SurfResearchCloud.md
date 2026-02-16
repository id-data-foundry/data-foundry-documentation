---
layout: default
title: Surf Research Cloud
nav_order: 5
has_children: true
has_toc: true
---

# SRC-DataFoundry
If you dont want to host the infrastructure of Data Foundry yourself, there always is the option to host your Data Foundry instance on the SurfResearchCloud. Specifically for this use-case we made a SurfResearchCloud module to make this super easy. All you have to do is apply for a computing grant, and set up a small 1 cpu 4gb/ram instance. Below we have a guide to get started.

## Getting started


### Requires:

- 1 CPU - 8Gb workspace
- 5Gb (or more) volume for data storage, Attached to workspace

### Guide:
#### 1. Apply for a small fund
https://researchcloud.surf.nl/

#### 2. Create Storage
in the quick actions section on the surf research cloud dashboard you can find a button to create new storage:
![Create Storage Button]({% link _Setup/SurfResearchCloud/assets/CreateStorage.png%})

There you can pick how much storage you desire (5gb is already plenty for most simple distributions)
![Select Storge Volume]({% link _Setup/SurfResearchCloud/assets/SelectStorage.png%})

Afterwards you have to name your storage volume. It is important that you need to call this volume `datafoundry`. Afterwards you can normally submit.

![Configure Storage Volume]({% link _Setup/SurfResearchCloud/assets/NameStorage.png%})

#### 3. Reserve IP Address

To reserve a new IP, Open the IP menu on the dashboard.
![IP Menu]({% link _Setup/SurfResearchCloud/assets/IPMenu.png%})

In the IP menu you can then press the plus button to reserve a new ip address:
![Reserve IP Window]({% link _Setup/SurfResearchCloud/assets/ReserveIP.png%})

After filling in the details like name and description (can be anything you want) you can submit and you will now have reserved an IP.
![Submit IP]({% link _Setup/SurfResearchCloud/assets/Submit.png%})

#### 4. Create Workspace
Now we can create a workspace to host Data Foundry, to do so first click the open workspace button.
![Create Workspace]({% link _Setup/SurfResearchCloud/assets/CreateWorkspaceSurf.png%})

This will lead us to the workspace creation form, here you have to search for Data Foundry Production and then click choose. ![Choose Image]({% link _Setup/SurfResearchCloud/assets/ChooseImage.png%})


After having selected the Data Foundry Image, assign your recently created storage and ip address to the workspace. ![Setup Storage]({% link _Setup/SurfResearchCloud/assets/SetupResources.png%})

Then we have to setup the Data Foundry settings. First select an expiration date, this is when the machine will automatically shut off, then create an unique workspace and hostname. Optionally it would be handy if you add a description and fill in an an admin email.
![Setup settings]({% link _Setup/SurfResearchCloud/assets/SetupInstance1.png%})

then its important to fill in the cookie domain, this should consist of the hostname you assign to your instance, your surf organisation name, and end with `.src.surf-hosted.nl`. the second domain should be the same as the first domain, but should start with https://. At last you need to create a registration key, this key allows new users to register an account on Data Foundry using `https://<yourdomain>/users/register`! 
![Setup settings]({% link _Setup/SurfResearchCloud/assets/SetupInstance2.png%})

After having set up these settings you can submit all details. This wil set-up your newly created surf instance and after 10-15 minutes you should see datafoundry appear at the configured domain.

