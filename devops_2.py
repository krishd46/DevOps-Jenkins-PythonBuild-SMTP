a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
s = (a + b + c) / 2  
  

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('Area of triangle: %0.2f' %area)   
