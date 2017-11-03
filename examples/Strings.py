#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = literal-comparison
# pylint: disable = missing-docstring

# ----------
# Strings.py
# ----------

# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

print("Strings.py")

assert isinstance('abc', str)
assert len('abc')  == 3

assert isinstance("abc", str)
assert len("abc")  == 3

assert isinstance(r'abc', str)
assert len(r'abc')  == 3

assert isinstance(r"abc", str)
assert len(r"abc")  == 3

assert isinstance('''abc''', str)
assert len('''abc''')  == 3

assert isinstance("""abc""", str)
assert len("""abc""")  == 3

assert len('a\nb') == 3
assert len("a\nb") == 3

assert len(r'a\nb') == 4
assert len(r"a\nb") == 4

assert len('''a\nb''') == 3
assert len("""a\nb""") == 3

assert len('a\
b') == 2
assert len("a\
b") == 2

assert len(r'a\
b') == 4
assert len(r"a\
b") == 4

assert len('''a
b''') == 3
assert len("""a
b""") == 3

assert str(True)  is     str(True)
assert str(2)     is not str(2)
assert str(2)     ==     str(2)
assert str(2.34)  is not str(2.34)
assert str(2.34)  ==     str(2.34)

assert "bcd"     in "abcde"
assert "xyz" not in "abcde"

assert "" is ""

s = "abc"
t = str(s)
assert s is t

s = "abcde"
t = s[:]
assert s is t

s = "abc"
t = s
assert s is t
s += "d"
assert s == "abcd"
assert t == "abc"

s = "abCbA"
t = s.upper()
assert s == "abCbA"
assert t == "ABCBA"

s = "ABCBA"
t = s.upper()
assert s is not t
assert s ==     t

s = "abCbACb"
n = s.find("Cb")
assert s == "abCbACb"
assert n == 2

s = "abCbACb"
n = s.find("Cx")
assert s == "abCbACb"
assert n == -1

s = "abCbACb"
n = s.rfind("Cb")
assert s == "abCbACb"
assert n == 5

s = "abCbACb"
t = s.replace("Cb", "Xy")
assert s == "abCbACb"
assert t == "abXyAXy"

s = "abCbACb"
t = s.replace("Cx", "Xy")
assert s is t

s = "abCbACb"
t = s.replace("Cb", "Xy", 1)
assert s == "abCbACb"
assert t == "abXyACb"

s = "abCbACb"
u = s.split("Cb")
assert s == "abCbACb"
assert u == ['ab', 'A', '']

s = "abCbACb"
u = s.split("Cx")
assert s == "abCbACb"
assert u == [s]

print("Done.")
