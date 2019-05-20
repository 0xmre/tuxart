#!/usr/bin/python3
import sys
import sysconfig
from kconfiglib import Kconfig, Symbol, Choice, COMMENT, MENU, MenuNode, \
                       BOOL, TRISTATE, HEX, STRING, \
                       TRI_TO_STR, \
                       escape, unescape, \
                       expr_str, expr_value, expr_items, split_expr, \
                       _ordered_unique, \
                       OR, AND, \
                       KconfigError

def search_item(node):
    #i=0
    while node:
        if isinstance(node.item, Symbol):
            #node.kconfig.load_config()*

            sym = node.item
            #if sym.str_value == "y":
                #i+=1
            print("\nvalue = " + sym.str_value)
            #for menuitem in node.item.nodes:
                #if menuitem.
                #print(menuitem.sym)
            #node.help()
        if node.list:
            search_item(node.list)

        node = node.next
    #print(i)

def main():

    kconf = Kconfig(sys.argv[1])
    search_item(kconf.top_node)








    #print(Kconfig.load_config("CONFIG_ETHERNET"))
    #print(IS_ENABLED("CONFIG_ETHERNET"))

    #kconf = Kconfig(sys.argv[1])



if __name__=="__main__":
    main()
