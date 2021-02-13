import re
def names():
    simple_string='''Amy is 5 years old, and her sister Mary is 2 years old.
    Ruth and Peter, their parents, have 3 kids.'''

    name_list=re.findall('[A-Z][\w]*', simple_string)
    return name_list

print(names())