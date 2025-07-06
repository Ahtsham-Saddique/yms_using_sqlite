# YMS_uisng_SQL.py
# C:\Users\HHC\Desktop\python projects\YMS_sql_project\YMS_uisng_SQL.py

import sqlite3,sys

conn=sqlite3.connect('youtube.db')
cursor=conn.cursor()

cursor.execute('''
    Create Table if not exists  videos(
        id integer primary key,
        name text not null,
        time text not null
        
               )
''')
def input_name_And_time():
    name=input("Enter video name : ")
    time=input("Enter video time : ")
    return name,time

def Add_video():
    name,time=input_name_And_time()
    cursor.execute("Insert into videos(name,time) values (?,?)",
                   (name,time))
    conn.commit()

def List_video():
    list=cursor.execute('Select * from videos')

    for row in list.fetchall():
        print(row)

def Delete_video(id):
    List_video()
    
    cursor.execute("Delete from videos where id=?",(id,))
    conn.commit()
    print(f"video {id} deleted sucessfully.")

def Update_video(id):
    name,time=input_name_And_time()
    cursor.execute("Update  videos set name=?,time=? where id=?",
                    (name,time,id))
    conn.commit()
   
def Exit_video():
    sys.exit()

def main():

    while True:
        print("      *$#Youtube_Management_System#$*     ")
        print("\n")
        print("Select your choice : ")
        print("1.List youtube videos")
        print("2.Add youtube videos")
        print("3.Update youtube videos")
        print("4.Delete youtube videos")
        print("5.Exit List ")
        choice=int(input("ENter your choice"))

        if choice==1:
            List_video()
        elif choice==2:
            Add_video()
        elif choice==3:
            id=int(input("Enter the id of video that you want to Update : "))
            Update_video(id)
        elif choice==4:
            id=int(input("Enter the id of video that you want to Delete : "))
            Delete_video(id)
        elif choice==5:
            Exit_video()
        else:
            print("Invalid input from user .")
    conn.close()
if __name__ == '__main__':
    main()
        
