#!/usr/bin/env python
# coding: utf-8

# In[2]:


from datetime import datetime
from meteostat import Point, Daily

# Define Lübeck coordinates
luebeck = Point(53.8655, 10.6866)

# Define date range
start = datetime(1994, 1, 1)
end = datetime(2024, 12, 31)

# Get daily data
data = Daily(luebeck, start, end)
data = data.fetch()

# Keep only the 'prcp' (precipitation) column
precip = data[['prcp']]

# Print first few rows
print(precip.head())

# Save to CSV
precip.to_csv('luebeck_daily_precipitation_30yr.csv')


# In[3]:


import pandas as pd

# Load daily precipitation data (make sure date is parsed)
precip = pd.read_csv("luebeck_daily_precipitation_30yr.csv", index_col=0, parse_dates=True)

print(precip.head())


# In[4]:


import pandas as pd

# Load daily precipitation if not loaded yet
precip = pd.read_csv("luebeck_daily_precipitation_30yr.csv", index_col=0, parse_dates=True)

# Resample daily to monthly precipitation sums
monthly_precip = precip.resample('M').sum()

# Reset index so date becomes a column (named 'date' or 'time' as needed)
monthly_precip = monthly_precip.reset_index()

# Rename columns to expected names (check SPI function docs, but commonly:)
monthly_precip.columns = ['date', 'precipitation']

print(monthly_precip.head())


# In[7]:


from standard_precip.spi import SPI
from standard_precip.utils import plot_index

spi_calculator = SPI()

spi_1 = spi_calculator.calculate(
    monthly_precip,
    date_col='date',
    precip_cols=['precipitation'],  # <-- fixed here
    freq="M",
    scale=1,
    fit_type="lmom",
    dist_type="gam"
)

spi_3 = spi_calculator.calculate(
    monthly_precip,
    date_col='date',
    precip_cols=['precipitation'],  # <-- fixed here
    freq="M",
    scale=3,
    fit_type="lmom",
    dist_type="gam"
)


# In[9]:


import matplotlib.pyplot as plt


# In[13]:


# Make sure your 'date' column is datetime type
monthly_precip['date'] = pd.to_datetime(monthly_precip['date'])

# Initialize the SPI calculator
spi_calculator = SPI()

# Calculate the 3-month SPI
spi_3 = spi_calculator.calculate(
    monthly_precip,
    date_col='date',
    precip_cols=['precipitation'],  # Adjust if your column name is different
    freq='M',
    scale=3,
    fit_type='lmom',
    dist_type='gam'
)

# Plot the SPI index
plot_index(spi_3, 'date', 'precipitation_scale_3_calculated_index')
plt.title("3-Month Standardized Precipitation Index (SPI)")
plt.show()


monthly_precip['date'] = pd.to_datetime(monthly_precip['date'])
spi_calculator = SPI()
spi_6 = spi_calculator.calculate(
    monthly_precip,
    date_col='date',
    precip_cols=['precipitation'],  # Adjust if your column name is different
    freq='M',
    scale=6,
    fit_type='lmom',
    dist_type='gam'
)
plot_index(spi_6, 'date', 'precipitation_scale_6_calculated_index')
plt.title("6-Month Standardized Precipitation Index (SPI)")
plt.show()

monthly_precip['date'] = pd.to_datetime(monthly_precip['date'])
spi_calculator = SPI()
spi_12 = spi_calculator.calculate(
    monthly_precip,
    date_col='date',
    precip_cols=['precipitation'],  # Adjust if your column name is different
    freq='M',
    scale=12,
    fit_type='lmom',
    dist_type='gam'
)
plot_index(spi_12, 'date', 'precipitation_scale_12_calculated_index')
plt.title("12-Month Standardized Precipitation Index (SPI)")
plt.show()

monthly_precip['date'] = pd.to_datetime(monthly_precip['date'])
spi_calculator = SPI()
spi_24 = spi_calculator.calculate(
    monthly_precip,
    date_col='date',
    precip_cols=['precipitation'],  # Adjust if your column name is different
    freq='M',
    scale=24,
    fit_type='lmom',
    dist_type='gam'
)
plot_index(spi_24, 'date', 'precipitation_scale_24_calculated_index')
plt.title("24-Month Standardized Precipitation Index (SPI)")
plt.show()

monthly_precip['date'] = pd.to_datetime(monthly_precip['date'])
spi_calculator = SPI()
spi_36 = spi_calculator.calculate(
    monthly_precip,
    date_col='date',
    precip_cols=['precipitation'],  # Adjust if your column name is different
    freq='M',
    scale=36,
    fit_type='lmom',
    dist_type='gam'
)
plot_index(spi_36, 'date', 'precipitation_scale_36_calculated_index')
plt.title("36-Month Standardized Precipitation Index (SPI)")
plt.show

monthly_precip['date'] = pd.to_datetime(monthly_precip['date'])
spi_calculator = SPI()
spi_48 = spi_calculator.calculate(
    monthly_precip,
    date_col='date',
    precip_cols=['precipitation'],  # Adjust if your column name is different
    freq='M',
    scale=48,
    fit_type='lmom',
    dist_type='gam'
)
plot_index(spi_48, 'date', 'precipitation_scale_48_calculated_index')
plt.title("48-Month Standardized Precipitation Index (SPI)")
plt.show()


# In[ ]:




