# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
# neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.
# test.assert_equals(disemvowel("This website is for losers LOL!"),
#                               "Ths wbst s fr lsrs LL!")

def disemvowel():
    # string = 'This website is for losers LOL!'
    string = 'What are you, a communist?'
    # string = 'No offense but,\nYour writing is among the worst I\'ve ever read'
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    new_string = []
    for i in string:
        if i not in vowels:
            new_string.append(i)
    new_string = ''.join(new_string)
    print(new_string)
    return new_string
