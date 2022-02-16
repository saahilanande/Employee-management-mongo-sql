# @author: Saahil pralhad Anande(1001855308) and Unnathi Reddy Nalla(1001828087)

import json
import mysql.connector
import pymongo
from dicttoxml import dicttoxml
from ast import literal_eval

connection = mysql.connector.connect(host='localhost',
                                         database='assignment11',
                                         user='root',
                                         password='saahil1234')

mongodb_host = "mongodb://localhost:27017/"
mongodb_dbname = "db2project"

#for fetching nested project document collection
mycursor = connection.cursor()
query = "select p_no,p_name,d_num,emp_first,emp_last,hours,d_name from project p join department d on p.d_num = d.d_no join workson w on w.pno=p.p_no join employee e on e.emp_ssn = w.essn order by p.p_no"
mycursor.execute(query)
myresult = mycursor.fetchall()

#to create nested jason file

jsonresult = {}
for p_no, p_name,d_num,emp_first, emp_last, hours,d_name in myresult:
   if p_no in jsonresult:
        emp = {
            "Employee_first_name" : emp_first,
            "Employee_last_name" : emp_last,
            "hours" : hours
            }
        jsonresult[p_no]["employee"].append(emp)
   else:
        jsonresult[p_no] =  {
        "Project_name" : p_name,
        "project_number" : p_no,
        "department_name" : d_name,
        "employee" : [{
             "Employee_first_name" : emp_first,
             "Employee_last_name" : emp_last,
             "hours" : hours
            }]
        }

print(jsonresult)
jsonfile= json.dumps(jsonresult)
for x in jsonresult:
    myclient = pymongo.MongoClient(mongodb_host)
    mydb = myclient[mongodb_dbname]
    mycol = mydb["project_document"]
    mycol.insert_one(jsonresult[x])


#write to file project_document.jason
file="project_document.json"
with open(file, 'w') as out:
   out.write(jsonfile + '\n')

#xml file converstion
convo = literal_eval(jsonfile)
xmlfile = dicttoxml(convo)

#write to file project_document.xml
with open("PROJECT_XML.xml", 'w') as out:
   out.write(str(xmlfile, 'utf-8'))


#for fetching nested Employee document collection
mycursor = connection.cursor()
query = "select e.emp_ssn,e.emp_first,e.emp_last,d.d_name,p.p_name,p.p_no,w.hours from employee e join workson w on e.emp_ssn=w.essn join project p on p.p_no = w.pno join department d on d.d_no = e.emp_depno order by e.emp_ssn"
mycursor.execute(query)
employee_col_result = mycursor.fetchall()

#to create nested jason file
jsonresult = {}
for emp_ssn, emp_first, emp_last,d_name,p_name, p_no, hours in employee_col_result:
   if emp_ssn in jsonresult:
        pro = {
            "project_name" : p_name,
            "project_number" : p_no,
            "Hours" : hours
            }
        jsonresult[emp_ssn]["project"].append(pro)
   else:
        jsonresult[emp_ssn] =  {
        "Employee_first_name" : emp_first,
        "Employee_last_name" : emp_last,
        "department_name" : d_name,
        "project" : [{
            "project_name" : p_name,
            "project_number" : p_no,
            "Hours" : hours
            }]
        }
print(jsonresult)
jsonfile= json.dumps(jsonresult)
for x in jsonresult:
    myclient = pymongo.MongoClient(mongodb_host)
    mydb = myclient[mongodb_dbname]
    mycol = mydb["employee_document"]
    mycol.insert_one(jsonresult[x])

#write to file project_document.jason
file="employee_document.json"
with open(file, 'w') as out:
   out.write(str(jsonfile) + '\n')

#xml file converstion
convo = literal_eval(jsonfile)
xmlfile = dicttoxml(convo)

#write to file employee_document.xml
with open("EMPLOYEE_XML.xml", 'w') as out:
   out.write(str(xmlfile, 'utf-8'))

#for fetching nested department document collection
mycursor = connection.cursor()
query = "SELECT d_name, d_no, mgr.emp_last as MGR_LNAME, mgr.emp_first as MGR_FNAME,e.emp_last as EMP_LNAME, e.emp_first as EMP_FNAME, e.emp_salary from department d, employee mgr, employee e where d.mng_ssn = mgr.emp_ssn and d.d_no = mgr.emp_depno and d.mng_ssn = e.mnger_ssn order by d.d_no"
mycursor.execute(query)
department_search = mycursor.fetchall()

#to create nested jason file
jsonresult = {}
for d_name, d_no, MGR_LNAME, MGR_FNAME, EMP_LNAME, EMP_FNAME, emp_salary in department_search:
    if d_no in jsonresult:
        emp = {
            "Emp_Lname": EMP_LNAME,
            "Emp_Fname": EMP_FNAME,
            "Salary": emp_salary

        }
        jsonresult[d_no]["Employee"].append(emp)
    else:
        jsonresult[d_no] = {
            "Dname": d_name,
            "Dnumber": d_no,
            "Mgr_Lname": MGR_LNAME,
            "Mgr_Fname": MGR_FNAME,

            "Employee": [{
                "Emp_Lname": EMP_LNAME,
                "Emp_Fname": EMP_FNAME,
                "Salary": emp_salary
            }]
        }

print(jsonresult)
jsonfile= json.dumps(jsonresult)
for x in jsonresult:
    myclient = pymongo.MongoClient(mongodb_host)
    mydb = myclient[mongodb_dbname]
    mycol = mydb["department_document"]
    mycol.insert_one(jsonresult[x])

    print("EXECUTED SUCCESSFULLY CHECK MONGODB FOR COLLECTION project_document,employee_document,department_document FOR PERFORMING QURIES")
#write to file project_document.jason
file="department_document.json"
with open(file, 'w') as out:
   out.write(str(jsonfile) + '\n')

#xml file converstion
convo = literal_eval(jsonfile)
xmlfile = dicttoxml(convo)

#write to file DEPARTMENT_document.xml
with open("DEPARTMENT_XML.xml", 'w') as out:
   out.write(str(xmlfile, 'utf-8'))