
# # Lists:
# # in [1]: []
# # out [1]: []
# # in [6]: 1
# # out [6]: [1, 3, 6, 10]
# # in[9]:l[-1]-gives last element
# # out [9]:
# # in[20]: l[1:4]-its 1-third element included
# # in[20]: l[1:4]:2 -every 2 steps from 1-third

# # in [25]: l[l.index(89)]-will give u back 89
# # out [25]: 89

# # in [27]:
# # l.append(40)

# # in[28]
# in[6]: 1
# out [6]: [1, 3, 6, 10]
# in[38]: len(l)

# l.remove(3) will remove the number 3
# l.pop(0)-pop/remove the number at index 0.and when look at l, youll see the list without that number
# in[47]:l
# out[47]:[45, 60, 80] will show up like this without the first number.

# can do strings and numbers inside the list.

# l.extend-will merge one list to another. 
# append-will add 

# tuple-ordered, but not mutable
# t =(1,6, 59, 784)
# t.count(4)-will show how many times the number 4 pops up in a list. 
# len(t)-will show the length of a list
# if type t, itll output the tuple list
# l=list(t)
# l=[1,6, 59, 784]
# list of whatever is in t, and then can make it mutable.


# y =l.copy() will copy the things inside of y

# DICTIONARY: no index. bec its not ordered

# similar to objects in javascript
# key and ValueError
# {}-defines a dictionary in python
d={"key1":1,"key2":56,"a":"whatever"}
>>> d={"key1":1,"key2":56,"a":"whatever"}
>>> d
{'key1': 1, 'key2': 56, 'a': 'whatever'}
>>> d["a"]
'whatever'
d["a"] ="something"
d
{'key1': 1, 'key2': 56, 'a': 'something'}
d["b"]="something else"
d
{'key1': 1, 'key2': 56, 'a': 'something', 'b': 'something else'}
 d.update({"a":"hbg"}

{'key1': 1, 'key2': 56, 'a': 'hbg', 'b': 'something else'}
 d.clear
<built-in method clear of dict object at 0x104b2e9c0>
d
{'key1': 1, 'key2': 56, 'a': 'hbg', 'b': 'something else'}
d.keys()
dict_keys(['key1', 'key2', 'a', 'b'])
 for key in d.keys():
...     print(d[key])
... 
1
56
hbg
something else

because dictionary not ordered, and every key mpped, its much faster to get objects from it.
complexity-how many times it needs to go through an operation

SETS:
cant have duplicates. itll remove all the duplicates
set
<class 'set'>
set((1,3,5))
{1, 3, 5}
s =set((1,3,5))
s
{1, 3, 5}
>>> s2 =set((1,3,5,6,8))
>>> s.intersection(s2)
{1, 3, 5}
>>> s.union(s2)
{1, 3, 5, 6, 8}
>>> s2=set([1,3,5,6,8])

input()
value=input()
something
>>> value
'something'
>>> value=input()
2
>>> value
'2'


>>> INPUTS always come in strings

value =int(input())
56
>>> value
56

s="a string"
>>> s
'a string'
>>> s[0]
'a'
>>> s[1]
' '
>>> s[::-1]
'gnirts a'
>>> s.index("s")
2
>>> s="a string whatever"
>>> s
'a string whatever'


SPLIT-removes the white space, or the space in between the string.
'a string whatever'
>>> s 
'a string whatever'
>>> s.split(" ")
['a', 'string', 'whatever']
>>> s="a, string, whatever"
>>> s.split(",")
['a', ' string', ' whatever']
REPLACE ALL "a" by "d"
s.replace("a","d")
'd, string, whdtever'

CAPITALIZE
>>> s.capitalize()
'A, string, whatever'

FORMATTING STRINGS:
placeholders inside your string, and can use inputs to place things there.
Formats can use any type.
%s is a sting and expects a string %age, %27 wont work because its waiting for string.if says %d which means digit, then %28 will work, but a string after wont work.
 s = "Your age is{}"
>>> s
'Your age is{}'
>>> input("tell me your age: ")
tell me your age: 28
'28'
>>> print(s.format(age))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>> age=input()
 print(s.format(age))
>>> "your age is {}".format(age)
'your age is  print(s.format(age))'
>>> "your age is {}, {},{}".format(age,89)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: Replacement index 2 out of range for positional args tuple
>>> f"your age is{age}"
'your age is print(s.format(age))'
>>> input("tell me your age: ")
tell me your age: tell me your age: 28
'tell me your age: 28'
>>> '28'
'28'
>>> age=input()
age
>>> age=28
>>> age
28
>>> input("tell me your age: ")
tell me your age: 28
'28'
>>> age=input
>>> age
<built-in function input>

BOOLEANS=bool
>>> bool([1])
True
>>> bool([])
False
>>> bool({})
False
>>> bool(())
False
>>> bool(0)
False
>>> bool([2,3])
True
>>> l =[1,2]
>>> if l:
...     print("hey")
... 
hey

