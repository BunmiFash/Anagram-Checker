running = True
while running:
    print("Welome to Bunmi's Anagram checker")
    print("Check if your words are anagrams in seconds!")    
    def find_anagram(word1, word2):
       
        #Remove spaces on both sides
        word1 = word1.strip()
        word2 = word2.strip()

        # Convert both words into lowercase
        word1 = word1.lower()
        word2 = word2.lower()

        #Split words
        word1 = word1.split()
        word2 = word2.split()

        # check word lenghth
        word1 = len(word1) 
        word2 = len(word2)

        if word1 == word2:
            return ("The words are anagrams!")
        else:
            return ("These words are not anagrams.")    


    input_word1 = input("Enter First Word: ")
    input_word2 = input("Enter Second Word: ")
    result = find_anagram(input_word1, input_word2)    
    print(result)

    option = input("Would you like to repeat the check? ")
    if option == "Yes" or "yes":
        pass
    if option == "No" or "no":
        running = False