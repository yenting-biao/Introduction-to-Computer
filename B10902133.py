class Judge:
    def __init__(self, answer: str) -> None:
        """
        Set the answer as the attribute of Judge
        answer: (int) the final answer
        """
        self.answer = int(answer) 

    def guess(self, num: str) -> bool:
        """
        Method that guess the number, it'll print info that shows:
            Your guess is ...; the result is xAxB
            e.g.: Your guess is 0123; the result is 0A1B
        num: the number that it guessed
        return: whether the player guess the correct answer
        """
        if self.answer == int(num):
            print(f"Your guess is {num}; the result is 4A0B")
            return True
        else:
            length=len(num)  

            digit=[int(num[i]) for i in range(length)]
            ans=[int(str(self.answer)[i]) for i in range (length)]

            A=0
            B=0
            for i in range(length):
                if(digit[i]==ans[i]):
                    A+=1
            for i in range (length):
                for j in range (length):
                    if(i!=j):
                        if(digit[i]==ans[j]):
                            B+=1
            print(f"Your guess is {num}; the result is {A}A{B}B")

            return False

        


def read_input(guess_len: int) -> str:
    
    """
    Function that read player's guess.
    guess_len: length the the player should guess. it would be same as the length of answer
    return: the valid string guessed by player
    You should show the hint message:
        "Enter your guess:\n"
    If the player's guess is invalid, you should print:
        "Invalid, please enter your guess again:\n"
    Note: a valid guess means contain only guess_len non-repetitive integer range from 0~9
    """

    while True :
        player_guess=input("Enter your guess:\n")
        length=len(player_guess)

        if (length != guess_len) :
            print("Invalid, please enter your guess again:\n")
            continue

        appeared=[False for i in range (10)]
        valid=True
        for i in range (length) :
            if(player_guess[i].isdigit()):
                if appeared[int(player_guess[i])] :
                    valid=False
                    break
                else:
                    appeared[int(player_guess[i])]=True
            else:
                valid=False
                break
        
        if(not valid):
            print("Invalid, please enter your guess again:\n")
            continue
        else:
            break
        
    return player_guess
    


def enter_answer() -> str:
    """
    Function that enter the answer, you can assume that the answer must be valid.
    """
    return input()





"""
main function
"""

if __name__ == "__main__":
    answer = enter_answer()
    print(f"The length of answer is {len(answer)}")
    judge = Judge(answer=answer)

    while True:
        guess_num = read_input(len(answer))

        if judge.guess(guess_num):
            break

    print("Finish!!!")