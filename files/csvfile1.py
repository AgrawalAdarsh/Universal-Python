import csv
path="/mnt/c/Users/pc/Documents/student_data.csv"
f = open(path,'r')
csv_r = csv.reader(f)
data = list(csv_r)
for line in data:
	for word in line:
		print(word,"\t",end=" ")
	print("\n")
f.close()
