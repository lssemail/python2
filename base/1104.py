import re

pattern = re.compile(r'\d')
for m in re.finditer(pattern, 'one1two2three3four4'):
    print(m.group())
