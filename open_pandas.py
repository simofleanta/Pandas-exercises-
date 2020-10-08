""" From given data set print first and last five rows"""

import pandas as pd

auto=pd.read_csv('a_data.csv')
print(auto.head(10))
print(auto.tail(5))

"""Extract only Toyota using group"""
#open
auto=pd.read_csv('a_data.csv')
#groupby and then get group
auto=auto.groupby('company')
Toyotauto=auto.get_group('toyota')
print(Toyotauto)
print(Toyotauto.head(2))

"""Count total cars per company"""

count_per_company=auto['company'].value_counts()
print(count_per_company)
#may be perform charts on count per company or unit 

















