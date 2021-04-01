import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute(
    """
    CREATE TABLE employee (
        first text,
        last text,
        pay integer
    )
    """
)

def insert_emp(emp):
    with conn:
        c.execute(
            "INSERT INTO employee VALUES (:first, :last, :pay)", {'first':emp.first, 'last':emp.last, 'pay': emp.pay}
        )
def get_emps_by_name(lastname):
    c.execute(
        "SELECT * FROM employee WHERE last = :last", {'last':lastname}
    )
    return c.fetchall()
def update_pay(emp, pay):
    with conn:
        c.execute(
            """
            UPDATE employee SET pay = :pay
            WHERE first = :first AND last = :last""",
            {'first':emp.first, 'last': emp.last, 'pay': pay}
        )

def remove_emp(emp):
    with conn:
        c.execute(
            """
            DELETE from employee
            WHERE first = :first AND last = :last""",
            {'first':emp.first, 'last': emp.last}
        )

emp1 = Employee('Deven', 'Shrestha', 80000)
emp2 = Employee('Syasu', 'Shrestha', 90000)



insert_emp(emp1)
insert_emp(emp2)

emps = get_emps_by_name('Shrestha')
print(emps)

update_pay(emp2, 95000)
remove_emp(emp2)

emps = get_emps_by_name('Shrestha')
print(emps)
# c.execute(
#     f"INSERT INTO employee VALUES('{emp1.first}','{emp1.last}', {emp1.pay})"
# )

# conn.commit() 

# c.execute(
#     "INSERT INTO employee VALUES(? ,? ,?)", (emp1.first, emp1.last, emp1.pay)
# )

# conn.commit()

# c.execute(
#     "INSERT INTO employee VALUES (:first, :last, :pay)", {'first':emp2.first, 'last':emp2.last, 'pay': emp2.pay}
# )

# conn.commit()

# c.execute(
#     "SELECT * FROM employee WHERE last = ?", ('Shrestha',)
# )
# print(c.fetchall()) 


# c.execute(
#     "SELECT * FROM employee WHERE last = :last", {'last':'Buddhathoki'}
# )
# print(c.fetchall()) 

# conn .commit() 
conn.close()
