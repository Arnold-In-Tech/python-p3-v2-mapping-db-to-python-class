from __init__ import CONN, CURSOR
from department import Department

import ipdb


# recreates the Department table and persists a few objects into the table.

def reset_database():
    Department.drop_table()
    Department.create_table()

    Department.create("Payroll", "Building A, 5th Floor")
    Department.create("Human Resources", "Building C, East Wing")
    Department.create("Accounting", "Building B, 1st Floor")

reset_database()
ipdb.set_trace()

# confirm tables were created
departments = CURSOR.execute('SELECT * FROM departments')
[row for row in departments]

# list dictionary of persisted values
Department.all


# ========= Get a row
# To Execute a query to get a row of data, then use that row to get a Python Department object :
row = CURSOR.execute("select * from departments").fetchone()
department = Department.instance_from_db(row)


#==========  Get all rows
Department.get_all()
# Interacting with the data which is returned as objects:
departments = Department.get_all()
departments[0]
# ==> <Department 1: Payroll, Building A, 5th Floor>
departments[0].name
# ==> 'Payroll'

# ========= find_by_id(1)
department = Department.find_by_id(1)
department
# ==> <Department 1: Payroll, Building A, 5th Floor>
department.name
# ==> 'Payroll'
department.location
# ==> 'Building A, 5th Floor'


# ========= find_by_name("Payroll")
department = Department.find_by_name("Payroll")
department
# ==> <Department 1: Payroll, Building A, 5th Floor>





