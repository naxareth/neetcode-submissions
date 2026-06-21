from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Store the strings
        result = defaultdict(list)

        # Loop through each strings
        for word in strs:

            # Sort the letters in the word alphabetically then join them
            sortedword = "".join(sorted(word))

            # Store the sorted words in the result variable
            result[sortedword].append(word)

            # Show the grouped anagrams
        return list(result.values())