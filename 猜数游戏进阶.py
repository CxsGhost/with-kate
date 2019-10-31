import random
the_secret=random.randint(0,10)
input_history_1=[]
input_history_2={}
answer_right=False
game_state=True

user_action_1=input("play game or Esc(input 'play'or'Esc'):")
if user_action_1=="Esc":
    game_state=False
    print("game over!")

elif user_action_1=="play":
     while game_state:
        user_action_2=input("check the records or guess(input 'guess'or'check'):")
        if user_action_2=="check":
            if input_history_2=={} and input_history_1==[]:
                print("you have not played game,there are no records!")
            else:
                which_times=input("get all or one(input 'get all'or'one'):")
                if which_times=="get all":
                    print(input_history_1)
                elif which_times=="one":
                    number=int(input("which one you want to check:"))
                    print("this times your guess:",input_history_2[number-1])
        elif user_action_2=="guess":
            while not answer_right:
                times=1
                user_answer=int(input("please input:"))
                input_history_1.append(int(user_answer))
                input_history_2[times]=int(user_answer)
                if user_answer==the_secret:
                    answer_right=True
                    game_state=False
                    print("you get it!",end=" ")
                    print("game over")
                else:
                    print("this is wrong!")
                break
            continue
else:
    print("sorry input wrong")
