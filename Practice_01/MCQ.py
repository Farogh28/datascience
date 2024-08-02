from tkinter import *
# import mysql.connector

# conn= mysql.connector.connect(
#     host= "localhost",
#     user= "root",
#     password= 'abc@123',
#     database= "db"
# )
# # print('connected...')
# a= conn.cursor()
# a.execute("create database db")

# a.execute("create table new(id int(20), name varchar(255), lang varchar(255))")

# a.execute("insert into new(id, name, lang) values (1, 'abc','core py')")
# conn.commit()

# sql= "insert into new(id, name, lang) value (%s, %s, %s)"
# val= [(2,'xyz', 'core py'),
#       (3,'ghi', 'py ai'),
#       (4, 'jkl', 'py ds')]

# a.executemany(sql, val)
# conn.commit()

# a.execute('select * from new')
# for i in a:
#     print(i)





questionnum = 1
score = 0
correct_n = 0
incorrect_n = 0

root = Tk()

def main_game():
    global root



    app_width = 600
    app_height = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    app_x = (screen_width / 2) - (app_width / 2)
    app_y = (screen_height / 2) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(app_x)}+{int(app_y)}')
    root.title('MCQ')
#     root.iconbitmap('mcqicon.ico')
    root.configure(bg='lightblue')
    root.resizable(False, False)
    root.overrideredirect(True)
    root.wm_attributes("-transparentcolor", "grey")


main_game()

frame_photo = PhotoImage(file="mcqframe.png")
frame_label = Label(root,
                    border=0,
                    bg='grey',
                    image=frame_photo,
                    )

mcq_photo = PhotoImage(file='mcq.png')
mcq_label = Label(root,
                  border=0,
                  image=mcq_photo,
                  bg='#AA55FF',
                  )

minimize_photo = PhotoImage(file='minimizebtn.png')
minimize_label = Label(root,
                       border=0,
                       image=minimize_photo,
                       bg='#AA55FF',
                       )

exit_photo = PhotoImage(file='closebtn.png')
exit_label = Label(root,
                   border=0,
                   image=exit_photo,
                   bg='#AA55FF',
                   )

mainmenu_photo = PhotoImage(file='mainmenu.png')
mainmenu_label = Label(root,
                       border=0,
                       image=mainmenu_photo,
                       bg='#A6FFC9',
                       )

start_photo = PhotoImage(file='startbtn.png')
start_label = Label(root,
                    border=0,
                    image=start_photo,
                    bg='#A6FFC9',
                    )

hs_photo = PhotoImage(file='hsbutton.png')
hs_label = Label(root,
                 border=0,
                 image=hs_photo,
                 bg='#A6FFC9',
                 )

exitf_photo = PhotoImage(file='exitbtn.png')
exitf_label = Label(root,
                    border=0,
                    image=exitf_photo,
                    bg='#A6FFC9',
                    )

yuvraj_photo = PhotoImage(file='yuvraj.png')
yuvrajlabel = Label(root,
                    border=0,
                    image=yuvraj_photo,
                    bg='#A6FFC9',
                    )


def nothing():
    pass


def clearwin():
    for child in root.winfo_children():
        if child == frame_label or child == exit_label or child == minimize_label or child == mcq_label or child == yuvrajlabel:
            pass
        else:
            child.destroy()


def exit_f():
    root.quit()


def minimize_f():
    root.overrideredirect(False)
    root.iconify()


def maximize_f():
    root.update_idletasks()
    root.overrideredirect(True)


def next_f():
    global questionnum
    global questionnumber_label
    global next_photo
    global next_label

    questionnum = questionnum + 1

    next_label.place(x=320, y=390)


def mcqframe():
    global mtitle_photo
    global mtitle_label
    global questionnumber_label
    global question_photo
    global question_label
    global question_frame
    global option1_photo
    global option2_photo
    global option3_photo
    global option4_photo
    global option1_label
    global option2_label
    global option3_label
    global option4_label
    global o1_frame
    global o2_frame
    global o3_frame
    global o4_frame
    global next_photo
    global next_label
    global questionnum

    clearwin()

    mtitle_photo = PhotoImage(file='mtitle.png')
    mtitle_label = Label(root,
                         border=0,
                         image=mtitle_photo,
                         bg='#A6FFC9',
                         )
    mtitle_label.place(x=114, y=70)

    question_photo = PhotoImage(file='question.png')
    question_label = Label(root,
                           border=0,
                           image=question_photo,
                           bg='#A6FFC9',
                           )
    question_label.place(x=50, y=120)

    question_frame = Frame(root,
                           width=480,
                           height=80,
                           bg='#FF7979',
                           )
    question_frame.place(x=60, y=130)

    option1_photo = PhotoImage(file='option.png')
    option1_label = Label(root,
                          border=0,
                          image=option1_photo,
                          bg='white',
                          )
    option1_label.place(x=50, y=240)

    o1_frame = Frame(root,
                     width=210,
                     height=30,
                     bg='#4870FF',
                     )
    o1_frame.place(x=60, y=250)

    option2_photo = PhotoImage(file='option.png')
    option2_label = Label(root,
                          border=0,
                          image=option2_photo,
                          bg='#A6FFC9',
                          )
    option2_label.place(x=320, y=240)

    o2_frame = Frame(root,
                     width=210,
                     height=30,
                     bg='#4870FF',
                     )
    o2_frame.place(x=330, y=250)

    option3_photo = PhotoImage(file='option.png')
    option3_label = Label(root,
                          border=0,
                          image=option3_photo,
                          bg='#A6FFC9',
                          )
    option3_label.place(x=50, y=320)

    o3_frame = Frame(root,
                     width=210,
                     height=30,
                     bg='#4870FF',
                     )
    o3_frame.place(x=60, y=330)

    option4_photo = PhotoImage(file='option.png')
    option4_label = Label(root,
                          border=0,
                          image=option4_photo,
                          bg='#A6FFC9',
                          )
    option4_label.place(x=320, y=320)

    o4_frame = Frame(root,
                     width=210,
                     height=30,
                     bg='#4870FF',
                     )
    o4_frame.place(x=330, y=330)

    next_photo = PhotoImage(file='nextbtn.png')
    next_label = Label(root,
                       border=0,
                       image=next_photo,
                       bg='#A6FFC9',
                       )
    next_label.place(x=320, y=390)

    questionnumber_label = Label(root,
                                 border=0,
                                 bg='#A6FFC9',
                                 text=f'Question: {questionnum}/25',
                                 font=("Regular", 20)
                                 )
    questionnumber_label.place(x=60, y=400)


def highscore():
    print("highscore")


def o1_correct():
    o1.bind("<Button>", lambda e: correct())
    o1_frame.bind("<Button>", lambda e: correct())
    option1_label.bind("<Button>", lambda e: correct())

    o2.bind("<Button>", lambda e: incorrect())
    o2_frame.bind("<Button>", lambda e: incorrect())
    option2_label.bind("<Button>", lambda e: incorrect())

    o3.bind("<Button>", lambda e: incorrect())
    o3_frame.bind("<Button>", lambda e: incorrect())
    option3_label.bind("<Button>", lambda e: incorrect())

    o4.bind("<Button>", lambda e: incorrect())
    o4_frame.bind("<Button>", lambda e: incorrect())
    option4_label.bind("<Button>", lambda e: incorrect())


def o2_correct():
    o1.bind("<Button>", lambda e: incorrect())
    o1_frame.bind("<Button>", lambda e: incorrect())
    option1_label.bind("<Button>", lambda e: incorrect())

    o2.bind("<Button>", lambda e: correct())
    o2_frame.bind("<Button>", lambda e: correct())
    option2_label.bind("<Button>", lambda e: correct())

    o3.bind("<Button>", lambda e: incorrect())
    o3_frame.bind("<Button>", lambda e: incorrect())
    option3_label.bind("<Button>", lambda e: incorrect())

    o4.bind("<Button>", lambda e: incorrect())
    o4_frame.bind("<Button>", lambda e: incorrect())
    option4_label.bind("<Button>", lambda e: incorrect())


def o3_correct():
    o1.bind("<Button>", lambda e: incorrect())
    o1_frame.bind("<Button>", lambda e: incorrect())
    option1_label.bind("<Button>", lambda e: incorrect())

    o2.bind("<Button>", lambda e: incorrect())
    o2_frame.bind("<Button>", lambda e: incorrect())
    option2_label.bind("<Button>", lambda e: incorrect())

    o3.bind("<Button>", lambda e: correct())
    o3_frame.bind("<Button>", lambda e: correct())
    option3_label.bind("<Button>", lambda e: correct())

    o4.bind("<Button>", lambda e: incorrect())
    o4_frame.bind("<Button>", lambda e: incorrect())
    option4_label.bind("<Button>", lambda e: incorrect())


def o4_correct():
    o1.bind("<Button>", lambda e: incorrect())
    o1_frame.bind("<Button>", lambda e: incorrect())
    option1_label.bind("<Button>", lambda e: incorrect())

    o2.bind("<Button>", lambda e: incorrect())
    o2_frame.bind("<Button>", lambda e: incorrect())
    option2_label.bind("<Button>", lambda e: incorrect())

    o3.bind("<Button>", lambda e: incorrect())
    o3_frame.bind("<Button>", lambda e: incorrect())
    option3_label.bind("<Button>", lambda e: incorrect())

    o4.bind("<Button>", lambda e: correct())
    o4_frame.bind("<Button>", lambda e: correct())
    option4_label.bind("<Button>", lambda e: correct())


def correct():
    global score
    global mtitle_photo
    global mtitle_label
    global correct_n

    score = score + 4
    correct_n = correct_n + 1

    mtitle_photo = PhotoImage(file='mtitlec.png')
    mtitle_label = Label(root,
                         border=0,
                         image=mtitle_photo,
                         bg='#A6FFC9',
                         )
    mtitle_label.place(x=229, y=70)

    o1.bind("<Button>", lambda e: nothing())
    o1_frame.bind("<Button>", lambda e: nothing())
    option1_label.bind("<Button>", lambda e: nothing())

    o2.bind("<Button>", lambda e: nothing())
    o2_frame.bind("<Button>", lambda e: nothing())
    option2_label.bind("<Button>", lambda e: nothing())

    o3.bind("<Button>", lambda e: nothing())
    o3_frame.bind("<Button>", lambda e: nothing())
    option3_label.bind("<Button>", lambda e: nothing())

    o4.bind("<Button>", lambda e: nothing())
    o4_frame.bind("<Button>", lambda e: nothing())
    option4_label.bind("<Button>", lambda e: nothing())

    next_f()


def incorrect():
    global mtitle_photo
    global mtitle_label
    global incorrect_n

    incorrect_n = incorrect_n + 1

    mtitle_photo = PhotoImage(file='mtitleic.png')
    mtitle_label = Label(root,
                         border=0,
                         image=mtitle_photo,
                         bg='#A6FFC9',
                         )

    mtitle_label.place(x=215, y=70)
    o1.bind("<Button>", lambda e: nothing())
    o1_frame.bind("<Button>", lambda e: nothing())
    option1_label.bind("<Button>", lambda e: nothing())

    o2.bind("<Button>", lambda e: nothing())
    o2_frame.bind("<Button>", lambda e: nothing())
    option2_label.bind("<Button>", lambda e: nothing())

    o3.bind("<Button>", lambda e: nothing())
    o3_frame.bind("<Button>", lambda e: nothing())
    option3_label.bind("<Button>", lambda e: nothing())

    o4.bind("<Button>", lambda e: nothing())
    o4_frame.bind("<Button>", lambda e: nothing())
    option4_label.bind("<Button>", lambda e: nothing())

    next_f()


def complete():
    global ename_photo
    global ename_label
    global totalq_photo
    global totalq_label
    global tcorrect_photo
    global tcorrect_label
    global tincorrect_photo
    global tincorrect_label
    global finalscore_photo
    global finalscore_label
    global submit_photo
    global submit_label
    global ename_frame
    global ename_entry

    clearwin()

    ename_photo = PhotoImage(file='ename.png')
    ename_label = Label(root,
                        border=0,
                        image=ename_photo,
                        bg='#A6FFC9',
                        )
    ename_label.place(x=125, y=85)

    ename_frame = Frame(root,
                        width=140,
                        height=30,
                        bg='#ffffff',
                        )
    ename_frame.place(x=315, y=95)

    ename_entry = Entry(ename_frame,
                        bd=0,
                        justify=CENTER,
                        font=("Regular", 15),
                        width=12,
                        )
    ename_entry.pack(fill=BOTH)
    ename_entry.focus()

    totalq_photo = PhotoImage(file='totalquestions.png')
    totalq_label = Label(root,
                         border=0,
                         image=totalq_photo,
                         bg='#A6FFC9',
                         )
    totalq_label.place(x=125, y=145)

    totalq_frame = Frame(root,
                         width=130,
                         height=30,
                         bg='#AA55FF',
                         )
    totalq_frame.place(x=315, y=155)

    totalqn_label = Label(totalq_frame,
                          text=questionnum - 1,
                          bd=0,
                          bg='#AA55FF',
                          justify=CENTER,
                          font=("Regular", 15),
                          width=12,
                          )
    totalqn_label.pack()

    tcorrect_photo = PhotoImage(file='tcorrect.png')
    tcorrect_label = Label(root,
                           border=0,
                           image=tcorrect_photo,
                           bg='#A6FFC9',
                           )
    tcorrect_label.place(x=125, y=205)

    tcorrect_frame = Frame(root,
                           width=130,
                           height=30,
                           bg='#45D664',
                           )
    tcorrect_frame.place(x=315, y=215)

    tcorrectn_label = Label(tcorrect_frame,
                            text=correct_n,
                            bd=0,
                            bg='#45D664',
                            justify=CENTER,
                            font=("Regular", 15),
                            width=12,
                            )
    tcorrectn_label.pack()

    tincorrect_photo = PhotoImage(file='tincorrect.png')
    tincorrect_label = Label(root,
                             border=0,
                             image=tincorrect_photo,
                             bg='#A6FFC9',
                             )
    tincorrect_label.place(x=125, y=265)

    tincorrect_frame = Frame(root,
                             width=130,
                             height=30,
                             bg='#FF7979',
                             )
    tincorrect_frame.place(x=315, y=275)

    tincorrectn_label = Label(tincorrect_frame,
                              text=incorrect_n,
                              bd=0,
                              bg='#FF7979',
                              justify=CENTER,
                              font=("Regular", 15),
                              width=12,
                              )
    tincorrectn_label.pack()

    finalscore_photo = PhotoImage(file='finalscore.png')
    finalscore_label = Label(root,
                             border=0,
                             image=finalscore_photo,
                             bg='#A6FFC9',
                             )
    finalscore_label.place(x=125, y=325)

    finalscore_frame = Frame(root,
                             width=130,
                             height=30,
                             bg='#AA55FF',
                             )
    finalscore_frame.place(x=315, y=335)

    finalscoren_label = Label(finalscore_frame,
                              text=score,
                              bd=0,
                              bg='#AA55FF',
                              justify=CENTER,
                              font=("Regular", 15),
                              width=12,
                              )
    finalscoren_label.pack()

    submit_photo = PhotoImage(file='submitbtn.png')
    submit_label = Label(root,
                         border=0,
                         image=submit_photo,
                         bg='#A6FFC9',
                         )
    submit_label.place(x=185, y=390)

    submit_label.bind("<ButtonRelease-1>", lambda e: submit())


def submit():
    name = ename_entry.get()
    print(
        f'Name : {name}\nTotal questions : {questionnum - 1}\ncorrect : {correct_n}\nIncorrect : {incorrect_n}\nScore : {score}')


def question1():
    global o1
    global o2
    global o3
    global o4

    mcqframe()
    next_label.place_forget()

    q = Label(question_frame,
              text="Q: Find the invalid variable among the following:",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="1st_string",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="my_string_1",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="_",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="foo",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o1_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question2())
    next_label.bind("<Return>", lambda e: question2())


def question2():
    global o1
    global o2
    global o3
    global o4

    mcqframe()
    next_label.place_forget()

    q = Label(question_frame,
              text="Q: Which one of these is incorrect?",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="float(‘nan’)",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="float(‘inf’)",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="float(’12+34′)",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="float(’56’+’78’)",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o3_correct()
    next_label.focus()

    next_label.bind("<ButtonRelease-1>", lambda e: question3())
    next_label.bind("<Return>", lambda e: question3())


def question3():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: The value of the Python expression given below \nwould be: 4+2**5//10",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="77",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="0",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="3",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="7",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o4_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question4())
    next_label.bind("<Return>", lambda e: question4())


def question4():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: The return value for trunc() would be:",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="bool",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="float",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="int",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="None",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o3_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question5())
    next_label.bind("<Return>", lambda e: question5())


def question5():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: What is the output of the Python code given below, if \nthe date of the system is June 21st,2017(Wednesday)?\n [ ] or { } { } or [ ]",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="[ ] [ ]",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="[ ] { }",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="{ } { }",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="{ } [ ]",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o4_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question6())
    next_label.bind("<Return>", lambda e: question6())


def question6():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: The output of this Python code would be:\ns='{0}, {1}, and {2}’\ns.format(‘hi’, ‘great’, ‘day’)",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="‘hi, great, and day’",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="‘hi great and day’",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="‘hi, great, day’",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="Error",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o1_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question7())
    next_label.bind("<Return>", lambda e: question7())


def question7():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: The output of this Python code would be:\nprint(“mno. PQR”.capitalize())",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="Mno. Pqr",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="Mno. pqr",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="MNO. PQR",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="mno. pqr",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o2_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question8())
    next_label.bind("<Return>", lambda e: question8())


def question8():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: Which arithmetic operators can we NOT use with \nstrings?",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="-",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="+",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="*",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="All of the above",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o1_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question9())
    next_label.bind("<Return>", lambda e: question9())


def question9():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: Which function removes a set’s first and the last \nelement from a list?",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="pop",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="remove",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="dispose",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="discard",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o1_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question10())
    next_label.bind("<Return>", lambda e: question10())


def question10():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: The output of this Python code would be:\nsum(1,2,3)\nsum([2,4,6])",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="6, 12",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="Error, Error",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="Error, 12",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="6, Error",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o3_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question11())
    next_label.bind("<Return>", lambda e: question11())


def question11():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: The output of this Python code would be:\na = [‘mn’, ‘op’]\nprint(len(list(map(list, a))))))",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="4",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="2",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="Not specified",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="Error",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o4_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question12())
    next_label.bind("<Return>", lambda e: question12())


def question12():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: Which of these functions can NOT be defined under\n the sys module?",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="sys.argv",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="sys.readline",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="sys.path",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="sys.platform",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o2_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question13())
    next_label.bind("<Return>", lambda e: question13())


def question13():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: Which function doesn’t accept any argument?",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="re.compile",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="re.findall",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="re.match",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="re.purge",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o4_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question14())
    next_label.bind("<Return>", lambda e: question14())


def question14():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: In Python, find which one isn’t an exception handling\n keyword.",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="accept",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="finally",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="try",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="except",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o1_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question15())
    next_label.bind("<Return>", lambda e: question15())


def question15():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: Which of these features of OOP would indicate code\n reusability?",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="Polymorphism",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="Abstraction",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="Inheritance",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="Encapsulation",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o3_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question16())
    next_label.bind("<Return>", lambda e: question16())


def question16():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: Which language does not support polymorphism but\n supports classes?",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="Ada",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="C++",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="Java",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="SmallTalk",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o1_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question17())
    next_label.bind("<Return>", lambda e: question17())


def question17():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: Which of these specifiers would be applied to the\n constructors only?",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="Explicit",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="Implicit",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="Protected",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="Public",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o1_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question18())
    next_label.bind("<Return>", lambda e: question18())


def question18():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: The access specifier that is/are the most secure\n during inheritance is/are _______________.",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="Protected",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="Private",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="Private and Default",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="Default",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o2_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question19())
    next_label.bind("<Return>", lambda e: question19())


def question19():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: The memory that is allocated for any objects is \n____________.",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="Cache",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="HDD",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="ROM",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="RAM",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o4_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question20())
    next_label.bind("<Return>", lambda e: question20())


def question20():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: Which of these classes is a specialization of some\n more general template classes?",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="Integer",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="Maths",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="String",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="Digit",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o3_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question21())
    next_label.bind("<Return>", lambda e: question21())


def question21():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: A derived class is also called a ______________.",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="Small class",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="Subclass",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="Noticeable class",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="Big class",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o2_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question22())
    next_label.bind("<Return>", lambda e: question22())


def question22():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: Hierarchical inheritance could be some subset of \n_________________ inheritance.",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="Multilevel",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="Single level",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="Multiple",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="Hybrid",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o4_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question23())
    next_label.bind("<Return>", lambda e: question23())


def question23():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: __________ is the universal handler class for \nexceptions.",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="Maths",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="Object",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="Exceptions",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="Errors",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o3_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question24())
    next_label.bind("<Return>", lambda e: question24())


def question24():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: What shall we use in the case of safe downcast?",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="Implicit cast",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="Manual cast",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="Dynamic cast",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="Static cast",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o3_correct()

    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: question25())
    next_label.bind("<Return>", lambda e: question25())


def question25():
    global o1
    global o2
    global o3
    global o4

    mcqframe()

    next_label.place_forget()

    q = Label(question_frame,
              text="Q: Which of these types of values result from a delete \noperator?",
              bg='#FF7979',
              border=0,
              font=("Regular", 14),
              )
    q.pack(fill=BOTH,
           expand=True)

    o1 = Label(o1_frame,
               text="null",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o1.pack(fill=BOTH,
            expand=True)

    o2 = Label(o2_frame,
               text="null pointer",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o2.pack(fill=BOTH,
            expand=True)

    o3 = Label(o3_frame,
               text="void pointer",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o3.pack(fill=BOTH,
            expand=True)

    o4 = Label(o4_frame,
               text="void",
               bg='#4870FF',
               border=0,
               font=("Regular", 14),
               padx=30,
               )
    o4.pack(fill=BOTH,
            expand=True)

    o4_correct()

    compltete_photo = PhotoImage(file='complete.png')
    next_label.configure(image=compltete_photo)
    next_label.image = compltete_photo
    next_label.focus()
    next_label.bind("<ButtonRelease-1>", lambda e: complete())
    next_label.bind("<Return>", lambda e: complete())


def game():
    # main_game()
    frame_label.pack(fill=BOTH,
                     expand=True,
                     )

    mcq_label.place(x=30, y=15)

    minimize_label.place(x=495, y=10)
    minimize_label.bind("<Button>", lambda e: minimize_f())
    minimize_label.bind("<Map>", lambda e: maximize_f())

    exit_label.place(x=545, y=10)
    exit_label.bind("<Button>", lambda e: exit_f())

    mainmenu_label.place(x=150, y=110)

    start_label.place(x=150, y=210)
    start_label.bind("<Button>", lambda e: question1())

    hs_label.place(x=150, y=265)
    hs_label.bind("<Button>", lambda e: highscore())

    exitf_label.place(x=150, y=320)
    exitf_label.bind("<Button>", lambda e: exit_f())

    yuvrajlabel.place(x=245, y=465)

    root.mainloop()


game()
