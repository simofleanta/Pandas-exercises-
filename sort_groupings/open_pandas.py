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

"""Find the average mileage of each car"""
average_mileage_per_car=auto['average-mileage'].mean()
print(average_mileage_per_car) 
 
 
"""Find the average mileage of each making company"""
#grouping by a name or avereage

average_mileage_per_company=auto['company','average-mileage'].mean()
print(average_mileage_per_company)

"""Sort all cars by Price column """
#sorting asc or desc
carsauto=pd.read_csv('a_data.csv')
carsauto = carsauto.sort_values(by=['price', 'horsepower'], ascending=False)
carsauto.head(5)























