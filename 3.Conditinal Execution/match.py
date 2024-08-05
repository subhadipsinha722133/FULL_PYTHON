x=int (input("enter the value"))
match x:
  case 0:
    print ("zero")
  case 1:
    print("one")
  case 2:
    print("two")  
  case _:
    print(x)   