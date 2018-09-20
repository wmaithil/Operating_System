print("Enter the number of process: ")
n = int(raw_input())
Allocation = []
Max = []
Need = []

#take inputs of Allocation

for i in range(n):
	theinputs = []
	for j in range(3):
		x = int(raw_input())
		theinputs.append(x)
	Allocation.append(theinputs)

#take inputs of Max

for i in range(n):
	theinputs = []
	for j in range(3):
		x = int(raw_input())
		theinputs.append(x)
	Max.append(theinputs)

#find Need

for i in range(n):
	theinputs = []
	for j in range(3):
		x = Max[i][j] - Allocation[i][j]
		theinputs.append(x)
	Need.append(theinputs)

#print(Need)

#take input of A,B,C at t0 time

A = int(raw_input())
B = int(raw_input())
C = int(raw_input())

#getting Available at t0 time

Available = []

x = 0
for i in range(n):
	x += Allocation[i][0]
x = A - x
Available.append(x)

x = 0
for i in range(n):
	x += Allocation[i][1]
x = B - x
Available.append(x)

x = 0
for i in range(n):
	x += Allocation[i][2]
x = C - x
Available.append(x)

#print(Available)

Work = Available

#take input for request

request = []
for i in range(3):
	x = int(raw_input())
	request.append(x)

# All finish is Zero at the initial

Finish = []
for i in range(n):
	Finish.append(0)

########################

#checking few things, ignore those codes

print(Allocation)
Allocation[0] = Work
print(Allocation)

#########################

#safety check after Pi request

Sequence = []

for i in range(n):
	for j in range(n):
		if(Finish[j] == 0):
			if(Need[j][0]<=Work[0] and Need[j][1]<=Work[1] and Need[j][2] <= Work[2]):
				Work[0] += Allocation[j][0]
				Work[1] += Allocation[j][1]
				Work[2] += Allocation[j][2]
				Finish[j] = 1
				Sequence.append(j)

print(Finish)

tag = 0

for i in range(n):
	if(Finish[i]== 0):
		tag = 1
		break

if(tag == 0):
	print("Granted!")
	print("The Process Sequence: ")
	print(Sequence)
else:
	print("Not Granted!")
