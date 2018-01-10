import re

url = r"http://192.168.1.102:8080/admin/login"
p = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
p2 = r"(?:\d.*\.){3}\d{1,3}"

pattern = re.compile(p2)
print(pattern.findall(url))