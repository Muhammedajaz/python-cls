str_cs = 'hello world...'
print(str_cs[0])
print(str_cs[2:5])
print(str_cs[2:])
print(str_cs * 5 )
print(str_cs + 'test')
print(str_cs[-1:])
print(str_cs[-11:])
print(str_cs[::-1])
print(len(str_cs))
print(str_cs.upper())
print(str_cs.lower())
print(str_cs.title())


name = '   helloo    '
print(name)
strip_name = name.strip()
print(strip_name)

head = 'helloo, cyber, square'
split_head = head.split(',')
print(split_head)
joint_name = '_'.join(split_head)
print(joint_name)