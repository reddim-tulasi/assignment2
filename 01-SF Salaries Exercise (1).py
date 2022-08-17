#!/usr/bin/env python
# coding: utf-8

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[15]:


sal=pd.read_csv("Salaries.csv")


# ** Check the head of the DataFrame. **

# In[16]:


sal.head()


# ** Use the .info() method to find out how many entries there are.**

# In[17]:


sal.info()


# **What is the average BasePay ?**

# In[18]:


sal["BasePay"].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[19]:


sal["OvertimePay"].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[29]:


sal[sal.EmployeeName.isin(["JOSEPH DRISCOLL"])]["JobTitle"]


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[30]:


sal.loc[sal.EmployeeName=="JOSEPH DRISCOLL"]["TotalPayBenefits"]


# ** What is the name of highest paid person (including benefits)?**

# In[33]:


sal["TotalPay"].max()
sal.loc[sal.TotalPay==567595.43]


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[36]:


sal["TotalPay"].min()
sal.loc[sal.TotalPay==-618.13]


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[16]:


sal.groupby(["Year"])["BasePay"].mean()


# ** How many unique job titles are there? **

# In[70]:


n=len(pd.unique(sal["JobTitle"]))
n


# ** What are the top 5 most common jobs? **

# In[18]:


sal["JobTitle"].value_counts().head()


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[19]:


sum(sal[sal["Year"]==2013]["JobTitle"].value_counts()==1)


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[148]:


def chief(x):
    if "chief" in x.lower().split():
        return True
    else:
        return False
sum(sal["JobTitle"].apply(lambda x: chief(x)))


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[142]:


sal["title_len"]=sal["JobTitle"].apply(len)


# In[143]:


sal[["title_len","TotalPayBenefits"]].corr()

