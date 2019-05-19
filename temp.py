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
    i = 0
    while node and i<10:
        if isinstance(node.item, Symbol):
            node.kconfig.load_config()
            #print(node.item)

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
