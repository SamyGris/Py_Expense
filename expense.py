from PyInquirer import prompt
from user import load_users
import csv

def load_expenses():
    expenses = []
    with open("expenses.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            amount, label, spender, involved = row
            expenses.append([amount, spender, involved.split(";")])
    return expenses

def expense_questions():
        return [
        {
            "type": "input",
            "name": "amount",
            "message": "New Expense - Amount: ",
            "validate": lambda val: val.replace(".", "", 1).isdigit() or "Please enter a valid number for the amount.",
        },
        {
            "type": "input",
            "name": "label",
            "message": "New Expense - Label: ",
        },
        {
            "type": "list",
            "name": "spender",
            "message": "New Expense - Spender: ",
            "choices": load_users(),
        },
        {
            "type": "checkbox",
            "name": "involved",
            "message": "New Expense - Involved: ",
            "choices": load_users(),
        }
    ]

def new_expense(*args):
    infos = prompt(expense_questions())
    amount = float(infos["amount"])
    involved_users = ";".join(infos["involved"])
    spender = infos["spender"]

    if (len(infos["involved"]) == 0):
        print("No one is involved in this expense !")
        return False
    
    if spender not in involved_users: involved_users += ";" + spender
    
    with open("expenses.csv", "a") as f:
        f.write(f"{amount},{infos['label']},{spender},{involved_users}\n")
    print("Expense Added !")