#keyboardInterrupt

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         print(x)
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

#------------------------------------------------

# import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(error))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Upexpected error:", sys.exc_info()[0])
#     raise

#-------------------------------------------------

# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))   # the exception instance
#     print(inst.args)    # arguments stored in .args
#     print(inst)         # __str__ allows args to be printed directly,
#                         # but may be overridden in exception subclasses
#     x, y = inst.args    # unpack args
#     print('x = ', x)
#     print('y = ', y)

#-------------------------------------------------

#Try ... Finally
import sys
import time

f = None
try:
    f = open("poem.txt")

    # Our usual file-reading idiom

    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end=' ')
        sys.stdout.flush()
        print("Press ctrl+c now")

        #To make sure it runs for a while

        time.sleep(2)

except IOError:
        print("Could not find file poem.txt")

except KeyboardInterrupt:
        print("!! You cancelled the reading from the file.")

finally:
        if f:
            f.close()
        print("(Cleaning up : Closed the file)")
