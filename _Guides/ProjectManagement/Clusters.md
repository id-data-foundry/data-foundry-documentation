---
layout: default
title: Clusters
parent: Project Management
nav_order: 3
has_children: true
---

# Clusters in Data Foundry

Data Foundry allows to combine groups of participants, devices and wearables into clusters. This can be a cluster consisting of one participants and one wearable, or a cluster for an entire household with several devices and participants of a study.

Clusters combine different project resources (participants, devices, and wearables) and they can be named. Cluster help organize projects and filter collected data.

Creating, editing and deleting clusters is only possible for project owners and collaborators. We suggest setting up clusters together with the project resources to maintain a good overview and organization of the project.

Clusters can also be used to annotate groups of project resources over time (see below). We can also create clusters that are overlapping, that means, if we have a cluster for a family participating in your study, we can also add a cluster for each family member to be able to annotate them individually or to group family members with their wearable or personalized devices.

## How to add or edit clusters

Open the project landing page of your project and click on the button "manage resources". If you do not see this button then you are not project or collaborator of this project.

![manage resources]({% link _Guides/ProjectManagement/images/cluster-edit.png %})

On this page, you can see an overview of all clusters in this project, and you can click "add cluster" to add new clusters. For existing clusters, you can edit them to add or remove resources such as participants, devices and wearables.

Let's see how this works: click on "edit" inside the cluster card.

![edit participants]({% link _Guides/ProjectManagement/images/cluster-edit-participants.png %})

Here, we can look inside the cluster "FAMILY ONE". We see different datasets that we can download pre-filtered for this cluster. We also see a small chart that shows the data for this cluster segmented by dataset.

In the tabs under "cluster configuration" we can add or remove project resources. This is the place to configure a household cluster "FAMILY ONE", for instance, with two participants, each one wearable, and three devices.

![edit wearables]({% link _Guides/ProjectManagement/images/cluster-edit-wearables.png %})

## Filter data with clusters

If you have defined one or more clusters consisting of participants, wearables or devices, then you can use these clusters to filter collected data. This means you can focus on a cluster when downloading data (you don't need to filter on your own). If you have generated token download links for a dataset, you will find the links in the fourth tab on the cluster page.

![filter data]({% link _Guides/ProjectManagement/images/cluster-filter-data.png %})

## How to annotate a cluster

If we go back to the "manage resource" page of the project, we also add annotations to all clusters. Annotation are an easy way to add qualitative data from the researcher's perspective to the cluster.

If you are interested in qualitative data from the participant's perspective, check out the DIARY dataset, which allows entering similar textual data for participants.
