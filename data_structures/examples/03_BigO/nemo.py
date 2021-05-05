from timeit import default_timer as timer
from random import randint
from secrets import token_hex
nemo = ["nemo"]
everyone = ["dory", "bruce", "marlin", "nemo", "gill",
                "bloat", "nigel", "squirt", "darla", "hank"]
#large = [randint(1, 9999) for i in range(1000)]
large = [token_hex(2) for i in range(1000)]


def findNemo(array):    
    start = timer()
    # for name in array:
    #     if name == "nemo":
    #         print("Found Nemo!")
    for i in range(len(array) -1):
        if array[i] == "nemo":
            print("Found Nemo!")
    end = timer()
    print(end - start)
findNemo(large)