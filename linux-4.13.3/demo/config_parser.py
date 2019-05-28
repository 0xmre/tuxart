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
    global block
    block=1
    found=False
    while node:
        sym = node.item

        if block==0:
            found=True

        if isinstance(sym, Symbol):
            if FOO in sym.name and sym.str_value == "y":
                print(sym.name + " value = " + sym.str_value)
                found = True
                block=block-1


        if isinstance(sym,Choice) and block==1:
            pass
        if isinstance(sym,MenuNode) and block==1:
            pass

        if node.list and block==1:
            if is_CONFIG_FOO_enable(node.list, FOO):
                found=True
                block=block-1

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
    print("\n#########################\n\tDEBUT\n#########################\n")

    is_CONFIG_FOO_enable(kconf.top_node, "SGI_IP22")


if __name__=="__main__":
    main()
