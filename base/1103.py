import re

pattern = re.compile(r'\d+')
str = 'one1two2three3four4'


print(re.split(pattern, str))

print(re.findall(pattern, str))