topics = {"Python", "Java", "JavaScript"}

def check_string(my_string):
    if my_string in topics:
        print(f"{my_string} is member of topics set")
    else:
        print(f"{my_string} is not member of topics set")

check_string("Java")

topics.add("TypeScript")
topics.add("C++")

for topic in topics:
    print(f"{topic}")
