---
title: "Journey to the Pythonic Peak 🗻"
marp: true
html: true
theme: gaia

---
<style>
p, pre {
    margin-top: 8px !important;
}
</style>
<style scoped>
h1 {
    font-size: 2.4rem;
}
h2 {
    font-size: 2rem;
}
</style>

<!-- _class: lead -->
## Pragmatic Python 2:
# Journey to the Pythonic Peak 🗻
_December 7, 2021_
Joe Riddle

---
<!-- _class: lead -->
# Hi, I'm Joe Riddle 👋

---

Next month's topic

## An _Anything but Mundane_ Intro to Machine Learning

Clayton Gravatt

---
# Previous recording available now
https://spokanepython.com

[IntelliTect YouTube](https://www.youtube.com/channel/UCZSEfrUQnLLohBWDKRRSohw)

---
# Pragmatic
> dealing with things sensibly and realistically in a way that is based on practical rather than theoretical considerations.

---
# Outline
- Why Python?
- Zen of Python
- List comprehensions
- Exception handling
- Decorators
- Generators

<!-- 
Why Python: Something I didn't cover last time
Zen of Python: What does "Pythonic" Python really mean? Where does it come from?
-->

---
# Why Python?

- Easy to read
- Gradual typing
- Wide ecosystem
  - ML, AI, automation, scraping, ...
- Mature
- Open source
  - Steering council


---
# Who uses Python?
- Google
  - "Python where we can, C++ where we must."
  - Guido worked there.
- Instagram
  - "We initially chose to use Python because of its reputation for simplicity and practicality, ..."
- Spotify, Netflix
  - Used heavily for data analysis

---
# Zen of Python

[PEP20](https://www.python.org/dev/peps/pep-0020/)

> Long time Pythoneer Tim Peters succinctly channels the BDFL's guiding principles for Python's design into 20 aphorisms, only 19 of which have been written down.

<!-- Pull up IDLE and do this... -->

---
# Zen of Python
```python
>>> import this
```
```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
...
```

<!-- Many "Pythonic" conventions come from the Zen of Python's philosophies -->

---
# List comprehensions

> List comprehensions provide a more concise way to create lists in situations where map() and filter() and/or nested loops would currently be used.

\- [PEP202]((https://www.python.org/dev/peps/pep-0202/))

> There should be one-- and preferably only one --obvious way to do it.

\- Zen of Python

---
# List comprehensions
```python
ages = [
    user.age
    for user
    in users
]
```

```
>>> print ages
[23, 56, 29]
```

---
# List comprehensions
```python
cool_friend_names = [
    friend.name
    for user
    in users
    for friend
    in user.friends
    if friend.name != "Joseph Riddle"
]
```

```
>>> print(cool_friend_names)
['Phil Spokas']
```

---
# Dict comprehensions
```python
{
    ...
    for key, value
    in dictionary.items() 
}
```

```python
{
    user.name: user
    for user
    in users
}
```

<!-- 
1: Using dict in comprehension
2: Creating dict from list using comprehension
-->

---
# `map` and `filter`

```python
cool_friends_names = []
friends_by_user = map(lambda user: user.friends, users)
for friends in friends_by_user:
    friend_names_for_user = map(lambda user: user.name, friends)
    cool_friend_names_for_user = \
        filter(lambda name: name != "Joseph Riddle", friend_names_for_user)
    cool_friends_names.extend(cool_friend_names_for_user)
```

> Simple is better than complex.

---

# Exception handling
> Errors should never pass silently.
> Unless explicitly silenced.

---
# Exception handling
This...
```python
def get_user(self, name: str) -> User:
    return self.users_by_name[name]
```

...is often better than this...
```python
def get_user(self, name: str) -> Union[User, None]:
    return self.users_by_name.get(name, None)
```

<!--
Why is it better? What do you have to always do when you get a user from the second example?
-->

---
# Exception handling
Don't do this...
```python
try:
    do_something()
except ValueError:
    pass
```

<!-- Errors should never pass silently -->

---
# Exception handling
...or this...
```python
try:
    do_something()
except BaseException:
    pass
```

<!--
BaseException covers many errors you shouldn't usually handle.
Show code example in `exception_handling_bad.py`
-->

---
# Decorators
[PEP318](https://www.python.org/dev/peps/pep-0318/)

Syntatic sugar for wrapping functions with reusable logic

---
# Decorators
Before decorators
```python
def square(x: int):
    return x ** 2

def log(func):
    """Simple decorator to print result"""
    def wrapper(x: int):
        result = func(x)
        print(f"The result is: {result}")
        return result
    return wrapper

square = log(square)
```
```python
>>> square(2)
4
```

---
# Decorators
With decorators (syntatic sugar)
```python
@log
def square(x: int):
    return x ** 2
```
```python
>>> square(2)
4
```

<!-- don't have to declare `square` multiple time... -->

---
# Decorators
Decorators with arguments
```python
def log_times(num_times: int=0):
    def log(func):
        def wrapper(x: int):
            result = func(x)
            for index in range(num_times):
                print(f"({index}) The result is: {result}")
            return result
        return wrapper
    return log

@log_times(num_times=3)
def square(x: int):
    return x ** 2
```

---
# Decorators
Decorators with arguments cont'd
```python
>>> square(2)
(0) The result is: 4
(1) The result is: 4
(2) The result is: 4
```

---
# Generators
[PEP255](https://www.python.org/dev/peps/pep-0255/)
> Each time the .next() method of a generator-iterator is invoked, the code in the body of the generator-function is executed until a yield or return statement (see below) is encountered, or until the end of the body is reached.

<!--
Without generators, we would have to implement iterator logic ourselves
-->

---
# Potential future topics
- What's new in Python 3.10
- Async in Python
- ...

---
<!-- _class: lead -->
Thank you for coming! Join us in January for 
# An _Anything but Mundane_
# Intro to Machine Learning!
