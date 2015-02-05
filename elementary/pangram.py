import string
import re

def check_pangram(text):

    text_modified = re.sub(r'\W+','',text)      # use a regular expression
                                                # to remove all non-alphanumeric
    text_list = list(text_modified.lower()      # make the text lowercase and remove '_'
                     .replace('_', ''))         # which for some reason escapes the re.sub()

    text_set = set(text_list)                   # turn the list into a set
    alphabet = set([x for x in                  # create a set from the alphabet characters
                    string.ascii_lowercase])    # in the string module
    if len(text_set) is not len(alphabet):      # if the length of sets is not the same
        return False                            # then the string doesn't contain all the letters
    return True                                 # if the function didn't exit in the previous lin
                                                # then the string must be a pangram
