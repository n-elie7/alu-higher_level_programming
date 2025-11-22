# 🔹 1. Strings are immutable
print("1️⃣ Immutability")
s = "hello"
try:
    s[0] = "H"
except TypeError as e:
    print("Cannot modify string:", e)
print("After change attempt:", s)
print()

# 🔹 2. String interning (memory sharing)
print("2️⃣ Interning")
a = "hello"
b = "hello"
print("a is b:", a is b)  # Usually True (interned)

x = "hello world"
y = "hello world"
print("x is y:", x is y)  # Usually False (not interned)
print()

# 🔹 3. Concatenation inefficiency
print("3️⃣ Concatenation cost")
import time
start = time.time()
s = ""
for i in range(10000):
    s += "a"
print("Time with += :", round(time.time() - start, 4), "seconds")

start = time.time()
s = "".join(["a" for i in range(10000)])
print("Time with join:", round(time.time() - start, 4), "seconds")
print()

# 🔹 4. Slicing creates new object
print("4️⃣ Slicing")
s = "abcdef"
t = s[2:5]
print("t:", t)
print("s is t:", s is t)
print()

# 🔹 5. 'is' vs '==' confusion
print("5️⃣ 'is' vs '=='")
a = "abc"
b = "".join(["a", "b", "c"])
print("a == b:", a == b)
print("a is b:", a is b)
print()

# 🔹 6. Escape characters & raw strings
print("6️⃣ Escape vs Raw")
print("Normal string:", "Hello\nWorld")
print("Raw string:", r"Hello\nWorld")
print()

# 🔹 7. Unicode characters
print("7️⃣ Unicode handling")
s = "😀"
print("String:", s)
print("Length:", len(s))
print()

# 🔹 8. String multiplication
print("8️⃣ Multiplication")
print("'ha' * 3 =", "ha" * 3)
print()

# 🔹 9. Strings behave like tuples of chars
print("9️⃣ Iterable behavior")
for ch in "abc":
    print(ch, end=" ")
print()
