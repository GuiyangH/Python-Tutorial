#########################
##                    ###
##    Phys 236-Tut    ###
##                    ###
##   2016/11/28       ###
#########################

##1. Open/Read/Create a file

#f = open('workf.txt','r') #'r'--'read', this will give an error because there is no such file

f = open('workf.txt','w') #'w'--'write', you cannot read the file, but write it(create on if not exist)
          #Caution that everytime this runs, it overwrite previous file(Erase everything)

#f = open('workf.txt','r+') #'r+' is for read and write together, so more compatable
                    # but it gives trouble sometimes.
# f.close() #be sure to close it.(or the file will be not notepad-table)

##2. Write Something

f.write('This is first line')
f.write('Why this is not second line\n')
f.write('because we not n it')

f.write('\n')
alst = [[1,2,3,4,5,6,7],[2,3,4]]
#f.write(alst) #this not works because they are not string
f.write(str(alst))
f.close()


##3. Readfile
f = open('workf','r')
print f.read()
print f.readline() # note there will be no line to read further because f.read
                   # already read it all.

#read line 1-by-1
for line in f:
    print line
f.close()
