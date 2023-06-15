import sys
import re

len_lst = len(sys.argv)
pattern = ".+\.txt$"

if len_lst == 1:
    print("hello world")

elif re.match(pattern,sys.argv[1]):
    with open(sys.argv[1]) as f:
        content = f.read()
        lst = content.split()
        for word in lst:
            print(f"{word}:{lst.count(word)}")
    
elif len_lst == 2:
    print(sys.argv[1][::-1])

else: 
    print("wrong format")

