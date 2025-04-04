
quiz = [
    '''Question 1: Who is the prime minister of India?
       A: Rahul Gandhi
       B: Narendra Modi
       C: Atal Bihari Vajpayee
       D: Ram''',

    '''Question 2: Who is the CM of Haryana?
       A: Depender Hooda
       B: Manohar Lal Khattar
       C: Jawaharlal Nehru
       D: Yogi Adityanath'''
]

for question in quiz:
    print(question)
    answer = input("Select your option: ").strip().upper()
    if answer == "B":
        print("Correct! You've won 1 lakh rupees.")
    else:
        print("You lost. Try again.")
        break
else:
    print("Congratulations! You've answered all questions correctly and won 2 lakh rupees.")
