---
title: Semantic Versioning for Data Products
published: true
description: Semantic versioning lets you communicate your promises effectively within your data analysis team.
tags:
- top
categories:
- data
author: koren
---

In one of my research projects, I study how Hungarian firms managed by foreign CEOs perform relative to those managed by domestic CEOs. I need to merge data on firm performance to data on manager nationality. This latter data we have collected ourselves in our research lab, based on manager names.

I recently noticed a data fluke that made us classify some Hungarian names in the early 1990s as foreign. Once found, it was relatively easy to fix. Now I want to make sure that my team uses the newer, better data product for manager nationality as opposed to the old one.

Enter semantic versioning: I have to release and refer to `manager-db-1.0.1`.

## What is semantic versioning?
As you probably know from software development, Semantic Versioning is a set of rules on how to number your releases:

> Given a version number MAJOR.MINOR.PATCH, increment the:
> 1. MAJOR version when you make incompatible API changes,
> 2. MINOR version when you add functionality in a backwards-compatible manner, and
> 3. PATCH version when you make backwards-compatible bug fixes.

I think the exact same rules can be applied to data products. Fixing a bug in the data is a patch, hence I incremented the patch number. Adding a new column to a data table is added functionality, so you should increment the minor version. But when do you increment the major version? What is the API of a data product?

The work of my fellow analysts depends on my data product in two ways:

- Their code is dependent on the schema of my data files. If I delete or rename a column, or change its meaning, their code may stop running. Schema is like compile-time dependence for code.
- Their output is dependent on the content of my data files. If I add new rows, their statistical analysis may yield different numbers. Content is like runtime dependence for code.

Because of that, schema should be protected even more than content. Analysts are used to iterative work and changing outcomes. But they hate breaking code. So schema is the public contract I am offering with my data product, and I should increment the major version every time I change the schema in an incompatible way.

## How does this work in practice?

![Photo by Lars Blankers on Unsplash](https://thepracticaldev.s3.amazonaws.com/i/ni0175aisq0f3btkn0ro.jpg)

Take this simple csv table of foods, for example.

```
---food-1.0.0.csv
food,category,diet_quality_score
apple,fruit,2
tomato,vegetable,2
```
Before I release it as food-1.0.0.csv, I have to explicitly declare its schema, for example, in Cerberus:
```
{'food': {'type': 'string'}, 'category': {'type': 'string', 'allowed': ['fruit', 'vegetable']}, 'diet_quality_score': {'type': 'integer'}}
```
Then I realize that tomato is, scientifically speaking, a fruit, not a vegetable. This is patch, released as `food-1.0.1.csv`:

```
---food-1.0.1.csv
food,category,diet_quality_score
apple,fruit,2
tomato,fruit,2
```
Reading more about nutrition, I add carrot to my dataset. This is added functionality, so the new name is `food-1.1.0.csv`. Notice that the patch number was reset to zero.

All the downstream code is still compatible with this new dataset. My team will see the new versions and will expect runtime changes, but they can safely reuse their old code.

```
---food-1.1.1.csv
food,category,diet_quality_score
apple,fruit,2
tomato,fruit,2
carrot,vegetable,1
```
Time to break the API. I added deep fried Mars bar, which is neither a fruit nor a vegetable.

```
---food-2.0.0.csv
food,category,diet_quality_score
apple,fruit,2
tomato,fruit,2
carrot,vegetable,1
deep fried mars bar,fried stuff,-10
```
Is this really breaking the API? The dataset has the same columns and the meaning of each column is the same as before. But I promised to only have fruit or vegetable in column 2 and I broke that promise. If your code relies on that promise, it will break too. Hence I bumped the major version.

How much you promise and how hard you fight to keep that promise is a judgement call. But semantic versioning lets you communicate your promises effectively within your data analysis team.