# Color constants to print sting to terminal

class BColors:
    PURPLE = '\033[95m{}\033[00m'
    BLUE = '\033[94m{}\033[00m'
    GREEN = '\033[92m{}\033[00m'
    YELLOW = '\033[93m{}\033[00m'
    RED = "\033[91m{}\033[00m"
    BLACK = "\033[98m{}\033[00m"
    LIGHTGRAY="\033[97m{}\033[00m"
    LIGHTPURPLE = "\033[94m{}\033[00m"
    CYAN = "\033[96m{}\033[00m"
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if __name__ == "__main__":
    print(BColors.PURPLE + "Color" + BColors.ENDC)
    print(BColors.BLUE + "Color" + BColors.ENDC)
    print(BColors.GREEN + "Color" + BColors.ENDC)
    print(BColors.RED + "Color" + BColors.ENDC)
    print(BColors.BLUE + BColors.BOLD + "Color" + BColors.ENDC)
    print(BColors.BLUE + BColors.UNDERLINE + "Color" + BColors.ENDC)
