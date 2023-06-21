def palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

string = input()
print(palindrome(string))