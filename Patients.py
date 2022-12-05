

class Patients:
    def __init__(self,ID, Name, Diagnosis, Gender, Age):
        self.ID = ID 
        self.Name =Name 
        self.Diagnosis =Diagnosis 
        self.Gender =Gender 
        self.Age= Age 

    #Returning a string in the required format
    def formatPatientInfo(self):
        return self.ID+"_"+self.Name+"_"+self.Diagnosis+"_"+self.Gender+"_"+self.Age
    
    #Displaying patients info in the object
    def __str__(self):
        return f"{self.ID},{self.Name},{self.Diagnosis},{self.Gender},{self.Age}"



def readPatientsFile():

    #opening file patients.txt(You can edit the name of the file)
    try:
        patients=open("patients.txt","r")
        lst=patients.readlines()
        i=0
        while(i<len(lst)):
        
            #Creating a separate patient object for each patients by splitting the string on ";"
            p=Patients(lst[i].split("_")[0],lst[i].split("_")[1],lst[i].split("_")[2],lst[i].split("_")[3],lst[i].split("_")[4])
            patientslist.append(p)
            i=i+1

    except FileNotFoundError:
        print("File not found")
        pass

#Initializing patients list for use
patientslist=[]
readPatientsFile()


def enterPatientInfo():

    #Generating a unique number for ID of the patient
    flag=False 
    while (flag==False):
        IDa=1
        for i in patientslist:
            if(i.ID==str(IDa)):
                IDa=IDa+1
            else:
                flag=True

    ID=str(IDa)
    Name=input("Enter the name of Patient:")
    Diagnosis=input("Enter the Diagnosed disease:")
    Gender=input("Enter the Gender of the Patient:")
    Age=input("Enter the Age of the Patient:")
    Age=Age+"\n"
    p=Patients(ID,Name,Diagnosis,Gender,Age)
    return p
    



def searchPatientById():
    ID=input("Enter the ID of the Patient:")
    #Searching the entered ID in the patientslist
    for i in patientslist:
            if(i.ID==ID):
                return i
    return -1
    pass



def editPatientInfo():
    
    flag=False 
    IDa=input("Enter the ID of the Patient:")

    #Searching and Editing the patient info if found
    for i in range(len(patientslist)):
        if(patientslist[i].ID==IDa):
            ID=str(IDa)
            Name=input("Enter the name of Patient:")
            Diagnosis=input("Enter the Diagnosed disease:")
            Gender=input("Enter the Gender of the Patient:")
            Age=input("Enter the Age of the Patient:")
            Age=Age+"\n"
            patientslist[i]=Patients(ID,Name,Diagnosis,Gender,Age)
    return -1
    
    pass


def displayPatientsList():

    print("-------------------------------------------------------")
    print("                    PATIENTS LIST                      ")
    print("-------------------------------------------------------")
    
    table=[]
    table.append(["ID","Name","Diagnosis","Gender","Age"])
    for i in patientslist:
        table.append([i.ID,i.Name,i.Diagnosis,i.Gender,i.Age])

    #Using Format function for tabular form
    for i in table:
        print("{: <7} {: <15} {: <15} {: <10} {: <7}".format(*i))
    



def writePatientsListToFile():
    lst=[]
    lst.append("")
    for i in patientslist:
        lst.append(i.formatPatientInfo())
    f=open("patients.txt","w")
    f.writelines(lst)
    f.close
    pass



def addPatientToList():
    patientslist.append(enterPatientInfo())
    pass

def patientsMenu():
    flag=False
    while(flag==False):
        print("---------------------------")
        print("     Patients Section      ")
        print("---------------------------")
        print("1. Add a new Patient.")
        print("2. Search Patient by ID.")
        print("3. Edit Patient info.")
        print("4. Add Patient to list.")
        print("5. Display Patients list.")
        print("6. Write Patientslist to file.")
        print("7. Quit")
        op=input("\nEnter your option:")
        if(op=="1"):
            enterPatientInfo()
        elif(op=="2"):
            print(searchPatientById())
        elif(op=="3"):
            editPatientInfo()
        elif(op=="4"):
            addPatientToList()
        elif(op=="5"):
            displayPatientsList()
        elif(op=="6"):
            writePatientsListToFile()
        elif(op=="7"):
            flag=True

patientsMenu()