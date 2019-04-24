def greet(**kk):
    if kk:
        print('hi',kk['name'],'ur msg',kk['msg'])

greet(name="koshal", msg="morning")
