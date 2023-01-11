#global_scope
my_global=10

# def fn1():
#     local_v = 5
#     print("Accessing global variable from fn1: ", my_global)
# fn1( )

#print("Accessing local variable from global scope: ", local_v)

def fn1():
    enclosed_v = 5
    def fn2():
        print("Access to Global", my_global)
        print("Access to Enclosed", enclosed_v)
    fn2()
fn1()