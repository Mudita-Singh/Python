import re
'''list = ["guru99 get" , " guru99 give" , "guru selenium"]
for element in list :
    z = re.match("(g\w+)\W(g\w+)" , element )
    if z:
        print ((z.groups()))'''

sentence = 'we are humans'
matched = re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.groups())

sentence = 'we are humans'
matched = re.match(r'(.*) (.*?) (.*)', sentence)
print(matched.group(2))

sentence = 'horses are fast'
regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
matched = re.search(regex, sentence)
print(matched.groupdict())

sentence = 'horses are fast'
regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
matched = re.search(regex, sentence)
print(matched.groups())




