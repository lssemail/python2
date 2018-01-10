import re

key1 = r"<h3>hello world</h3>"
p1 = r"<h([1-6]).*?</h\1>";
pattern1 = re.compile(p1)
m1 = re.search(pattern1, key1)
print(m1.group(0))