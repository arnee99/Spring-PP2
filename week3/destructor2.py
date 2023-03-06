class Employee:
    
    def __init__(self):
        print('Employee created!')
        
    def __del__(self):
        print('Destructor called!')
        
def create_object():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj

print('Calling create_object() function...')
obj = create_object()
print('Program end...')