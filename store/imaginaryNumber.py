#here how to saperate real and imagenary from complex number 

import math

a = complex(input('Enter the complex Number : '))

print('The real part = ',a.real)
print('The imag part = ',a.imag)

m = math.sqrt(math.pow(a.real,2) + math.pow(a.imag,2))

print("\nThe m value = %.2f" % m)

