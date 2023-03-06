# importing sqrt() and factorial from the
# module math
import math as mt
# import numpy as np
 
# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(mt.sqrt(16))
print(mt.factorial(6))
for i in dir(mt):
    print(i)