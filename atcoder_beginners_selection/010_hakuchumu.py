s = input()

er_flag = False
break_flag = False

while len(s) != 0:
    if 'dream' in s[:5] and not er_flag:
        s_prev = s
        s = s.replace('dream', '', 1)
        break_flag = False
    elif 'erase' in s[:5] and not er_flag:
        s_prev = s
        s = s.replace('erase', '', 1)
        break_flag = False
    elif 'dreamer' in s[:7]:
        s = s.replace('dreamer', '', 1)
        er_flag = False
        break_flag = True
    elif 'eraser' in s[:6]:
        s = s.replace('eraser', '', 1)
        er_flag = False
        break_flag = True
    elif not er_flag and not break_flag:
        er_flag = True
        try:
            s = s_prev
        except NameError:
            break
    else:
        break

if len(s) == 0:
    print('YES')
else:
    print('NO')
