import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


# call dataset

df = pd.read_csv(r"C:\Users\rohit.pandey\OneDrive - Walker Digital Table Systems\Documents\PythonLearning\DataAnalysis\Expanded_data_with_more_features.csv")
#print(df.head())

#print(df.describe())

#print(df.info())
#print(df.isnull().sum())

#drop column

df=df.drop("Unnamed: 0",axis=1)

#change weekly study hours
df["WklyStudyHours"]=df["WklyStudyHours"].str.replace("10-May","5-10")

#gender distribution
plt.figure(figsize=(3,3))
ax=sns.countplot(data=df,x="Gender")
ax.bar_label(ax.containers[0])
#plt.show()

#From the above we have analysed that the number of female is greater than Male
#Transport distribution

plt.figure(figsize=(3,3))
td=sns.countplot(data=df,x="TransportMeans")
td.bar_label(ax.containers[0])
#plt.savefig(r"C:\Users\rohit.pandey\OneDrive - Walker Digital Table Systems\Documents\PythonLearning\DataAnalysis\gender_distribution.png")
#plt.show()

#Parent education Impact
gb=df.groupby("ParentEduc").aggregate({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
#print(gb)

plt.figure(figsize=(5,5))
sns.heatmap(gb,annot=True)
#plt.savefig(r"C:\Users\rohit.pandey\OneDrive - Walker Digital Table Systems\Documents\PythonLearning\DataAnalysis\ParentEdu.png")
plt.show()

#from the above chart we have conclude that the education of parent good impact

# write the output of data in the excel

# excel_path = r"C:\Users\rohit.pandey\OneDrive - Walker Digital Table Systems\Documents\PythonLearning\DataAnalysis\grouped_aggregated_data.xlsx"

# with pd.ExcelWriter(excel_path) as writer :
#     gb.to_excel(writer,sheet_name="AggregateEducation")
    
# print(f"Data Saved to {excel_path}")

#parent marital status report

gbmsr=df.groupby("ParentMaritalStatus").aggregate({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gbmsr)

sns.heatmap(gbmsr,annot=True)
plt.show()
