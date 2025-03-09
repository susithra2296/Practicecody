
item_incart = 0

# if item_incart != 2:
#     raise Exception("product cart is 0")


assert(item_incart == 0)
'''assert -- condition is satisfied or not 
#explicily fail the test when the condition is not met
#validate the test cast scenorious '''

'''try --except -- we don't want to fail the testcase , catch the exception (get the error),
hit one website sometime popup will appear , sometime popup it wont happen , two possiblity , it may or may not come'''
#customazed error , python known error
try:
    with open('nofiletext.txt') as reader:
        reader.readlines()
except Exception as e:
    print(f"file is not existing{e}")

# cleaning up the setup. try- create the data , finally - clening up the data , no matter where the testcase fail, it will clear the created cookies , whrer the testcase pass or fail ,
finally:
    print("clear the testcase")