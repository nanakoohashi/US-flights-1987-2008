
# Flights - README

## Summary
This dataset reports flights in the United States, including carriers, arrival and departure delays, and reasons for delays, for 2008. This dataset was obtained from the **RITA** (Research and Technology Bureau of Transportation Statistics) found [here](https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp).

## Getting Started
### Dependencies
- Windows 10
- Python 3

### Libraries
- pandas
- numpy
- matplotlib
- seaborn
- calendar


## Steps
### 1. Assess the data
I started this project by importing essential packages and reading the **.csv** file. Then, using common data assessing code, I found that the data set is very large. I decided to use a sample of the full data set to save some time.
I decided that I wanted to focus on flight delays and cancellations.

### 2. Univariate Exploration
I began my univariate exploration by looking at how many domestic flights there were in the United States based on day of week, month, and day of year. Then, I looked at percentage of flight cancellations. Finally, I looked at duration of each type of delay.

### 3. Bivariate Exploration
I focused my bivariate exploration on the relationship between delays/cancellations and month/day of week.

### 4. Multivariate Exploration
I focused my multivariate exploration on the relationship between average lengths of each type of delay/type of cancellation and month/day of week.


## Main Findings
## Results
### Visualizations
I created dashboards using Tableau which can be seen by clicking on the links below:

### Univariate Exploration
#### Total Flights by Month
Most flights occur in the months of July and August. The months that had the least flights are in the months between September and December.

#### Total Flights by Day of Week
Most flights occur on Wednesdays. Saturdays have the least flights on average.

#### Percentage of Flights that are Cancelled
1.96% of all flights are cancelled. That is almost two flights per one hundred.

#### Causes of Flight Cancellations
The most common cause of flight cancellations is weather. There are 12 flights cancelled due to security.

#### Length of Carrier Delays
Carrier delays are most commonly 19-39 minutes long.

#### Length of Weather Delays
Weather delays are most commonly 11-24 minutes long.

#### Length of NAS Delays
NAS delays are most commonly 8-17 minutes long.

#### Length of Security Delays
Security delays are most commonly 1-6 minutes long.

#### Length of Late Aircraft Delays
Late aircraft delays are most commonly 25-56 minutes long

### Bivariate Exploration
#### Cancellation cf. Month
Flights are most commonly cancelled in February. Flights are least commonly cancelled in October.

#### Carrier Delay cf. Month
Flights experience carrier delays most commonly in August. Flights are least commonly delayed in November.

#### Weather Delay cf. Month
Flights experience weather delays most commonly in December. Flights are least commonly delayed in October.

#### NAS Delay cf. Month
Flights experience NAS delays most commonly in June. Flights are least commonly delayed in October.

#### Security Delay cf. Month
Flights experience security delays most commonly in March. Flights are least commonly delayed in November.

#### Late Aircraft Delay cf. Month
Flights experience late aircraft delays most commonly in December. Flights are least commonly delayed in September.

#### Cancellations cf. Day of Week
Flights are most commonly cancelled on Fridays. Flights are least commonly cancelled on Saturdays.

#### Carrier Delay cf. Day of Week
Flights experience carrier delays most commonly on Saturdays. Flights are least commonly delayed on Tuesdays.

#### Weather Delay cf. Day of Week
Flights experience weather delays most commonly on Sundays. Flights are least commonly delayed on Wednesdays.

#### NAS Delay cf. Day of Week
Flights experience NAS delays most commonly on Tuesdays. Flights are least commonly delayed on Saturdays.

#### Security Delay cf. Day of Week
Flights experience security delays most commonly on Saturdays. Flights are least commonly delayed on Tuesdays.

#### Late Aircraft Delay cf. Day of Week
Flights experience late aircraft delays most commonly on Sundays. Flights are least commonly delayed on Wednesdays.

### Multivariate Exploration
#### Types of Cancellations by Month
Carrier is the most common monthly cause for flight cancellations, followed by weather. Security cancellations are the least common cause for cancellations for all months.

#### Average Length of Delays by Month
Weather and late carrier delays have the longest average duration of delay of total monthly flights amd security has the shortest duration of delay of total monthly flights.

#### Percent of Flights Delayed by Type and Month
Results were similar to that of types of delays by month where weather and late carrier delays have the highest percentage of delays of total monthly flights amd security has the least percentage of delays of total monthly flights.

#### Types of Cancellations by Day of Week
Weather is the most common weekly cause for flight cancellations, followed by carrier. Security cancellations are the least common cause for cancellations for all days of the week.

#### Average Length of Delays by Day of Week
Weather and late carrier delays had the longest average delay length. Security delays had the shortest average delay length for all days of the week.

#### Percent of Flights Delayed by Type and Day of Week
Results were similar to that of types of delays by week where weather and late carrier delays have the highest percentage of delays of total weekly flights and security has the least percentage of delays of total weekly flights.
