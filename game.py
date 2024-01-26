import random
import os


def run():

    IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========''']
  
    DB = [

      "PYTHON",

      "JAVASCRIPT",
    ]
    
    word = random.choice(DB)
    
    spaces = ["_"] * len(word)
    
    lives = 0
    
    
    while True:
        print(IMAGES[lives])
        print("".join(spaces))
        
        guess = input("guess a letter: ").upper()
        
        os.system("cls")
        
        if guess in word:
            index = 0
            for letter in word:
                if letter == guess:
                    spaces[index] = guess
                index += 1
        else:
            lives += 1
            print("wrong guess")
            print(f"you have {6 - lives} lives left")
            
        if "_" not in spaces:
            print("you win")
            break
          
        if lives == 6:
            print("you lose")
            break
    
    print("the word was", word)
    
    print("thank you for playing")
    
    

if __name__ == "__main__":
  run()
