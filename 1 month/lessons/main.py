# def wave(people):
#   b=[]
#   c=[]
#   d=""
#   t=0
#   e=''
#   for i in people:
#     b.append(i)
#     d+=b[t]
#     t+=1
#     e=d
    
  

#   print(e.lower())

# wave("Hello")

def cC(s):
  counts={}

  for ch in s:
    if ch in counts:
      counts[ch] = counts[ch] +1
    else:
      counts[ch] = 1
  return counts


def ano():
  s1 = input('Enter first world: ')
  s2 = input('Enter second world: ')

  counts1 = cC(s1)
  counts2 = cC(s2)

  if counts1 == counts2:
    print('ok')
  else:
    print('Not ok')
  
ano()