def greetMe(**args):
    for key, value in args.items():
        print("{0} = {1}".format(key, value))


it = {"name":"grishma", "name1":"john"}
greetMe(**it)

print('---------------------------')
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
greetMe(**kwargs)