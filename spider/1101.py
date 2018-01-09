# -*- coding: utf-8 -*-

import re

pattern = re.compile(r'hello')

result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo ABCD!')
result3 = re.match(pattern, 'hell')
result4 = re.match(pattern, 'hello ABCD!')

if result1:
    print(result1.group())
else:
    print('1 fail')

if result2:
    print(result2.group())
else:
    print('2 fail')

if result3:
    print(result3.group())
else:
    print('3 fail')

if result4:
    print(result4.group())
else:
    print('4 fail')