#!/usr/bin/env python
# coding: utf-8

# ## 성적관리 프로그램

# In[ ]:


## show, search, changescore, searchgrade, add, remove, quit


# In[34]:


fr = open('students.txt', "r")
stu_list = list()

while True:
    data = fr.readline()
    if data =="":
        break
    else:
        data = data.split()
        stu_list.append(data)

for i in range(len(stu_list)):
    avg = ((int(stu_list[i][3]))+(int(stu_list[i][4])))/2
    stu_list[i].append(avg)
    
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    stu_list[i].append(grade)


for i in range(len(stu_list)):
    c=stu_list[i][1]+" "+stu_list[i][2]
    stu_list[i].pop(2)
    stu_list[i][1]=c
    stu_list[i][5]=str(stu_list[i][5])

stu_list.sort(key=lambda e : e[4], reverse=True)
import copy

def show_function(stu_list):
    print("Student \t Name \t\t Midterm \t Final \t Average  Grade")
    print("--------------------------------------------------------------------------")
    stu_list.sort(key=lambda e : e[4], reverse=True)

    for i in range(len(stu_list)):
        stu_list[i][5]=str(stu_list[i][5])
        print("%s \t%s \t%s \t\t %s \t %s \t   %s"%(stu_list[i][0],stu_list[i][1],stu_list[i][2],stu_list[i][3],stu_list[i][4],stu_list[i][5]))

def search_function(stu_list):
    k = 0
    idx = input("Student ID: ") #ID 입력
    
    for i in range(len(stu_list)):
        if idx in stu_list[i][0]: #입력된 ID가 기존 stu_list에 있을 때
            print("Student \t Name \t\t Midterm \t Final \t Average  Grade")
            print("--------------------------------------------------------------------------")
            print("%s \t%s \t%s \t\t %s \t %s \t   %s"%(stu_list[i][0],stu_list[i][1],stu_list[i][2],stu_list[i][3],stu_list[i][4],stu_list[i][5])) #id가 포함된 행을 출력한다
        else:
            k+=1#입력된 ID가 stu_list에 없을 때
    if k == len(stu_list):
        print ("NO SUCH PERSON.") #해당 문구를 출력한다
        
def changescore_function(stu_list):
    new_stu_list = copy.deepcopy(stu_list)
    idx = input("Student ID: ") #ID 입력
    k = 0
    for i in range(len(stu_list)):
        if idx in stu_list[i][0]: #입력된 ID가 기존 stu_list에 있을 때
            checking = input("Mid/Final: ") #Mid/Final 치는 란 입력
            #만약 Mid/Final 나옴 >> if mid: 해당 mid 점수 행을 선택
            #or if final: 해당 final 점수 행 선택 
            
            if checking == 'mid':
                new_s = int(input("new score : "))
                if new_s > 100:
                    pass
                else:
                    stu_list[i][2]=new_s
                    new_avg = ((int(stu_list[i][2]))+(int(stu_list[i][3])))/2
                    stu_list[i][4]=new_avg

                    if new_avg >= 90:
                        new_grade = "A"
                    elif new_avg >= 80:
                        new_grade = "B"
                    elif new_avg >= 70:
                        new_grade = "C"
                    elif new_avg >= 60:
                        new_grade = "D"
                    else:
                        new_grade = "F"

                    stu_list[i][5]=new_grade

                    print("Student \t Name \t\t Midterm \t Final \t Average  Grade")
                    print("--------------------------------------------------------------------------")
                    print("%s \t%s \t%s \t\t %s \t %s \t   %s"%(new_stu_list[i][0],new_stu_list[i][1],new_stu_list[i][2],new_stu_list[i][3],new_stu_list[i][4],new_stu_list[i][5]))
                    print("Score changed")
                    print("%s \t%s \t%s \t\t %s \t %s \t   %s"%(stu_list[i][0],stu_list[i][1],stu_list[i][2],stu_list[i][3],stu_list[i][4],stu_list[i][5]))

                
            elif checking == 'final':
                new_s = int(input("new score : "))
                if new_s >100:
                    pass
                else:
                    stu_list[i][3]=new_s
                    new_avg = ((int(stu_list[i][2]))+(int(stu_list[i][3])))/2
                    stu_list[i][4]=new_avg
                    if new_avg >= 90:
                        new_grade = "A"
                    elif new_avg >= 80:
                        new_grade = "B"
                    elif new_avg >= 70:
                        new_grade = "C"
                    elif new_avg >= 60:
                        new_grade = "D"
                    else:
                        new_grade = "F"
                    stu_list[i][5]=new_grade


                    print("Student \t Name \t\t Midterm \t Final \t Average  Grade")
                    print("--------------------------------------------------------------------------")
                    print("%s \t%s \t%s \t\t %s \t %s \t   %s"%(new_stu_list[i][0],new_stu_list[i][1],new_stu_list[i][2],new_stu_list[i][3],new_stu_list[i][4],new_stu_list[i][5]))
                    print("Score changed")
                    print("%s \t%s \t%s \t\t %s \t %s \t   %s"%(stu_list[i][0],stu_list[i][1],stu_list[i][2],stu_list[i][3],stu_list[i][4],stu_list[i][5]))

            elif checking not in ('mid','final'):
                pass

                #new stu_list의 평균과 grade를 바꿔줘야함
                #평균은 어떻게 구하지? 
                #new score 치는 란 입력
            
            #만약 Mid/Final 나옴 >> if mid: 해당 mid 점수 행을 선택
            #or if final: 해당 final 점수 행 선택 
            #이후 input new score 치는 란 나옴 >> 새점수 입력 >> 해당 mid or final에 새 점수 넣어서 해당 행 결과 출력. 
    
        else:
            k+=1
            
            if k == len(stu_list):
                print ("NO SUCH PERSON.")
                
def add_function(stu_list):
    k = 0
    new_idx = input("Student ID: ")
    for i in range(len(stu_list)):
        if new_idx in stu_list[i][0]:
                print("ALREADY EXISTS.")
        elif new_idx not in stu_list[i][0]:
            k+=1
            if k == len(stu_list):
                s_list = list()
                new_grade_add = ''
                new_name = input("name: ")
                new_ms = int(input("Midterm Score: "))
                new_fs =int(input("Final Score: "))
                new_avg_add = (new_ms+new_fs)/2
                print("Student added.")
                if new_avg_add >= 90:
                    new_grade_add = "A"
                elif new_avg_add >= 80:
                    new_grade_add = "B"
                elif new_avg_add >= 70:
                    new_grade_add = "C"
                elif new_avg_add >= 60:
                    new_grade_add = "D"
                else:
                    new_grade_add = "F"
                s_list.append(new_idx)
                s_list.append(new_name)
                s_list.append(new_ms)
                s_list.append(new_fs)
                s_list.append(new_avg_add)
                s_list.append(new_grade_add)
                stu_list.append(s_list)
    
def searchgrade_function(stu_list):
    k = 0
    grade_list = ['A','B','C','D','F']
    s_grade = input("Grade to search: ")
    for i in range(len(stu_list)):
        if s_grade not in grade_list:
            pass
        elif s_grade not in stu_list[i][5]:
            k+=1
            if k == len(stu_list):
                print("No Result")
        else:
            pass
    for i in range(len(stu_list)):
        if s_grade in stu_list[i][5]:
            k+=1
            if k == len(stu_list):
                print("Student \t Name \t\t Midterm \t Final \t Average  Grade")
                print("--------------------------------------------------------------------------")
    for i in range(len(stu_list)):
        if s_grade in stu_list[i][5]:
            print("%s \t%s \t%s \t\t %s \t %s \t   %s"%(stu_list[i][0],stu_list[i][1],stu_list[i][2],stu_list[i][3],stu_list[i][4],stu_list[i][5]))                                                            

def remove_function(stu_list):
    pop_list = list()
    new_stu_list = copy.deepcopy(stu_list)
    k = 0
    idx = input("Student ID: ")
        
    for i in range (len(new_stu_list)):
        if idx == new_stu_list[i][0]:
            r = i
        else:
            k+=1
    if k == len(new_stu_list):
        print("NO SUCH PERSON.")
    else:
        stu_list.pop(r)
        print ("Student removed.")

          

def quit_function(stu_list):
    
    s_data = input("Save data?[yes/no]: ")
    if s_data == 'yes':
        new_file = input("File name: ")
        fw = open ("%s"%new_file,"w")
        stu_list.sort(key=lambda e : e[4], reverse=True)
        for i in range (len(stu_list)):
            x = list()
            x.append(stu_list[i][0])
            x.append(stu_list[i][1])
            x.append(str(stu_list[i][2]))
            x.append(str(stu_list[i][3]))
            y = '\t'.join(x)+'\n'
            fw.write(y)
        fw.close()
    elif s_data == 'no':
        pass
            
while True:
    
    command = input("# ")
    if command == "show":
        show_function(stu_list)
    elif command == "search":
        search_function(stu_list)
    elif command == "changescore":
        changescore_function(stu_list)
    elif command == "add":
        add_function(stu_list)
    elif command == "searchgrade":
        searchgrade_function(stu_list)
    elif command == "remove":
        if len(stu_list) == 0:
            print("List is empty.")
            pass
        remove_function(stu_list)
    elif command == "quit":
        quit_function(stu_list)
        break
    else:
        print("wrong input!")
        
fr. close()


# In[ ]:





# In[30]:


stu_list


# In[32]:


stu_list.pop(0)


# In[33]:


stu_list


# In[1]:


a = []
if not len(a):
    print("List is empty.")


# In[33]:


def quit_function(stu_list):
    s_data = input("Save data?[yes/no]: ")
    if s_data == 'yes':
        new_file = input("File name: ")
        fw = open ("%s"%new_file,"w")
        stu_list.sort(key=lambda e : e[4], reverse=True)
        for i in range (len(stu_list)):
            x = list()
            x.append(str(stu_list[i][0]))
            x.append(stu_list[i][1])
            x.append(str(stu_list[i][2]))
            x.append(str(stu_list[i][3]))
            y = '\t'.join(x)+'\n'
            fw.write(y)
        fw.close()
    elif s_data == 'no':
        pass
            
quit_function(stu_list)


# In[32]:


stu_list


# In[30]:


y


# In[ ]:




