import re
def logs():
    with open ('assets/logdata.txt', 'r') as file:
        logdata=file.read()
    
    l=[]
    pattern='''
    (?P<host>.*)
    (\ -\ )
    (?P<user_name>.*)
    (\ \[)
    (?P<time>.*)
    (\]\ \")
    (?P<request>.*)
    (\") '''
    for item in re.finditer(pattern, logdata, re.VERBOSE):
        l.append(item.groupdict())
    return l

