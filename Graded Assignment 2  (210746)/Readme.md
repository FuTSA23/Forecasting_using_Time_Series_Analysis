## FORECASTING USING TIME SERIES ANALYSIS 
* GRADED ASSIGNMENT 2 
* DEADLINE: 30th MAY 2023

DATASET FILES:  
Machine_temp_failure_missing.csv 
machine_temp_failure_original.csv

TASKS: 
* Read the machine_temp_failure_missing.csv dataset into a Pandas DataFrame, must use PathLib. Inspect the dataset, and look for missing values if there are any. Find statistics such as mean, max, min. Rename the value column to temperature. 
* Create a new feature delta_temperature which would be temp[i+1] - temp[i] where i is in range(Index). The feature represents the difference between consecutive temperature values. 
* Generate two separate plots for temperature and delta_temperature using both matplotlib and hvPlot.
* Generate a plot in which temperature values greater than 70.00 are marked as red, and those below 70.00 are marked as blue. 
* Write three functions read_datasets(), plot_dfs(), rmse_score() for these datasets (as discussed in 1_4 notebook).
* Perform univariate imputation on temperature and  using Pandas (mean, ffill, bfill) and Scikit-Learn (SimpleImputer), and interpolation. Compare the RMSE score for each imputation with machine_temp_failure_original.csv  and find the method with the least RMSE score.
* Now the dataset will have no missing values. Check the frequency of data and resample the dataset to an hourly frequency. 
* Draw box plot, boxen plot, lag plot and write your conclusions about outliers (in your own language). Define iqr_outliers() function for this data, and find the outliers. Compute z-score and plot z-score as discussed in the notebooks. 

INFO: 
- Make an .ipynb file which will then be used for submission. 
- All the functions have already been discussed in the notebooks shared with you, you may refer to them for each sub-task. 
