class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        TAKEAWAYS:
        - ultimate aim is to check the string's length and frequenices are same by any order.
        - 'using Up' - occurrence of the character that was originally found in string s.
        """
        if len(s) != len(t):
           return False    # if length dont match they are not anagram.
        
        trace = {}
        for letter in s:
            trace[letter] = trace.get(letter, 0) + 1 # collect character frequenices.

        for letter in t:
            if letter not in trace: # check if the letter present in t but in s.
                return False

            trace[letter] -= 1 # loop goes through t, if letter is found in trace (s) its decremented (using-up). 
            if trace[letter] < 0: # next step the frequency must be 0, if negative then False. 
                return False

        return True

              
        



    
            
        