---
title: "Journey to the Pythonic Peak 🗻"
marp: true
html: true
theme: gaia

---
<style>
p, pre {
    margin-top: 8px !important;
}
</style>
<style scoped>
h1 {
    font-size: 2.4rem;
}
h2 {
    font-size: 2rem;
}
</style>

<!-- _class: lead -->
## Pragmatic Python 2:
# Journey to the Pythonic Peak 🗻
_December 7, 2021_
Joe Riddle

---
<!-- _class: lead -->
# Hi, I'm Joe Riddle 👋

---

Next month's topic

## An _Anything but Mundane_ Intro to Machine Learning

Clayton Gravatt

---
# Previous recording available soon
https://spokanepython.com

[IntelliTect YouTube](https://www.youtube.com/channel/UCZSEfrUQnLLohBWDKRRSohw)

---
# Pragmatic
dealing with things sensibly and realistically in a way that is based on practical rather than theoretical considerations.

---
# Today's Format
- Talk / live code for ~60 minutes
- Pair programming for ~20 minutes
- Lightning presentations for ~15-20 minutes

---
# Outline
- Why Python
- Zen of Python
- Exception handling
- Decorators
- Generators
- Testing
- ...

---
# Live Coding Example
Craigslist CLI tool
- Search cars for sale
- Find lowest priced cars
- Save car images
- Search multiple Craigslist regions at once

---
# Why Python?

- ...
- ...

---
# Craigslist CLI
- Search cars for sale
- Find lowest priced cars
- Save car images
- Search multiple Craigslist regions at once

---
# Craigslist CLI
**Search cars for sale**

```bash
$ python -m app \
    "https://spokane.craigslist.org/d/cars-trucks-by-owner/search/cto?query=montero"
mitsubishi montero XlS 2002
Montero/Pajero SR Safari roof 1998
2002 Mitsubishi Montero Sport 2002
```

---
# Craigslist CLI
**Find lowest priced cars**

```bash
$ python -m app --lowest \
    "https://spokane.craigslist.org/d/cars-trucks-by-owner/search/cto?query=montero"
2002 Mitsubishi Montero Sport is the lowest priced vehicle at $650
```

---
# Craigslist CLI
**Save car images**
```bash
$ python -m app --images --output ./out \
    "https://spokane.craigslist.org/d/cars-trucks-by-owner/search/cto?query=montero"
$ ls ./out
mitsubishi-montero-XlS-2002.jpg
Montero-Pajero-SR-Safari-roof-1998.jpg
2002-Mitsubishi-Montero-Sport-2002.jpg
```

---
# Craigslist CLI
**Search multiple Craigslist regions at once**
```bash
$ python -m app --query "montero" --locations "spokane" "seattle"
```
```text
mitsubishi montero XlS 2002
Montero/Pajero SR Safari roof 1998
2002 Mitsubishi Montero Sport 2002
2 rare Mitsubishi Monteros Gen 1
2003 Mitsu Montero Sport XLS
2002 Mitsubishi Montero Sport Mechanics Special
...
```

---
# Craigslist CLI Ideas
- Filter posts from within the last week
- Scrape data from item details page
- Calculate average price for vehicle
- Create UI using `tkinter`
- Read and parse `robots.txt`
- ...

---
# Pair Programming
Find a fellow Pythonista and tackle an improvement for the next 20 minutes.
</br>
[https://code.visualstudio.com/learn/collaboration/live-share](https://code.visualstudio.com/learn/collaboration/live-share)

---
# Lightning Presentations
Showcase the improvement you and your buddy made!

---
<!-- _class: lead -->
Thank you for coming! Join us in January for 
# An _Anything but Mundane_
# Intro to Machine Learning!
