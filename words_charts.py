# Open the file in read mode 
text = open('words.txt', 'r')
#print(text) wrong
  
# Create an empty dictionary 
dico = dict() 
  
# Loop through each line of the file 
for line in text: 
    # Remove the leading spaces and newline character 
    line = line.strip() 
  
    # Convert the characters in line to  
    # lowercase to avoid case mismatch 
    line = line.lower() 
  
    # Split the line into words 
    words = line.split(" ") 
    
    #print(words)
  
    # Iterate over each word in line 
    for word in words: 
        # Check if the word is already in dictionary 
        if word in dico: 
            # Increment count of word by 1 
            dico[word] = dico[word] + 1
        else: 
            # Add the word to dictionary with count 1 
            dico[word] = 1


#      donner un ordre decroissant au dictionnaire

for pair in sorted(dico.items(), key=lambda t:t[-1], reverse=True):
    print(pair)

print('\n')

#      celui avec le plus d'apparition

bigcount = None
bigword = None

for word, count in dico.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print("the word with the biggest number of apparitions is => " + bigword + " <= with %d apparitions.\n" %bigcount)

#      celui demandé par l'utilisateur



while True:

    userword = input("Type the word you're looking for or 'stopper' to stop the loop: ")

    if userword in dico:
        print(userword, dico[userword])
        print('\n')
    elif userword == 'stopper':
        print('END\n')
        break
    else:
        print(userword, "is not in the dictionnary\n")