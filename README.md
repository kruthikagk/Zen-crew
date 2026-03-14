# Zen-crew
This project analyzes Billboard chart datasets using Python and Pandas. The data is cleaned, standardized, and merged to create a unified dataset. Charts are generated to explore trends such as genre distribution, artist popularity, and country representation in the music charts.
# 🎵 Billboard Autopsy: 60 Years of Hits, One Dataset

This project explores more than six decades of Billboard Hot 100 chart data to understand what truly makes a hit song. The goal is to analyze historical chart patterns and provide insights that could help a record label make better decisions about which songs or artists are most likely to succeed.

## Data Preparation and Cleaning

Before performing analysis, the datasets were cleaned and prepared using Python and the Pandas library. The data contained inconsistencies such as extra spaces, mixed capitalization in artist names, and duplicate entries. These issues were corrected by trimming unnecessary spaces, standardizing text formats, and normalizing artist names and genres. Missing values and duplicate records were also checked to ensure the dataset was reliable for analysis. After cleaning, the datasets containing chart positions and artist information were merged to create a unified dataset for further exploration.

## Insights from the Objectives

**Objective 1 — The Legacy Question**
The analysis revealed that some artists dominate only for a short period while others remain relevant for many years. Sustained success often comes from artists who appear repeatedly on the chart across different years rather than those with a single massive hit.

**Objective 2 — The Stickiness Mystery**
Most songs remain on the chart for only a short period, while a small number stay for several weeks or months. Songs that remain longer often maintain consistent chart positions instead of rapidly dropping after their debut.

**Objective 3 — The Evolution of Taste**
Music trends clearly change across decades. Different genres and artists dominate different eras, reflecting shifts in listener preferences and the influence of cultural and technological changes in the music industry.

**Objective 4 — The Launch Paradox**
Songs that debut at very high positions sometimes fade quickly, while songs that gradually climb the chart tend to stay longer. This suggests that organic popularity growth can lead to longer chart life.

**Objective 5 — The Hit Machine**
A predictive model was built to estimate whether a song could reach the top tier of the chart. Factors such as previous artist success and chart trajectory played a role, but predicting hits remains challenging.

**Objective 6 — The Success Formula**
The analysis suggests that no single formula guarantees a hit. While data patterns provide strong signals, creativity, timing, and cultural influence still play a major role in determining chart success.

