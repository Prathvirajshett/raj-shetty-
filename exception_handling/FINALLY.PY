try:
   a= int(input("enter number:"))
   b=int(input("enter a number:"))
   print(a/b)
except Exception as e:
    print("ERROR IS",e)
finally:
     print("no error")