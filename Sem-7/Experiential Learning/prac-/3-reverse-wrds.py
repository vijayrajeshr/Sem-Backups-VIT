def reverse_words(sentence):
    
    spl_str = sentence.split()
    rev_res = spl_str[::-1]
    fin = " ".join(rev_res)
    
    return fin
