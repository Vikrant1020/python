# show data in a table form.
import pandas as pds
car={
	'hel':['asd','asdf'],
	'ok':[56,560]
}
a=pds.DataFrame(car)
print(a)

print(pds.__version__)

# show data in a series.
b= (1,31,'AK')
c=pds.Series(b)
print(c)
print(c[1])

d=pds.DataFrame(car, index=['a','b'])
print(d)

# for a sepicify data form a series.
e={'day1':20, 'day2':21,'day3':24}
f=pds.Series(e, index=['day1','day3'])
print(f)
g=pds.Series(car,index=['ok'])
print(g)

# for a sepicify row form a directory.
print(a.loc[0])

#for loading a file in data frame.
x=pds.read_csv('data.csv')
print(x)	
# for showing the entire data.
print(x.to_string())
print(x.head(10))
print(x.head())
print(x.tail())
print(x.tail(10))
print(x.info())

"""# for removing the rows with empty cell's. without changing the exesting data.
new_x=x.dropna()
print(new_x.to_string())
print("\n")"""

# for removing the row wtih empty cell's. and also change the data.
"""x.dropna(inplace=True)
print(x)"""

"""# for entering new values in place of empty cell.
x.fillna('ANKUR',inplace=True)
print(x)"""

"""# for entering the value to sepicify coloum.
x['Maxpulse'].fillna('Vikrant',inplace=True)
print(x)"""

"""# for entering the new value as the mean, median or mode values.
y=x['Maxpulse'].mean()
x['Maxpulse'].fillna(y,inplace=True)
print(x)
# y is the mean value of Maxpulse.
print(y)"""

"""x.dropna(subset=['Maxpulse'],inplace=True)
print(x)"""

# for changing the data.
x.loc[8, 'Duration']=90
print(x.to_string())

# adding a condation.
for z in x.index:
	if x.loc[z,'Duration']>75:
		x.loc[z,'Duration']=75
print(x.to_string())

#for duplicat rows.
print(x.duplicated())

# for removing the duplicate rows.
x.drop_duplicates(inplace=True)
print(x.to_string())
print("\n")

# for data collaration. or for inding the relationship b/w coloums of a Dataframe.
print(x.corr())