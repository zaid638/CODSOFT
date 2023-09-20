from itertools import count
import random
import select
import sys
from tracemalloc import start
from tkinter import Tk,Label,Button,Radiobutton,Frame,IntVar,StringVar,PhotoImage,Canvas,font,Scrollbar,RIGHT,CENTER,Y,BOTH,Listbox,END,Entry

class Question:
    def __init__(self):
        self.question = [None, [], None]
    
    def setQuestion(self,qs):
        self.question[0] = qs

    def setOptions(self,o1,o2,o3,o4):
        self.question[1].append(o1)
        self.question[1].append(o2)
        self.question[1].append(o3)
        self.question[1].append(o4)

    def setAnswer(self,a):
        self.question[2] = a

    def printQuestion(self):
        print(self.question[0])
        print('a)',self.question[1][0])
        print('b)',self.question[1][1])
        print('c)',self.question[1][2])
        print('d)',self.question[1][3]) 
    
    def printCorrectAnswer(self):
        return self.question[1][self.question[2]-1]
    
    def printQuestionWithAnswer(self):
        print(self.question[0])
        print('a)',self.question[1][0])
        print('b)',self.question[1][1])
        print('c)',self.question[1][2])
        print('d)',self.question[1][3])
        print('Correct Answer is: ',self.question[1][self.question[2]-1])

    def checkAnswer(self, ans):
        key={'a':1,'b':2,'c':3, 'd':4}
        if self.question[2]==key[ans]:
            return True
        else:
            return False


class QuestionDB:
    def __init__(self):
        self.loadQuestionList()

    def addQuestion(self):
        q = Question()
        x = input('\nEnter Question: ')
        q.setQuestion(x)
        x1 = input('Enter option 1: ')
        x2 = input('Enter option 2: ')
        x3 = input('Enter option 3: ')
        x4 = input('Enter option 4: ')
        q.setOptions(x1,x2,x3,x4)

        while True:
            try:
                x5 = int(input('Enter answer(1,2,3 or 4): '))
                if 1 > x5 > 4:
                    raise ValueError
            except ValueError:
                print('Enter valid option number!')
        
            else:
                q.setAnswer(x5)
                self.questionList.append(q.question)
                break
    
    def printQuestionList(self):
        try:
            if self.questionListObj == []:
                raise Exception
            else:
                ID = 1
                for question in self.questionListObj:
                    print('\nQID:',ID)
                    question.printQuestionWithAnswer()
                    ID += 1
        except:
            print('Not enough questions in question bank1!')



    def removeQuestion(self):
        try:
            Id = int(input('Entre QID to remove question: '))
            print('Please save the changes')
            return self.questionList.pop(int(Id)-1)
            QuestionDB.loadQuestionList(self)
        except:
            print('Invalid QID!')

        
    
    def saveQuestionList(self):
        f = open('QuestionsDB.txt','w')

        for qs in self.questionList:
            f.write(str(qs)+'\n')
        f.close()
        QuestionDB.loadQuestionList(self)

    def loadQuestionList(self):
        self.questionList = []
        self.questionListObj = []
        try:
            f = open('QuestionsDB.txt','r')
        except:
            return
        
        for line in f:
            question = eval(line)
            q = Question()
            q.setQuestion(question[0])
            q.setOptions(question[1][0],question[1][1],question[1][2],question[1][3])
            q.setAnswer(question[2])
            self.questionList.append(q.question)
            self.questionListObj.append(q)        
        f.close()
        
    

class GUIQG(Tk):
    def __init__(self):
        super().__init__()
        self.title('Quiz Game')
        self.minsize(550,150)

        self.QDB=QuestionDB()
        self.makeQuiz()
        self.mainInterface()
        #self.displayQuiz()

        self.mainloop()

    def makeQuiz(self):
        count = 0
        self.selectedQsList = []
        while True:
            try:
                n = random.choice(self.QDB.questionListObj)
            except:
                print('Not enough questions in question bank2!')
                break
            if n not in self.selectedQsList:
                self.selectedQsList.append(n)
                count += 1
            if count == 10:
                break


    def mainInterface(self):
        self.geometry("550x150+380+180")
        bg = PhotoImage(file = "Add_a_heading.png")   
        bg2 = PhotoImage(file = "Play2.png")    
        bg3 = PhotoImage(file = "manage.png")    
        l1=Label(self, image = bg)
        l1.place(x = 0,y = 0)
        b1 = Button( self, image = bg2, relief='flat', bd=0, command=self.subInterface)
        b1.place(x = 140, y = 90)
        b2 = Button( self, image = bg3, relief='flat', bd=0, command=self.Manage_int)
        b2.place(x = 280, y = 90)
        self.mainloop()

    def subInterface(self):
        self.geometry("650x200")
        bg = PhotoImage(file = "Add_a_heading3.png")   
        l3=Label(self, image=bg)
        l3.place(x = 0,y = 0)
        self.displayQuiz()


    def Manage_int(self):
        QDB=QuestionDB()
        count1 = 0
        entry_list = []
        def dltqs():
            def subdlt():
                dlt = dt_entry.get()
                QDB.questionList.pop(int(dlt)-1)
                dt_entry.delete(0, END)
                button1.destroy()
                dt_entry.destroy()
                l4.destroy()
                QDB.saveQuestionList()
                label=Label(f5, text='***SUCCESSFULLY DELETED***', font=('Bahnschrift SemiBold SemiConden',20), bg='#7696F3', foreground='#03723D')
                label.place(x = 180,y = 20)
                button2 = Button(f5, text='MAIN MENU', font=('Bahnschrift SemiBold SemiConden',20), bg='#7696F3', command=self.mainInterface)
                button2.place(x = 250,y = 70)

            f2.destroy()
            self.geometry("650x250")
            bg = PhotoImage(file = "Add_a_heading3.png")   
            l3=Label(self, image=bg)
            l3.place(x = 0,y = 0)
            f5 = Frame(self, width=650, height=150, bg='#7696F3')
            l4 = Label(f5, text='PLEASE ENTER QUESTION ID', font=('Bahnschrift SemiBold SemiConden',20), bg='#7696F3')
            l4.place(x = 180,y = 5)
            dt_entry = Entry(f5, width=30, font='arial 20', bd=0)
            dt_entry.place(x=10, y=70)
            dt_entry.focus()

            button1 = Button(f5, text='DELETE', font='arial 20 bold', width=10, bg='#5a95ff', fg='#fff', bd=0, command=subdlt)
            button1.place(x=450, y=65)           
            f5.place(x=0, y=50)
            self.mainloop()  

        def addqs():      
            def subadd():
                nonlocal count1
                qs = qs_entry.get()
                entry_list.append(qs)
                qs_entry.delete(0, END)
                button_list[count1].destroy()
                count1 += 1
                if count1 != 6:
                    addqs()
                else:
                    qs_entry.destroy()
                    q = Question()
                    q.setQuestion(entry_list[0])
                    q.setOptions(entry_list[1],entry_list[2],entry_list[3],entry_list[4])
                    q.setAnswer(int(entry_list[5]))
                    QDB.questionList.append(q.question)
                    QDB.saveQuestionList()
                    label=Label(f4, text='***SUCCESSFULLY SAVED***', font=('Bahnschrift SemiBold SemiConden',20), bg='#7696F3', foreground='#03723D')
                    label.place(x = 180,y = 20)
                    button = Button(f4, text='MAIN MENU', font=('Bahnschrift SemiBold SemiConden',20), bg='#7696F3', command=self.mainInterface)
                    button.place(x = 250,y = 70)
                    
            f2.destroy()
            self.geometry("650x250")
            bg = PhotoImage(file = "Add_a_heading3.png")   
            l3=Label(self, image=bg)
            l3.place(x = 0,y = 0)
            f4 = Frame(self, width=650, height=150, bg='#7696F3')

            button_list = ['ADD QS', 'OPT1', 'OPT2', 'OPT3', 'OPT4', 'ADD ANS']

            qs_entry = Entry(f4, width=30, font='arial 20', bd=0)
            qs_entry.place(x=10, y=5)
            qs_entry.focus()

            button_list[count1] = Button(f4, text=button_list[count1], font='arial 20 bold', width=10, bg='#5a95ff', fg='#fff', bd=0, command=subadd)
            button_list[count1].place(x=450, y=0)
            
            f4.place(x=0, y=50)
            self.mainloop()           


        def listqs():
            f2.destroy()
            self.geometry("650x250")
            bg = PhotoImage(file = "Add_a_heading3.png")   
            l3=Label(self, image=bg)
            l3.place(x = 0,y = 0)
            f3 = Frame(self, bg='#7696F3')
            listbox = Listbox(f3, font=('Bahnschrift SemiBold SemiConden',20), width=200, height=250, bg ='#7696F3')
            listbox.pack(side='left', fill=BOTH)

            scrollbar = Scrollbar(self)
            scrollbar.pack(side=RIGHT, fill=Y)
            try:
                if QDB.questionListObj == []:
                    raise Exception
                else:
                    ID = 1
                    for qs in QDB.questionListObj:
                        listbox.insert(END, '\n'+'QID:'+str(ID))
                        listbox.insert(END, str(ID)+') '+qs.question[0])
                        listbox.insert(END, 'a) '+qs.question[1][0])
                        listbox.insert(END, 'b) '+qs.question[1][1])
                        listbox.insert(END, 'c) '+qs.question[1][2])
                        listbox.insert(END, 'd) '+qs.question[1][3])
                        listbox.insert(END, 'Correct Answer is: '+qs.question[1][qs.question[2]-1])
                        ID += 1
            except:
                lid2 = Label(f3, text='Not enough questions in question bank!')
                lid2.pack()
            listbox.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=listbox.yview)
            button = Button(f3, text='MAIN MENU', font=('Bahnschrift SemiBold SemiConden',20), bg='#7696F3', command=lambda: [f3.destroy(), scrollbar.destroy(), self.mainInterface()])
            button.place(x = 487,y = 5)
            f3.pack()
            self.mainloop()

        self.geometry("650x250")
        bg = PhotoImage(file = "Add_a_heading3.png")   
        l3=Label(self, image=bg)
        l3.place(x = 0,y = 0)
        f2 = Frame(self, bg='#7696F3')
        font1 = font.Font(family='Bahnschrift SemiBold SemiConden', size=18)
        b1=Button(f2, width=18, text='LIST QUESTIONS', bg='#7696F3', font=font1, command=listqs)
        b1.pack(pady=7)
        b2=Button(f2, width=18, text='ADD QUESTIONS', bg='#7696F3', font=font1, command=addqs)
        b2.pack()
        b3=Button(f2, width=18,text='REMOVE QUESTIONS', bg='#7696F3', font=font1, command=dltqs)
        b3.pack(pady=7) 
        b4=Button(f2, width=18,text='MAIN MENU', bg='#7696F3', font=font1, command=lambda: [f2.destroy(),  self.mainInterface()])
        b4.pack()
        f2.pack(pady=5)
        self.mainloop()




    def displayQuiz(self):
        self.score=0
        for i in range(10):
            self.createFrame(self.selectedQsList[i],i)



    def createFrame(self,q,i):

        def checkans():
            font3 = font.Font(family='Bahnschrift SemiBold SemiConden', size=13)
            if q.checkAnswer(radioSelection.get()):
                lcheck = Label(f, text='*****Corrrect answer*****', bg='#7696F3', foreground='#03723D', font=font3)
            else:
                lcheck = Label(f, text='****Wrong answer!****\n'+'Correct answer is: '+q.printCorrectAnswer(), bg='#7696F3', foreground='#841010', font=font3)    
            lcheck.pack()   


        def nextClicked():
            if q.checkAnswer(radioSelection.get()):
                self.score+=1
            f.destroy()
            wait.set(1)
            
        def finishClicked():
            font4 = font.Font(family='Bahnschrift SemiBold SemiConden', size=15)
            nextClicked()
            self.geometry("550x150")
            bg = PhotoImage(file = "Add_a_heading2.png")   
            l1=Label(self, image=bg)
            l1.place(x = 0,y = 0)
            b1 = Button( self, text='MAIN MENU', font=('Bahnschrift SemiBold SemiConden',20), bg='#7696F3', bd=2, command=lambda: [lResult.destroy(), l2.destroy(), self.mainInterface()])
            b1.place(x = 200, y = 80)
            lResult=Label(self,text='You scored '+str(self.score)+' out of 10', bg='#7696F3', font=font4)
            lResult.pack()
            performance = ''
            if self.score < 5:
                performance = 'Poor'
            elif 5 <= self.score < 8:
                performance = 'Good'
            else:
                performance = 'Excellent'
            l2 = Label(self, text=str(performance)+' Performance', bg='#7696F3', font=font4)
            l2.pack()
            self.mainloop()
            
        self.geometry("680x250")
        f = Frame(self, bg='#7696F3')
        font1 = font.Font(family='Arial Rounded MT Bold', size=15)
        font2 = font.Font(family='Franklin Gothic Heavy', size=13)
        lQuestion=Label(f,text=q.question[0], bg='#7696F3', font=font1)
        lQuestion.pack()
        radioSelection=StringVar(f,' ') 
        rb1=Radiobutton(f,text=q.question[1][0],variable=radioSelection, value='a', command=checkans, bg='#7696F3', font=font2)
        rb1.pack()
        rb2=Radiobutton(f,text=q.question[1][1], variable=radioSelection, value='b', command=checkans, bg='#7696F3', font=font2)
        rb2.pack()
        rb3=Radiobutton(f,text=q.question[1][2], variable=radioSelection, value='c', command=checkans, bg='#7696F3', font=font2)
        rb3.pack()         
        rb4=Radiobutton(f,text=q.question[1][3], variable=radioSelection, value='d', command=checkans, bg='#7696F3', font=font2)
        rb4.pack()


        if i<9:
            button=Button(f,text='Next',command=nextClicked)
        else:
            button=Button(f,text='Finish',command=finishClicked)
        button.pack()
        f.pack()

        wait=IntVar()
        wait.set(0)
        button.wait_variable(wait)      



GUIQG()

###font_list###
#Arial Rounded MT Bold
#Bahnschrift SemiBold SemiConden
#Franklin Gothic Heavy
#Impact
#Rockwell Extra Bold