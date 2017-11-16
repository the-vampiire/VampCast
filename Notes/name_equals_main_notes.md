
**high-level `if __name__ == "__main__"` explanation**

"basically like saying “when this script is called has it been called as an import or as a program?”


the way to check if it has been imported or called as a program is by checking the "__name__" of the file (a hidden property that is set in the background based on the context in which it was called)


in fact you can write a simple test to prove this. put this at the bottom of your script and try running it from the terminal and again in another file as an import:

```
if __name__ == "__main__":
    print("i am being called as a program from the command line or as an executable")
    print("__name__ = {0}".format(__name__))
    print("is __name__ == __main__?: {0}".format("yes" if __name__ == "__main__" else "no"))
else:
    print("i am being called as an import")
    print("__name__ = {0}".format(__name__))
    print("is __name__ == __main__?: {0}".format("yes" if __name__ == "__main__" else "no"))
```

