import inspect
from django.views.generic.edit import CreateView
# class D:
#     def dark(self):
#         print("i am D")
#
# class B(D):
#     pass
#
# class C(D):
#     def dark(self):
#         print("I am C")
#
# class A(B, C):
#     pass
#
# f = A()
#
# f.dark()
# print(inspect.getmro(A))
class D(object):
    pass

class E(object):
    pass

class F(object):
    pass

class C(D, F):
    pass
class B(E, D):
    pass

class A(B, C):
    pass
if __name__ == '__main__':
    print(CreateView.__mro__)