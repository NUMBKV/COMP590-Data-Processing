# COMP590-Data-Processing
## 1. Confirmed Cases Data Processing
### 1.1 Project Introduction
This is a project that collects COVID-19 confirmed cases data from [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19) 
and process the data (originally cumulative) into the desired format (daily increment) 
that is need by the COMP590 frontend and backend team. This project contains the usage of 
[Google Colab](https://colab.research.google.com/), [Python3](https://www.python.org/) 
and [pandas library](https://pandas.pydata.org/).

### 1.2 Database
Our database provider is the [JHU CSSE COVID-19 Data](https://github.com/CSSEGISandData/COVID-19) 
and the main dataset we use for this project is the [CSSE COVID-19 Time series data](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv)
(time_series_covid19_confirmed_US.csv). This file is 11.7MB and contains cumulative confirmed 
cases data of all 3343 counties in all 58 states and territories of the United States. Specifically, 
the time range of this dataset is from 01/22/20 to current.

### 1.3 Detailed Workflow
To get started with our data processing, we firstly downloaded the dataset using pandas then directly 
converted the dataset into a pandas dataframe. Since that the original data is in cumulative form, and we 
desired the daily form, we subtracted one day's data with the day before it to get the daily increment. 
And we save that into [daily_cases/new_daily.csv](https://github.com/NUMBKV/COMP590-Data-Processing/blob/2f3621c39b0d5599fa7ba75eee4e8fb67c5e4a4d/daily_cases/new_daily_all.csv).

Then, based on our backend team's demands, we sum the counties' daily data by state to show every states' daily 
confirmed cases and save the aggregation result into [daily_cases/new_daily_states.csv](https://github.com/NUMBKV/COMP590-Data-Processing/blob/2f3621c39b0d5599fa7ba75eee4e8fb67c5e4a4d/daily_cases/new_daily_states.csv). 
Below is a plot of a sample visualization of this result.
![Samples visualization from new_daily_states.csv](daily_cases/state.jpeg)

Finally, to ease the backend load and accelerate our website's performance, we separate the counties' that belongs to the same state/territory and then 
aggregate them into a csv file called confirmed_cases_statename.csv. 
All these saved file are in [daily_cases/new_daily_states_county](https://github.com/NUMBKV/COMP590-Data-Processing/blob/2f3621c39b0d5599fa7ba75eee4e8fb67c5e4a4d/daily_cases/new_daily_states_county).

## 2. Vaccination Data Processing
## Our team members
___, ___, ___, Kaiwen Deng([kd45@rice.edu](mailto:kd45@rice.edu)), Jing Gao([jg107@rice.edu](mailto:jg107@rice.edu))
