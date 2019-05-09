import string
import re

globalcontainer = []

def categorieslist():
    with open('.config','r') as f:
         res = ""
         categories = re.compile(r'(#\n)(# (.)*\n)(#\n)')
         contents = f.read()
         res = categories.findall(contents)
         out = open("output.txt", "a")
         for i in res:
             out.write(i[1])
             globalcontainer.append(i[1])
         f.close()
         out.close()

# def categoriescontent():
#     with open('.config','r') as f:
#          res = ""
#          catcontent = re.compile(r'(#\n)(# (.)*\n)(#\n)(.)*(\n)\s$')
#          contents = f.read()
#          res = categories.findall(contents)
#          for i in res:
#              globalcontainer.append(i[1])
#          f.close()
#          out.close()

def main():
    categorieslist()


if __name__=="__main__":
    main()
