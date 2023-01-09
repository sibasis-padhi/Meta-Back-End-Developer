#global_scope
my_global=10

def fn1():
    local_v = 5
    print("Accessing global variable from fn1: ", my_global)
fn1( )