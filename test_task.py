def foo1(res):
    def foo2(num=None):
        nonlocal res
        if num == None:
            return res

        res += num
        return foo2

    return foo2


print(foo1(1)(3)())
print(foo1(2)(3)(4)())
print(foo1(2)(3)(4)(5)(7)())
