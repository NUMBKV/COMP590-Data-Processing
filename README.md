# COMP590-Data-Processing
## 1. Data Source
Our daily confirmed cases database provider: [COVID-19 Data Repository at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)  

Our vaccination database provider: [COVID-19 Vaccinations in the United States,County](https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh)
## 2. Data Processing
### 2.1 Daily Confirmed Cases Raw
All processed data and python notebook located at /daily_cases, raw data from JHU Database.

/daily_cases/new_daily_all.csv: All the counties' daily cases.

/daily_cases/new_daily_states.csv: All the counties' daily cases aggregate and sum by states.

/daily_cases/new_daily_states_county: All the counties' daily cases aggregate by states and split into different files.
### 2.2 Vaccination Report
TBD, empty folder /vaccination

### 2.3 Remove outlier cases
3 different methods of detect outliers including median filtering, using the Classification and Regression Trees (CART) model, and the Facebook Prophet model. located at /remove_outlier_cases
All processed data done by Python located at /code, can be done by either ipynb or py  


### 2.4 Cumulative result from 2.3
Cumulative result where value equals to the cases until that day. located at /cumulative_remove_outlier_cases
