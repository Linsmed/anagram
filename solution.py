# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(len(word) == len(anagram)):
        sorted_word =sorted(word)
        sorted_anagram = sorted(anagram)
        if(sorted_word == sorted_anagram):
            return True
        else:
            return False
print(find_anagram("mosque", "church"))

print(find_anagram("car", "arc"))
