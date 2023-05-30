import mysql.connector
from tkinter import Tk, Button, StringVar, Text
import tkinter.ttk
from tkinter.simpledialog import askstring

try:
    database = mysql.connector.connect(host='localhost', user='root', passwd='')
    connection = mysql.connector.connect(host='localhost', user='root', database='LAB9', passwd='')
    if database.is_connected:
        print(database)
    if connection.is_connected:
        print(connection)
    datacursor = database.cursor()
    conncursor = connection.cursor()
    #mysql.tablequery= """CREATE TABLE MARVEL (ID INT, MOVIE VARCHAR(100), DATE VARCHAR(50) , MCU_PHASE VARCHAR(20))"""
    inputquery = """INSERT INTO MARVEL(id,movie,date,mcu_phase) VALUES (%s,%s,%s,%s)"""


    def loadfromfile():
        marvel = open('marvel.txt')
        text = marvel.readlines()
        for x in text:
            textlist = x.split('\t') #Changed the ID-name space to a tab, because it was clearly intended to be a tab
            print(textlist)
            id = textlist[0] #Since we know the size and placement for the entire file, we can safely assume the locations
            name = textlist[1]
            date = textlist[2]
            phase = textlist[3]
            phase = phase.rstrip()
            row = (id,name,date,phase)
            conncursor.execute(inputquery, row)
            connection.commit()
            marvel.close()

    def fetch(movieid):
        movielist = [str(movieid)]
        conncursor.execute("""SELECT * FROM MARVEL WHERE id=%s""", movielist)
        result = conncursor.fetchone()
        return result

    def fetchids():
        fetchquery = """SELECT id FROM MARVEL"""
        conncursor.execute(fetchquery)
        result = conncursor.fetchall()
        ids = []
        for y in result:
            ids.append(y[0])
        return ids

    def listall():
        fetchquery = """SELECT * FROM MARVEL"""
        conncursor.execute(fetchquery)
        result = conncursor.fetchall()
        fetch_msg.delete(1.0, 'end')
        fetch_msg.insert('end', str(result))

    r = Tk()
    r.title('Lab Task #9')

    def work(event):
        search_id = drop_box.get()
        if search_id:
            search_res = fetch(search_id)
            fetch_msg.delete(1.0, 'end')
            fetch_msg.insert('1.0', str(search_res))


    def confirm():
        answer = askstring('Text Entry', 'Enter text. Space delimits:')
        if answer:
            answerlist = answer.split(' ')
            if answer[3]:
                tempid = answerlist[0]
                tempmovie = answerlist[1]
                tempdate = answerlist[2]
                tempphase = answerlist[3]
                temprow = (tempid, tempmovie, tempdate, tempphase)
                conncursor.execute(inputquery, temprow)
                connection.commit()


    target_movie = StringVar()
    drop_box = tkinter.ttk.Combobox(r, values=fetchids(), textvariable=target_movie)
    drop_box.bind("<<ComboboxSelected>>", work)
    drop_box.pack(pady=20)

    fetch_msg = Text(r)
    fetch_msg.pack(pady=5)

    add_btn = Button(r, text='Add', width=12, bg='#F49B3D', command=confirm)
    add_btn.pack()

    listall_btn = Button(r, text='List All', width=12, bg='#FFFFFF', command=listall)
    listall_btn.pack()

    r.mainloop()
finally:
    conncursor.close()
    connection.close()
    datacursor.close()
    database.close()
