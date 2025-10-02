questions = [
    ["Question 1:Which planet is known as the 'Red Planet'?"],
    ["Venus","Mars","Jupiter","Saturn"],
     ["Question 2:Which of the following is the smallest prime number?"],
    [0,1,2,3],
    ["Who was the first Prime Minister of India?"],
    ["Mahatma Gandhi","Jawaharlal Nehru","Sardar Vallabhbhai Patel","Dr. B.R. Ambedkar"]

]


for q in range(6):
    if(q == 0):
        print(questions[0][0])
        option1  = questions[1]
        for i in option1:
            print(i)
        answer1 = input("Enter your answer: ")
        if(answer1 == "Mars" or answer1 == "mars"):
            print("congratulation you won 1 level and 1000 rupees")
            print(questions[2][0])
            option2 = questions[3]
            for k in option2:
                print(k)
            answer2 = int(input("Enter your answer: "))
            if(answer2 == 2):
                 print("congratulation you won 2 level and 2000 rupees Total 3000")
                 print(questions[4][0])
                 option3 = questions[5]
                 for i in option3:
                    print(i)
                 answer3 = input("Enter your answer: ")
                 if(answer3 == "Jawaharlal Nehru" or answer3 == "jawaharlal nehru"):
                        print("congratulation you won 3 level and 4000 rupees Total 6000")
            else:
                print("lose money")
        else:
            print("lose Money")
    
            
          
                 
               
                

            
                
               
                