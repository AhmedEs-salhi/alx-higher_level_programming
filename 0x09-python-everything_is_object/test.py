class Me:
    __slots__ = ("first_name")

me = Me()
me.first_name = "Ahmed"
print(me.first_name)
try:
	me.last_name = "Essalhi"
	print(me.last_name)
except AttributeError as err:
    print("[{}] {}".format(err.__class__.__name__, err))