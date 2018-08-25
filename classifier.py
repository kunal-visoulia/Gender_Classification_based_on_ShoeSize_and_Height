from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier #nearest neighbour classifier
from sklearn.ensemble import RandomForestClassifier #Random Forest classifier
from sklearn.naive_bayes import GaussianNB #Naive Bayes classifier
import xlrd

workbook = xlrd.open_workbook('original_dataset.xls')
worksheet = workbook.sheet_by_index(0)
X=[]
Y=[]
num_rows = worksheet.nrows - 1
curr_row = 1
while curr_row<num_rows:
	row = worksheet.row(curr_row)
	templist=[row[2].value, row[3].value]
        X.append(templist)
	if row[1].value=='F':
		templist='female'
	else:
		templist='male'
	Y.append(templist)		
	curr_row+=1

clf1 = tree.DecisionTreeClassifier()
clf2 = KNeighborsClassifier()
clf3 = RandomForestClassifier()
clf4 = GaussianNB()  

clf1 = clf1.fit(X, Y)
clf2 = clf2.fit(X, Y)
clf3 = clf3.fit(X, Y)
clf4 = clf4.fit(X, Y)

# we have taken 377 labelled datasets for testing the accuracy of each classifier
total_data=377.0
DCtree=0
Kneigh=0
RandForest=0
GaussNB=0
i=0
while i<377:
	prediction1 = clf1.predict([X[i]])
	if prediction1[0]==Y[i]:
		DCtree+=1
	
	prediction2 = clf2.predict([X[i]])
	if prediction2[0]==Y[i]:
		Kneigh+=1
	prediction3 = clf3.predict([X[i]])
	if prediction3[0]==Y[i]:
		RandForest+=1
	prediction4 = clf4.predict([X[i]])
	if prediction4[0]==Y[i]:
		GaussNB+=1
	i+=1

DCtree=DCtree/total_data
DCtree=DCtree*100

Kneigh=Kneigh/total_data
Kneigh=Kneigh*100

RandForest=RandForest/total_data
RandForest=RandForest*100

GaussNB=GaussNB/total_data
GaussNB=GaussNB*100

print "DecisionTreeClassifier Accuracy: "+"{0:.2f}".format(DCtree)+"%"
print "KNeighborsClassifier   Accuracy: "+"{0:.2f}".format(Kneigh)+"%"
print "RandomForestClassifier Accuracy: "+"{0:.2f}".format(RandForest)+"%"
print "GaussianNB             Accuracy: "+"{0:.2f}".format(GaussNB)+"%"
