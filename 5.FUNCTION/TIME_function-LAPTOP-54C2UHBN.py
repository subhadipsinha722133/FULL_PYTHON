from time import perf_counter
print('enter your name',end='')
start_time= perf_counter()
name=input()
a=perf_counter() -start_time
print(name,'it took you =',a)








