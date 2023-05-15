def checkname(a):
  count=0
  for i in a:
    if i==" ":
      count+=1
  count+=1
  count2=0
  for j in a:
    if ord(j)>=65 and ord(j)<=90:
      count2+=1
  if count==count2:
    return True
  else:
    return False
print(checkname("Md Tnaz Zafri"))        