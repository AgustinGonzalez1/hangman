import random

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
      "C",
      "PYTHON",
      "JAVA",
      "JAVASCRIPT",
      "PHP",
      "RUBY",
      "PERL",
      "SWIFT",
    ]
    
    word = random.choice(DB)
    
    spaces = ["_"] * len(word)
    
    lives = 6
    
    while lives > 0:
        print(IMAGES[lives])
        print("".join(spaces))
        
        guess = input("guess a letter: ").upper()
        
        if guess in word:
            index = 0
            for letter in word:
                if letter == guess:
                    spaces[index] = guess
                index += 1
        else:
            lives -= 1
            print("wrong guess")
            print(f"you have {lives} lives left")
            
        if "_" not in spaces:
            print("you win")
            break
          
    print("you lose")
    
    print("the word was", word)
    
    print("thank you for playing")
    
    

if __name__ == "__main__":
  run()