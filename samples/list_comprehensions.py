from __future__ import annotations
from attr import dataclass


@dataclass
class User():
    name: str
    age: int
    friends: list[User] = []


joseph = User("Joseph Riddle", 23)
clayton = User("Clayton Gravatt", 56)
phil = User("Phil Spokas", 29)

users = [
    joseph,
    clayton,
    phil,
]


# Simple

ages = [
    user.age
    for user
    in users
]
print(ages)


# Advanced
clayton.friends = [phil]
phil.friends = [joseph]


cool_friend_names = [
    friend.name
    for user
    in users
    for friend
    in user.friends
    if friend.name != "Joseph Riddle"
]
print(cool_friend_names)


# map and filter
cool_friends_names = []
friends_by_user = map(lambda user: user.friends, users)
for friends in friends_by_user:
    friend_names_for_user = map(lambda user: user.name, friends)
    cool_friend_names_for_user = filter(lambda name: name != "Joseph Riddle", friend_names_for_user)
    cool_friends_names.extend(cool_friend_names_for_user)
print(cool_friends_names)
