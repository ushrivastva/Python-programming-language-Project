def box(text):
    
    padding = 81
    width = len(text) + padding * 2

    print("*" * (width+2))
    print("*" +" " * padding + text +" " * padding + "*")
    print("*"* (width+2))

def small(text):
    padding = 83
    width = len(text) + padding * 2
    
    print("*" * (width+2))
    print("*" + " " * padding + text +" "*padding + "*")
    print("*"* (width+2))
    

def small_box(text1, text2):

    padding = 37
    width = len(text1 + text2) + padding * 4

    print("*" * (width+3))
    print("*" + " " * padding + text1 +" "*padding + "*" + " " * padding + text2 + " "*padding + "*")
    print("*"* (width+3))

def wt_unit(text1, text2, text3):

    padding = 27
    width = len(text1 + text2 + text3) + padding * 6

    print("*" * (width+4))
    print("*" + " " * padding + text1 +" "*padding + "*" + " " * padding + text2 + " "*padding + "*" + " " * padding + text3 + " "*padding + "*")
    print("*"* (width+4))

def hg_unit(text1, text2, text3, text4):

    padding = 17
    width = len(text1 + text2 + text3+text4) + padding * 8

    print("*" * (width+5))
    print("*" + " " * padding + text1 +" "*padding + "*" + " " * padding + text2 + " "*padding + "*" + " " * padding + text3 + " "*padding + "*" + " " * padding + text4 + " "*padding + "*")
    print("*"* (width+5))
