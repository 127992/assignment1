def main():
    plate=input("Plate: ")
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")

def is_valid(s):
    #Rule1: must have between 2 and 6 characters
    if len(s) <2 or len(s)>6:
        return False
    #Rule2: must start with at least two letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    #rule3: only letters and numbers are allowed
    if not s.isalnum():
        return False
    #rule4: numbers can only appear at the end
    for i in range(len(s)):
        if s[i].isdigit():
            #first number cannot be 0
            if s[i]=="0":
                return False
            #everything after the first number must also be a number
            if not s[i:].isdigit():
                return False
            break
    return True
main()

