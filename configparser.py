import string
import re

globalcontainer = []
with open('.config','r') as file:
    content = file.read()
    file.close()

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

         f.close()
         out.close()

def categoriescontent(CONFIG_target):
    with open('.config','r') as f:

         contents = f.read()
         for key in globalcontainer:
            #pattern = r"^(" + key + r")(\n#\n)(CONFIG\w+=\w+)"
            pattern = key + "(\n#\n)(CONFIG\w+)"
            #patternstring = re.compile(pattern)
            #respattern = re.findall(pattern, contents, re.MULTILINE)

            print(respattern)
            if CONFIG_target in key:
                print(key)
                #for config in pattern:
                    #tmp.append(pattern[1])

                #globalcontainer[key] = tmp

                #print(tmp)
         f.close()

def contentsplit():
    #value = re.split("\n\n",content)
    #globalcontainer.append(value[0])
    #while value[1]:
    value = re.split("\n\n",content,re.X)
    globalcontainer.append(value)



def parseconfig():
    with open('.config', 'r') as f:
        contents = f.read()
        res = re.split("((.)*(\n))*(\n)", contents)
        print(len(res))

def main():
    #categorieslist()
    #categoriescontent("USB")
    #print(globalcontainer)
    contentsplit()
    print(globalcontainer)
    #parseconfig()

if __name__=="__main__":
    main()
