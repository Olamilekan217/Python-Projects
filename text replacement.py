sentence=input("Enter a sentence:  ")
print(sentence)

alt_sentence=input("\nOops! You made a mistake?\nWe gat you covered\nKindly reply \033[1m\"yes\" \033[0mto help you replace  ")

if alt_sentence == "yes":
    replace_word=input("\nEnter word to replace:  ")

    correct_word=input("\nEnter replacement word:  ")

    print(sentence.replace(replace_word, correct_word))
    
else:
    print("\nYou haven't made any mistake")
    
