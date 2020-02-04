import time
import sqlite3
import csv

#Sqlite connection and cursor
conn= sqlite3.connect("kartik.db") #connect to db
cursor = conn.cursor()  # create cursor

#get the count of tables with the name
cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='bangla' ''')


#if the count is 1, then table exists

if cursor.fetchone()[0]==1 : 
	print('SQL: OK\nTable: OK\n\n\n')
else :
       cursor.execute('CREATE TABLE bangla (ID INTEGER PRIMARY KEY, broken TEXT, fixed TEXT)')
       print('SQl table has been created.\n\n\n')
       



timestr = time.strftime("%Y%m%d") #You must use timestr not datetime.

e2t = dict()                #create a dictionary
count = 0 # create a var
while True: # use while for taking multiple values
    #try:
        #dick = open('dic.txt', 'w') #try opening the txt file
    #except:
        #print('Couldnt find a dictionary file')
       # break
    eword = input('add bangla words or Break\n')
    if(eword == 'break'):
        break
    elif(eword ==''):
        print("Input can't be empty")
        exit()
    tword = str(input('add the replace word\n'))
    e2t[eword] = tword
    


# show the keys and values  
vals = list(e2t.values())


dick = open(timestr+'.txt', 'a+') #open the file, clears previous data

for i in e2t:
    #SQLite
    cursor.execute('INSERT INTO bangla(broken, fixed) VALUES(?, ?)', (i, vals[count])) # i and Vals vallues will be stored in sqlite
    count = count +1
    
#CSV    
with open(timestr+'.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, e2t.keys())
    w.writeheader()
    w.writerow(e2t)

    
conn.commit()    
dick.write(str(e2t)) #each time it appends new line to the old.
dick.close() #You must close file

                   
   
    
    


    
        

