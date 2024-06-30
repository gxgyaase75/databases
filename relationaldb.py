### This file requires the use of MySQL Workbench ###
# Imports
import mysql.connector
from mysql.connector import Error
import time
# Important variables
pw = "password"
start = time.time()
search = """
SELECT *
FROM students;
"""

# Creates server connection through given password
def create_server_connection(host_name, user_name, user_password):
link = None
try:
  link = mysql.connector.connect(
    host=host_name,
    user=user_name,
    passwd=user_password
  )
  print("MySQL Database connection successful")
except Error as err:
  print(f"Error: '{err}'")
return link

# Creates database in MySQL
def create_database(link, query):
  cursor = link.cursor()
  try:
    cursor.execute(query)
    print("Database created successfully.")
  except Error as err:
    print(f"Error: '{err}'")
  end = time.time()
  print("The time of execution of above program is :",
      (end - start) * 10 ** 3, "ms")
# Connects program to new database
def db_connect(host_name, user_name, user_password, db_name):
  link = None
  try:
    link = mysql.connector.connect(
      host=host_name,
      user=user_name,
      passwd=user_password,
      database=db_name
    )
    print("MySQL Database connection successful")
  except Error as err:
    print(f"Error: '{err}'")
  
  return link

# Transfers and executes commands to the database
def query_execution(link, query):
  cursor = link.cursor()
  try:
    cursor.execute(query)
    link.commit()
    print("Query successful")
  except Error as err:
    print(f"Error: '{err}'")
  end = time.time()
  print("The time of execution of the program is :",
    (end - start) * 10 ** 3, "ms")

# Reads everything with search variable
def read_query(link, query):
  cursor = link.cursor()
  result = None
  try:
    cursor.execute(query)
    result = cursor.fetchall()
    return result
  except Error as err:
    print(f"Error: '{err}'")

# Creates the student data table in database
create_student_table = """
CREATE TABLE students (
student_name VARCHAR(40) NOT NULL,
class_no INT,
id_no INT
);
""" 
# Data that goes into database
pop_student = """
INSERT INTO students VALUES
('William Coffey', '3', '1'),
('Rodney Taylor', '8', '18'),
('Kyle Thompson', '6', '22'),
('Gabrielle Grant', '5', '30'),
('Brandon Bell', '3', '4'),
('Andrew Smith', '7', '8'),
('Victor Sullivan', '1', '26'),
('Kristina Heath', '3', '14'),
('Beverly Fuller', '7', '1'),
('Charles Juarez', '6', '15');
""" 
# Updates a student (Rodney in this case)
update_student
= """
UPDATE students
SET class_no = 2
WHERE id_no = 18;
""" 
# Deletes a student from table (Kristina in this case)
delete_student = """
DELETE FROM students
WHERE id_no = 14;
""" 
# Commands used in experiment
plug = db_connect("localhost" ,"root", pw, "sqltest")
query_execution(plug, create_student_table)
query_execution(plug, pop_student)
query_execution(plug, update_student)
query_execution(plug, delete_student)
# Reads data and prints it
data = read_query(plug, search)
for info in data:
  print(info)
# Returns time in milliseconds
end = time.time()
print("The time of execution of the reading is :",
   (end - start) * 10 ** 3 , "ms")
