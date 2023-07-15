#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install yfinance


# In[2]:


pip install statsmodels --upgrade


# In[38]:


from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
df = yf.download('AAPL')


# In[4]:


df = df['Adj Close']
df.head()


# In[5]:


df=df.fillna(method='ffill')


# In[6]:


from scipy import stats
z_scores = np.abs(stats.zscore(df))


# In[7]:


df.index = pd.date_range(start=df.index[0], periods=len(df), freq='D')


# In[8]:


from statsmodels.tsa.seasonal import seasonal_decompose, STL
import statsmodels as sm
df_decom = seasonal_decompose(df,model='additive')
plot = df_decom.plot()


# In[9]:


df_mul = seasonal_decompose(df,model='multiplicative')


# In[10]:


plot = df_mul.plot()


# In[11]:


plot = df.plot()
#Since magnitude of seasonal component is increasing , we should accept multiplicative model


# In[12]:


from statsmodels.tsa.filters.hp_filter import hpfilter
cycle, trend = hpfilter(df)


# In[13]:


fig, ax = plt.subplots(1,2, figsize=(16, 4))
cycle.plot(ax=ax[0], title='AAPL Cyclic Component')
trend.plot(ax=ax[1], title='AAPL Trend Component')


# # Test for Stationarity

# In[14]:


from statsmodels.tsa.stattools import adfuller, kpss
result_adf = adfuller(df)
print("ADF Statistic:", result_adf[0])
print("p-value:", result_adf[1])
print("Critical Values:")
for key, value in result_adf[4].items():
    print(f"{key}: {value}")

# Perform the Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test
result_kpss = kpss(df)
print("KPSS Statistic:", result_kpss[0])
print("p-value:", result_kpss[1])
print("Critical Values:")
for key, value in result_kpss[3].items():
    print(f"{key}: {value}")


# The p-values suggest that data is not stationary Now performing test on residual of data

# In[15]:


decomposition = seasonal_decompose(df, model='additive')

# Extract the residual component
residual = decomposition.resid
residual = residual.dropna()


# In[16]:


result_adf = adfuller(residual)
print("ADF Statistic:", result_adf[0])
print("p-value:", result_adf[1])
print("Critical Values:")
for key, value in result_adf[4].items():
    print(f"{key}: {value}")

# Perform the Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test
result_kpss = kpss(residual)
print("KPSS Statistic:", result_kpss[0])
print("p-value:", result_kpss[1])
print("Critical Values:")
for key, value in result_kpss[3].items():
    print(f"{key}: {value}")


# # Make the series stationary

# In[17]:


#sqrt method
df_sqrt = np.sqrt(df)
#differencing method
df_diff = df.diff().dropna()
resid_diff = residual.diff().dropna()
#double difference
df_dif2 = df.diff().diff().dropna()
resid_dif2 = residual.diff().diff().dropna()


# In[18]:


result_adf = adfuller(df_sqrt)
print("ADF Statistic:", result_adf[0])
print("p-value:", result_adf[1])
print("Critical Values:")
for key, value in result_adf[4].items():
    print(f"{key}: {value}")

# Perform the Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test
result_kpss = kpss(df_sqrt)
print("KPSS Statistic:", result_kpss[0])
print("p-value:", result_kpss[1])
print("Critical Values:")
for key, value in result_kpss[3].items():
    print(f"{key}: {value}")


# So upon taking sqrt, the series became stationary

# In[19]:


plot = df_sqrt.plot()


# # Test for Normality

# In[20]:


from scipy.stats import shapiro, kstest, normaltest
from statsmodels.stats.diagnostic import kstest_normal, normal_ad


# In[21]:


def is_normal(test, p_level=0.05):
    stat, pval = test
    return 'Normal' if pval > 0.05 else 'Not Normal'


# In[22]:


print(is_normal(shapiro(df)))
print(is_normal(shapiro(df_sqrt)))


# In[23]:


from statsmodels.graphics.gofplots import qqplot
qqplot(df, line='q')


# In[24]:


qqplot(df_sqrt,line='q')


# 
# Series can't be considered normal

# # Test for Homoscedasticity and Apply Box-Cox Transformation

# In[25]:


from statsmodels.stats.api import (het_breuschpagan, het_white)


# In[26]:


from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tools.tools import add_constant
model = AutoReg(df_sqrt.dropna(), lags=1, trend='n').fit()
resid = model.resid
def het_test(model, test=het_breuschpagan):
    lm, lm_pvalue, fvalue, f_pvalue = (
        het_breuschpagan(model.resid, 
                         add_constant(
                             model.fittedvalues)
                        ))
    
    return "Heteroskedastic" if f_pvalue < 0.05 else "Homoskedastic"
het_test(model, test=het_breuschpagan)


# In[27]:


from scipy.stats import boxcox


# In[28]:


xt, lmbda = boxcox(df)


# In[29]:


xts = pd.Series(xt, index=df.index)


# In[30]:


plot = xts.plot()


# In[31]:


model = AutoReg(xts.dropna(), lags=1, trend='n').fit()
het_test(model, test=het_breuschpagan)


# In[32]:


from statsmodels.stats.diagnostic import acorr_ljungbox


# In[34]:


# Plot ACF
import statsmodels.graphics.tsaplots as tsa
lags = 28
tsa.plot_acf(df_sqrt, lags=lags, alpha=0.05)
plt.xlabel("Lag")
plt.ylabel("Autocorrelation")
plt.title("Autocorrelation Function (ACF)")
plt.show()

# Plot PACF
tsa.plot_pacf(df_sqrt, lags=lags, alpha=0.05)
plt.xlabel("Lag")
plt.ylabel("Partial Autocorrelation")
plt.title("Partial Autocorrelation Function (PACF)")
plt.show()


# In[35]:


# Splitting data into training and testing sets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
train_data, test_data = train_test_split(df_sqrt, test_size=0.2, shuffle=False)


ar_model = AutoReg(df_sqrt.dropna(), lags=1, trend='n').fit()
# Making predictions on the testing set
predictions = ar_model.predict(start=len(train_data), end=len(train_data)+len(test_data)-1)
# Calculating evaluation metrics
mse = mean_squared_error(test_data, predictions)
mae = mean_absolute_error(test_data, predictions)

print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)

