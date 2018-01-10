import re

html = r"<html><body><h1>hello world</h1></body></html>"

p = r"(?<=<h1>).*?(?=</h1>)"

pattern = re.compile(p)

macther = re.search(pattern, html)

print(macther.group())

key = "javapythonc#"
p = r"python"
pattern = re.compile(p)
m = re.search(pattern, key)
print(m.group())


key = r"<h1>hello world<h1>"
p1 = r"<h1>.+<h1>"
pattern1 = re.compile(p1)
print pattern1.findall(key)

key = r"thisisemailpython.126.comwithgoogle"
p2 = r"python\.126\.com"
pattern2 = re.compile(p2)
print(pattern2.findall(key))

key3 = r"lalala<hTml>hello</Html>heiheihei"
p3 = r"<[Hh][Tt][Mm][Ll]>.*?</[Hh][Tt][Mm][Ll]>"
pattern3 = re.compile(p3)
print(pattern3.findall(key3))

key4 = r"chuxiuhong@hit.edu.cn"
p4 = r"@.+?\."
pattern4 = re.compile(p4)
print(pattern4.findall(key4))
