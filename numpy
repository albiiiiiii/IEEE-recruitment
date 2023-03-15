import pandas as ps
import numpy as np

s=ps.read_csv('diabetes.csv')
print(s)
pregnancies=np.array(s['Pregnancies'])
glucose=np.array(s['Glucose'])
bp=np.array(s['BloodPressure'])
st=np.array(s['SkinThickness'])
insulin=np.array(s['Insulin'])
bmi=np.array(s['BMI'])
dpf=np.array(s['DiabetesPedigreeFunction'])
age=np.array(s['Age'])
out=np.array(s['Outcome'])

#to find the average of the columns
print('average of insulin=',np.mean(insulin))
print('average of glucose=',np.mean(glucose))
print('average of blood pressure=',np.mean(bp))

#to find the maximum value in the column
print('*')
print('the maximum glucose level is: ',np.amax(glucose))
print('the maximum insulin level is: ',np.amax(insulin))
print('the maximum skin thickness is: ',np.amax(st))

#to find the minimum value in the column
print('*')
print('the minimum BMI level is: ',np.amin(bmi))
print('the minimum skin thickness is: ',np.amin(st))
print('the minimum age is: ',np.amin(age))

#to find the round value of the column
print('*')
print('the rounded glucose levels are: \n',list(map(int,np.rint(glucose))))

#to find the absolute value of a column
print("*")
print("the absolute values of bp levels are: \n",list(map(int,np.abs(bp))))
