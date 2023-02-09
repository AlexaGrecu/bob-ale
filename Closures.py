def get_hello_fn():
    def hello():
        print('Hello Cathy!')
    return hello


hello_fn = get_hello_fn()

print(hello_fn())


def greet_hello_by_name(name):
    def hello():
        print('Hello!', name)

    hello()

    return hello


greet_hello_fn =  greet_hello_by_name('Chris')
print(greet_hello_fn)
print(greet_hello_fn())
del greet_hello_by_name
print(greet_hello_fn())