Yahoo ESG Scores for Python
=============================

This module retrieves esg scores and other sustainability information about a company from the yahoo finance website.

**Warning: The retrieved data might be outdated. Use at your own risk.**

Installation
------------

You can install the library by using:
``` {.sourceCode .bash}
pip install yesg
```

Import
------

``` {.sourceCode .python}
import yesg
```


Get ESG scores and sustainability data 
--------------------------------------
To download all available sustainability information for a company, simply use this:

``` {.sourceCode .python}
# All sustainability information about THE BOEING COMPANY
print(yesg.get_esg_full('BA').to_string())
```

```{r, engine='python', count_lines}
OUTPUT:
  Ticker Total-Score E-Score S-Score G-Score Last Rated ESG Performance           peer Group  Highest Controversy  peer Count  total Percentile environment Percentile social Percentile governance Percentile related Controversy  min peer ESG  avg peer ESG  max peer ESG  min peer Environment  avg peer Environment  max peer Environment  min peer Social  avg peer Social  max peer Social  min peer Governance  avg peer Governance  max peer Governance  min Highest Controversy  avg Highest Controversy  max Highest Controversy                   Controversial Business Areas
0     BA        36.6     8.1    19.7     8.8   May 2021        OUT_PERF  Aerospace & Defense                  4.0          24             78.79                   None              None                  None  Customer Incidents         24.07         32.06         39.54                  5.27              8.631667                 11.21             9.94          16.0825            20.83                 4.76             7.344583                10.08                      0.0                 2.416667                      4.0  Controversial Weapons, Military Contracting, 
```


Only get ESG scores 
--------------------------------------
To only download the quantitative ESG risk rating of a company, use can use this: 
``` {.sourceCode .python}
# ESG risk rating from THE BOEING COMPANY
print(yesg.get_esg_short('BA').to_string())
```

```{r, engine='python', count_lines}
OUTPUT:
  Ticker Total-Score E-Score S-Score G-Score Last Rated
0     BA        36.6     8.1    19.7     8.8   May 2021
```


Return description
-----------------

Yahoo gets it data from Sustainalytics. They describe their ratings as follows: \
*"The ESG Risk Ratings measure the degree to which a company’s economic value is at risk driven by ESG factors or, more technically speaking, the magnitude of a company’s unmanaged ESG risks. "*

&rarr; **The lower the rating, the more sustainable a company is**

The dataframe consists of:
- **Ticker** - Ticker symbol of the company
- **Total-Score** - Overall ESG risk rating
- **E-Score** - Environmental risk rating of a company
- **S-Score** - Social risk rating of a company
- **G-Score** - Governance risk rating of a company
- **Last Rated** - The month in which the rating was updated
  

- **ESG Performance** - Verbal description of the ESG performance. Translates to 'Negligible' (LAG_PERF), 'Low' (UND_PERF), 'Medium' (AVG_PERF), 'High' (OUT_PERF) and 'Severe' (LEAD_PERF)
- **peer Group** - Sector of the company
- **Highest Controversy** - The Highest controversy of the company, compared to the peer group
- **peer Count** - Size of the peer group
- **total Percentile** - Percentile of the overall ESG risk rating
- **environment Percentile** - Percentile of the environmental risk rating
- **social Percentile** - Percentile of the social risk rating
- **governance Percentile** - Percentile of the governance risk rating
- **related Controversy** - Controversies the company was involved in
- **peer ESG** - min/avg/max overall risk rating within the peer group
- **peer Environment** - min/avg/max environmental risk rating within the peer group
- **peer Social** - min/avg/max social risk rating within the peer group
- **peer Governance** - min/avg/max governance risk rating within the peer group
- **Highest Controversy** - min/avg/max of the highest controversy within the peer group
- **Controversial Business Areas** - Controversial business areas in which the company is involved

  