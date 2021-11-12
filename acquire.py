#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import mason_functions as mf
import warnings
warnings.filterwarnings("ignore")


def get_db_url(db_name):
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


# ## Exercise I

# In[ ]:


def titanic_data():
    sql = '''
    SELECT * 
    FROM passengers
    '''
    url = get_db_url('titanic_db')
    df = pd.read_sql(sql, url)
    df.to_csv('titanic.csv')
    return df


# In[ ]:


titanic_data()


# In[ ]:


def get_titanic_data():
    file_name = 'titanic.csv'
    if os.path.isfile(file_name):
        df = pd.read_csv(file_name, index_col = 0)
    else:
        df = titanic_data()
        df.to_csv(file_name)
    return df


# In[ ]:


titanic_df = get_titanic_data()
titanic_df.head()


# ## Exercise II

# In[ ]:


def iris_data():
    sql = '''
    SELECT *
    FROM measurements
    JOIN species USING(species_id)
    '''
    url = get_db_url('iris_db')
    df = pd.read_sql(sql, url)
    df.to_csv('iris.csv')
    return df


# In[ ]:


iris_data()


# In[ ]:


def get_iris_data():
    if os.path.isfile('iris.csv'):
        df = pd.read_csv('iris.csv', index_col = 0)
    else:
        df = iris_data()
        df.to_csv('iris.csv')
    return df


# In[ ]:


iris_df = get_iris_data()
iris_df.head(), iris_df.shape


# ## Exercise III

# In[ ]:


def telco_data():
    sql = '''
    SELECT *
    FROM customers
    JOIN contract_types USING(contract_type_id)
    JOIN internet_service_types USING(internet_service_type_id)
    JOIN payment_types USING(payment_type_id)
    '''
    url = get_db_url('telco_churn')
    df = pd.read_sql(sql, url)
    df.to_csv('telco.csv')
    return df


# In[ ]:


telco_data()


# In[ ]:


def get_telco_data():
    if os.path.isfile('telco.csv'):
        df = pd.read_csv('telco.csv', index_col = 0)
    else:
        df = telco_data()
        df.to_csv('telco.csv')
    return df


# In[ ]:


telco_df = get_telco_data()
telco_df.head()


# ## Exercise IV

# In[ ]:


#Complete

