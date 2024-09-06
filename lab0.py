def myFunction():
    '''
    Write a Python function that returns sum of the odd digits of your student ID
    - Example 1: 312552006 -> 3+1+5+5 = 14
    - Example 2: 313551164 -> 3+1+3+5+5+1+1 = 19
    
    '''

    # Remember to change to your student ID
    ID = '113550088'
    sum = 0
    
    # Write your code here
    q = ID.count("1")
    w = ID.count("3")
    e = ID.count("5")
    r = ID.count("7")
    t = ID.count("9")
    sum = q*1+ w*3+ e*5+ r*7+ t*9

    return sum

if __name__ == '__main__':
    print(f'sum = { myFunction() }')
