from user import load_users
from expense import load_expenses

def show_status():
    users = load_users()
    expenses = load_expenses()

    print("Status Report:")
    for user in users:
        user['balance'] = []
        for expense in expenses:
            amount, spender, involved = expense
            split_amount = float(amount) / len(involved)
            if user['name'] in involved and user['name'] != spender:
                user['balance'].append((split_amount, spender))
    
    for user in users:
        if user['balance'] == []:
            print(f"{user['name']} owes nothing.")
        else:
            for b in user['balance']:
                print(f"{user['name']} owes {b[0]}€ to {b[1]}.")