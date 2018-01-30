
import random

a=[2,3,4,10,11,12,20,25,30]
a.sort()
k=2

m1=a[2]
m2=a[5]

means=[]
means.append(m1)
means.append(m2)

def cal(m11,m22):
	k1=[]
	k2=[]
			
	for i in range(len(a)):
		s1=0
		s2=0

		if(a[i]<m11 or a[i]==m11):
			k1.append(a[i])
		else:
			if(a[i]>m22 or a[i]==m22):
				k2.append(a[i])
		if(a[i]>m11 and a[i]<m22):	
			s1=a[i]-m11
			s2=m22-a[i]
			if(s2<s1):	
				k2.append(a[i])			
			if(s1<s2):	
				k1.append(a[i])			

	m11=sum(k1)/len(k1)
	m22=sum(k2)/len(k2)

	if(m11 in means and m22 in means):
		print "Final k1:- "+str(k1) 	
		print "Final k2:- "+str(k2)

		print 'Means   :- ['+str(means[len(means)-2]),str(means[len(means)-1])+']'

		return 0 	

	else:
		means.append(m11)
		means.append(m22)
		cal(m11,m22)


cal(m1,m2)



