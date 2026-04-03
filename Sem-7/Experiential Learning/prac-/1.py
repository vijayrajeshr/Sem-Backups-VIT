class Solution(object):
    def reverseWords():
        s = input("entter the sentence : ")
        word_list = s.split()
        print(word_list)
        
        rev_word = word_list.reverse()
        
        res = " ".join(rev_word)
        
        print(res)
        
        
    reverseWords()
        
        