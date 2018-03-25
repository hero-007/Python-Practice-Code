# Regular expression is a small programming language  of it own kind.
# It is useful to pull some data from string.

'''
Identifiers
\d any number
\D any thing but a number
\s space
\S anything but a space
\w any character
\W anything but a character
.  anything except a new line
\b the whitespace around words
\. a period


Modifiers:
{1,3} we're expecting 1-3 ex: \d{1,3}
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ Match the end of the string
^ Match the begining of a string
| either or
[] range or 'variance' [A-Za-z1-5]
{x} expecting 'x' amount

White Space Characters:
\n new line
\s space
\t tab
\e escape
\f form feed
\r return

Don't Forget:
. + * ?[ ] $ ^ ( ) | \ { }
'''

import re

exampleString = '''
Hero is 20 years old, and Daniel is 27 years old.
Edwardo is 97, and his grandfather, Oscar, is 102.
'''

# we want to extact names and ages from the exampleString


ages = re.findall(r'\d{2,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)

dict_a = {}
for i in range(0,len(names)):
    dict_a[names[i]]=ages[i]

print(dict_a)




