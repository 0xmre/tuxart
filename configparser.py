import string
import re

globalcontainer = {}

def categorieslist():
    with open('.config','r') as f:
         res = ""
         categories = re.compile(r'(#\n)(# (.)*)(\n#\n)')
         contents = f.read()
         contents = re.sub("\( | \)", "\s", contents)
         res = categories.findall(contents)

         out = open("output.txt", "a")
         for i in res:
             out.write(i[1]+'\n')
             globalcontainer[i[1]] = []
             #globalcontainer.append(i[1])
         f.close()
         out.close()

def categoriescontent():
    with open('.config','r') as f:
         #res = ""
         #catcontent = re.compile(r'(#\n)(# (.)*\n)(#\n)(.)*(\n)\s$')
         contents = f.read()
         #res = categories.findall(contents)
         for key in globalcontainer:

            print(key)
            tmp = []
            #pattern = r"^"+i+r"(.)*\n{0|1}"
            #print(pattern)
            #pattern2 = re.compile(r'(^'+globalcontainer[i]+')(.)*(\n{0|1})')
            pattern2 = re.search(key + '(\n#\n)(.)*(\n)', contents)
            if pattern2:
                print("ok")
            else:
                print("Eh non")
            #pattern2 = re.compile(r'(^'+key+')(.)*(\n{0|1})')

            #option = pattern2.findall(contents)
            #tmp.append(pattern2.string)
            #for j in option:
                 #tmp.append(j)
                 #globalcontainer[i].append(j[1])
                 #print(globalcontainer[i])
                 #for y in subcat.group():
                    #globalcontainer[i].append(y)
            print(tmp)
            globalcontainer[key] = tmp
         f.close()

def parseconfig():
    with open('.config', 'r') as f:
        contents = f.read()
        res = re.split("((.)*(\n))*(\n)", contents)
        print(len(res))

def main():
    #categorieslist()
    #categoriescontent()
    #print(globalcontainer)
    parseconfig()

if __name__=="__main__":
    main()
