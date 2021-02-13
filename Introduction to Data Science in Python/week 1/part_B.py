import re
def grades():
    with open('assets/grades,txt', 'r') as file:
        grades=file.read()

    names_B=[]
    for item in re.finditer('(?P<name>.*)(\: B)', grades):
        names_B.append(item.group('name'))
    return names_B