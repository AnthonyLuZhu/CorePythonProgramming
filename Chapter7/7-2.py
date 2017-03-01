
dict4 = {'abc':123}
dict5 = {'abc': 456}
dict6 = {'abc':123, 98.6:37}
dict7 = {'xyz': 123}

print dict4 < dict5

print (dict4 < dict6) and (dict4 < dict7)

print  (dict5 < dict6) and (dict5 < dict7)

print dict6 < dict7