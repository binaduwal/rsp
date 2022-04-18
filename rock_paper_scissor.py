#rock vs scissor->rock
# scissor vs paper->scissor
# paper vs rock->paper
count=0 
player1_score=0   
player2_score=0 
player1_name=input("Enter your name Player1:") 
player2_name=input("Enter your name Player2:") 
while (count<3):
    print(player1_name,end=',')
    player1=input("Press 'r' for rock ,'p'for paper and 's' for scissor:")
    print(player1)
    print(player2_name,end=',')
    player2=input( "Press 'r' for rock ,'p'for paper and 's' for scissor:")
    print(player2)
    if (player1=='r' and player2=='s'):
        print(f"{player1_name} won.")
        player1_score=+player1_score
    elif (player1=='r' and player2=='p'):
        print(f"{player2_name} won.")
        player2_score=+player2_score
    elif (player1=='p' and player2=='s'):
        print(f"{player2_name} won.")
        player2_score=+player2_score
    elif (player1=='p' and player2=='r'):
        print(f"{player1_name} won.")
        player1_score=+player1_score
    elif (player1=='s' and player2=='r'):
        print(f"{player2_name} won.")
        player2_score=+player2_score
    elif (player1=='s' and player2=='p'):
        print(f"{player1_name} won.")
        player1_score=+player1_score
    elif(player1==player2):
        print("It's draw.")
    else:
        print("Invalid input.")
        print("Please enter 'r' for rock ,'p'for paper and 's' for scissor")
    count=count+1  #count is incremented by 1
    chance=3-count
    print(f"You have {chance} chance left")
    print("-----------------------------------------------------------")
print("Game Over.")
print( player1_name," score is",player1_score)   #(,/+)
print( player2_name+"score is",player2_score)
if (player1>player2):
    print("-------------------------------------------")
    print(f"Congratulation!! {player1_name} won the game.")
    print("-------------------------------------------")
elif((player1<player2)):
    print("-------------------------------------------")
    print(f"Congratulation!! {player2_name} won the game.")
    print("-------------------------------------------")
elif((player1==player2)):
    print("-------------------------------------------")
    print("It's draw.")
    print("-------------------------------------------")
print(" ")
print("Play again?")













 

