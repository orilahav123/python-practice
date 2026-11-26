def is_anagram(a, b):
    if a == "" or b == "":
        raise ValueError("Nothing was typed")
    return sorted(a.lower()) == sorted(b.lower())
        
print(is_anagram("listen", "silent"))   
print(is_anagram("hello", "world"))  
print(is_anagram("aab", "abb"))         

