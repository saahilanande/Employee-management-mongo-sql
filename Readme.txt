Name: Saahil pralhad anande and Unnathi Reddy Nalla
Programing Language Used     : Python3.8

libraries needed :pymongo, sql.connector, dicttoxml,jason

Run code using below command : Please run the below commands to run the code

*First create tables in mysql using this commands:

CREATE TABLE employee (
	emp_first varchar(255),
    emp_last varchar(255),
    emp_ssn int,
	emp_birth varchar(255),
    emp_address varchar(255),
    emp_gender varchar(50),
    emp_salary int,
    mnger_ssn varchar(50),
    emp_depno int,
    PRIMARY KEY (emp_ssn)
);

CREATE TABLE department (
	d_name varchar(255),
    d_no int,
	mng_ssn int,
    mng_start_date varchar(50),
    primary key (d_no)
);

CREATE TABLE project (
	p_name varchar(255),
    p_no int,
	p_location varchar(50),
    d_num int,
    primary key (p_no)
);

create table workson
(essn int,
 pno int,
 hours int,
 primary key (essn,pno)
 );

*Then run the code to populate the created tables
python to_sql.py

*then run the code to populate mongodb with collections
python convert_to_json_and_mongo_import.py

*then open perform quries on mongo


Additional Information: Please replace the mysql database user, password and database name (In  and to_sql.py from line 8 to 13) with your mysql database user, password and database name. 

