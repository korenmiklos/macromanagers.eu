---
title: eventbaseline
description: Correct Event Study After `xthdidregress`
date: 2024-01-23
language: stata
categories:
- stata
code: |-
    xthdidregress ra (y) (d), group(i)
    eventbaseline, pre(5) post(5) baseline(-1) graph
download_url: "https://github.com/codedthinking/eventbaseline"
tags:
- macromanagers
---
