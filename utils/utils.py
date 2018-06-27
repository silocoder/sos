
class BColors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = "\033[91m{}\033[00m"
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# dump out an objects attributes
# ignore builtins and methods
def dump(obj):
    def ignore(attrib):
        if attrib[0:2] == '__':
            return False
        else:
            return attrib
    print('\n')
    for attr in filter(ignore, dir(obj)):
        if hasattr( obj, attr ) and  not (attr[0:2] == '__' or callable(getattr(obj, attr))):
            print( "obj.%s = %s %s" % (attr, getattr(obj, attr), callable(getattr(obj, attr))))


if __name__ == "__main__":
    print(BColors.PURPLE + "Color" + BColors.ENDC)
    print(BColors.BLUE + "Color" + BColors.ENDC)
    print(BColors.GREEN + "Color" + BColors.ENDC)
    print(BColors.RED + "Color" + BColors.ENDC)
    print(BColors.BLUE + BColors.BOLD + "Color" + BColors.ENDC)
    print(BColors.BLUE + BColors.UNDERLINE + "Color" + BColors.ENDC)

    def prRed(skk): print("\033[91m{}\033[00m".format(skk))
    def prGreen(skk): print("\033[92m{}\033[00m".format(skk))
    def prYellow(skk): print("\033[93m{}\033[00m".format(skk))
    def prLightPurple(skk): print("\033[94m{}\033[00m".format(skk))
    def prPurple(skk): print("\033[95m{}\033[00m".format(skk))
    def prCyan(skk): print("\033[96m{}\033[00m".format(skk))
    def prLightGray(skk): print("\033[97m{}\033[00m".format(skk))
    def prBlack(skk): print("\033[98m{}\033[00m".format(skk))