import string
import re

def main():

    with open('.config','r') as f:
         res = ""
         res2= ""
         categories = re.compile(r'(#\n)(# (.)*\n)(#\n)')
         contents = f.read()
         res = categories.findall(contents)
         for i in res:
             print(i[1])


         #print(res2)

if __name__=="__main__":
    main()
