
mat=[['x',1,'x','x','x',12],['x','x',3,1,'x','x'],['x','x','x','x',3,'x'],[1,'x','x','x',2,2],['x','x','x','x','x',3],['x','x','x','x','x','x']]
visit=[]
cc=[]
mat1=[]

mat1=mat
def check(a):
	k=a.index(min(a))
	visit.append(mat.index(a))
	if(k==5):
		print k
		return 0
	else:	
		if(k not in visit):
			print k
			cc.append(k)	
			check(mat[k])
		else:
			a[k]='x'
			kk=mat.index(a)
			check(mat[kk])		

print "\nsource:-0 \t Destination:-5"
print "\ncheapest cost:-"

check(mat[0])

def create(aa):
	for i in range(len(aa)):		
		if(aa[i]=='x'):
			aa[i]=0
for i in range(len(mat1)):
	create(mat1[i])	

print "\nGraph:-"
print mat1






















