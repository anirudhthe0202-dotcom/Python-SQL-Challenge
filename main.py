import mysql.connector as con

database = con.connect(user="root", password = "12345", host = "localhost")
cursor = database.cursor()

cursor.execute("use query;")

def signup():
    a = ""
    while True:
        a = input("Enter username: ")
        cursor.execute(f"SELECT * FROM login_info WHERE username = '{a}';")
        b = cursor.fetchone()
        if b:
            print("This username has already been taken. Try a different one")
        else:
            break
    
    while True:
        password = input("Set a password: ")
        c_pass = input("Confirm password: ")
        if password == c_pass:
            cursor.execute(f"INSERT INTO login_info VALUES('{a}','{password}', NULL )")
            database.commit()
            return a
        else:
            print("Enter the same password in both")
        
def login():
    while True:
        a = input("Enter username: ")
        cursor.execute(f"SELECT * FROM login_info WHERE username = '{a}';")
        b = cursor.fetchall()
        if not b:
            print("This username does not exist")
        else:
            break
    
    while True:
        password = input("Enter your password: ")
        cursor.execute(f"SELECT password FROM login_info WHERE username = '{a}';")
        c = cursor.fetchone()
        if password == c[0]:
            return a
        else:
            print("Incorrect password")


def test():
    ques = ["Which of the following is a mutable data type in Python?",
            "Which keyword is used to define a function in Python?",
            "Which of the following statements about tuples is true?",
            "Which method is used to add an element at the end of a list?`",
            "Which operator is used for floor division in Python?",
            "Which statement is used to terminate a loop immediately?",
            "Which data structure stores key-value pairs?",
            "What is the purpose of the pass statement?",
            "Which keyword is used to handle exceptions?",
            "Which of the following is not a valid loop in Python?",
            "What does SQL stand for?",
            "Which SQL command is used to retrieve data from a table?",
            "Which clause is used to filter records?",
            "Which command is used to insert new records into a table?",
            "Which SQL statement is used to modify existing records?",
            "Which command removes records from a table?",
            "Which key uniquely identifies a record in a table?",
            "Which key establishes a relationship between two tables?",
            "Which clause is used to sort query results?",
            "Which aggregate function counts the number of records?",
            ]
    options = ["A) Tuple\nB) String\nC) List\nD) Integer",
               "A) function\nB) define\nC) def\nD) func",
               "A) Tuples are mutable.\nB) Tuples can be modified after creation.\nC) Tuples are immutable.\nD) Tuples cannot store mixed data types.",
               "A) add()\nB) append()\nC) insert()\nD) extend()",
               "A) /\nB) %\nC) //\nD) **",
               "A) stop\nB) terminate\nC) continue\nD) break",
               "A) List\nB) Tuple\nC) Dictionary\nD) Set",
               "A) Exit a loop\nB) Skip an iteration\nC) Do nothing\nD) Return a value",
               "A) error\nB) catch\nC) try\nD) check",
               "A) for\nB) while\nC) do-while\nD) Nested loop",
               "A) Structured Query Language\nB) Simple Query Language\nC) Standard Question Language\nD) Sequential Query Language",
               "A) GET\nB) FETCH\nC) SELECT\nD) DISPLAY",
               "A) ORDER BY\nB) WHERE\nC) GROUP BY\nD) HAVING",
               "A) ADD\nB) INSERT\nC) INSERT INTO\nD) UPDATE",
               "A) ALTER\nB) UPDATE\nC) MODIFY\nD) CHANGE",
               "A) DELETE\nB) REMOVE\nC) DROP\nD) CLEAR",
               "A) Candidate Key\nB) Foreign Key\nC) Primary Key\nD) Alternate Key",
               "A) Candidate Key\nB) Foreign Key\nC) Primary Key\nD) Composite Key",
               "A) SORT BY\nB) GROUP BY\nC) ORDER BY\nD) ARRANGE BY",
               "A) SUM()\nB) COUNT()\nC) TOTAL()\nD) NUMBER()",
               ]
    answers = ["C",
               "C",
               "C",
               "B",
               "C",
               "D",
               "C",
               "C",
               "C",
               "C",
               "A",
               "C",
               "B",
               "C",
               "B",
               "A",
               "C",
               "B",
               "C",
               "B"
               ]
    score=0
    for i in range(0,20):
        print(f"Question {i+1}/20")
        print("[","█"*(i+1), " "*(19-i), "]  ", (i+1)*5, "%" , sep = "" )
        print(f"{ques[i]}")
        print(options[i])
        print("Your answer: ", end = "")
        while True:
            ans=input().upper()
            if ans not in "ABCD":
                print("Invalid option. Enter again: ", end = "")
            else:
                break
        if ans==answers[i]:
            score+=1
    print("Your score is:", score,"/20")
    return score
    
    
    
def leaderboard(user):
    cursor.execute(f"SELECT TRIM(username),score FROM login_info ORDER BY score DESC;")
    scores = cursor.fetchall()
    print(f"{'_______THE LEADERBOARD IS_______':^40}")
    n = 0
    u_r = 0
    print(f"{'NAME':<20}{'SCORE':<20}{'RANK':<20}")
    for i in scores:
        n+=1
        print(f"{i[0].strip():<20} {str(i[1]):<20} {n:<20}")
        if i[0] == user:
            u_r = n
    print(f"\nYour rank is: {u_r}/{len(scores)}")



def score_change(user, score):
    cursor.execute(f"UPDATE login_info SET score = {score} WHERE username = '{user}';")
    database.commit()

def change_password(user):
    while True:
        password = input("Enter new password: ")
        c_password = input("Confirm password: ")
        if password == c_password:
            cursor.execute(f"UPDATE login_info SET password = '{password}' WHERE username = '{user}';")
            database.commit()
            break
        else:
            print("Enter the same password in both")
    
#Main
print("Welcome to Techy quiz")
while True:
    a = input("Enter 1 to sign up, 2 to login: ")
    if a == "1":
        user = signup()
        score = test()
        score_change(user, score)
        leaderboard(user)
        break
    
    elif a == "2":
        user = login()
        while True:
            x = input("Enter 1 to give a retest, 2 to display leaderboard, 3 to change password: ")
            if x == "1":
                score = test()
                score_change(user, score)
                leaderboard(user)
                break
            elif x == "2":
                leaderboard(user)
                break
            elif x == "3":
                change_password(user)
            else:
                print("Incorrect choice.")
        break
            
    else:
        print("Incorrect choice. Enter choice as per given")



