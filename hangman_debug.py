
from word import *
from images import*

def is_word_guessed(secret_word, letters_guessed):
  if secret_word == get_guessed_word(secret_word, letters_guessed):
      return True
  return False
def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word
def get_available_letters(letters_guessed):
    
    import string
    letters_left = string.ascii_lowercase

    return letters_left

def hangman(secret_word):
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

    letters_guessed = []
    

    available_letters = get_available_letters(letters_guessed)
    
    print("Available letters: " + available_letters)
    print("Remember it you have only 8 chance to playing this game", "(if you will guess wrong then only your chance decrease)")
    status=input("easy or normal or hard=")
    #hint=input("Do you want hint press yes or not=")
    if status == "easy":
      print("Hello , you choosed easy status so will get 8 chance")
      
      i=0
      chance=8
      while i<8:
        # hint=input("Do you want hint press yes or not=")
        # if hint=="yes":
        #     print((get_guessed_word(secret_word,letters_guessed))
        guess =input("Please guess a letter=")
        letter = guess.lower()
        if letter in secret_word:
          letters_guessed.append(letter)
          print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
          print ("")
          if is_word_guessed(secret_word, letters_guessed) == True:
            print("Congratulations , You won ! This is 🥇for you")
            print("")
            break
        else:
            print("Oops! That letter is not in my word:") # + get_guessed_word(secret_word, letters_guessed))
            letters_guessed.append(letter)
            print("")
            chance=chance-1
            if(chance ==0):
                print("Soory your guess is wrong , you lost")
            print("Your remaining chance is =",chance)
            if chance==7:
                print(IMAGES[1])
            if chance==6:
                print(IMAGES[2])
            if chance==5:
                print(IMAGES[3])
            if chance==4:
                print(IMAGES[4])
            if chance==3:
                print(IMAGES[5])
            if chance==2:
                print(IMAGES[6])
            if chance==1:
                print(IMAGES[7])
            if chance==0:
                print(IMAGES[8])
            i=i+1
    if status=="normal":
      print("hello , you choosed normal status so you will get 6 chance")
      chance=6
      i=0
      while i<6:
        guess =input("Please guess a letter=")
        letter = guess.lower()
        if letter in secret_word:
          letters_guessed.append(letter)
          print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
          print ("")
          if is_word_guessed(secret_word, letters_guessed) == True:
            print("Congratulations , You won ! This is 🥇 for you")
            print("")
            break
        else:
            print("Oops! That letter is not in my word: ")# + get_guessed_word(secret_word, letters_guessed))
            letters_guessed.append(letter)
            print("")
            chance=chance-1
            if(chance ==0):
                print("Soory your guess is wrong , you lost")
            print("Your remaining chance is =",chance)
            if chance==7:
                print(IMAGES[1])
            if chance==6:
                print(IMAGES[2])
            if chance==5:
                print(IMAGES[3])
            if chance==4:
                print(IMAGES[4])
            if chance==3:
                print(IMAGES[5])
            if chance==2:
                print(IMAGES[6])
            if chance==1:
                print(IMAGES[7])
            if chance==0:
                print(IMAGES[8])
            i=i+1

    if status=="hard":
      print("Woww 😇 you choosed hard status so you will get 4 chance")
      chance=4
      i=0
      while i<4:
        guess =input("Please guess a letter=")
        letter = guess.lower()
        if letter in secret_word:
          letters_guessed.append(letter)
          print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
          print ("")
          if is_word_guessed(secret_word, letters_guessed) == True:
            print("Congratulations , You won ! This is 🏆🥇for you")
            print("")
            break

        else:
            print("Oops! That letter is not in my word: ")# + get_guessed_word(secret_word, letters_guessed))
            letters_guessed.append(letter)
            print("")
            chance=chance-1
            if(chance ==0):
                print("Soory your guess is wrong , you lost")
            print("Your remaining chance is =",chance)
            if chance==7:
                print(IMAGES[1])
            if chance==6:
                print(IMAGES[2])
            if chance==5:
                print(IMAGES[3])
            if chance==4:
                print(IMAGES[4])
            if chance==3:
                print(IMAGES[5])
            if chance==2:
                print(IMAGES[6])
            if chance==1:
                print(IMAGES[7])
            if chance==0:
                print(IMAGES[8])
            i=i+1
secret_word =choose_word()
hangman(secret_word)