#!/usr/bin/env python3

class NewUser(object):
    def __init__(self,id,name):
        self.id = id
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if len(value) <= 3:
            print("ERROR")
        else:
            self.__name = value
    def __call__(self):
        print("{}'s id is {}".format(self.name, self.id))
if __name__ == '__main__':
    user = NewUser(101, 'Jack')
    user()
