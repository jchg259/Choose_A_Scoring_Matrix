import numpy as np

from matrices import matrices_reader

from galignment import nw_algoirthm

from PAMScoreList import PAM_Score_List

'''
sequence1 = "GAVLIMXCST"
sequence2 = "GAV-YZXC--"



matrix = np.loadtxt("MatricesTest/Test20.txt", dtype=str)
#print(matrix)

n = len(sequence1)
m = len(sequence2)

pamscore = 0
row = 0
col = 0

for i in range(0,max(n,m)):
	a=0
	b=0
	
	for j in range(0,23):
		if sequence1[i] != matrix[0][a]:
			a = a+1
		else:
			col = a
			#print(col)
			break
		    
	for k in range(0,23):
		if sequence2[i] != matrix[0][b]:
			b = b+1
		else:
			row = b+1
			#print(row)
			break
		    
	pamscore = pamscore + float(matrix[row][col])

print(pamscore)
'''

#letters, matrixlist = matrices_reader()
#matrixitem = matrixlist[1]
#print(letters)
#print(matrixitem)



#sequence_1 = "gavlimxcst"
#sequence_2 = "gavyzxc"

#sequence_1, sequence_2, GA_Score = nw_algoirthm("GAVLIMXCST","GAVYZXC",letters, matrixlist[0])
#print(sequence_1)
#print(sequence_2)
#print(GA_Score)

max, list = PAM_Score_List("GAVLIMXCST","GAVYZXC")
print(max)
print(list)