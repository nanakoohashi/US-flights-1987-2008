#!/usr/bin/env python
# coding: utf-8

# # Flights Data Exploration
# ## Preliminary Wrangling
# >This dataset reports flights in the United States, including carriers, arrival and departure delays, and reasons for delays, from 1987 to 2008.
# #### Variable descriptions

# | --- | **Name** | **Description** |
# | --- | --- | --- |
# | 1 | Year | 1987-2008 |
# | 2 | Month | 1-12 |
# | 3	| DayofMonth | 1-31 |
# | 4 | DayOfWeek	| 1 (Monday) - 7 (Sunday) |
# | 5	| DepTime | actual departure time (local, hhmm) |
# | 6	| CRSDepTime | scheduled departure time (local, hhmm) |
# | 7	| ArrTime | actual arrival time (local, hhmm) |
# | 8	| CRSArrTime | scheduled arrival time (local, hhmm) |
# | 9	| UniqueCarrier | unique carrier code |
# | 10 | FlightNum | flight number |
# | 11 | TailNum | plane tail number |
# | 12 | ActualElapsedTime | in minutes |
# | 13 | CRSElapsedTime | in minutes |
# | 14 | AirTime | in minutes |
# | 15 | ArrDelay | arrival delay, in minutes |
# | 16 | DepDelay | departure delay, in minutes |
# | 17 | Origin | origin IATA airport code |
# | 18 | Dest | destination IATA airport code |
# | 19 | Distance | in miles |
# | 20 | TaxiIn | taxi in time, in minutes |
# | 21 | TaxiOut | taxi out time in minutes |
# | 22 | Cancelled | was the flight cancelled? |
# | 23 | CancellationCode | reason for cancellation (A = carrier, B = weather, C = NAS, D = security) |
# | 24 | Diverted | 1 = yes, 0 = no |
# | 25 | CarrierDelay | in minutes |
# | 26 | WeatherDelay | in minutes |
# | 27 | NASDelay | in minutes |
# | 28 | SecurityDelay | in minutes |
# | 29 | LateAircraftDelay | in minutes |

# In[1]:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import calendar

%matplotlib inline

# In[2]:
df_2008 = pd.read_csv('2008.csv')

# In[3]:
print(df_2008.shape)
print(df_2008.dtypes)
print(df_2008.head(10))

# In[4]:
# Due to large file size, take a sample to more efficiently analyze trends in data
df_2008.sample(100000).to_csv('2008_sampled_100000.csv')

# In[5]:
df_2008s = pd.read_csv('2008_Sampled_100000.csv')

# In[6]
print(df_2008s.shape)
print(df_2008s.dtypes)
print(df_2008s.head(10))
print(df_2008s.describe())

# ### What is the structure of your dataset?
# >There are 7,009,728 flights in this dataset with 25 features (Year, Month, Day of Month, Day Of Week, Actual Departure Time, Scheduled Departure Time, Actual Arrival Time, Scheduled Arrival Time, Unique Carrier Code, Flight Number, Plane Tail Number, Actual Elapsed Time, Scheduled Elapsed Time, Air Time, Arrival Delay, Departure Delay, Origin, Destination, Distance, Taxi in time, Taxi Out Time, Cancelled, Reason For Cancellation (A = carrier, B = weather, C = NAS, D = security), Diverted, Carrier Delay, Weather Delay, NAS Delay, Security Delay, Late Aircraft Delay.

# ### What is/are the main feature(s) of interest in your dataset?
# >I am most interested in figuring out what features are best for predicting the likelihood a flight is delayed or cancelled. I am also interested in the proportion of delays and cancellations for day of week and month of year.

# ### What features in the dataset do you think will help support your investigation into your feature(s) of interest?
# I expect that weather delays and number of flights will have the strongest effect on delay or cancellation. This means that the **CancellationCode** column and each of the delay columns will be of interest. To calculate the number of flights, I plan to use the `.value_counts()` on the **Month** and **DayOfWeek** columns.

# ## Univariate Exploration
# In[7]:
# Making sure that we're converting numbers to days/months correctly
days = list(calendar.day_name)
days_abbr = list(calendar.day_abbr)
print(days, days_abbr)
month = list(calendar.month_name)
month_abbr = list(calendar.month_abbr)
print(month, month_abbr)
print(calendar.month_abbr[1])
exit()

# In[8]:
# Calculating how many flights there are per month.
df_2008s_month_value_counts = df_2008s.Month.value_counts().reset_index()
df_2008s_month_value_counts.columns = ["Month", "Total_Flights"]
df_2008s_month_value_counts = df_2008s_month_value_counts.sort_values(by=['Month'])
df_2008s_month_value_counts['Month'] = df_2008s_month_value_counts['Month'].apply(lambda x: calendar.month_abbr[x])
print(df_2008s_month_value_counts)
df_flights_by_month = df_2008s_month_value_counts.reset_index()
df_flights_by_month = df_flights_by_month.drop(columns=['index'])
df_flights_by_month


# In[9]:
# Plot month value counts as bar plot
df_2008s_month_value_counts.plot(kind='bar', x='Month', y='Total_Flights', color = 'teal', legend=False)
plt.title("Total Flights by Month")
plt.ylabel("Total Flights")
plt.xlabel("")
plt.show();


# In[10]:
######### Day of the Week
# Calculating how many flights there are per day of week.
df_2008s_day_value_counts = df_2008s.DayOfWeek.value_counts().reset_index()
df_2008s_day_value_counts.columns = ["DayOfWeek", "Total_Flights"]
df_2008s_day_value_counts = df_2008s_day_value_counts.sort_values(by=['DayOfWeek'])
df_2008s_day_value_counts['DayOfWeek'] = df_2008s_day_value_counts['DayOfWeek'].apply(lambda x: calendar.day_abbr[x-1])
print(df_2008s_day_value_counts)


# In[11]:
# Plot day value counts as bar plot
df_2008s_day_value_counts.plot(kind='bar', x='DayOfWeek', y='Total_Flights', color = 'teal', legend=False)
plt.title("Total Flights by Day of Week")
plt.ylabel("Total Flights")
plt.xlabel("")
plt.show();


# In[12]:
######### Day of the Year
# Calculating how many flights there are per day of year.
df_dvc2 = df_2008s
df_dvc2['Date']=df_dvc2['Year'].astype(str)+'/'+df_dvc2['Month'].astype(str)+'/'+df_dvc2['DayofMonth'].astype(str)
df_dvc2 = df_dvc2.Date.value_counts().reset_index()
df_dvc2.columns = ["Day", "Total_Flights"]
df_dvc2['Date'] = pd.to_datetime(df_dvc2['Day'], format='%Y/%m/%d')
df_dvc2 = df_dvc2.sort_values(by=['Day'])
print(df_dvc2)


# In[13]:
# Plot day value counts as bar plot
df_dvc2.plot(kind='line', x='Day', y='Total_Flights', color = 'teal', legend=False, figsize = (16,10))
plt.title("Total Flights by Day of Year")
plt.ylabel("Total Flights")
plt.xlabel("")
plt.show();


# In[14]:
# Total Cancellations
df_2008s.Cancelled.unique()


# In[15]:
df_cancelled = df_2008s['Cancelled'].value_counts()
df_cancelled = df_cancelled.reset_index()
df_cancelled


# In[16]:
cancelled_percent = df_cancelled.Cancelled[1] / (df_cancelled.Cancelled[0] + df_cancelled.Cancelled[1]) * 100
cancelled_percent = str(round(cancelled_percent, 2)) + "%"
cancelled_percent

# In[17]:
not_cancelled_percent = df_cancelled.Cancelled[0] / (df_cancelled.Cancelled[0] + df_cancelled.Cancelled[1]) * 100
not_cancelled_percent = str(round(not_cancelled_percent, 2)) + "%"
not_cancelled_percent

# In[18]:
df_cancelled.Cancelled.plot(kind= 'pie', labels = ['Not Cancelled (' + not_cancelled_percent + ')', 'Cancelled (' + cancelled_percent + ')'], figsize=(8,8))
plt.title("Percentage of Flights that are Cancelled")
plt.ylabel("");

# >1.96% of all flights are cancelled. That is almost two flights per one hundred.

# In[19]:
# Mean Cancellations
df_2008s.Cancelled.mean()


# In[20]:
# Cancellations by Cancellation Code
df_2008s['CancellationCode'].value_counts()


# In[21]:
df_2008s['CancellationCode'].replace({'A': 'carrier', 'B': 'weather', 'C': 'NAS', 'D': 'security'}, inplace = True)


# In[22]:
# A = carrier, B = weather, C = NAS, D = security
df_2008s['CancellationCode'].value_counts().plot(kind= 'bar', color = 'teal', figsize=(8,8))
plt.title("Causes of Flight Cancellations")
plt.ylabel("Count")
plt.xlabel("Type of Cancellation")
plt.show();


# In[23]:
# Carrier Delays
df_cd_1 = df_2008s.query('CarrierDelay != "NaN"')
df_cd_1 = df_cd_1.query('CarrierDelay != "0.0"')
df_cd_1


# In[24]:
df_cd_1.describe().CarrierDelay


# In[25]:
bin_edges = [1, 9, 19, 41, 2436]
bin_names = ['1-8', '9-18', '19-39', '40-1951']
df_cd_1['CDGroup'] = pd.cut(df_cd_1['CarrierDelay'], bin_edges, labels=bin_names)
df_cd_1


# In[26]:
df_cd_1['CDGroup'].value_counts()


# In[27]:
df_cd_1['CDGroup'].value_counts(sort = False).plot(kind= 'bar', color = 'teal', figsize=(8,8))
plt.title("Length of Carrier Delay")
plt.ylabel("Count")
plt.xlabel("Length of Delay (min)")
plt.show();


# In[28]:
# Weather Delays
df_wd_1 = df_2008s.query('WeatherDelay != "NaN"')
df_wd_1 = df_wd_1.query('WeatherDelay != "0.0"')
df_wd_1


# In[29]:
df_wd_1.describe().WeatherDelay


# In[30]:
bin_edges = [1, 11, 25, 57, 1352]
bin_names = ['1-10', '11-24', '25-56', '57-1352']
df_wd_1['WDGroup'] = pd.cut(df_wd_1['WeatherDelay'], bin_edges, labels=bin_names)
df_wd_1


# In[31]:
df_wd_1['WDGroup'].value_counts()


# In[32]:
df_wd_1['WDGroup'].value_counts(sort = False).plot(kind= 'bar', color = 'teal', figsize=(8,8))
plt.title("Length of Weather Delay")
plt.ylabel("Count")
plt.xlabel("Length of Delay (min)")
plt.show();


# In[33]:
# NAS Delays
df_nd_1 = df_2008s.query('NASDelay != "NaN"')
df_nd_1 = df_nd_1.query('NASDelay != "0.0"')
df_nd_1


# In[34]:
df_nd_1.describe().NASDelay


# In[35]:
bin_edges = [1, 8, 18, 31, 1357]
bin_names = ['1-7', '8-17', '18-30', '31-1357']
df_nd_1['NDGroup'] = pd.cut(df_nd_1['NASDelay'], bin_edges, labels=bin_names)
df_nd_1


# In[36]:
df_nd_1['NDGroup'].value_counts()


# In[37]:
df_nd_1['NDGroup'].value_counts(sort = False).plot(kind= 'bar', color = 'teal', figsize=(8,8))
plt.title("Length of NAS Delay")
plt.ylabel("Count")
plt.xlabel("Length of Delay (min)")
plt.show();


# In[38]:
# Security Delays
df_sd_1 = df_2008s.query('SecurityDelay != "NaN"')
df_sd_1 = df_sd_1.query('SecurityDelay != "0.0"')
df_sd_1


# In[39]:
df_sd_1.describe().SecurityDelay


# In[40]:
bin_edges = [1, 7, 13, 22, 392]
bin_names = ['1-6', '7-12', '13-21', '22-392']
df_sd_1['SDGroup'] = pd.cut(df_sd_1['SecurityDelay'], bin_edges, labels=bin_names)
df_sd_1


# In[41]:
df_sd_1['SDGroup'].value_counts()


# In[42]:
# Plot
df_sd_1['SDGroup'].value_counts(sort = False).plot(kind= 'bar', color = 'teal', figsize=(8,8))
plt.title("Length of Security Delay")
plt.ylabel("Count")
plt.xlabel("Length of Delay (min)")
plt.show();


# In[43]:
# >Security delays are most commonly 1-6 minutes long.


# #### Length of Late Aircraft Delays


# In[44]:
# Query 'LateAircraftDelay' to only select entries that are neither NaN or 0.
df_ld_1 = df_2008s.query('LateAircraftDelay != "NaN"')
df_ld_1 = df_ld_1.query('LateAircraftDelay != "0.0"')
df_ld_1


# In[45]:
df_ld_1.describe().LateAircraftDelay


# In[46]:
# Create bins of late aircraft delay lengths using information from the cell above.
bin_edges = [1, 11, 25, 57, 1352]
bin_names = ['1-10', '11-24', '25-56', '57-1352']
df_ld_1['LDGroup'] = pd.cut(df_ld_1['LateAircraftDelay'], bin_edges, labels=bin_names)
df_ld_1


# In[47]:
# value counts for each bin
df_ld_1['LDGroup'].value_counts()


# In[48]:
# Plot
df_ld_1['LDGroup'].value_counts(sort = False).plot(kind= 'bar', color = 'teal', figsize=(8,8))
plt.title("Length of Late Aircraft Delay")
plt.ylabel("Count")
plt.xlabel("Length of Delay (min)")
plt.show();

# >Late aircraft delays are most commonly 25-56 minutes long.
# #### Total Destinations
# In[49]:
# create value counts data set for 'Dest' column
df_dest = df_2008s['Dest'].value_counts()
df_dest = df_dest.reset_index()


# In[50]:
#df_dest.to_csv('dest.csv', index=False)


# In[51]:
get_ipython().run_cell_magic('HTML', '', "<div class='tableauPlaceholder' id='viz1555730357000' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;To&#47;TotalDomesticFlightsintheU_S_in2008&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='TotalDomesticFlightsintheU_S_in2008&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;To&#47;TotalDomesticFlightsintheU_S_in2008&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1555730357000');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.minWidth='420px';vizElement.style.maxWidth='1650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>")

# ### Of the features you investigated, were there any unusual distributions? Did you perform any operations on the data to tidy, adjust, or change the form of the data? If so, why did you do this?
# >#### Total Flights by Day of Year
# Due to working with such a large data set, I initially used a sample of the data set (10,000 entries) to visualize my data. Doing this, I was unable to see an obvious pattern in the visualization of total flights by day of year. However, when I used the full data set, I was able to group the data into four sections of the year where the number of flights were similar. Using the full data set paints a clearer picture as to how flights are distributed throughout the year.

# ## Bivariate Exploration
# #### Cancellation cf. Month


# In[52]:
# average cancellations
df_2008s.Cancelled.mean()


# In[53]:
# Convert to new data set
df_cancelled_month = df_cancelled_month.reset_index()


# In[54]:
# convert numbered months to letter months
df_cancelled_month['Month'] = df_cancelled_month['Month'].apply(lambda x: calendar.month_abbr[x])


# In[55]:
# plot
df_cancelled_month.plot(kind='bar', x='Month', y='Cancelled', color = 'teal', legend=False, figsize= (15,8))
plt.title("Average Flight Cancellations by Month")
plt.ylabel("Cancellations")
plt.xlabel("Month")
plt.show();

# >Flights are most commonly cancelled in February. Flights are least commonly cancelled in October.

# In[56]:
# sort values of monthly flight cancellations
df_cancelled_month.sort_values(['Cancelled'], ascending = False)


# #### Delay cf. Month
# In[57]:
# Average Carrier Delay in minutes
df_2008s.CarrierDelay.mean()


# In[58]:
# Average carrier delay by month in minutes
df_cd_month = df_2008s.groupby(['Month'])['CarrierDelay'].mean()


# In[59]:
# Convert to new data set
df_cd_month = df_cd_month.reset_index()


# In[60]:
# Convert numbered months to lettered months
df_cd_month['Month'] = df_cd_month['Month'].apply(lambda x: calendar.month_abbr[x])


# In[61]:
# Plot
df_cd_month.plot(kind='bar', x='Month', y='CarrierDelay', color = 'teal', legend=False, figsize= (15,8))
plt.title("Average Length of Carrier Delays by Month")
plt.ylabel("Carrier Delays (in minutes)")
plt.xlabel("Month")
plt.show();

# >Flights experience carrier delays most commonly in August. Flights are least commonly delayed by carrier in November.


# In[62]:
# sort average monthly carrier delays
df_cd_month.sort_values(['CarrierDelay'], ascending = False)


# In[63]:
# Average Weather Delay in minutes
df_2008s.WeatherDelay.mean()


# In[64]:
# average weather delay by month in minutes
df_wd_month = df_2008s.groupby(['Month'])['WeatherDelay'].mean()


# In[65]:
# convert to new data set
df_wd_month = df_wd_month.reset_index()


# In[66]:
# convert numbered months to lettered months
df_wd_month['Month'] = df_wd_month['Month'].apply(lambda x: calendar.month_abbr[x])


# In[67]:
# plot
df_wd_month.plot(kind='bar', x='Month', y='WeatherDelay', color = 'teal', legend=False, figsize = (15,8))
plt.title("Average Length of Weather Delays by Month")
plt.ylabel("Weather Delays (in minutes)")
plt.xlabel("Month")
plt.show();

# >Flights experience weather delays most commonly in December. Flights are least commonly delayed by weather in October.


# In[68]:
# sort monthly average weather delays
df_wd_month.sort_values(['WeatherDelay'], ascending = False)


# In[69]:
# Average NAS Delay in minutes
df_2008s.NASDelay.mean()


# In[70]:
# average monthly NAS delays in minutes
df_nd_month = df_2008s.groupby(['Month'])['NASDelay'].mean()


# In[71]:
# convert to new data set
df_nd_month = df_nd_month.reset_index()


# In[72]:
# convert numbered months to lettered months
df_nd_month['Month'] = df_nd_month['Month'].apply(lambda x: calendar.month_abbr[x])


# In[73]:
# plot
df_nd_month.plot(kind='bar', x='Month', y='NASDelay', color = 'teal', legend=False, figsize = (15,8))
plt.title("Average Length of NAS Delays by Month")
plt.ylabel("NAS Delays (in minutes)")
plt.xlabel("Month")
plt.show();

# >Flights experience NAS delays most commonly in June. Flights are least commonly delayed by the NAS in October.


# In[74]:
# sort average monthly NAS delays 
df_nd_month.sort_values(['NASDelay'], ascending = False)


# In[75]:
# Average Security Delay in minutes
df_2008s.SecurityDelay.mean()


# In[76]:
# average monthly security delay in minutes
df_sd_month = df_2008s.groupby(['Month'])['SecurityDelay'].mean()


# In[77]:
# convert to new data set. 
# convert numbered months to lettered months.
df_sd_month = df_sd_month.reset_index()
df_sd_month['Month'] = df_sd_month['Month'].apply(lambda x: calendar.month_abbr[x])


# In[78]:
# plot
df_sd_month.plot(kind='bar', x='Month', y='SecurityDelay', color = 'teal', legend=False, figsize = (15,8))
plt.title("Average Length of Security Delays by Month")
plt.ylabel("Security Delays (in minutes)")
plt.xlabel("Month")
plt.show();

# >Flights experience security delays most commonly in March. Flights are least commonly delayed by security in November.


# In[79]:
# sort average monthly security delays.
df_sd_month.sort_values(['SecurityDelay'], ascending = False)


# In[80]:
# Average Late Aircraft Delay in minutes
df_2008s.LateAircraftDelay.mean()


# In[81]:
# average monthly late aircraft delays in minutes
df_ad_month = df_2008s.groupby(['Month'])['LateAircraftDelay'].mean()


# In[82]:
# convert to new data set
# convert numbered months to lettered months
df_ad_month = df_ad_month.reset_index()
df_ad_month['Month'] = df_ad_month['Month'].apply(lambda x: calendar.month_abbr[x])


# In[83]:
# plot
df_ad_month.plot(kind='bar', x='Month', y='LateAircraftDelay', color = 'teal', legend=False, figsize = (15,8))
plt.title("Average Length of Late Aircraft Delays by Month")
plt.ylabel("Late Aircraft Delays (in minutes)")
plt.xlabel("Month")
plt.show();


# >Flights experience late aircraft delays most commonly in December. Flights are least commonly delayed by late aircrafts in September.


# In[84]:
# sort average monthly late aircraft delays.
df_ad_month.sort_values(['LateAircraftDelay'], ascending = False)


# #### Cancellations cf. Day of Week


# In[85]:
# average cancellations by day of week in minutes
df_cancelled_weekday = df_2008s.groupby(['DayOfWeek'])['Cancelled'].mean()


# In[86]:
# convert to data set.
# convert numbered days of week to lettered days of week
df_cancelled_weekday = df_cancelled_weekday.reset_index()
df_cancelled_weekday['DayOfWeek'] = df_cancelled_weekday['DayOfWeek'].apply(lambda x: calendar.day_abbr[x-1])


# In[87]:
# plot
df_cancelled_weekday.plot(kind='bar', x='DayOfWeek', y='Cancelled', color = 'teal', legend=False, figsize = (15,8))
plt.title("Average Flight Cancellations by Day of Week")
plt.ylabel("Cancellations")
plt.xlabel("Day Of Week")
plt.show();


# >Flights are most commonly cancelled on Fridays. Flights are least commonly cancelled on Saturdays.


# In[88]:
# sort average weekly cancellations
df_cancelled_weekday.sort_values(['Cancelled'], ascending = False)
