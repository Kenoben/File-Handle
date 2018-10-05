# -*- coding: cp1252 -*-
##################################################################################
######                                                                      ######
######         each task requires you to write a seperate function          ######
######     write your functions below that my code will use for each task   ######
######                                                                      ######
######          uncomment the lines of code with the function calls         ######
######                  for each Task to test your function                 ######
######                                                                      ######
##################################################################################


# Task 1: Write a function, printFile(filename), that prints the contents of
# file named “printFileExample.txt” to screen

def printFile(index):

    file = open(index,'r')
    filefact = file.read()
    print(filefact)
    file.close()

def sumColumn(index):
    sumofall = 0
    file = open(index,'r')
    for line in file:
        sumofall += int(line)
    file.close()
    return(sumofall)

def sumAll(index):
    sumofall = 0
    file = open(index,'r')
    for line in file:
        intlist = str.split(line)
        for x in range(len(intlist)):
            sumofall += int(intlist[x]) 
    file.close()
    return(sumofall)

def readColumn(index, collumn):
    Columnall = []
    file = open(index,'r')
    for line in file:
        strlist = str.split(line)
        Columnall.append(strlist[collumn] )
    file.close()
    return(Columnall)

def countWord(index, word):
    strlist = []
    total = 0
    word = " " + word + " "
    file = open(index,'r')
    for line in file:
        strlist.append(line)
    for y in range(len(strlist)):
        total += strlist[y].count(word)
    file.close()
    return(total)

def writeName(index, firstname, lastname):
    file = open(index,'w')
    file.write(firstname + " " + lastname)
    file.close
    
def writeColumn(index, list1):
    file = open(index,'w')
    file.write("")
    file.close
    file = open(index,'w+')
    for z in range(len(list1)):
        file.write(str(list1[z]) + "\n")

def filterFile(index, otherfile, word):
    strlist = []
    total = 0
    file = open(index,'r')
    file2 = open(otherfile, 'w+')
    for line in file:
        if line.count(word + " ") != 0:
            strlist.append(line)
    for a in range(len(strlist)):
        file2.write(strlist[a] + "\n")
        
        
    

    file.close()
    file2.close()
    return(total)



    


print ('Task 1: printFile(filename)')
printFile('printFileExample.txt')
print ('\n')


#################################################################################

# Task 2: Write a function, sumColumn(filename), that should read a file
# that has exactly one integer on each line and return the sum of these integers.
# Hint: You will read strings from the file, but want to sum integers.

print ('Task 2: print sumColumn(filename)')
print (str(sumColumn('sumColumnExample.txt')))
print ('\n')


#################################################################################

# Task 3: Write a function, sumAll(filename), that should read a file
# containing only integers and return the sum of all these integers.
# Hint: Use str.split() to split a line containing multiple integers.

print ('Task 3: print sumAll(filename)')
print (str(sumAll('sumAllExample.txt')))
print ('\n')


#################################################################################

# Task 4: Write a function, readColumn(filename, columnNo). The file
# named by filename should contain columns of integers separated by whitespace.
# The function should read the column number “columnNo”, convert it to
# integers and return it as a list. 

print ('Task 4: print readColumn(filename, columnNo)')
print (readColumn('readColumnExample.txt', 0))
print ('\n')


#################################################################################

# Task 5: Write a function, countWord(filename, word), that should count
# and return how many times word appears in file called "zenOfPython.txt"

print ('Task 5: countWord(filename, word)')
print (countWord('zenOfPython.txt', 'the')) ##okay so this counts the "there" as the word the, inst against the rules tho
print ('\n')


#################################################################################

# Task 6: Write a function, writeName(filename, firstName, lastName),
# that writes the full name consisting of firstName and lastName to
# a single line in a file called "filename".

print ('Task 6: writeName(filename, firstName, lastName)')
writeName('writeNameTest.txt', 'Charles', 'Darwin')
printFile('writeNameTest.txt')
print ('\n')


#################################################################################

# Task 7: Write a function, writeColumn(filename, column), that writes
# the elements of the list column to a file called "filename". There
# should be one element per line.

print ('Task 7: writeColumn(filename, column)')
writeColumn('writeColumnTest.txt', [1, 1, 2, 3])
printFile('writeColumnTest.txt')
print ('\n')


#################################################################################

# Task 8: Write a function, filterFile(fromFilename, toFilename, word).
# It should copy all lines that contain the word word from file "fromFilename"
# to file "toFilename".
print ('Task 8: filterFile(fromFilename,toFilename,word)')
filterFile('filterFileExample.txt', 'filterFileTest.txt', 'line')
printFile('filterFileTest.txt')
print ('\n')


#################################################################################
