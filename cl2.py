# # try:
# #     print("hello")
# # except:
# #     print("we have problems")
# # else:
# #     # print("no problem")
#
# try:
#     print("start code")
# except NameError as error:
#     print(error)
# else:
#     print("I am ELSE")
# finally:
#     # print("finally code")

# def checker(var_1):
#     if type(var_1)!= str:
#         raise TypeError(f"Sorry, we can`t work with {type(var_1)},"
#                         f"we need class str")
#     else:
#         return var_1
#
# first_var = 10
# checker(first_var)

# import warnings
# warnings.simplefilter("ignore", SyntaxWarning)
# warnings.simplefilter("always", ImportWarning)
#
# warnings.warn("Warning, no code here", SyntaxWarning)
# warnings.warn("Warning, module not import", ImportWarning)

a = int(input("a = "))
b = int(input("b = "))

try:
    print(a*b)
except TypeError as error:
    print("Only number")
