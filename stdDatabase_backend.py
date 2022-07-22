# stdDatabase_backend.py

# backend
import sqlite3


def studentData():
    con = sqlite3.connect("student.db")
    q = """
	CREATE table if NOT exists student(
	id integer primary key,
	stdID text,
	Firstname text,
	Surname text,
	Dob text,
	Age text,
	Gender text,
	Address text,
	Mobile text)
	"""
    q1 = """
	CREATE table student(
	id integer primary key,
	stdID text,
	Firstname text,
	Surname text,
	Dob text,
	Age text,
	Gender text,
	Address text,
	Mobile text)
	"""
    cur = con.cursor()
    cur.execute(q)
    print("table created")
    con.commit()
    con.close()


def addStdRecord(StdID, Firstname, Surname, Dob, Age, Gender, Address, Mobile):
    con = sqlite3.connect("student.db")
    cur = con.cursor()

    cur.execute("insert into student values (NULL,?,?,?,?,?,?,?,?)",
                (StdID, Firstname, Surname, Dob, Age, Gender, Address, Mobile))
    # cur.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s)",(stdID,Firstname,Surname,Dob,Age,Gender,Address,Mobile))
    # cur.execute("insert into student values(?,?,?,?,?,?,?,?",stdID,Firstname,Surname,Dob,Age,Gender,Address,Mobile)
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("select * from student")
    rows = cur.fetchall()
    con.close()
    return rows


def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("delete from student where id=?", (id,))
    con.commit()
    con.close()


def searchData(StdID="", Firstname="", Surname="", Dob="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("select * from student where StdID=? or Firstname=? or Surname=? or Dob=? \
		or Age=? or Gender=? or Address=? or Mobile=? ", (StdID, Firstname, Surname, Dob, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    cur.close()
    return rows


def dataUpdate(id, StdID="", Firatname="", Surname="", Dob="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("update student set StdID=? , Firatname=? , Surname=? , Dob=? \
		Age=? , Gender=? , Address=? , Mobile=?  where id=?",
                (StdID, Firatname, Surname, Dob, Age, Gender, Address, Mobile, id))
    con.commit()
    cur.close()

#studentData()
#addStdRecord('1','2','3','4','5','6','7','8')