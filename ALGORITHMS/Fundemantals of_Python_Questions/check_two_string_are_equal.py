"""
input = "ankara" == "rakana"
output = True

input = "ankara" == "asjdj"
output = False
"""

def comparision(str1, str2):

    sum_string1 = 0
    sum_string2 = 0
    
    for each in str1:
        sum_string1 += ord(each) # ord function converts a letter into ascii code integer
    
    for each in str2:
        sum_string2 += ord(each)
    
    if sum_string1 == sum_string2:
        return True
    else:
        return False


def main():

    print(comparision("ankara", "arakan"))
    print(comparision("ankara", "karana"))

if __name__ == "__main__":

    main()