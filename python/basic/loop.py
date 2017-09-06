
# Loop
def from_for_loop():
    list = [1,2,3,4,5]
    for n in list[1:]:
        print(n)
# from_for_loop()

def nested_for_loop():
    list = [1,2,3,4,5]
    for n in list:
        for n in list:
            print(n)
# nested_for_loop()

def single_for_loop():
    list = [1,2,3,4,5]
    for n in list:
        print(n)
# single_for_loop()

def single_for_loop_v2():
    list = [1,2,3,4,5]
    for i in range(len(list)):
        print(list[i])
# single_for_loop_v2()
