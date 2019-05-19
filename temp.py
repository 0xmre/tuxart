#!/usr/bin/python3
import sys
import sysconfig
import kconfiglib 

def search_item(node):
    i = 0
    while node:
        if isinstance(node.item, Symbol):
            #node.kconfig.load_config()*
            for menuitem in node.item.nodes:
                #if menuitem.
                print(menuitem)
            #node.help()

        if node.list:
            search_item(node.list)
        i = i+1
        node = node.next

def main():

    kconf = Kconfig(sys.argv[1])
    search_item(kconf.top_node)
    #print(Kconfig.load_config("CONFIG_ETHERNET"))
    #print(IS_ENABLED("CONFIG_ETHERNET"))

    #kconf = Kconfig(sys.argv[1])
    #search_items(kconf.top_node)



if __name__=="__main__":
    main()
