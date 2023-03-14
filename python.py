theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

#this is a dictionary function, each key represents a space on the board while each value represents a move made the by the player. 

#this is defining the print function, allowing the board to be printed and updated
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

    #defines that this is coding for a game
    def game():

    turn = 'X'
    count = 0
    
#for is a loop function will iterate until the count = 10, the range represents the sequence of numbers, so numbers 1-9 are the ammount of moves that can be made within a game
    for i in range(10):
    # i indicates the ammount of turns taken 
            printBoard(theBoard)
            print("It's your turn," + turn + ".Move to which place?")

            #the input function is when the user makes their move, converting that input data into a sting.
            move = input()        
            #excutes a function if the condition is meet, if will count a move and place an X or O if the space the user slected is free
            if theBoard[move] == ' ':
                theBoard[move] = turn
                #the users move will counted and 'i' will change values until it reaches the range of 10
                count += 1
            #based on the if function, if the space selected is filled the else function will tell the user to pick again
            else:
                print("That place is already filled.\nMove to which place?")
                #will tell the code to iterate to the next function in the list
                continue
  #the winning combinations have to be excuted within 5 moves
  if count >= 5:
            #if one player has all moves across the top then the game will end, and print who won
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****") 
                #if a condition is met then the loop will stop                
                break
            #if there are many condtions that can be excuted elif will be used rather then if or else
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins within 9 moves, and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X' 
