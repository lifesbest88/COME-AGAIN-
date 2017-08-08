def customBox(width,height):
  box=""
  for i in range(width): #range(0,width)
    box = box+"#"

  for i in range(height):
    print(box)

customBox(8,10)

print

def customBox2(width,height):

  tbborder= '########'
  lrborder= '##    ##'

  for i in range(2):
    print tbborder

  for i in range(4):
    print lrborder

  for i in range(2):
    print tbborder

customBox2(8,10)



def customBox3(width,height):

  tbborder= "#"* width
  lrborder= '##'+' '*(width-4) +'##'

  for i in range(2):
    print tbborder

  for i in range(height-4):
    print lrborder

  for i in range(2):
    print tbborder

customBox3(80,15)

print



def customBox4():
  tbborder = ' ########'
  lrborder = '#      #'

  print (' 123456')
  print (tbborder)
  print ('A'+ lrborder)
  print ('B'+ lrborder)
  print ('C'+ lrborder)
  print ('D'+ lrborder)
  print ('E'+ lrborder)
  print ('F'+ lrborder)
  print ('G'+ lrborder)
  print ('H'+ lrborder)
  print (tbborder)

customBox4()


print


print "{0} and {1}{2} up the {3}"
print "{verena} and {michelle}{sprinted} up the hill"
print "{richard} and {rebbecca}{held hands} and went to the store"


info=""


info =("#"*29) + '\n'

for j in range(26):
  info = info +'# '
  for i in range(1,10):
    info = info +chr(65+j)+ str(i)
    info = info +" "
  info = info +'#\n'
info = info+("#"*29)
print(info)
