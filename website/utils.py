import random as rd
import datetime as dt
import re


def salt_generator(text, length=10):
    sref = (ord(ch) for ch in text)
    rd.seed(sum(sref))
    chars = ('abcdefghijklmnopqrstuvwxyz'
             'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
             '0123456789'
             '!@#$%^&*()-_=+')
    return ''.join((rd.choice(chars) for _ in range(length)))


def titlecase(string):
    pattern = r"[a-zA-Z]+('[a-zA-Z]+)?"
    return re.sub(pattern, lambda x: x.group(0).capitalize(), string)
