str1 = "n"
str2 = "g"
str3 = "x"

if (str1 < str2) and (str1 < str3):
  print(str1)
  if (str2 < str3):
    print(str2)
    print(str3)
  else:
    print(str3)
    print(str2)
elif (str2 < str1) and (str2 < str3):
  print(str2)
  if (str1 < str3):
    print(str1)
    print(str3)
  else:
    print(str3)
    print(str1)
else:
  print(str3)
  if (str1 < str2):
    print(str1)
    print(str2)
  else:
    print(str2)
    print(str1)
