def make_class(name, attrs):
    return type(name, (object,), attrs)

Person = make_class("Person", {"name": "Bill", "age": 63})
p = Person()
print(p.name, p.age)
