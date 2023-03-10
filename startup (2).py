# -*- coding: utf-8 -*-
"""startup.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sigU052bniV_7qSvqEf3HzKoJ3I2H1IB

# **startup's successrate comparison**

> jan 27, 2023

1. ***import the packages***
"""

import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import datetime as dt

"""2. ***upload the file***"""

startup_df = pd.read_csv("/content/big_startup_secsees_dataset.csv")
startup_df.head(5)

"""3. ***understand the data***"""

startup_df.shape

startup_df.info()

startup_df.isna().sum()

startup_df["category_list"].value_counts()

"""4. ***data cleaning***

4.1 *drop null value with respect to column name*
"""

startup_df=startup_df.dropna(axis=0,subset=["category_list"])

startup_df.isna().sum()

startup_df=startup_df.dropna(axis=0,subset=["country_code"])

startup_df=startup_df.dropna(axis=0,subset=["region"])

startup_df.isna().sum()

"""**# we can do above data cleaning in single line but for understanding purpose i done step by step and show the cahnge**

5. ***filter only india's data***
"""

indian_startup = startup_df.query("country_code=='IND'")
indian_startup.head(5)

indian_startup.shape

"""6. ***graphical view of the above data***

6.1 *using pie graph viewing number startup operating, closed, acquired, ipo*
"""

fig=go.Figure(go.Pie(labels=indian_startup["status"],hole=0.5))
fig.update_layout(
    autosize=False,
    width=400,
    height=400,)
fig.update_traces(textposition="outside")
fig.show()

"""6.2 *using histogram graph viewing startup population with respect to region*

.

.

.
"""

fig=px.histogram(x=indian_startup["region"],color=indian_startup["status"])
fig.show()

indian_closed_startup = indian_startup.query("status=='closed'")
indian_closed_startup.head(5)

"""6.3 *Graphical view of category wise startup closed*"""

fig=go.Figure(go.Pie(labels=indian_closed_startup["category_list"],hole=0.5))

fig.update_traces(textposition="outside")
fig.show()

"""**# Software and Finance are the leading closed startup in india**

6.4 *Graphical view of category wise startup operating*
"""

indian_operating_startup = indian_startup.query("status=='operating'")
indian_operating_startup.head(5)

""".

**# Ecommerce and Software are the leading operating startup in india**
"""

fig=px.histogram(x=indian_operating_startup["category_list"],color=indian_operating_startup["region"])
fig.update_layout(
    autosize=False,
    width=1200,
    height=1200,)
fig.show()

avgFunding_Status=indian_startup
avgFunding_Status.head(5)

"""7.1 *Droping null value in "founded_at" & "first_funding_at" columns (why we not done this in 4.1 because for above few analysis we don't need to consider this columns but for below analysis we need this data so now we done this*"""

avgFunding_Status=avgFunding_Status.dropna(axis=0,subset=["founded_at","first_funding_at"],how="any")

avgFunding_Status.isna().sum()

"""7.2 *Data correction date is in wrong format*"""

avgFunding_Status['founded_at']= pd.to_datetime(avgFunding_Status['founded_at'], errors = 'coerce')

avgFunding_Status['founded_at']=pd.to_datetime(avgFunding_Status['founded_at'])

"""7.3 *Seperating year from date*"""

avgFunding_Status['founded_year']=avgFunding_Status['founded_at'].dt.year

avgFunding_Status['first_funding_at']= pd.to_datetime(avgFunding_Status['first_funding_at'], errors = 'coerce')

avgFunding_Status['first_funding_at']=pd.to_datetime(avgFunding_Status['first_funding_at'])

avgFunding_Status['first_funding_year']=avgFunding_Status['first_funding_at'].dt.year
avgFunding_Status.head(5)

avgFunding_Status["founded_year"].value_counts().head(5)

"""**# More startup founded at 2012**"""

avgFunding_Status["first_funding_year"].value_counts().head(5)

"""**# More funding happens at 2015**"""

average_waiting_period_for_first_funding_in_india=avgFunding_Status["first_funding_year"]-avgFunding_Status["founded_year"]

avgFunding_Status["waiting_period_for_funding"]=average_waiting_period_for_first_funding_in_india

avgFunding_Status.head(5)

"""7.4 *Finding waiting period*"""

average_waiting_period_for_first_funding_in_india.mean()

"""**# average waiting period to get first funding is "3.3 years" in india**

7.5 *Graphical view of waiting period with respect to category of startup, waiting years and region*

.
"""

fig=px.scatter(avgFunding_Status,x="category_list",y="waiting_period_for_funding",color="region",animation_frame="region",width=800, height=800)
fig.update_layout(
    autosize=False,
    width=1200,
    height=1200,)
fig['layout']['updatemenus'][0]['pad']=dict(r= 10, t= 600)
fig['layout']['sliders'][0]['pad']=dict(r= 10, t= 600,)
fig.show()

"""**INDUSTRIES GET THEIR FIRST FUND WITHIN 1 YR WITH RESPECT TO REGION**

***# MUMBAI- Credit card company, Ecommerce, Real Estate, Cleaning technology, Delivery company***

***# CHENNAI- Ecommerece, Saas, Digital marketing***

***# BANGALORE-  Saas, Credit card company, Ecommerce***
"""