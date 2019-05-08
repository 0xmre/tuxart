import string
import re

def main():

    with open('.config','r') as f:
         res = ""
         categories = re.compile(r'(#\n)(# (.)*\n)(#\n)')
         contents = f.read()
         res = categories.findall(contents)
         out = open("output.txt", "a")
         for i in res:
             out.write(i[1])
         f.close()
         out.close()


if __name__=="__main__":
    main()
