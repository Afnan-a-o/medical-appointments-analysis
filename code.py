import pandas as pd
#Make DateFrame for data inside CSV
data = pd.read_csv('data.csv') 
#Print First 5 rows of data
print("Let's See some rows\n" , data.head())
print("--------------------")
#Print out the size of our DataFrame How many columns and rows.
print("The Data Size we have\n" , data.shape)
print("--------------------")
#Know our Data types inside our DataFrame
print("The Data Type we have\n" , data.dtypes)
print("--------------------")
#Filterd some features and we will work with these features
features = ['PatientId','Gender','AppointmentDay','Age','Neighbourhood','Scholarship','Hipertension','Diabetes','Alcoholism','SMS_received','No-show']
#make new DataFrame and set it with the features selected
new = data[features] 
#Print first 5 rows of our new DataFrame
print("Let's See some rows in our new dataset\n" , new.head())
print("--------------------")
#Quick look into our data
print("Some statistics\n" , new.describe())
print("--------------------")
