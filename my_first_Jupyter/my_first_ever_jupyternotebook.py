# -*- coding: utf-8 -*-
"""Orange with conclusions of CR1& CR2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WT3GAUHNO6KUQWPJgmonQDY0Ib6l__Nq
"""

f= open ('C:\\Users\\sf\\Desktop\\bi portfolio\\a3\\orangejson.json', 'r') #read the dcoument
s=f.read()

s

#load the json in json strings and transform it in dictionary or object, something that allows to access information
import json

orange=json.loads(s)

orange

#generating DataFrame in Pandas

from pandas import DataFrame

df=DataFrame(orange)

df.head(1)

"""change column names so that there'll be no parsing issues as the process goes along"""

df=DataFrame(orange)

df.columns

df.columns=['events', 'received', 'opened',
       'onboarded_opened', 'not_onboarded_opened',
       'not_onboarded_received', 'onboarded_received',
       'onboarded', 'not_onboarded', 'sr',
       'type', 'ci', 'group', 'total_users',
       'users_number', 'users_number_ne', 'onboarded_ne', 'nonboarded_ne',
       'openers', 'receivers', 'openers_onb', 'nopeners_onb',
       'summary_impact_dir', 'summary_impact_txt', 'links_ot',
       'last_step_name', 'snr', 'groups_inc', 'groups_neu', 'groups_not']

df.dropna() #generate DataFrame using new columns and using dropna function to remove NaN values

"""# Performing the calculations for the subset"""

#subsetting data in:
#A. received
#B. opened
#C. not_opened (calculated: received - opened)
#D. opened_onboarded
#E. not_opened_onboarded (calculated: onboarded - opened_onboarded)

#Rata de conversie pe opened: CR1 = D / B.
#Rata de conversie pe not opened:  CR2 = E / C.

"""Perorm calcs"""

from pandas import DataFrame

df.columns

#C. not_opened (calculated: received - opened)

not_opened=df.received-df.opened

not_opened.head(2)

df['not_opened']=df.received-df.opened

df.columns

#E. not_opened_onboarded (calculated: onboarded - opened_onboarded)

not_opened_onboarded=df.onboarded-df.onboarded_opened

not_opened_onboarded.head(2)

df['not_opened_onboarded']=df.onboarded-df.onboarded_opened

df.columns

#Rata de conversie pe opened: CR1 = D / B.

conversion_rate_opened=df.onboarded_opened/df.opened

conversion_rate_opened.head(2)

df['conversion_rate_opened']=df.onboarded_opened/df.opened

df.columns

#Rata de conversie pe not opened:  CR2 = E / C.

conversion_rate_not_opened=df.not_opened_onboarded/df.not_opened

conversion_rate_not_opened.head(3)

df['conversion_rate_not_opened']=df.not_opened_onboarded/df.not_opened

df.columns

"""# Subsetting """

from pandas import DataFrame

subset=df [['received','opened', 'not_opened','onboarded_opened','not_opened_onboarded','conversion_rate_opened','conversion_rate_not_opened']]

subset.dropna() #the dataset on which we can work now

"""# 95 confidence interval stats on CR2"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt 
# %matplotlib inline
from scipy.stats import norm
import numpy as np
import math

norm.ppf(0.975)## 95% #I'll work with this

norm.ppf(0.995)##99%

norm.ppf(0.95)##90

plt.hist(subset.conversion_rate_not_opened)

"""# Alpha level"""

n=len(subset)
con_coef=.95
#alpha level
alpha=1. - con_coef

alpha

"""# First find out mean and sigma """

mean=subset.conversion_rate_not_opened.mean()

mean

sigma=subset.conversion_rate_not_opened.std()

sigma

"""# Find z critical level"""

import scipy.stats as stats

z_critical=stats.norm.ppf(0.975)

z_critical

"""# Finding the intervals """

zinterval=stats.norm.interval(alpha=con_coef)

zinterval

"""# Finding the standard error to calculate boundries """

standard_error= sigma/math.sqrt(n)

standard_error

"""# calculate upper and lower limits"""

CI_lower=mean-z_critical*standard_error
CI_upper=mean+z_critical*standard_error

CI_lower, CI_upper

"""# Testing statistical relevance using CI for CR2"""

n_sample=95
subset_sample=subset.ix[np.random.choice(subset.index, n)]
subset_sample.head()

plt.hist(subset_sample.conversion_rate_not_opened)

mean_sample=subset_sample.conversion_rate_not_opened.mean()

mean_sample

sigma_sample=subset_sample.conversion_rate_not_opened.std()

sigma_sample

SE_sample=sigma_sample/math.sqrt(n_sample)

SE_sample

CI_lower_sample=mean_sample-z_critical*SE_sample
CI_upper_sample=mean_sample+z_critical*SE_sample

CI_lower_sample,CI_upper_sample

subset_sample.conversion_rate_not_opened.hist()

"""# Conclusion on CR2

With this sample size, on conversion_rate_not_opened we are 95% sure that the mean population is withon the range of low Confidence Interval to upper CI.

# Testing statistical relevance using CI for CR1
"""

plt.hist(subset_sample.conversion_rate_opened)

mean_sample1=subset_sample.conversion_rate_opened.mean()

mean_sample1

sigma_sample1=subset_sample.conversion_rate_opened.std()

sigma_sample1

SE_sample1=sigma_sample1/math.sqrt(n_sample)

SE_sample1

CI_lower_sample1=mean_sample1-z_critical*SE_sample1
CI_upper_sample1=mean_sample1+z_critical*SE_sample1

CI_lower_sample1,CI_upper_sample1

subset_sample.conversion_rate_opened.hist()

"""# Conclusion on CR1

With this sample size, on conversion_rate_opened we are not 95% sure that the mean population is withon the range of low Confidence Interval to upper CI.

# Conclusion

I was not able to perform Bayesian formula to calculate the conversion rates that cover 95% of the overall distribution however I used a different 95% CI that confirms Bayesian approach:
              Ex. quantile(post_rate. c(0.025,0.975)). 
              
My formula for confidence interval is:  mean-1.96*sigma/sqrt(n)mean + 1.96*sigma/sqrt(n).

My approach was to fin out all paramaters above using Python libraries scipy and other modules, norm, ppf-percentage point function etc. 
The 1.96 is the z_critical interval used to calculate CI 95% norm when you calculate 95% CI. There are also z_critical intervals for other intervals of 70, 90%; but I am using the 95%. 

After setting the parameters such as Alpha, sigma, CI lower and upper boundries, I will take the conversion_rate_not_opened sample and see if its distribution falls in between the CI 95% range.

# Finally

Given the calculation of both scenarios, CR1 and CR2, CR2 looks to be in the range intervals that is, it is 95% sure that the mean population is within the range of low Confidence Interval to upper CI. CR1 is not 95% sure that the mean population is within the range of low Confidence Interval to upper CI. This leads to the idea that scenario CR2 is better than CR1.
"""