__author__ = 'Martin'

import os
import colorama

colorama.init()

def ensure_dir(f):
    """
    create folder structure, if not exits
    """
    d = os.path.dirname(f)
    if not os.path.exists(f):
        print "shoud make dir"
        os.makedirs(f)

class style:
    def h1(self):
        return colorama.Back.GREEN + colorama.Fore.BLACK + colorama.Style.DIM

    def h2(self):
        return colorama.Back.BLUE + colorama.Fore.WHITE + colorama.Style.DIM

    def h3(self):
        return colorama.Back.GRAY + colorama.Fore.BLACK + colorama.Style.DIM

    def error(self):
        return colorama.Back.RED + colorama.Fore.WHITE + colorama.Style.DIM

    def info(self):
        return colorama.Back.BLACK + colorama.Fore.WHITE + colorama.Style.DIM

    def normal(self):
        return colorama.Back.BLACK + colorama.Fore.WHITE + colorama.Style.BRIGHT




