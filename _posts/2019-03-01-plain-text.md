---
title: The Power of Plain Text
published: true
description: I believe portability and ease of exploration beats a tight schema-conforming database any time. 
tags:
- top
categories:
- data
author: koren
---

I sometimes get excited by binary file formats for storing data. A couple of years ago it was [HDF5](https://www.hdfgroup.org/solutions/hdf5/). Now [Apache Parquet](https://parquet.apache.org/) looks pretty promising. But most of my data work, especially if I share it with others, is stored in just simple, plain text.

> I believe portability and ease of exploration beats a tight schema-conforming database any time.

Be it CSV, JSON or YAML, I love it that I can just peek into the data real quick.

```bash
head -n100 data.csv
wc -l data.csv
```
are commands I use quite often. And nothing beats the human readability of a nice YAML document.

Sure, performance is sometimes an issue. If you are regularly reading and writing tens of millions of rows, you probably don’t want to use plain text. But in most of our use cases, a data product is read and written maybe a couple times a day by its developer and then shared with several users who read it once or twice. It is more important to facilitate sharing and discovery than to save some bytes. And you can always zip of gzip. (Never rar or 7z or the like. Do you really expect me to install an app just to read your data?)

![](https://thepracticaldev.s3.amazonaws.com/i/ni9gxpezx7dpno6wjfdx.jpeg)

Besides size (big) and speed (slow), there are three issues with CSV files:

1. No standard definition. Should all strings be encapsulated in quotes? What happens to quotes inside quotes? Never write your own csv parser. There will be [special cases](https://chriswarrick.com/blog/2017/04/07/csv-is-not-a-standard/) you didn’t think of. Use a standard library like [Python3 csv](https://docs.python.org/3/library/csv.html) or [pandas](https://pandas.pydata.org/).
2. Character encoding. As with all plain text files, you have to realize there is no such thing as plain text. Your file is just a sequence of bytes, and you have to tell your computer [what your bytes mean](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/). In our daily work, conversion to UTF-8 is the first order of business.
3. No schema. This is a big headache. Is this column a string? A date? I am constantly struggling with leading zeros and weird date formats. (But I would struggle with these in a proprietary data format, too. Date/time functions are impossible to remember in any programming language.) I have played around with schema validation in [Cerberus](http://docs.python-cerberus.org/en/stable/) and it looks cool, but we haven’t adopted anything formal yet.

So why am I a big fan of plain text data despite all these problems? I believe portability and ease of exploration beats a tight schema-conforming database any time. (Mind you, I am not working in a bank. Or health care.) See your data for what it is and play with it.