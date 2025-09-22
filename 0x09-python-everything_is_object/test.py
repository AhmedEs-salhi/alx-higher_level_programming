class Me:
    def __init__(self, number):
        self._number = number
    
    def times_two(self):
        return self._number * 2

    def times_three(self):
        return self._number * 3
        
class OtherMe(list):
    def __init__(self, number):
        self._number = number
    
    def times_foor(self):
        return self._number * 4

me = Me(4)
other_me = OtherMe(5)

print(dir(Me))
print("--")
print(dir(OtherMe))