s = input()

target_strings = ['dream', 'dreamer', 'erase', 'eraser']
for string in target_strings:
    s = s.replace(string, '')

if len(s) == 0:
    print('YES')
else:
    print('NO')