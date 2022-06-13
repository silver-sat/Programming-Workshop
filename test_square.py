#
# Test square function

from square import square

print("Starting test of square function")

assert square(-1) == 1
    
assert square(0) == 0
    
assert square(4) == 16
    
assert square(4.0) == 16.0
    
print("Ending test of square function")