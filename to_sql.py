# @author: Saahil pralhad Anande(1001855308) and Unnathi Reddy Nalla(1001828087)


import mysql.connector
import json

connection = mysql.connector.connect(host='localhost',
                                         database='assignment11',
                                         user='root',
                                         password='saahil1234')

emplist = []
deplist=[]
proj=[]
# cursor = connection.cursor()
# query = "TRUNCATE TABLE  employee;"
# cursor.execute(query)
# cursor = connection.cursor()
# query = "TRUNCATE TABLE  department;"
# cursor.execute(query)
# cursor = connection.cursor()
# query = "TRUNCATE TABLE  project;"
# cursor.execute(query)
# cursor = connection.cursor()
# query = "TRUNCATE TABLE  workson;"
# cursor.execute(query)

#for reading the employee text file and putting in the sql database
with open('EMPLOYEE.txt', 'r') as file:  # reading the input file
    for line in file.readlines():
        emplist = line.split(",")
        firstname = emplist[0].replace("'","")
        middlename = emplist[1].replace("'","")
        lastname = emplist[2].replace("'","")
        emp_ssn = emplist[3].replace("'","")
        dateofbirth= emplist[4].replace("'","")
        address = emplist[5].replace("'","")
        city = emplist[6].replace("'","")
        state= emplist[7].replace("'","")
        gender = emplist[8].replace("'","")
        salary = emplist[9].replace("'","")
        mng_ssn = emplist[10].replace("'","")
        depno = emplist[11].replace("'","")
        #print("firstname"+firstname+" middlename "+middlename+" lastname"+lastname+" ssn="+emp_ssn+" dateofbirth="+dateofbirth+" address="+address+" salary="+salary+"")
        cursor = connection.cursor()
        query = "INSERT INTO employee (emp_first,emp_last , emp_ssn, emp_birth, emp_address,emp_gender,emp_salary,mnger_ssn,emp_depno) VALUES ('"+firstname+"','"+lastname+" "+middlename+"','"+emp_ssn+"','"+dateofbirth+"','"+address+", "+city+", "+state+"','"+gender+"','"+salary+"','"+mng_ssn+"','"+depno+"'); "
        cursor.execute(query)
        connection.commit()

#for reading the department text file and putting in the sql database
with open('DEPARTMENT.txt', 'r') as file:  # reading the input file
    for line in file.readlines():
        deplist = line.split(",")
        dname = deplist[0].replace("'", "")
        dno = deplist[1].replace("'", "")
        dmng_snn = deplist[2].replace("'", "")
        dmng_start_date = deplist[3].replace("'", "")
        cursor = connection.cursor()
        query = "INSERT INTO department (d_name,d_no,mng_ssn,mng_start_date) VALUES ('"+dname+"','"+dno+"','"+dmng_snn+"','"+dmng_start_date+"');"
        cursor.execute(query)
        connection.commit()


#for reading the project text file and putting in the sql database
with open('PROJECT.txt', 'r') as file:  # reading the input file
    for line in file.readlines():
        proj = line.split(",")
        pname = proj[0].replace("'", "")
        pno = proj[1].replace("'", "")
        plocation = proj[2].replace("'", "")
        dnum = proj[3].replace("'", "")
        cursor = connection.cursor()
        query = "INSERT INTO project (p_name,p_no,p_location,d_num) VALUES ('"+pname+"','"+pno+"','"+plocation+"','"+dnum+"');"
        cursor.execute(query)
        connection.commit()


#for reading the workson text file and putting in the sql database
with open('WORKS_ON.txt', 'r') as file:  # reading the input file
    for line in file.readlines():
        proj = line.split(",")
        essn = proj[0].replace("'", "")
        pno = proj[1].replace("'", "")
        hours = proj[2].replace("'", "")
        cursor = connection.cursor()
        query = "INSERT INTO workson (essn,pno,hours) VALUES ('"+essn+"','"+pno+"','"+hours+"');"
        cursor.execute(query)
        connection.commit()


#to set foreign keys
cursor = connection.cursor()
query = "alter table department add foreign key (mng_ssn) references employee(emp_ssn);"
cursor.execute(query)
connection.commit()
cursor = connection.cursor()
query = "alter table project add foreign key (d_num) references department(d_no);"
cursor.execute(query)
connection.commit()
cursor = connection.cursor()
query = "alter table workson add foreign key (essn) references employee(emp_ssn), add foreign key (pno) references project(p_no)"
cursor.execute(query)
connection.commit()





#reference:
#https://dzone.com/articles/migrate-mysql-table-data-to-mongodb-collections-us