class Solution:
    """
    TAKEAWAYS:
    pointers:-
    - current_index:- acts as the main pointer or read head for the entire
    encoded string s. Its purpose is to keep track of where we are currently reading in the input string.

    - hash_index:- a temporary pointer used within each iteration of the outer loop. To 
    find the position of the # delimiter that separates the string's length from the original string. 

    while loops:
    - outer:- to iterate through the encoded string s and process each length-prefixed string segment one by one,
    for decoding one original string from the s.
    - inner:- to extract the numeric length of the current string. by starting hashIndex at currIndex and 
    incrementing it until it finds the # character.
    """

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for char in strs: # encoding a list of strings to one with its length + delimiter + original.
            encoded.append(str(len(char)) + '#' + char)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        current_index = 0

        while current_index < len(s):
              hash_index = current_index

              while s[hash_index] != '#': # the goal here is get the position of delimiter, then only will proceed.
                    hash_index += 1

              length = int(s[current_index:hash_index]) # extracts the number i.e., length which is before the #.

              string_start = hash_index + 1 # as per pattern, string begins right after #.
              string_end = string_start + length

              string_out = s[string_start:string_end]
              decoded.append(string_out)

              current_index = string_end # move the pointer to the next segment after current string.

        return decoded      

