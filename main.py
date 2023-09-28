print("Welcome to the Quiz Game")
score = 0
play = input("You want to play y/n: ").lower()
if play == "y":
    print("Rule: Choice the correct answer of the following. Total marks are 10")
    print("1. What is the maximum length of a Python identifier?")
    print("(A) 32   (B) 16   (C) 128   (D) not fixed length")
    ans1 = input().upper()
    if ans1 == "D":
        print("Correct")
        score +=1
    else:
        print("incorrect")
        print("The correct answer is Not fixed length")
    print("2. What will be the output of the following code snippet? \n print(2**3 + (5 + 6)**(1 + 1))")
    print("(A) 129   (B) 8   (C) 121   (D) none of these")
    ans2 = input().upper()
    if ans2 == "A":
        print("Correct")
        score += 1
    else:
        print("incorrect")
        print("The correct answer is 129")
    print("3. How is a code block indicated in Python?")
    print("(A) Brackets   (B) indentation   (C) key   (D) none of these")
    ans3 = input().upper()
    if ans3 == "B":
        print("Correct")
        score += 1
    else:
        print("incorrect")
        print("The correct answer is indentation")
    print("4. Which of the following concepts is not a part of Python?")
    print("(A) Pointers   (B) Loops   (C) Dynamic Typing   (D) All of these")
    ans4 = input().upper()
    if ans4 == "A":
        print("Correct")
        score += 1
    else:
        print("incorrect")
        print("The correct answer is Pointers")
    print("5. Which of the following statements are used in Exception Handling in Python?")
    print("(A) try   (B) except   (C) final   (D) All of these")
    ans5 = input().upper()
    if ans5 == "D":
        print("Correct")
        score += 1
    else:
        print("incorrect")
        print("The correct answer is All of these")
    print("6. Which of the following types of loops are not supported in Python?")
    print("(A) while   (B) for   (C) do-while   (D) none of these")
    ans6 = input().upper()
    if ans6 == "C":
        print("Correct")
        score += 1
    else:
        print("incorrect")
        print("The correct answer is do-while")
    print("7. Which of the following is the proper syntax to check if a particular element is present in a list?")
    print("(A) if ele in list   (B) if not ele not in list   (C) Both A and B   (D) none of these")
    ans7 = input().upper()
    if ans7 == "C":
        print("Correct")
        score += 1
    else:
        print("incorrect")
        print("The correct answer is Both A and B")
    print("8. Which of the following functions converts date to corresponding time in Python?")
    print("(A) strptime()   (B) strftime()   (C) Both A and B   (D) none of these")
    ans8 = input().upper()
    if ans8 == "A":
        print("Correct")
        score += 1
    else:
        print("incorrect")
        print("The correct answer is strptime")
    print("9. As what datatype are the *args stored, when passed into a function?")
    print("(A) List   (B) Tuple   (C) Dictionary  (D) none of these")
    ans9 = input().upper()
    if ans9 == "B":
        print("Correct")
        score += 1
    else:
        print("incorrect")
        print("The correct answer is Tuple")
    print("10. As what datatype are the *kwargs stored, when passed into a function?")
    print("(A) List   (B) Tuple   (C) Dictionary  (D) none of these")
    ans10 = input().upper()
    if ans10 == "C":
        print("Correct")
        score += 1
    else:
        print("incorrect")
        print("The correct answer is Dictionary")
    print("No. of question is 10")
    print("Your Score is", score)
    per = score*100/10
    print('Percentage = ', per)
    if per == 90:
        print("Grade = A+")
        print("Excellent Performance")
    elif per == 80:
        print("Grade = A")
        print("Very Well Performance")
    elif per == 70:
        print("Grade = B")
        print("Very Good Performance")
    elif per == 60:
        print("Grade = D")
        print("Good Performace")
    elif per == 50:
        print("Grade = E")
        print("Just Pass")
    else:
        print("You are Fail")
elif play == "n":
    print("Thank you for comming")
else:
    print("You enter invalid value")
