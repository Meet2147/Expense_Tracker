import sqlite3
conn = sqlite3.connect("data.db")
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS expensetable(expense_date DATE, item TEXT, expense_type TEXT, expense_amount INT)')
    
def add_expense(expense_date ,item, expense_type, expense_amount):
    c.execute('INSERT INTO expensetable (expense_date ,item, expense_type, expense_amount) VALUES (?,?,?,?)', (expense_date ,item, expense_type, expense_amount))
    conn.commit()
    
# def total_expense():
#     c.execute('SELECT SUM(expense_amount) FROM expensetable')
#     total = c.fetchall()
#     return total
        
def view_all_expenses():
    c.execute('SELECT * FROM expensetable')
    data = c.fetchall()
    return data