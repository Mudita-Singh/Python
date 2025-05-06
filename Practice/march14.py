import re

txt="hello hi byeeeeee"
re.split(txt," ")
print(txt)
a = "The rain in Spain"
x = re.search("^The.*Spain$", a)
print(x)
txt1 = "The rain in Spain"
b = re.findall("ai", txt1)
print(b)

t = "hello planet"
z = re.findall("^hello", t)
if z:
  print("Yes")
else:
  print("No")

abc="green planet earth bye"
e=re.findall("yes$",abc)
if e:
  print("Yes")
else:
  print("No")

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)