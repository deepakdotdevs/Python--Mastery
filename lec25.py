# Key Point -> Kaun Banega crorepati (KBC) program :

# ---------------------------------------------------------------------

# Create a program capable of displaying questions to the user like KBC .?
# Use list data type to store and questions and their correct answers.
# Display the final amout the person is taking home after playing the game.

# ---------------------------------------------------------------------

questions = [
    ["Which language was used to create fb?", "Python", "French", "Javascript, 'Php", 'None', 4], # correct answer is on 4th index
    ["Which language was used to create fb?", "Python", "French", "Javascript, 'Php", 'None', 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript, 'Php", 'None', 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript, 'Php", 'None', 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript, 'Php", 'None', 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript, 'Php", 'None', 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript, 'Php", 'None', 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript, 'Php", 'None', 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript, 'Php", 'None', 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript, 'Php", 'None', 4],
    ["Which language was used to create fb?", "Python", "French", "Javascript, 'Php", 'None', 4],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}            b. {question[2]}")
    print(f"c. {question[3]}            d. {question[4]}")
    reply = int(input("Enter your answer (1-4) : "))
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i==4):
            money = 10000
        elif(i==9):
            money = 20000
        elif(i==14):
            money = 320000
    else:
        print("Wrong Answer!")
        break
print(f"Your take home monday is Rs. {money}")