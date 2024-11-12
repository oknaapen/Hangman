from random_word import RandomWords
r = RandomWords()



# Choose random word
random_woord = r.get_random_word()

#make list of all letters in word
code = list(random_woord)  # voorbeeld woord

#list to save the letters
geraden = ['_'] * len(code)
print(' '.join(geraden))



#function hangman
def raad():

#Hangman list
    man = [r'''_______
             |     |
             |    
             |
             |
             |
             |
             |___ 
    ================
    ''' ,r''' _______
            |     |
            |    (
            |     
            |
            |
            |
            |___
    ''' ,r'''_______
           |     |
           |    (_
           |     
           |     
           |
           |
           |___
    ================
    ''' ,r'''_______
           |     |
           |    (_)
           |    
           |     
           | 
           |
           |___
    ================
    ''' ,r'''_______
           |     |
           |    (_)
           |     | 
           |     |
           |    
           |
           |___
    ================
     ''',r'''_______
           |     |
           |    (_)
           |   \ | 
           |     |
           |     
           |
           |___
    ================
     ''',r'''_______
           |     |
           |    (_)
           |   \ | /
           |     |
           |     
           |
           |___
    ================
     ''',r'''_______
           |     |
           |    (_)
           |   \ | /
           |     |
           |    / 
           |
           |___
    ================
     ''',r'''_______
           |     |
           |    (_)
           |   \ | /
           |     |
           |    / \
           |
           |___
    ================
     ''']


#turn
    guess = []
    beurt = 0
    #make the loop for the guessing
    while "_" in geraden and beurt < 8:
      # Ask for new letter or ask for guessing the right word
      vraag = input("Denk je het woord te weten? Type dan: 'ik weet het antwoord', anders typ één letter ")
      if vraag == "ik weet het antwoord":
        antwoord = str(input("Geef het woord maar"))
        if antwoord == random_woord: #Check if specified word is correct
          print("Ja dit is het woord")
          break
        else:
          beurt += 1
          print(man[beurt])
          print(' '.join(geraden))
          print(f"geraden letters: {guess}")
      elif vraag in code:  #if letter is in word
        for count, ele in enumerate(code):
          if vraag == ele:
            guess.append(vraag)
            geraden[count] = ele  # Change underscore for the letter
            print(' '.join(geraden))  # Toon de huidige status van het woord
            print(f"geraden letters: {guess}")
      elif vraag == code and len(vraag) > 1:
           print("Je hebt het woord geraden!")
      else:
         print(f"{vraag} zit niet in het woord")  # Foutmelding als de letter niet in het woord zit
         guess.append(vraag)
         beurt += 1
         print(man[beurt])
         print(f"geraden letters: {guess}")
         print(' '.join(geraden))  # Toon de huidige status van het woord
    print("je hangt")
    print(random_woord)



raad()



