import csv

#name of the file and path so that we can read it. Flag is to mention whether to remove the last character F/S.
activity_identifier_list = []
#path = "WI_WB_37647941_SITES.csv"
#name = "test"

def calculateUniqueFrequencies(name, path, flag):
	with open(path, 'r', encoding='UTF-8') as inp:
		for row in csv.reader(inp):
			if(row[3] != "" and row[3]!="ActivityIdentifier"):
				if(flag):
					activity_identifier_list.append(row[3][:-1])
				else:
					activity_identifier_list.append(row[3])

def getUniqueFrequencies(name, path):
	flag=1 #initialize flag as 1. Flag 1 is used to remove the last character from name!
	calculateUniqueFrequencies(name, path, flag)
	activity_identifier_set = set(activity_identifier_list) 
	return len(activity_identifier_set)

# frequencies = getUniqueFrequencies(name, path)
# print(frequencies)