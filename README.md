# Time Series Analysis 

## Project Overview

This project aims to analyze the levels of air pollutants before and after a specific intervention period. The dataset contains various air quality metrics recorded at regular intervals.

## Problem Statement

The detailed problem statement for this project can be found in the following Google Document:
[Problem Statement](https://docs.google.com/document/d/1AZUVKoSruMhK3jN-uLD4ZJ-eHcOSqr9W0FWvytr3bfA/edit)

## Dataset

The dataset used for this analysis can be accessed from the following link:
[Complete Blasting Info Dataset](https://github.com/FuTSA23/time-series-analysis-datasets/raw/main/Complete_Blasting_info%20(1).csv)

### Dataset Description

The dataset includes the following columns:
- `DateTime`: The timestamp of the recorded data.
- `PM10 (µg/m3)`: Concentration of particulate matter 10 micrometers or less in diameter.
- `NO (µg/m3)`: Concentration of Nitric Oxide.
- `PM2.5 (µg/m3)`: Concentration of particulate matter 2.5 micrometers or less in diameter.
- `NO2 (µg/m3)`: Concentration of Nitrogen Dioxide.
- `NOX (ppb)`: Concentration of Nitrogen Oxides.
- `CO (mg/m3)`: Concentration of Carbon Monoxide.
- `SO2 (µg/m3)`: Concentration of Sulfur Dioxide.
- `NH3 (µg/m3)`: Concentration of Ammonia.
- `Ozone (µg/m3)`: Concentration of Ozone.
- `Benzene (µg/m3)`: Concentration of Benzene.

## Analysis Steps

1. **Data Preprocessing**:
   - The dataset was read and parsed correctly with `DateTime` set as the index.
   - Handled any missing values to ensure accurate calculations.

2. **Defining the Intervention Period**:
   - The intervention period was specified as starting from '2023-02-01 13:45:00' to '2023-02-01 14:45:00'.

3. **Segmenting the Data**:
   - The data was divided into pre-intervention and post-intervention periods based on the defined time range.

4. **Calculating Mean Levels of Pollutants**:
   - The mean levels of `PM10` and `PM2.5` were calculated for both pre- and post-intervention periods.

## Results

The mean levels of pollutants before and after the intervention were calculated as follows:

- **Pre-Intervention Mean PM10**: `80.24` µg/m3
- **Post-Intervention Mean PM10**: `71.00` µg/m3
- **Pre-Intervention Mean PM2.5**: `35.65` µg/m3
- **Post-Intervention Mean PM2.5**: `17.20` µg/m3

## Interpretation of Results

The results indicate the mean concentration levels of `PM10` and `PM2.5` before and after the intervention period. A comparison of these mean values provides insights into the impact of the intervention on air quality.

- **Decreased Levels**: The mean levels of both `PM10` and `PM2.5` decreased post-intervention, suggesting that the intervention was effective in reducing air pollution. Specifically, the mean `PM10` level decreased from `80.24` µg/m3 to `71.00` µg/m3, and the mean `PM2.5` level decreased from `35.65` µg/m3 to `17.20` µg/m3.

## Model Application

### Models Used

1. **Intervention Analysis**
2. **ARIMA Model**

### Intervention Analysis

**Intervention Analysis** is a statistical technique used to determine the impact of an intervention on a time series dataset. It helps to identify whether the intervention has significantly changed the mean level of the series.

**Steps**:
1. Define the intervention time.
2. Segment the data into pre-intervention and post-intervention periods.
3. Calculate mean levels of the variables for both periods.
4. Perform statistical comparison (e.g., t-test) to determine if differences are statistically significant.

### ARIMA Model

**ARIMA (AutoRegressive Integrated Moving Average)** is a popular statistical model for time series forecasting that uses past values and past errors to predict future values.

**Steps**:
1. **Model Selection**: Identify the ARIMA model parameters (p, d, q).
2. **Fit the Model**: Fit the selected ARIMA model to the dataset.
3. **Forecasting**: Use the model to forecast future values and analyze model performance.

## Model Comparison

The intervention analysis provided a straightforward comparison of mean pollutant levels before and after the intervention, showing a clear decrease in pollution levels post-intervention. 

The ARIMA model, on the other hand, offered a more detailed statistical approach to forecasting and understanding time series behavior, with specific parameters indicating the nature of pollutant level changes over time.

Both methods are valuable, with the intervention analysis offering immediate insight into the impact of specific events, while the ARIMA model provides a robust framework for predicting future trends based on historical data.

## Conclusion

This analysis helps in understanding the impact of interventions on air quality by comparing the mean levels of key pollutants before and after the intervention. The observed decrease in mean pollutant levels indicates a positive effect of the intervention on air quality. The ARIMA model further provides a detailed forecast and understanding of the pollutant levels over time. Future work can include extending the analysis to additional pollutants and a longer timeframe to validate these findings.

