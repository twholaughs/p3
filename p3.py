
import csv
import matplotlib.pyplot as plt




def Read_Csv_File(FileName):
    Data = []
    File = open(FileName,"r")
    Read_Csv = csv.reader(File)
    
    for i in Read_Csv:
        Data.append(i)
    return Data

def Write_Csv_File(data,FileName):
    File = open(FileName,"w",newline="")
    Write_Csv = csv.writer(File)

    for row in data:
        Write_Csv.writerow(row)

def menu():

    print("*"*20)
    print("1. Display avg scores of students over the 12 months")
    print("2. Display students' score for specific month")
    print("3. Add new score which is the avg of old score and input score")
    print("4. Quit")
    print("*"*20)

    
    


def Choice1(d):
    xaxisdata=[]
    yaxisdata=[]
    xaxis="students"
    yaxis="score"


    for i in d[1:]:
        xaxisdata.append(i[0])
        ytotal=0
        for y in i[1:]:
            ytotal+=float(y)
        yaxisdata.append(ytotal/12)
    
    PointX = range(len(xaxisdata))
    plt.figure(figsize=(15,10))
    plt.subplot(1,1,1)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.xticks(PointX,xaxisdata)
    plt.bar(PointX,yaxisdata,color='r',label=yaxis,width=0.5)
        


    plt.show()

def Choice2(d):
    month=input("Enter Month(Jan,Feb,etc): ")
    index=0
    for i in range(len(d[0])):
        if d[0][i]==month:
            index=i
    xaxisdata=[]
    yaxisdata=[]
    xaxis="students"
    yaxis="score"

    for i in d[1:]:
        xaxisdata.append(i[0])
        yaxisdata.append(float(i[index]))

    PointX = range(len(xaxisdata))
    plt.figure(figsize=(15,10))
    plt.subplot(1,1,1)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.xticks(PointX,xaxisdata)
    plt.bar(PointX,yaxisdata,color='r',label=yaxis,width=0.5)
        


    plt.show()

def Choice3(d,f):

    name= input("Enter student name: ")
    month= input("Enter month:")
    score= int(input("Enter new score: "))
    newscore=0

    index1=0
    index2=0

    months=d[0]

    for i in range(len(months)):
        if months[i]==month:
            index1=i

    for j in range(len(d)):
        if d[j][0]==name:
            index2=j
            newscore= int(d[j][index1])+score

    d[index2][index1]=str(newscore/2)

    Write_Csv_File(d,f)




    

def main():
    while True:
        while True:
            try:
                filen=input("Enter file name: ")
                Data = Read_Csv_File(filen)
                break
            except Exception as e:
                print(e)

        menu()    
        userChoice=input("Enter choice: ")

        if userChoice=="1":
            Choice1(Data)
        elif userChoice=="2":
            Choice2(Data)
        elif userChoice=="3":
            Choice3(Data,filen)
        elif userChoice=="4":
            break
        else:
            print("Invalid input")

if __name__=="__main__":
    main()
