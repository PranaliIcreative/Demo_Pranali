def iterdict(d):
  for k,v in d.items():
     if type(v) ==dict:
         iterdict(v)
     else:
         print (k,":",v)

D1={1: {2: {3: 4, 5: 6}, 3: {4: 5, 6: 7}}, 2: {3: {4: 5}, 4: {6: 7}}}
iterdict(D1)
