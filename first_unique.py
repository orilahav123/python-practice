def first_unique(words):
        
    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
            
    
    for word in words:
        if counts[word] == 1:
            return word
    return None
 
                      