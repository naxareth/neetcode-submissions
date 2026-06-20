class Solution:
    def isValid(self, s: str) -> bool:
        match = {")": "(", "]": "[", "}": "{"} # Create a list of matching parenthesis
        stack = [] # Create a variable to store opening parenthesis

        for char in s: # Loop through each parenthesis from the input
            if char in match: # IF the parentheses is a closing
                if not stack:
                    return False
                compare = stack.pop() # Get the parentheses from the stack variable
                if compare != match[char]: # Then compare the current parenthesis to the stack if theyre not matching
                    return False # Not matching
            else:
                stack.append(char) # Else just put it in the stack cuz its an opening parenthesis
        return  not stack # Empty stack means all brackets were matched