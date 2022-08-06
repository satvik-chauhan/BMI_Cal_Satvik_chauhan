import pandas as pd 
list1=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
df=pd.DataFrame(list1)
df['HeightCm']=df['HeightCm']/100
l1=[]
try:
 for i in df.index:
    l1.append(round(df['WeightKg'][i]/df['HeightCm'][i],2))
 df['BMI']=l1
except Exception as e:
    print("weight can not be zero",e)
bmi_cat = []
health_risk = []
for i in df['BMI']:
                if i <= 18.4:
                    bmi_cat.append("Underweight")
                    health_risk.append('Malnutrition risk')
                elif i >= 18.5 and i <= 24.9:
                    bmi_cat.append('Normal weight')
                    health_risk.append('Low risk ')
                elif i >= 25 and i <= 29.9:
                    bmi_cat.append('Overweight')
                    health_risk.append('Enhanced risk')
                elif i >= 30 and i <= 34.9:
                    bmi_cat.append('Moderately obese')
                    health_risk.append('Medium risk')
                elif i >= 35 and i <= 35.9:
                    bmi_cat.append('severely obese')
                    health_risk.append('High risk')
                else:
                    bmi_cat.append('Very severely obese')
                    health_risk.append('Very High risk ')

df['Bmi category'] = bmi_cat
df['Health Risk'] = health_risk
print(df)


counts_cat = df['Bmi category'].value_counts()
print(counts_cat)
