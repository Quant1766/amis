"""
Тут написати умову до завдання
"""

# from  lab_1_ import *
from km_84.Goncharic_Andrew.workshop1.source.pacg.lab_1_ import *
def sum_n(n):

   if n>0:
      vector = -1
   else:
      vector = +1

   if n == 1:
      return 1

   elif n == 0:
      return 0


   return n+sum_n(n+vector)

def f(n,resp_0=2,resp_1=5):
   print("n",n)

   if n==0:
      return resp_0

   elif n == 1:
      return resp_1

   else:
      resp = (f(n-1)+4)/(f(n - 2))
      print('resp',resp)
      return resp

if __name__ == "__main__":

   print(f(0))
   print(sum_n(0))

   print(division(get_float(text='a'),get_float(text='b')))

