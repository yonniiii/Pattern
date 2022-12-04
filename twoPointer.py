def runTwoPointer(arr):
    left = 0
    right = len(arr)-1

    while left < right:
        ## do some logic
        '''
        1. left ++
        2. right --
        3. left++ and right--
        '''

def checkIfPalindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] !=s[right]:
            return False
        left +=1
        right -=1
    return True

print(checkIfPalindrome('ABCBA'))