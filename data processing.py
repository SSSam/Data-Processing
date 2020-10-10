 ### Samuel Jen


def read_string_list_from_file(the_file):
    fileRef = open(the_file,"r")      # opening file to be read
    localList_ofstrings=[]            # new list being constructed 
    
    for line in fileRef:
        string = line[0:len(line)-1]  # -1 to eliminate trailing '\n'
                                      # of each line           
        localList_ofstrings.append(string)      # adds string (line) to list
        
    fileRef.close()  
    #........
    print ("\n JUST TO TRACE, the list OF STRINGS is:\n")
    print(localList_ofstrings)
    
    #print("\n TRACE printing input file one STRING per line\n")
    #for element in localList_ofstrings:
    #    print (element)  # element is a string for one student
    #........
    return localList_ofstrings

def write_perstudent_to_file(lout_Strings,the_file):
    fileRef = open(the_file,"w") # opening file to be written
    for line in lout_Strings:
        fileRef.write(line)                  
    fileRef.close()
    return
def opening():
    #recieve the user's needs of comparing time
    print('''
    WELCOME to Preferences and Similarities system! 
     ============================================================ 

    This system will process data from the file: IN_all_data.txt
      (the file with that exact name needs to be in this folder!!!) 

    The file has answers of students opinions
      from 1 - strongly disagree  to 5- strongly agree

    The system will produce:
      - an output file with avgs per student: OUT_perstudent.csv
      - several statistics

    You will also be able to check if pairs of students are similar
    ''')
    while True:
        maxpair=input("Maximum number of pairs ==> ")
        if maxpair.isdigit():
            break
        else:
            print("What you provided is not an integer  number, please re-type")
    print('''
    Initial processing ...
    ''')
    return maxpair

def printcontinue():
    #another print that report some part of the information
    print('''
Processing all students' responses  ...


All students' responses have been processed ...


 SOME STATS!! 
 ============ 

The input file had responses from:'''+ str(studs)+''' students
Each student responded to: '''+ str(nqns)+''' questions
The maximum agrees (response 4 or 5) in a student was: '''+str(countmax)+'''

The averages per question were: 
question num - average''')

def onestringperline(the_list):
    #print one string per line to let the user can review the data easier
    print("now printing one STRING per line \n")
    for i in range(len(the_list)):
        onestring=str(the_list[i])
        print(onestring+"\n")
    return 

def onestudentperline(the_list, name_list):
    print("TRACE printing one STUDENT (name and LIST responses) per line")
    i=0
    cresp=0
    while i in range(0,len(the_list)):
        print(name_list[i]+" -- "+ str(resp[cresp:(cresp+nqns)]))
        i=i+1
        cresp=cresp+nqns
    return

def making_name_list(the_list):
    name_string=""
    for i in range(len(the_list)):
        name_string+=str((the_list[i].split()[0]))+" "
#use the split to only concatenate the name from the list of string
    name_list=list(name_string.split(" "))[:-1]
    print(name_list)
    return name_list

def alltheresp(the_list):
#use this function to list out all the resp to have an easier acess for the algorithm 
    resp=[]
    for k in range(len(the_list)):
        for i in range(len(the_list[k])):
            if the_list[k][i].isdigit():
                   resp+=(the_list[k][i])
    for i in range(len(resp)):
        resp[i]=int(resp[i])
    resp_string=str(resp)
    return resp

def findmaxaggree(the_list, resp, nqns):
    #create a list to count how many 4s and 5s a person resp
    maxcount=0
    countmax=0
    countmaxlst=[]
    for j in range(0,studs):
        indlst=resp[j*nqns:j*nqns+nqns]
        for k in range(nqns):
            if indlst[k]>=4:
                countmax+=1
        countmaxlst+=[countmax]
        countmax=0
    #calculate and find the maxium in the list
    j=0
    maxcount=0
    while j < len(countmaxlst):
        if countmaxlst[j]< maxcount:
            maxcount=maxcount
        elif countmaxlst[j]>maxcount:
            maxcount=int(countmaxlst[j])
        j=j+1
    return maxcount

def qna(nqns,studs,resp):
    #question and average calculating
    i=0
    avelst=[]
    oldaverage=0
    while i < nqns:
        total=0
        for x in range(studs):
            total+=resp[i+x*nqns]
        newaverage=total/studs
        avelst+=[newaverage]
        print(i+1," - ",round(newaverage,2))
        i=i+1
    return avelst

def mostagreeq(avelst):
    #counting the response that has the most agree average
    i=0
    maxnum=0
    while i < len(avelst):
        if avelst[i]< maxnum:
            maxnum=maxnum
        elif avelst[i]>maxnum:
            maxnum=int(avelst[i])
        i=i+1
    return maxnum

def findmaq(nqns,studs, resp,maxnum):
    #finding the maxium averaged resp quesiton(s)
    i=0
    maq=''
    while i < nqns:
        total=0
        for x in range(studs):
            total+=resp[i+x*nqns]
        average=total/studs
        if int(average)==maxnum:
            maq+=str(i+1)+","
        i=i+1
    return 

maxpair=int(opening())
the_list=read_string_list_from_file("IN_all_data.txt")
onestring=onestringperline(the_list)
name_list=making_name_list(the_list)
resp=alltheresp(the_list)
studs=len(the_list)
nqns=int(len(resp)/len(the_list))
onestudentperline(the_list, name_list)
print("studs, nqns: ",studs, nqns)
countmax=findmaxaggree(the_list, resp,nqns)
printcontinue()
avelst=qna(nqns,studs,resp)
maxnum=mostagreeq(avelst)
maq=findmaq(nqns,studs, resp,maxnum)

#coming to the next section.

print("The most agreed questions were: \n"+ str(maq)+"\n")
print('''
NOW... LET'S SEE SIMILARITIES BETWEEN PAIRS OF STUDENTS!!... \n
============================================================ \n
You can check up to '''+str(maxpair)+" pairs!!" )
#We have already asked the user how many pairs they wanna ask
pairs=0
while pairs< int(maxpair):
    if pairs==0:
        msg="Please provide the first name in the pair (or END to finish)==> "
    elif pairs== (maxpair-1):
        msg="One last pair!! Provide the first name in the pair (or END to finish)==> "
    else:
        msg="Another pair? provide the first name (or END to finish)==> "
    first= input(msg)
    if first=="END":
        print("***** Ok, I see that you do not want to consult any pairs... ")
        break   #ending the loop can only happen in the first input
    second= input ("Please provide the second name in the pair ==>")
    if first not in name_list or second not in name_list:
        print("** Sorry! The name is not in the data")
        pairs=pairs+1 #This will allow the loop to continue running, yet it won't proceed the following
    else:
        data1=[]    #store the data that we need so that we can just compare both og them easily
        data2=[]
        for i in range(len(name_list)):
            if first==name_list[i]:
                data1=resp[i*nqns:i*nqns+nqns]
            if second==name_list[i]:
                data2=resp[i*nqns:i*nqns+nqns]
            if first==second:
                data1==data2
        # Here is the loop to compare the similarity
        sim=0
        for i in range(nqns):
            if data1[i]==data2[i]:
                sim+=1
        #Respond to how similar 2 users are
        print(first+" and "+second+ " have "+str(sim)+" questions out of "+ str(nqns)+" responded the same.")
        percentage=(sim/nqns)*100
        if percentage<10:
            print(first+" and "+second+ " have nothing in common")
        elif percentage < 50:
            print(first+" and "+second+ " have just few opinions in common (<50%)!")
        elif percentage >50 and percentage<70:
            print(first+" and "+second+ " have about half opinions in common")
        elif percentage> 90:
            print (first+" and "+second+ " have a lot in common (>90%)!")
        pairs=pairs+1
if pairs==int(maxpair):
    #Ending the loop differently based on how many times the user has been tried
    print("***** Sorry you cannot check more pairs.. you reached the maximum: "+ str(maxpair)+" !")
print("Output file being saved ... \n TRACE list of strings ready to save to output file, one per line")
indresp=[]
lout_string=[]
for i in range(len(name_list)):
    total=0
    indresp=resp[i*nqns:i*nqns+nqns]
    for k in range(nqns):
        total+=indresp[k]
    lout_string+=[name_list[i]+", "+str(round(total/nqns, 4))+" \n"]
write_perstudent_to_file(lout_string, "OUT_perstudent.csv")
