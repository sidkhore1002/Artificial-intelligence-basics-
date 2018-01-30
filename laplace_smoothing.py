
spam=["first game cricket","second game football","third game cricket"]

ham=["ronaldo plays football","football is best game","cricket football kabbadi are all game","rahul plays cricket"]

d=[]

spam_len=len(spam)
ham_len=len(ham)

print "\nSpam = "+str(spam)
print "\nHam = "+str(ham)
#----------------------------------------------------------spam--------------------------------------------------------

def prob_spam():
	p1=round(float(spam_len)/float(spam_len+ham_len),4)
	return p1

def prob_ham():
	p2=round(float(ham_len)/float(spam_len+ham_len),4)
	return p2
#----------------------------------------------------------m_spam--------------------------------------------------------
def tot_d():
	cnt1=0
	cnt2=0
	rr=0
	for i in range(0,len(spam)):
		s1=spam[i].split()
		for j in range(0,len(s1)):
			if(s1[j] in d):
				continue
			else:
				d.append(s1[j])
				cnt1 +=1

	for i in range(0,len(ham)):
		s1=ham[i].split()
		for j in range(0,len(s1)):
			if(s1[j] in d):
				continue
			else:
				d.append(s1[j])
				cnt2 +=1

	rr=cnt1+cnt2
	return rr

def total_spam():
	tot=0
	for i in range(0,len(spam)):
		s1=spam[i].split()
		tot=tot+len(s1)

	return tot

def cnt_m_spam(w1):
	s2=0
	for i in range(0,len(spam)):
		s1=spam[i].split()
		if(w1 in s1): 	
			s2 +=1
	return s2

def prob_m_spam(w1,k):
	a1=cnt_m_spam(w1)
	a2=total_spam()
	a3=tot_d()	
	s2=float(a1+k)/float(a2+float(a3*k))
	return s2

#----------------------------------------------------------m_ham--------------------------------------------------------
def total_ham():
	tot=0
	for i in range(0,len(ham)):
		s1=ham[i].split()
		tot=tot+len(s1)

	return tot

def cnt_m_ham(w1):
	s2=0
	for i in range(0,len(ham)):
		s1=ham[i].split()
		if(w1 in s1): 	
			s2 +=1
	return s2

def prob_m_ham(w1,k):
	a1=cnt_m_ham(w1)
	a2=total_ham()
	a3=tot_d()	
	s2=float(a1+k)/float(a2+float(a3*k))
	return s2
#----------------------------------------------------------spam_m  &  ham_m --------------------------------------------------------

def prob_spam_m():
	w1=raw_input("\nEnter word:-\n")
	k=input("\nEnter value for k:-\n")

	t1=1
	t2=1
	t11=1
	t22=1
	w=w1.split()
	if(len(w)>1):
		for i in range(0,len(w)):
			t1=round(float(t1)*float(prob_m_spam(w[i],k)),4)
			t2=round(float(t2)*float(prob_m_ham(w[i],k)),4)
		tt1=round(float(t1)*float(prob_spam()),4)
		tt2=round(float(t2)*float(prob_ham()),4)
		final_t=round(float(tt1)/(float(tt1)+float(tt2)),4)
		print "\np(spam | "+ w1+") = "+str(final_t)+"\n"

	else:
		s3=round(float(prob_m_spam(w1,k)),4)
		print "\np(Spam | "+ w1+") = "+str(s3)+"\n"


def prob_ham_m():
	w2=raw_input("\nEnter word:-\n")
	k=input("\nEnter value for k:-\n")

	t1=1
	t2=1
	t11=1
	t22=1
	w=w2.split()
	if(len(w)>1):
		for i in range(0,len(w)):
			t1=round(float(t1)*float(prob_m_ham(w[i],k)),4)
			t2=round(float(t2)*float(prob_m_spam(w[i],k)),4)
		tt1=round(float(t1)*float(prob_ham()),4)
		tt2=round(float(t2)*float(prob_spam()),4)
		final_t=round(float(tt1)/(float(tt1)+float(tt2)),4)
		print "\np(Ham | "+ w2+") = "+str(final_t)+"\n"

	else:
		s3=round(float(prob_m_ham(w2,k)),4)
		print "\np(Ham | "+ w2+") = "+str(s3)+"\n"

#----------------------------------------------------------spam_m  &  ham_m --------------------------------------------------------

print "\nLaplas smoothing\n"
print "\n 1-m_Spam"
print " 2-m_Ham"

n=input("\nEnter ur choice for laplas smoothing\n")

options = {
	1 : prob_spam_m,		
	2 : prob_ham_m,		
}

options[n]()

