#!/usr/bin/python3
import string
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


def is_CONFIG_FOO_enable(node,FOO):
    found = False

    while node and not found:
        sym = node.item

        if isinstance(sym, Symbol):
            if FOO in sym.name:
                if "y" or "m" in sym.str_value:
                    print(sym.name + "value = " + sym.str_value)
                    found = True
            #else:
                #  print("#\n# non\n#")

        if node.list:
            is_CONFIG_FOO_enable(node.list, FOO)

        node = node.next

    return found


def search_item(node):
    i=0

    while node:
        if node.item == MENU:
            if "USB" in node.prompt[0]:
                print(node.prompt)


        if isinstance(node.item, Symbol):
            sym = node.item
            if "USB" in sym.name and sym.str_value == "y":
                i==i+1

            #print("\nvalue = " + sym.str_value)
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
    print("########################\n\tDEBUT\n#########################")
    print(kconf.syms.items)

    #search_item(kconf.top_node)
    #if is_CONFIG_FOO_enable(kconf.top_node, "SGI_IP22"):
    #    print("C'est incroyalbe")
    #else:
    #    print ("fuck")



    #print(Kconfig.load_config("CONFIG_ETHERNET"))
    #print(IS_ENABLED("CONFIG_ETHERNET"))

    #kconf = Kconfig(sys.argv[1])



if __name__=="__main__":
    main()
