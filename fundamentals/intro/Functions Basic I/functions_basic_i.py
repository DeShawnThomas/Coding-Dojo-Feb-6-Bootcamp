# #1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# p output: 5


# #2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# p output: error bc first function not defined

# #3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# p output: 10 bc it's the last line of function... I'll be mad if it's 15. (Edit: I'm dumb. "return" immediately exits the function)



# #4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# p output: 5. As I noticed from the last function. "return" immediately exits the function!


# #5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# p output: it'll print 5 to the console bc of the function, then nothing bc the function didnt save anything...


# #6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# p output: it'll print 8 to the console (Edit: I'm wrong here. It prints the numbers indiviually but runs into an error since the functions don't return those values.)

# #7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# p output: it'll print "25" due to str() changing the integers to strings.


# #8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# p output: it'll print 100 to the console first. Then since b is greater than 10 it returns 10, exits the function and prints `0`.

# #9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# p output: 1st print: 7 2nd print: 14 3rd print: 21

# #10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# p output: 8


# #11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# p output: 1st print: 500 2nd print: 500 3rd print: 300 4th print: 500

# #12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# p output: 1st print: 500 2nd print: 500 3rd print: 300 4th print: 500

# #13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# p output: 1st print: 500 2nd print: 500 3rd print:300 (Edit: Okay I learned now when you set b = to the foobar function, the function runs!)


# #14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# p output: 1st print: 1 2nd print: 3 3rd print: 2


# #15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# p output: 1st print: 1 2nd print: 3 3rd print: 5 (this is because bar() returns 5 ) 4th print: 10 (this is because foo() returns 10)