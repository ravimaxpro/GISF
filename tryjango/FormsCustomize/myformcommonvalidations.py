import re


def SpecialCharCheck(string):
    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    # Pass the string in search
    # method of regex object.
    if (regex.search(string) == None):
        print("String is accepted")
        return False
    else:
        return True
        print("String is not accepted.")
