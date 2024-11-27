---
title: Targets.jl
description: Computational pipeline management for Julia
date: 2024-08-15
language: julia
categories:
- julia
code: |-
    using Targets

    add(x, y) = x + y

    @target a = 1
    @target b = 2
    @target c = add(a, b)

    @get c
download_url: "https://github.com/codedthinking/Targets.jl"
docs: "https://github.com/codedthinking/Targets.jl"
tags:
- macromanagers
---

