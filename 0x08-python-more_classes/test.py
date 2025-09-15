class Me:
    def __str__(self):
        return '{}'.format(hex(id(Me)))

me = Me()
print(str(me))
