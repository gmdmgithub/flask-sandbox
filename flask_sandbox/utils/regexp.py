import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

def search_and_print(mathces):
    for match in matches:
        print('match',match)
    print('mathes:',matches)

pattern = re.compile(r'Mr') #r - givs raw example "\tno" will be '    no"
pattern = re.compile(r'\.aaaa') #only dot (\) - escape character

matches = pattern.finditer(text_to_search)

search_and_print(matches)




def check_username_pattern(username):
    """ Check if the pattern is corrct for the username name.

    Arguments:
        :username: name to check in the given pattern
    """

    print('username to test:',username)
    username_pattern = re.compile(r'[^[0-9_]\w')
    return username_pattern.match(username)

print('username test:',check_username_pattern('test'))

