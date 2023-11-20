import os
def add(a,b):
  return a+b
def subtract(a,b):
   return a-b
def multplication(a,b):
   return a*b
def divided(a,b):
   return a/b
opr_dict={
             "+":add,
             "-":subtract,
             "*":multplication,
             "/":divided
            }
def calculator():
    num1=float(input("enter first number"))
    for symbol in opr_dict:
      print(symbol)
    continue_flog=True
    while continue_flog:
     op_symbol=input("pick opration")
     num2=float(input("enter second number"))
     calculation=opr_dict[op_symbol]
     output=calculation(num1,num2)
     print(f"{num1}  {op_symbol} {num2} = {output}")
     should_continue=input(f"enter 1 for calculation with {output}\nenter 2 for new caculation\n enter N for exit ").lower()
     if should_continue =="1":
         num1=output
         continue_flog=True
     elif should_continue =="2":
         continue_flog=False
         os.system('cls')
         calculator()
     elif should_continue == "3":
         continue_flog=False
         print("bye")
calculator()
