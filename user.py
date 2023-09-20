from PyInquirer import prompt
import csv

def load_users():
    users = []
    with open("users.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            users.append({"name": row[0]})
    return users

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    }
]

def add_user():
    # This function should create a new user, asking for its name
    # and then adding it to the users.csv file
    infos = prompt(user_questions)
    with open("users.csv", "a") as f:
        f.write(f"{infos['name']}\n")
    print("User Added !")
    return True