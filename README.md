# Red Bull x Claremont Colleges 
[![Build Status](https://github.com/maxplush/5c-redbull/actions/workflows/test-workflows.yml/badge.svg)](https://github.com/maxplush/5c-redbull/actions/workflows/test-workflows.yml)
### A Micro Shopper Insights Proof-of-Concept Across the 5C Campuses
![Survey Promo](images/redbull_banner.png)

## What's This?

This was a **scrappy, creative passion project** inspired by the Red Bull **Insights & Analytics Graduate Program**.

I ran a lightweight survey activation across the Claremont Colleges (Pomona, Pitzer, Scripps, CMC, Harvey Mudd), offering free Red Bull and collecting feedback on:

- When students drink energy drinks (study, party, workout, etc.)
- Where they go to buy them on campus
- What would make them choose Red Bull over competitors
- And if Red Bull were a person, what kind of vibe it would have 👀

Only **44 people responded**, so the insights aren't statistically strong—but this was more of a **proof of concept** to show how I think about segmentation, pricing, brand image, and on-premise execution.

---

## The Fun Stuff

To bring the project to life, I:
- Created a short, insight-driven [survey](https://docs.google.com/forms/d/e/1FAIpQLSfxxcizbHYAWEm_0Lt3ikPXFAVtqOTN9WGs7SRDaZHa89hzhA/viewform) focused on consumption habits, purchase paths, and brand perception 
- Built a **life-sized Red Bull can** to attract attention [Check it out!](images/redbull_craft.jpg)
- **Gave away free Red Bull** to incentivize survey signups
- Was planning a **DJ set activation** to drive more responses (ran out of time)

This project was a way to blend **creativity, hustle, and analytical thinking**—everything I’m excited to bring to the Red Bull team.

## What's in This Repo

Just a simple pipeline:

- `main.py`: reads the survey export CSV and loads it into a SQLite database
- `analyze.py`: runs preset SQL queries and light sentiment analysis, then generates a clean insights summary
- `red_bull_summary.txt`: auto-generated insights report with survey breakdowns, purchase patterns, and brand sentiment.

## Why It Matters

This project let me:
- Simulate small-scale **shopper & on-premise insights**
- Get creative with execution (events, giveaways, branding)
- Learn how Red Bull is perceived at the Claremont Colleges

<p align="center">
  <img src="images/redbull_craft.jpg" alt="Red Bull Can Craft" width="300">
</p>

<p align="center">
  <img src="images/max_tabeling.jpeg" alt="Survey Tableing" width="300">
</p>