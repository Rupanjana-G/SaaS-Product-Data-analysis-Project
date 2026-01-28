import pandas as pd

df = pd.read_csv('DATA.csv')
df = df.drop(columns=['account_manager','customer_name','last_success_touch_date','notes'])
print(df)


#Churn status
def churn_type(score):
    if score >= 0.7:
        return 'High Risk'
    elif score >= 0.4:
        return 'Medium Risk'
    else:
        return 'Low Risk'

df['churn_status'] = df['churn_risk_score'].apply(churn_type)
print(df['churn_status'].value_counts())


#churn_by_plan_type
churn_plan_type = df.groupby('plan_type')['churn_status'].value_counts()
print("Churn by plan type")
print(churn_plan_type)


#churn_by_industry_type
churn_by_industry = df.groupby('industry')['churn_status'].value_counts()
print ("Churn status for each industry type")
print(churn_by_industry)


#customer with the highest risk
highest_index = df['churn_risk_score'].idxmax()
print ("Highest churn risk data")
print(df.loc[highest_index])


#usage vs churn
print("Usage v/s Churn")
print(df.groupby('churn_status')['feature_usage_score'].mean())


#retention vs churn
print("retention rate v/s Churn(6m) ")
print(df.groupby('churn_status')['retention_rate_6m'].mean())
print("retention rate v/s Churn(12m) ")
print(df.groupby('churn_status')['retention_rate_12m'].mean())


#plan with the highest average churn score
print ("plan with the highest average churn score : ")
print(df.groupby('plan_type')['churn_risk_score'].mean().idxmax())


#most common plan
c = df['plan_type'].value_counts().idxmax()
print("Most common plan is:",c)


df.to_csv("cleaned_DATA.csv", index=False)
print("Saved cleaned data")










