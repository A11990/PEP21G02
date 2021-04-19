name='Jhon'
age= 26
print('name: ', name, 'age:', age)

#print='print'
#print('name: ', name, 'age:', age)

#type function
result = type(name)
print(result)
result = type(age)
print(result)

print(5*name)

name2=(5*name)
result = type(name2)
print(result)

result= id(name)
print(result)


print(8+8)
print((8).__add__(8))

print(8 * ' text')

print((' text').__mul__(8))


print(8-8)
print((8).__sub__(8))

print(8/8)
print((8).__truediv__(8))

#Float
x=1.0

result = type(x)
print(result)

print(8**8)
print((8).__pow__(8))
print(pow(8, 8))

a=3
b=4
c=5
x=(-b+((b**2)-4*a*c))**(1/2)/(2*a)
print(x)

a=3
b=4
c=5
bsqr= b.__pow__(2)
multi= (4).__mul__(a.__mul__(c))
dif= bsqr.__sub__(multi)
dif=float(dif)
var=(1).__truediv__(2)
rad=dif.__pow__(var)
b= complex(b)
dif2=(-b).__sub__(rad)
mul1=(2).__mul__(a)
ec= dif2.__truediv__(mul1)
print(ec)

#Complex
nr1= 1.0+1.0j
nr2=3+5j
print(nr1+nr2)
print(type(nr1))

#String
#my_str1='My String\n'
#print(my_str1)

my_str2=r"My String \n no multi line"
#my_str3=f"""My String"""
#print(my_str3)

#dir
info=dir(my_str2)
print(info)

var1='this is {}'
cap=var1.capitalize()
print(cap)
format1 = var1.format('Sparta')
print(format1)

phone = "0747.655.444"
split1= phone.split("7")
print(split1)

phone = "0747.655.444"
split1=phone.rsplit(sep=".",maxsplit=1)
print(split1)

#input
#input('give me your name:')

#slice
text ="My Text"
first_letter = "My Text"[0]
print(first_letter)
slice1=text[4:1]
print(slice1)
slice2=text[0:6:2]
print(slice2)

#text=input('Enter a 10 text here:')
#slice1=text[0:5]
#slice2=text[5:10]
#print(slice2+slice1)

#negative step
#reverse = text[::-1]
#print(reverse)
my_bool = True
print(type(my_bool))
my_bool=False
print(type(my_bool))

print(id(True))
print(id(False))
print(id(10))
print(True+False)
print(dir(True))
x=True.__add__(False)
print(x)

#None
my_none= None
x= print('')
print(x)

# Truth

print(bool(0+0j))
print)bool(0.0)













