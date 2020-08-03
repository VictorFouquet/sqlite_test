import sqlite3

from employee import Employee


def insert_emp(conn, cursor, emp):
    with conn:
        cursor.execute(
            "INSERT INTO employees VALUES (:first, :last, :pay)", 
            {'first': emp.first, 'last': emp.last, 'pay': emp.pay}
        )

def get_emps_by_name(cursor, lastname):
    cursor.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return cursor.fetchall()

def update_pay(conn, cursor, emp, pay):
    with conn:
        cursor.execute(
            '''UPDATE employees SET pay = :pay
            WHERE first = :first AND last = :last''',
            {'first': emp.first, 'last': emp.last, 'pay': pay}
        )

def remove_emp(conn, cursor, emp):
    with conn:
        cursor.execute(
            "DELETE from employees WHERE first = :first AND last = :last",
            {'first': emp.first, 'last': emp.last}
        )

def main():
    conn = sqlite3.connect('employee.db')

    cursor = conn.cursor()

    try:
        cursor.execute(
            '''CREATE TABLE employees (
                first text,
                last text,
                pay integer
            )'''
        )
        conn.commit()
    except:
        pass

    emps = [Employee('John', 'Doe', 30000), Employee('Jane', 'Doe', 32000)]

    for emp in emps:
        insert_emp(conn, cursor, emp)
        if emp.last == 'Doe':
            update_pay(conn, cursor, emp, 50000)

    print(get_emps_by_name(cursor, 'Doe'))

    for emp in emps:
        remove_emp(conn, cursor, emp)

    conn.close()

if __name__ == '__main__':
    main()
