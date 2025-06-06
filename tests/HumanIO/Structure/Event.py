

from DSSS.HumanIO.Structure.Event import EventStructure, MousePressed, Mouse


if __name__ == '__main__':
    test = EventStructure()
    print(eval(repr(test)))

    test = MousePressed(Mouse.RIGHT)
    print(eval(repr(test)))
    ...
