import time
import sqlite3

conn= sqlite3.connect("kartik.db") #connect to db
cursor = conn.cursor()  # create cursor


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
    tword = str(input('add the replace word\n'))
    e2t[eword] = tword
    
p = "else if(res.search("
p2 = ")!=-1){"
p3 = "\nres = res.replace("
p4 = ");\n}"

# show the keys and values  
vals = list(e2t.values())

dick = open(timestr+'.txt', 'a+') #open the file, clears previous data
for i in e2t:
    print(p+'"'+i+'"'+p2+''+p3+'"'+i+'","'+vals[count]+'"'+p4)
    
    dick.write(p+'"'+i+'"'+p2+''+p3+'"'+i+'","'+vals[count]+'"'+p4) #each time it appends new line to the old.
    cursor.execute('INSERT INTO bangla(broken, fixed) VALUES(?, ?)', (i, vals[count]))
    count = count +1
conn.commit()
dick.close() #You must close file. 
   
    
    


    
        

