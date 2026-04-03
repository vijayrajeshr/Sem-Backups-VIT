#exercise : 

def count_votes(votes_list):
  count = {}
  for name in range (len(votes_list)):
      if name in count:
          count[name]+=1
      else:
          count[name]=1
          
      return count
