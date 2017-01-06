print ('Faye', 'Leanna', 'Daylen')[1]

s = 'abcdefgh'
print s[::-1]
print s[::-2]
print s[::2]

print ('Faye', 'Leanna', 'Daylen')[-100:100]

s = 'abcde'
i = -1
for i in [None] + range(-1, -len(s), -1):
    print s[:i]

