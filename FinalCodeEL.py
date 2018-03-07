import random
turns = 6
def Hangman():
    global turns
    name = raw_input("What is your name? ")
    print "Hello, " + name, "Time to play hangman!"
    print "Start guessing..."
    WORDS = ("secret", "python", "computer", "landfried", "keyboard", "mouse")
    word = random.choice(WORDS)
    guesses = ''
    turns = 6  
    while turns > 0:         
        failed = 0  
        HangmanGraphics()           
        for char in word:      
            if char in guesses:    
                print char,    
            else:
                print "_",     
                failed += 1    
        if failed == 0:        
            print "You won"  
            break              
        print
        print guesses
        guess = raw_input("guess a character:") 
        guesses += guess                    
        if guess not in word:  
            turns -= 1        
            print "Wrong"    
            print "You have", + turns, 'more guesses' 
            if turns == 0:           
                print "You Lost"
                print"the word was:"
                print(word)
        
    
def HangmanGraphics():
    global turns
    if turns == 0:
        print '''
                +---+
                |   |
                O   |
               /|\  |
               / \  |
                    |
                ========='''

    if turns == 1:
        print'''
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
                ========='''
    if turns == 2:
        print  '''
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
                ========='''
    if turns == 3:
        print'''
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
                ========='''
    if turns == 4:
        print'''
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                ========='''
    if turns == 5:
        print '''
                +---+
                |   |
                O   |
                    |
                    |
                    |
                ========='''
    if turns == 6:
        print '''
                +---+
                |   |
                    |
                    |
                    |
                    |
                ========='''

    
                    
    
        
    
                
    
        