# -*- coding: utf-8 -*-
"""Pr-Default-CC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1owXQIBbeetsNBk9uJxI2ioaIbprO0t5c

# **Project Name**    - **Credit Card Default Prediction**

**Project Type**    - Classification

**Contribution**    - Team

**Team Member 1**- Bharat Kumar Soni

**Team Member 2**- Abhilasha

# **Project Summary**

The objective of this project is to train various supervised learning algorithms to predict the client’s behavior in paying off the credit card balance. In classification problems, an imbalanced dataset is also crucial to enhance the performance of the model, so different resampling techniques were also used to balance the dataset. We first investigated the datasets by using exploratory data analysis techniques, including data normalization.

 We started with the logistic regression model, then compared the results with traditional machine learning-based models. Then K-means SMOTE resampling method on Taiwan client’s credit dataset.

In the end, the proposed method has also been deployed on the web to assist the different stakeholders. Therefore, when the financial institution considers issuing the client a credit card, the institution needs to check the payment history of that person because the decision on whether to pay on duly or owe the bill on a specific month usually relates to the previous payment history.

For instance, if a person owes numerous bills already, he or she is likely to delay the payment of the current month unless this person gets a windfall so that the total arrears can be paid off. Besides the payment history, it is also imperative to look at the applicants’ credit limit of their current credit cards. This is a result of a virtuous circle: people who pay on duly tend to have better credit scores, so the banks prefer to increase these people’s credit lines by taking less risk. As a result, if a potential client already has a credit card with a high credit limit line, this person is unlikely to fail to pay the full amount owed in the future.

Although the financial institution often collects clients’ personal information such as age, educational level, and marital status when people apply for credit cards, this information also affects the default behavior.

# **GitHub Link**

https://github.com/bharatsoni0047/Credit-Card-Default-Prediction

# **Problem Statement**

**This project is aimed at predicting the case of customers default payments in Taiwan.**

From the perspective of risk management, the result of predictive accuracy of the estimated probability of default will be more valuable than the binary result of classification - credible or not credible clients.

 We can use the K-S chart to evaluate which customers will default on their credit card payments

# **General Guidelines** : -

1.   Well-structured, formatted, and commented code is required.
2.   Exception Handling, Production Grade Code & Deployment Ready Code will be a plus. Those students will be awarded some additional credits.
     
     The additional credits will have advantages over other students during Star Student selection.
       
             [ Note: - Deployment Ready Code is defined as, the whole .ipynb notebook should be executable in one go
                       without a single error logged. ]

3.   Each and every logic should have proper comments.
4. You may add as many number of charts you want. Make Sure for each and every chart the following format should be answered.
        

```
# Chart visualization code
```
            

*   Why did you pick the specific chart?
*   What is/are the insight(s) found from the chart?
* Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

5. You have to create at least 15 logical & meaningful charts having important insights.


[ Hints : - Do the Vizualization in  a structured way while following "UBM" Rule.

U - Univariate Analysis,

B - Bivariate Analysis (Numerical - Categorical, Numerical - Numerical, Categorical - Categorical)

M - Multivariate Analysis
 ]





6. You may add more ml algorithms for model creation. Make sure for each and every algorithm, the following format should be answered.


*   Explain the ML Model used and it's performance using Evaluation metric Score Chart.


*   Cross- Validation & Hyperparameter Tuning

*   Have you seen any improvement? Note down the improvement with updates Evaluation metric Score Chart.

*   Explain each evaluation metric's indication towards business and the business impact pf the ML model used.
"""



"""# ***Let's Begin !***

## **Know Your Data-**

### Import Libraries
"""

# Commented out IPython magic to ensure Python compatibility.
# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

import os
import sys
import warnings
warnings.filterwarnings('ignore')

"""### Dataset Loading"""

from google.colab import drive
drive.mount('/content/drive')

# Load Dataset
df = pd.read_excel('/content/drive/MyDrive/Supervised/Classification/Default of credit card clients.xls', header=1)

"""### Dataset First View"""

# Dataset First Look
df.head()   #first 5 rows

df.tail()   #last 5 rows

"""### Dataset Rows & Columns count"""

# Dataset Rows & Columns count
df.shape

"""As we can see that we have around 30000 rows and 25 columns in our dataset."""

# since there are too many columns in the dataframe, we are not able to see all of them.
# we can remedy this using set_option function.
pd.set_option('display.max_columns', None)
df.head()

"""### Dataset Information"""

# Dataset Info
df.info()

# getting descriptive statistics of the data.
df.describe(include='all')

"""#### Duplicate Values"""

# Dataset Duplicate Value Countd
duplicates = df.duplicated()

# Count the number of duplicates
duplicate_count = duplicates.sum()
# Print the number of duplicates
print(f"Number of duplicates: {duplicate_count}")

"""There is no duplicate values in our dataset

#### Missing Values/Null Values
"""

# Missing Values/Null Values Count
df.isna().sum()

"""we dont have any null values in our dataset

### What did you know about your dataset?

This research employed a binary variable, default payment (Yes = 1, No = 0), as the response variable. This study reviewed the literature and used the following 23 variables as explanatory variables and predict the case of customers default payments in Taiwan.

## **Data Preprocessing-**

### Variables Description

1. ID: ID of each client (unique identifier)
2. LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit)
3. SEX: Gender (1=male, 2=female)
4. EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown)
5. MARRIAGE: Marital status (1=married, 2=single, 3=others)
6. AGE: Age in years
7. PAY_0: Repayment status in September, 2005 (-2 = Unused,-1=pay duly,0=Revolving Credit, 1=payment delay for one month, 2=payment delay for two months,8=payment delay for eight months, 9=payment delay for nine months and above)
8. PAY_2: Repayment status in August, 2005 (scale same as above)
9.PAY_3: Repayment status in July, 2005 (scale same as above)
10.PAY_4: Repayment status in June, 2005 (scale same as above)
11.PAY_5: Repayment status in May, 2005 (scale same as above)
12.PAY_6: Repayment status in April, 2005 (scale same as above)
13.BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)
14.BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
15.BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
16.BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
17.BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
18.BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
19.PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)
20.PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
21.PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
22.PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
23.PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
24.PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)
25.default.payment.next.month: Default payment (1=yes, 0=no)
"""

# Dataset Columns
df.columns

# Let's rename the columns for better understanding.
df.rename(columns={'PAY_0':'REPAY_STATUS_SEPT','PAY_2':'REPAY_STATUS_AUG','PAY_3':
                   'REPAY_STATUS_JUL','PAY_4':'REPAY_STATUS_JUN','PAY_5':'REPAY_STATUS_MAY','PAY_6':'REPAY_STATUS_APR'},inplace=True)

df.rename(columns={'BILL_AMT1':'BILL_AMT_SEPT','BILL_AMT2':'BILL_AMT_AUG',
                   'BILL_AMT3':'BILL_AMT_JUL','BILL_AMT4':'BILL_AMT_JUN','BILL_AMT5':'BILL_AMT_MAY','BILL_AMT6':'BILL_AMT_APR'}, inplace = True)

df.rename(columns={'PAY_AMT1':'PRE_PAY_AMT_SEPT','PAY_AMT2':'PRE_PAY_AMT_AUG','PAY_AMT3':'PRE_PAY_AMT_JUL',
                   'PAY_AMT4':'PRE_PAY_AMT_JUN','PAY_AMT5':'PRE_PAY_AMT_MAY','PAY_AMT6':'PRE_PAY_AMT_APR'},inplace=True)

df.head()

"""### Check Unique Values for each variable."""

# Check Unique Values for each variable.
df.nunique()

# now let's save this data before operating on it.
credit_card_df = df.copy()

"""## **EDA-**

---


"""

# Although the data in our df in all numerical, there are some categorical variables present in our dataset in encoded form.
# Exploring our dependent variable.
# first lets rename our dependent variable.
df.rename(columns={'default payment next month' : 'is_defaulter'}, inplace=True)

# plotting the value counts of our DV
plt.figure(figsize=(12,7))
sns.countplot(data=df, x='is_defaulter', hue='is_defaulter', palette=['dodgerblue', 'salmon'])
plt.xlabel('Defaulter status', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks([0, 1], ['Non-defaulters', 'Defaulters'], fontsize=12)
plt.legend

"""**We can see from the above graph and value counts, that we have a unbalanced dataset. The no. of instances for class 0 is significantly higher than class 1**"""

df.columns

# Now, we have several other categorical columns like marriage, education, sex.
# Let's check them and see the relationship with our dependent variable.
df['MARRIAGE'].value_counts()

df['SEX'].value_counts()

df['EDUCATION'].value_counts()

"""**In the education variable, as per our data description, 1 refers to graduate school, 2 refers to university etc.  however we have no understanding of some numbers present. so we will replace these will others**.

**Similarly, in our marriage variable, there is a 0 value which has unknown meaning. so we will add that to others.**
"""

# As we can see that there are numerical values in these variables. so lets replace them with their original meanings for eda.
# we do this by creating another df by copying a slice of current df.

cat_var_df = df[['SEX','EDUCATION','MARRIAGE','is_defaulter']].copy()

cat_var_df.replace({'SEX': {1 : 'MALE', 2 : 'FEMALE'},
                   'EDUCATION' : {1 : 'graduate school', 2 : 'university', 3 : 'high school', 4 : 'others', 5:'others',6:'others', 0:'others'},
                   'MARRIAGE' : {1 : 'married', 2 : 'single', 3 : 'others', 0 : 'others'}, 'is_defaulter' :{1:'defaulter',0:'non-defaulter'}},
                   inplace = True )

cat_var_df.head()

# Now Plotting the value counts of these categorical variables.
# Also visualizing the relationship of these variables with our dependent variable using subplots on the above categorical dataframe.

for col in cat_var_df.columns[:-1]:
  plt.figure(figsize=(10,5))
  fig, axes = plt.subplots(ncols=2,figsize=(16,7))

  # Plotting the value counts of categorical variables using pie chart.
  cat_var_df[col].value_counts().plot(kind="pie",autopct='%1.3f%%',ax = axes[0],subplots=True, legend=True)

  # Plotting the relationship between above categorical features and our dependent variables using count plot.
  ax = sns.countplot(x=col, data=cat_var_df,  palette = 'coolwarm', hue="is_defaulter" ,edgecolor = 'magenta',lw =3)

  # Setting the legend at the best location and setting the title.
  plt.legend(loc='best')
  plt.title(f'No. of defaulters vs {col}',weight ='bold', fontsize= 15)

# Annotating the counts in countplot charts.
  for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2, height+100, '{:1.0f}'.format(height),ha = "center", fontsize= 16)

"""From above graphs we can see draw following insights:

*   There are more females credit card holders, and therefore there are more female defaulters.
*   We can clearly see that single people opt for credit cards more than married people.
*   We can clearly see that higher educated people tend to opt for credit cards more than other people.


"""

# Checking the relationship between age and our dependent variable.
plt.figure(figsize=(18,6))
ax = sns.countplot(x = 'AGE', hue = 'is_defaulter', data =df, lw=2)
ax.legend(loc='upper right')
plt.title('No. of Defaulter and non-defaulter with age')
plt.show()

# Now lets explore LIMIT_BAL column which contains the credit limit data of our clients.
df['LIMIT_BAL'].describe()

plt.figure(figsize=(12,7))
sns.barplot(x='is_defaulter', y='LIMIT_BAL', data=df)

# plotting the count plot to vizualize the data distribution with respect to Limit Balance
plt.figure(figsize=[16, 6])
sns.countplot(x='LIMIT_BAL', hue='is_defaulter', data=df, palette='husl')
plt.xticks(rotation=90)                       # Rotate the value of x-ticks so values annotated on x-axis don't get squashed together.
plt.xlabel('Limit Balance (NT dollar)', fontsize=15)
plt.ylabel('Frequency', fontsize=15)
plt.title('LIMIT BALANCE ON TYPE OF CREDIT CARD', fontsize=15)
plt.show()

"""### **Payment Status History**"""

# Looking at the repayment columns for each month.
repayment_feature_list = ['REPAY_STATUS_SEPT',	'REPAY_STATUS_AUG',	'REPAY_STATUS_JUL',	'REPAY_STATUS_JUN',	'REPAY_STATUS_MAY',	'REPAY_STATUS_APR']

# Plotting graph for each payment feature.
for pay_column in repayment_feature_list:
  plt.figure(figsize=(12,6))
  sns.countplot(x = pay_column, hue = 'is_defaulter', data = df ,palette = 'Paired')

"""From above graph it is clear that most often when there is a delay in payment, there is a delay of 2 months. Also we can see that most of our users have revolving credit(value 0) which is defined as credit that is automatically renewed as debts are paid off."""

# Lets now check the bill amount features.
# Assigning the bill amount features to a single variable

df_bill_amount = df[['BILL_AMT_SEPT', 'BILL_AMT_AUG', 'BILL_AMT_JUL', 'BILL_AMT_JUN', 'BILL_AMT_MAY', 'BILL_AMT_APR']]
sns.pairplot(data = df_bill_amount)

# Checking the correlation between our numerical features.
plt.figure(figsize= (20,10))
correlation= df.corr()
sns.heatmap(correlation, annot=True, cmap='Spectral_r')

"""### **Detecting outliers in our dataframe**"""

# Draw box plot to see if there is any outliers in our dataset
plt.figure (figsize= (18,7))
df.boxplot()
plt.xticks(rotation=90)
# rotating xticks to 90 degrees. this is done when we want our x-axis label annotators to be vertical
# because there may not be enough space for us to visualize them.

"""From the above boxplot, we can see that there are quite a few outliers present in our features. And most of these outliers are present in features containing Pre-payment and Bill amount data."""

# creating a list columns in which outliers are present.
outlier_columns = ['LIMIT_BAL', 'BILL_AMT_SEPT','BILL_AMT_AUG', 'BILL_AMT_JUL', 'BILL_AMT_JUN', 'BILL_AMT_MAY',
                 'BILL_AMT_APR', 'PRE_PAY_AMT_SEPT', 'PRE_PAY_AMT_AUG', 'PRE_PAY_AMT_JUL','PRE_PAY_AMT_JUN', 'PRE_PAY_AMT_MAY',
                 'PRE_PAY_AMT_APR']
# using IQR method for dropping outliers from above columns
Q1 = df[outlier_columns].quantile(0.25)
Q3 = df[outlier_columns].quantile(0.75)

IQR = Q3 - Q1                   # interquartile range

# using interquartile range to find and remove outliers from our dataframe.
df = df[~((df[outlier_columns] < (Q1 - 1.5 * IQR)) |(df[outlier_columns] > (Q3 + 1.5 * IQR))).any(axis=1)]

# checking the new shape of the data.
df.shape

# Dropping some of the unnecessary columns.
df.drop(['ID'], axis=1,inplace =True)

df.shape

"""## **Feature Engineering-**

---


"""

# Now checking for correlation among our dependent variables (Multicollinearity) using VIF analysis.
from statsmodels.stats.outliers_influence import variance_inflation_factor

def calc_vif(X):

    # Calculating VIF
    vif = pd.DataFrame()
    vif["variables"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

    return(vif)

# performing VIF analysis
calc_vif(df[[i for i in df.describe().columns if i not in ['is_defaulter']]])

"""As we can see from above, that some of our features have high multicollinearity in them particularly the bill amount columns. so we need to do some feature engineering on them."""

# Lets add up all bill amount features together in one.
df['TOTAL_BILL_PAY'] = df['BILL_AMT_SEPT'] + df['BILL_AMT_AUG'] + df['BILL_AMT_JUL'] + df['BILL_AMT_JUN'] +  df['BILL_AMT_MAY'] + df['BILL_AMT_APR']

# Lets check again.
calc_vif(df[[i for i in df.describe().columns if i not in ['is_defaulter','BILL_AMT_SEPT','BILL_AMT_AUG','BILL_AMT_JUL','BILL_AMT_JUN','BILL_AMT_MAY','BILL_AMT_APR']]])

"""## **Label and One Hot Encoding-**"""

df['SEX']

# Label encoding. encoding sex variable. assigning 2 to 0 (which means female) and 1 to male
df.replace({'SEX' : {1:1,2:0}}, inplace=True)

# One hot encoding.
df = pd.get_dummies(df,columns=['EDUCATION','MARRIAGE'])

df.head()

# final data shape
df.shape

# Creating dependent variable and independent variable
independent_variables = df.drop(['is_defaulter'],axis=1)
dependent_variable = df['is_defaulter']

# scaling the data using zscore.
from scipy.stats import zscore
x = round(independent_variables.apply(zscore),3)
y = dependent_variable

# train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

"""## **Applying SMOTE (Synthetic Minority Oversampling Technique)-**

---

Since we have an imbalanced dataset, we are going to need to apply some technique to remedy this. So we will try oversampling technique called SMOTE.
"""

# applying oversampling to overcome class imbalance
from imblearn.over_sampling import SMOTE
smote= SMOTE()
x_train_smote,y_train_smote = smote.fit_resample(x,y)

from collections import Counter
print('Original dataset shape', Counter(y_train))
print('Resample dataset shape', Counter(y_train_smote))
Counter(y_train_smote)

"""## **MODEL IMPLEMENTATION-**

"""

# importing all the evaluation metrics that we will need for comparison.
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.metrics import roc_auc_score, confusion_matrix, roc_curve, auc, classification_report

"""### **Model1. Logistic Regression**"""

# Importing Logistics Regression and GridSearchCV

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# initiate the model.
logistic_model = LogisticRegression(class_weight='balanced')

# define the parameter grid.
param_grid = {'penalty':['l1','l2'], 'C' : [0.0001,0.001,0.003,0.004,0.005, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 10, 20, 50, 100] }

# implementing the model.
logistic_model= GridSearchCV(logistic_model, param_grid, scoring = 'accuracy', n_jobs = -1, verbose = 3, cv = 3)
logistic_model.fit(x_train_smote, y_train_smote)

# getting the best estimator
logistic_model.best_estimator_

# getting the optimal parameters
logistic_model.best_params_

# getting the predicted probability of target variable.
y_train_preds_logistic = logistic_model.predict_proba(x_train_smote)[:,1]
y_test_preds_logistic = logistic_model.predict_proba(x_test)[:,1]

# getting the predicted class
y_train_class_preds_logistic = logistic_model.predict(x_train_smote)
y_test_class_preds_logistic = logistic_model.predict(x_test)

# checking the accuracy on training and unseen test data.
logistic_train_accuracy= accuracy_score(y_train_smote, y_train_class_preds_logistic)
logistic_test_accuracy= accuracy_score(y_test, y_test_class_preds_logistic)

print("The accuracy on train data is ", logistic_train_accuracy)
print("The accuracy on test data is ", logistic_test_accuracy)

# writing a function for evaluating various metrics
def evaluation_metrics(actual, predicted):

  """ This function is used to find the accuracy score , precision score , recall score , f1 score , ROC_AUC Score ,
      Confusion Matrix , Classification  report """
  metrics_list = []
  accuracy = accuracy_score(actual,predicted)
  precision = precision_score(actual, predicted)
  recall = recall_score(actual, predicted)
  model_f1_score = f1_score(actual, predicted)
  auc_roc_score = roc_auc_score(actual , predicted)
  model_confusion_matrix = confusion_matrix(actual , predicted)

  metrics_list = [accuracy,precision,recall,model_f1_score,auc_roc_score, model_confusion_matrix]
  return metrics_list

evaluation_metrics(y_test, y_test_class_preds_logistic)

# Let's store these metrics in a dataframe. that way we can easily compare metrics of different models.
# first store this data in a dict.
metric_name_list = ['accuracy','precision','recall','f1_score','roc_auc_score','confusion_matrix']
metric_values = evaluation_metrics(y_test, y_test_class_preds_logistic)

# zipping together above lists to form a dictionary
metric_dict = dict(zip(metric_name_list,metric_values))

# creating a dataframe out of this.
evaluation_metric_df = pd.DataFrame.from_dict(metric_dict, orient='index').reset_index()
evaluation_metric_df.columns = ['Evaluation Metric','Logistic Regression']

evaluation_metric_df

# Plotting the confusion matrix from test data

labels = ['Non Defaulter', 'Defaulter']
cm = confusion_matrix(y_test,y_test_class_preds_logistic)
ax= plt.subplot()
sns.heatmap(cm, annot=True, cmap='coolwarm', ax = ax, lw = 3) #annot=True to annotate cells

# labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('Actual labels')
ax.set_title('Confusion Matrix of Logistics Regression from testing data')
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)

# also printing confusion matrix values
print(cm)

# Plotting Roc_auc_curve for test data
y_test_pred_logistic = logistic_model.predict_proba(x_test)[:,1]
fpr, tpr, _ = roc_curve(y_test,y_test_pred_logistic)
plt.plot(fpr,tpr)
plt.title("Roc_auc_curve on Test data")
plt.legend(loc=4)
plt.show()

# printing the classification report.
print('classification_report is \n {}'.format(classification_report(y_test, y_test_class_preds_logistic)))

evaluation_metric_df

"""* We have implemented logistic regression and we are getting accuracy_score is approx 68%
 * Precision score is around 41% and f1_score is around 50%
 * roc_auc approx is 67% and recall_score is approx 64%

### **Mode2. Random Forest Classifier**
"""

# Importing Random forest
from sklearn.ensemble import RandomForestClassifier

model_rf= RandomForestClassifier()                                                              # initializing the model.

grid_values = {'n_estimators':[50,80,90,100], 'max_depth':[9,11,14]}              # initializing the parameter grid.
grid_rf = GridSearchCV(model_rf, param_grid = grid_values, scoring = 'accuracy', cv=3)

# Fitting the model.
grid_rf.fit(x_train_smote, y_train_smote)

# getting the best estimator
grid_rf.best_estimator_

# getting the best parameter
grid_rf.best_params_

# Getting the predicted classes
y_train_class_preds_rf = grid_rf.predict(x_train_smote)
y_test_class_preds_rf = grid_rf.predict(x_test)

# Getting the evaluation metrics using our function and adding it to evaluation dataframe to better read it.
evaluation_metric_df['Random Forest']=evaluation_metrics(y_test,y_test_class_preds_rf)
evaluation_metric_df

# Plotting the confusion matrix from test data

labels = ['Non Defaulter', 'Defaulter']
cm = confusion_matrix(y_test,y_test_class_preds_rf)
ax= plt.subplot()
sns.heatmap(cm, annot=True, cmap='coolwarm', ax = ax, lw = 3) #annot=True to annotate cells

# labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('Actual labels')
ax.set_title('Confusion Matrix of Random Forest from testing data')
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)

# also printing confusion matrix values
print(cm)

print('classification_report is \n {}'.format(classification_report(y_test, y_test_class_preds_rf)))

# Printing Roc_auc_curve from test data

y_test_preds_proba_rf = grid_rf.predict_proba(x_test)[::,1]
fpr, tpr, _ = roc_curve(y_test,  y_test_preds_proba_rf)
auc = roc_auc_score(y_test,  y_test_preds_proba_rf)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.title("Roc_auc_curve on testing data")
plt.legend(loc=4)
plt.show()

"""Random Forest model has inbuilt support for showing the feature importances - i.e. which feature is more important in coming up with the predicted results. This helps us interpret and understand the model better."""

# getting columns names from training data
features = x_train_smote.columns

# getting the feature importances
importances = grid_rf.best_estimator_.feature_importances_
indices = np.argsort(importances)

# plotting the feature importances using a horizontal bar graph.
plt.figure (figsize= (12,12))
plt.title('Relative Feature Importance', fontsize=14)
plt.barh(range(len(indices)), importances[indices], color='magenta', edgecolor='mediumblue', align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.ylabel('Features', fontsize=14)
plt.show()

"""### **Mode3. K-Nearest Neighbour Classifier**

---


"""

# Import K Nearest Neighbour Classifier
from sklearn.neighbors import KNeighborsClassifier

# initializing the model
knn = KNeighborsClassifier()

# knn the parameter to be tuned is n_neighbors
param_grid = {'n_neighbors':[4,5,6,7,8,10,12,14]}

# Fitting the model

knn_cv= GridSearchCV(knn,param_grid, scoring = 'accuracy',cv=3)
knn_cv.fit(x_train_smote,y_train_smote)

# find best score
knn_cv.best_score_

# best parameters
knn_cv.best_params_

knn_cv.best_estimator_

# Get the predicted classes
y_train_class_preds_knn = knn_cv.predict(x_train_smote)
y_test_class_preds_knn = knn_cv.predict(x_test)

# getting the evaluation metrics and adding it to metric dataframe.
evaluation_metric_df['KNeighborsClassifier'] = evaluation_metrics(y_test,y_test_class_preds_knn)
evaluation_metric_df

# Printing the classification report.
print('classification_report is \n {}'.format(classification_report(y_test, y_test_class_preds_knn)))

# Plotting the confusion matrix for testing data
labels = ['Not Defaulter', 'Defaulter']
cm = confusion_matrix(y_test,y_test_class_preds_knn)
print(cm)

ax= plt.subplot()
sns.heatmap(cm, annot=True, linewidths=1, cmap='coolwarm',ax = ax)

# labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Confusion Matrix of KNN Classifier for testing data')
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)

# Printing Roc_auc_curve from test data

y_test_preds_proba_knn = knn_cv.predict_proba(x_test)[::,1]
fpr, tpr, _ = roc_curve(y_test,  y_test_preds_proba_knn)
auc = roc_auc_score(y_test,  y_test_preds_proba_rf)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.title("Roc_auc_curve on testing data")
plt.legend(loc=4)
plt.show()

"""### **Model4. Support Vector Classifier**"""

# Importing support vector machine algorithm from sklearn
from sklearn import svm

# initiate a svm Classifier
svm_model = svm.SVC(kernel = 'poly',gamma='scale', probability=True)

# fit the model using the training sets
svm_model.fit(x_train_smote, y_train_smote)

# Get the predicted classes
y_train_class_preds_svm = svm_model.predict(x_train_smote)
y_test_class_preds_svm = svm_model.predict(x_test)

evaluation_metric_df['Support Vector classifier'] = evaluation_metrics(y_test,y_test_class_preds_svm)
evaluation_metric_df

# Plotting the confusion matrix for testing data
labels = ['Not Defaulter', 'Defaulter']
cm = confusion_matrix(y_test,y_test_class_preds_svm)
print(cm)

ax= plt.subplot()
sns.heatmap(cm, annot=True, linewidths=1, cmap='coolwarm',ax = ax)

# labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Confusion Matrix of SVM Classifier for testing data')
ax.xaxis.set_ticklabels(labels)
ax.yaxis.set_ticklabels(labels)

# Printing the classification report.
print('classification_report is \n {}'.format(classification_report(y_test, y_test_class_preds_knn)))

# Roc_auc_curve on taining data

y_train_preds_proba_svm = svm_model.predict_proba(x_train_smote)[::,1]
fpr, tpr, _ = roc_curve(y_train_smote,  y_train_preds_proba_svm )
auc = roc_auc_score(y_train_smote,  y_train_preds_proba_svm )
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.title("Roc_auc_curve on Training data")
plt.legend(loc=4)
plt.show()

# finally, we can compare our models on variour evaluation metric values.
evaluation_metric_df

"""#**Model Deploy**

"""

#Model Deployment
# elasticnet_regressor
#pickle library is used to save model

import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt



filename = "trained_model.sav"
pickle.dump(svm_model,open(filename,"wb"))

#loading the model
loaded_model = pickle.load(open("trained_model.sav","rb"))

def predict_defaulter(input_data):
     #input_data =  (200000, 2, 35, -1, 2, 0, 0, 0, 0, 167080, 170788, 174764, 173774, 170788, 174764, 10000,
#9000, 8000, 7000, 6000, 5000, 167080, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not Defaulter'
    else:
      return 'The person is Defaulter'



def main():



    # Giving a title
    st.title('Defaulter Prediction Web App')

    # Getting the input data from the user
    LIMIT_BAL = st.text_input('LIMIT_BAL')
    SEX = st.text_input('SEX')
    AGE = st.text_input('AGE')
    REPAY_STATUS_SEPT = st.text_input('REPAY_STATUS_SEPT')
    REPAY_STATUS_AUG = st.text_input('REPAY_STATUS_AUG')
    REPAY_STATUS_JUL = st.text_input('REPAY_STATUS_JUL')
    REPAY_STATUS_JUN = st.text_input('REPAY_STATUS_JUN')
    REPAY_STATUS_MAY = st.text_input('REPAY_STATUS_MAY')
    REPAY_STATUS_APR = st.text_input('REPAY_STATUS_APR')
    BILL_AMT_SEPT = st.text_input('BILL_AMT_SEPT')
    BILL_AMT_AUG = st.text_input('BILL_AMT_AUG')
    BILL_AMT_JUL = st.text_input('BILL_AMT_JUL')
    BILL_AMT_JUN = st.text_input('BILL_AMT_JUN')
    BILL_AMT_MAY = st.text_input('BILL_AMT_MAY')
    BILL_AMT_APR = st.text_input('BILL_AMT_APR')
    PRE_PAY_AMT_SEPT = st.text_input('PRE_PAY_AMT_SEPT')
    PRE_PAY_AMT_AUG = st.text_input('PRE_PAY_AMT_AUG')
    PRE_PAY_AMT_JUL = st.text_input('PRE_PAY_AMT_JUL')
    PRE_PAY_AMT_JUN = st.text_input('PRE_PAY_AMT_JUN')
    PRE_PAY_AMT_MAY = st.text_input('PRE_PAY_AMT_MAY')
    PRE_PAY_AMT_APR = st.text_input('PRE_PAY_AMT_APR')
    TOTAL_BILL_PAY = st.text_input('TOTAL_BILL_PAY')
    EDUCATION_0 = st.text_input('EDUCATION_0')
    EDUCATION_1 = st.text_input('EDUCATION_1')
    EDUCATION_2 = st.text_input('EDUCATION_2')
    EDUCATION_3 = st.text_input('EDUCATION_3')
    EDUCATION_4 = st.text_input('EDUCATION_4')
    EDUCATION_5 = st.text_input('EDUCATION_5')
    EDUCATION_6 = st.text_input('EDUCATION_6')
    MARRIAGE_0 = st.text_input('MARRIAGE_0')
    MARRIAGE_1 = st.text_input('MARRIAGE_1')
    MARRIAGE_2 = st.text_input('MARRIAGE_2')
    MARRIAGE_3 = st.text_input('MARRIAGE_3')

    # Code for prediction
    Defaulter = ''

    # Creating a button for prediction
    if st.button('Defaulter  Result'):
        Defaulter = ([LIMIT_BAL, SEX, AGE, REPAY_STATUS_SEPT, REPAY_STATUS_AUG, REPAY_STATUS_JUL, REPAY_STATUS_JUN, REPAY_STATUS_MAY,
                       REPAY_STATUS_APR, BILL_AMT_SEPT, BILL_AMT_AUG, BILL_AMT_JUL, BILL_AMT_JUN, BILL_AMT_MAY,BILL_AMT_APR
                       ,PRE_PAY_AMT_SEPT, PRE_PAY_AMT_AUG,PRE_PAY_AMT_JUL, PRE_PAY_AMT_JUN, PRE_PAY_AMT_MAY, PRE_PAY_AMT_APR,
                       TOTAL_BILL_PAY, EDUCATION_0, EDUCATION_1,EDUCATION_2,EDUCATION_3,EDUCATION_4,EDUCATION_5,EDUCATION_6,MARRIAGE_0,
                       MARRIAGE_1,MARRIAGE_2,MARRIAGE_3,])

    st.success(Defaulter)

if __name__ == '__main__':
    main()







