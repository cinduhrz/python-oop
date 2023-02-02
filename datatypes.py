## Python is a strictly typed language, which is better

## an integer - a whole number
my_int = 1
## a float - a number with a decimal
my_float = 1.2

print(my_int + my_float) ## works!

## a string - characters inside quotations
my_str = "1"

# print(my_int + my_str) ## cant add an num (int or float) to a str (yields TypeError)

## Typecasting - changing a piece of data from one type to another
print (my_int + int(my_str))
print (str(my_int) + my_str)


# Functional Programming Example
# make function for each step (you never make objects)
# results in a lotta functions inside functions
# more math-y

# add subtract
# in JS: const add = (x, y) => x + y
# long python: def add(x,y): return x + y
add = lambda x,y: x + y
sub = lambda x,y: x - y

sub(add(5, 5), 4)