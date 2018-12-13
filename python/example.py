#
#   Simple example of Monolog with dialog
#   =====================================
#
#   exampleDialog00 & exampleDialog01
#   are simple Monolog and Dialog examples
#
#   exampleDialog02
#   complex example with a lot of keywords
#   good example for a basic workflow
#

# Import dialog
import dialog as dia

# exampleDialog00
def printMonolog(d):
    while(dia.Dialog.ending(d) == False):
        print(dia.Dialog.getSpeaker(d) + ": " + dia.Dialog.nextText(d))
        dia.Dialog.update(d)

# exampleDialog01
def printDialog(d):
    while(dia.Dialog.ending(d) == False):
        print(dia.Dialog.getSpeaker(d) + ": " + dia.Dialog.nextText(d))
        dia.Dialog.update(d)

# exampleDialog02
def printDialog(d):
    while(dia.Dialog.ending(d) == False):
        print(dia.Dialog.getSpeaker(d) + ": " + dia.Dialog.nextText(d))
        dia.Dialog.update(d)

def main():
    # exampleDialog00
    print("=== exampleDialog00 ===")
    d = dia.Dialog("exampleDialog00.txt", "../exampleDialogs/") # Setup a dialog
    printMonolog(d)

    # exampleDialog01
    print("=== exampleDialog01 ===")
    d = dia.Dialog("exampleDialog01.txt", "../exampleDialogs/")
    printDialog(d)

    # exampleDialog02
    print("=== exampleDialog02 ===")
    d = dia.Dialog("exampleDialog02.txt", "../exampleDialogs/")
    printDialog(d)

if __name__ == '__main__':
    main()
