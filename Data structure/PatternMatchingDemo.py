# Ref https://towardsdatascience.com/the-match-case-in-python-3-10-is-not-that-simple-f65b350bb025
#
# convert an integer in the range 0..15 to a single hex digit (as a string)
def toHexDigit(value):
    match int(value):
        case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
            digit = chr(value + ord("0"))       
        case 10 | 11 | 12 | 13 | 14 | 15:
            digit = chr(value -10 + ord("A"))
        case _:
            print("no match on ",value)
            digit = "X"  # default to an invalid value
    return digit


# convert a single hex digit (as a string) to an integer in the range 0..15
def fromHexDigit(digit):
    if "0" <= digit <= "9" :
        return ord(digit) - ord("0")
    elif "A" <= digit <= "F" :
        return 10 + ord(digit) - ord("A")
    else:
        return None # invalid hex digit

    
def main():
    #for i in range(16):
    #    print(toHexDigit(i))
    
    for i in range(17):
        digit = toHexDigit(i)
        value = fromHexDigit(digit)
        print( "i ",i,"value",value)
    

if __name__ == "__main__":
    main()