import re
from os.path import dirname

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
moad_sd.pc@delj.com
moad-sd.pc12@delj23.com
moad-sd.pc12@delj23.eu
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

def read_sample_file():
    try:
        with open( dirname(__file__)+"\\"+'pattern-test.txt','r', encoding='utf-8') as f:
            conttent = f.read()
            return conttent
    except Exception as e:
        print(str(e))
        return ''
       

#pattern to test
pattern = re.compile(r'Mr') #r - givs raw example "\tno" will be '    no"
pattern = re.compile(r'\.aaaa') #only dot (\) - escape character

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

pattern = re.compile(r'[89]0\d[.-]\d\d\d[.-]\d\d\d\d')

pattern = re.compile(r'[a-zA-Z-0-9_.-]+@[a-zA-Z-0-9_.-]+\.(com|net|edu)') #only emails from domain com net or edu

#finditter to get itteration object
matches = pattern.finditer(text_to_search)

#matches = pattern.finditer(read_sample_file())


search_and_print(matches)


def check_username_pattern(username):
    """ Check if the pattern is corrct for the username name.
    Arguments:
        :username: name to check in the given pattern
    """
    username_pattern = re.compile(r'[^[0-9_]\w+') #cannot start from letter only word
    return username_pattern.fullmatch(username) #fullmatch search at start

#print('check:', check_username_pattern('0testme'))
#print('check 2',check_username_pattern('testme0'))
