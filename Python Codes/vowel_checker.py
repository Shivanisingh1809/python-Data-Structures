def check_vowel(string, vowels):
     
    # casefold has been used to ignore cases
    string = string.casefold()
     
    # Forms a dictionary with key as a vowel
    # and the value as 0
    count = {}.fromkeys(vowels, 0)
    sum = 0 
    # To count the vowels
    for character in string:
        if character in count:
            sum += 1   
    return sum
     
# Driver Code
vowels = 'aeiou'
print("Vowel letter count")
print("Input string : ")
string = input()
print ("There are ", check_vowel(string, vowels), " vowel characters")