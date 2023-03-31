import random


#Brant Cass
# this program generates random numbers for 2 balls to input it into a bowling game and then prints out the summary
#date: 5/4/21
#functions: roll_ball(), roll_frame(), play_game(), print_game() 




def main():
    
    frame_played = list()
    frame_list = list()
    question = str()
    Error = str()
    file = str()
    
    file = open('score_board.txt', 'w+')

    print("Hello! Welcome to the lanes.")

    Name = str(input("Enter your name: "))
    print('Hello', Name)
   

    play_again = str(input("Would you like to bowl?\nType (Yes) or (No): ")).lower()

    try:
#loop for playing the game again
        while play_again != 'no':
            

            if play_again == 'yes':
                question = str(input("\nWould you like a printed version of the game summary? (Yes) or (No) ")).lower()
                
                if question == 'yes':
                    print_game( frame_played )

                elif question == 'no':
                    play_game(frame_list)
            
                play_again = str(input("Would you like to play again?\nType (Yes) or (No): ")).lower()
#end if
            elif play_again == 'no':
                print('Goodbye!, {Name}')

            else:
                print('Something messed up.')
                play_again = str(input("Would you like to play again?\nType (Yes) or (No): ")).lower()
       #end if

#end while loop
                          
    except ValueError as Error:
        print(Error)

    return
frame_list = list()
#passing arguemnts ball and pins to be able to roll the ball as well as set it back to 0
def roll_ball( ball, pins ):
    ball = int()
    
    ball = random.randint(1,pins)

    return ball

# end roll_ball()

def roll_frame( frame_list ):
    frame_counter = int()
    balls = list()
    ball = int()
    pins = 10
    round_1 = int()
    round_2 = int()
    frame_total = int()
    frame_list = list()
    pins_left = int()




    # roll ball
    round_1 = roll_ball( ball, pins )
    #calculate roll
    pins_left = pins - round_1

    if pins_left == 0:
        frame_total = 10
    elif pins_left > 0:
        round_2 = roll_ball( ball, pins_left )
        pins_left = round_1 + round_2
        frame_total = round_1 + round_2
        if pins_left == 10:
            frame_total = 10
        elif round_1 == 0 and round_2 == 0:
            frame_total = 0
        elif pins_left != 10:
            frame_total = (round_1 + round_2)
        # End if
    else:
        frame_total = round_1 + round_2


    # End if

    frame_list = [ round_1, round_2, frame_total ]




    return frame_list


# roll_frame( )

def play_game( frame_list ):
    frame_counter = int()
    score_total = int()
    frame_played = list()
    frame_total = int()
    frame_list = list()
    items_list = int()
    statment = str()
    statment_list = list()
    
#putting score into file
    
    for items_list in range( 10 ):

        frame_counter += 1

        frame_list = roll_frame( frame_list )


        frame_total = frame_list[2]

        score_total = score_total + frame_total
        
        frame_list.append(score_total)
        
        frame_played.append(frame_list)


       


#printing totals

            # If variables for round types
        print(f"\n*** Frame { frame_counter } ***\n")
        if frame_list[0] == 10:
            print(f"Ball One: { frame_list[0] }.... Wow! You got a strike!")
            statment = (f"\n*** Frame { frame_counter } ***\nBall One: { frame_list[0] }.... Wow! You got a strike!")
            frame_played.append(statment)

        elif frame_list[0] + frame_list[1] == 10:
            print(f"Ball One: { frame_list[0] }")
            print(f"Ball Two: { frame_list[1] }.... Wow, you got a spare!")

            statment = (f"\n*** Frame { frame_counter } ***\nBall One: { frame_list[0] }\nBall Two: { frame_list[1] }.... Wow, you got a spare!")
            frame_played.append(statment)

        elif frame_list[0] < 10 and frame_list[1] < 10:
            print(f"Ball One: { frame_list[0] }")
            print(f"Ball Two: { frame_list[1] }.... Look... Maybe you should practice. Open frame.")

            statment = (f"\n*** Frame { frame_counter } ***\nBall One: { frame_list[0] }\nBall Two: { frame_list[1] }.... Look... Maybe you should practice. Open frame.")
            frame_played.append(statment)

        elif frame_list[0] == 0 and frame_list[1] == 0:
            print(f'.... Uhhh.... bowl much?')

        # End if

        #### PRINTED TOTALS FOR USER TERMINAL ####
        print('= '*10)
        print(f"Frame Total: { frame_list[2] }")
        print(f"Total Score: { score_total }")
        print('= '*10)



    # End for


#### SCORE BOARD FOR USER TERMINAL ####

    print("\nFRAME\t\tBALL ONE\tBALL TWO\tFRAME TOTAL\tGAME SCORE\n")

    print(f"\n  1\t\t   { frame_played[0][0] }\t\t   { frame_played[0][1] }\t\t    { frame_played[0][2] }\t\t    { frame_played[0][3] }")
    print(f"\n  2\t\t   { frame_played[2][0] }\t\t   { frame_played[2][1] }\t\t    { frame_played[2][2] }\t\t    { frame_played[2][3] }")
    print(f"\n  3\t\t   { frame_played[4][0] }\t\t   { frame_played[4][1] }\t\t    { frame_played[4][2] }\t\t    { frame_played[4][3] }")
    print(f"\n  4\t\t   { frame_played[6][0] }\t\t   { frame_played[6][1] }\t\t    { frame_played[6][2] }\t\t    { frame_played[6][3] }")
    print(f"\n  5\t\t   { frame_played[8][0] }\t\t   { frame_played[8][1] }\t\t    { frame_played[8][2] }\t\t    { frame_played[8][3] }")
    print(f"\n  6\t\t   { frame_played[10][0] }\t\t   { frame_played[10][1] }\t\t    { frame_played[10][2] }\t\t    { frame_played[10][3] }")
    print(f"\n  7\t\t   { frame_played[12][0] }\t\t   { frame_played[12][1] }\t\t    { frame_played[12][2] }\t\t    { frame_played[12][3] }")
    print(f"\n  8\t\t   { frame_played[14][0] }\t\t   { frame_played[14][1] }\t\t    { frame_played[14][2] }\t\t    { frame_played[14][3] }")
    print(f"\n  9\t\t   { frame_played[16][0] }\t\t   { frame_played[16][1] }\t\t    { frame_played[16][2] }\t\t    { frame_played[16][3] }")
    print(f"\n  10\t\t   { frame_played[18][0] }\t\t   { frame_played[18][1] }\t\t    { frame_played[18][2] }\t\t    { frame_played[18][3] }")

    return frame_played



def print_game( frame_played ):
    round_counter = int()
    frame_counter = int()
    score_total = int()
    items_list = int()


    frame_played = play_game( frame_list)

#exception for file errors 

    try:

#appending information to file

        with open("score_board.txt", "a") as file:
            file.write(frame_played[1])
            file.write(frame_played[3])
            file.write(frame_played[5])
            file.write(frame_played[7])
            file.write(frame_played[9])
            file.write(frame_played[11])
            file.write(frame_played[13])
            file.write(frame_played[15])
            file.write(frame_played[17])
            file.write(frame_played[19])
            file.write("\n")


            
           

            file.write("\nFRAME\t\tBALL ONE\t\tBALL TWO\t\tFRAME TOTAL\tGAME SCORE\n")
            
            file.write(f"\n  1\t\t  {frame_played[0][0]}\t\t   {frame_played[0][1]}\t\t    {frame_played[0][2]}\t\t    {frame_played[0][3]}\n")
            file.write(f"\n  2\t\t  {frame_played[1][0]}\t\t   {frame_played[1][1]}\t\t    {frame_played[1][2]}\t\t    {frame_played[1][3]}\n")
            file.write(f"\n  3\t\t  {frame_played[2][0]}\t\t   {frame_played[2][1]}\t\t    {frame_played[2][2]}\t\t    {frame_played[2][3]}\n")
            file.write(f"\n  4\t\t  {frame_played[3][0]}\t\t   {frame_played[3][1]}\t\t    {frame_played[3][2]}\t\t    {frame_played[4][3]}\n")
            file.write(f"\n  5\t\t  {frame_played[4][0]}\t\t   {frame_played[4][1]}\t\t    {frame_played[4][2]}\t\t    {frame_played[4][3]}\n")
            file.write(f"\n  6\t\t  {frame_played[5][0]}\t\t   {frame_played[5][1]}\t\t    {frame_played[5][2]}\t\t    {frame_played[5][3]}\n")
            file.write(f"\n  7\t\t  {frame_played[6][0]}\t\t   {frame_played[6][1]}\t\t    {frame_played[6][2]}\t\t    {frame_played[6][3]}\n")
            file.write(f"\n  8\t\t  {frame_played[7][0]}\t\t   {frame_played[7][1]}\t\t    {frame_played[7][2]}\t\t    {frame_played[7][3]}\n")
            file.write(f"\n  9\t\t  {frame_played[8][0]}\t\t   {frame_played[8][1]}\t\t    {frame_played[8][2]}\t\t    {frame_played[8][3]}\n")
            file.write(f"\n  10\t\t {frame_played[9][0]}\t\t   {frame_played[9][1]}\t\t    {frame_played[9][2]}\t\t    {frame_played[9][3]}\n")

            file.close()
            
    except Exception as Error:
        print("Error:", Error)

    return

main()






#find a way to not call the function when appending the list to the file (line 197)
#change stuff up
#fix 'would you like a game summary' to a try statment so it will only accept strings and or yes/no
#change spacing (/t) for the game summary to make it look better
