# Wires
def wires(wires, odd_serial):
    """Uses the instructions from the manual
    to defuse the simple wires module."""
    if len(wires) == 3:
        if "red" not in wires:
            return "Cut the second wire"
        elif wires[-1] == "white":
            return "Cut the last wire"
        elif wires.count("blue") > 1:
            return "Cut the last blue wire"
        else:
            return "Cut the last wire"
            
    elif len(wires) == 4:
        if wires.count("red") > 1 and odd_serial:
            return "Cut the last red wire"
        elif wires[-1] == "yelow" and wires.count("red") == 0:
            return "Cut the first wire"
        elif wires.count("blue") == 1:
            return "Cut the first wire"
        elif wires.count("yellow") > 1:
            return "Cut the last wire"
        else:
            return "Cut the second wire"
    
    elif len(wires) == 5:
        if wires[-1] == "black" and odd_serial:
            return "Cut the fourth wire"
        elif wires.count("red") == 1 and wires.count("yellow") > 1:
            return "Cut the first wire"
        elif wires.count("black") == 0:
            return "Cut the second wire"
        else:
            return "Cut the first wire"
    
    elif len(wires) == 6:
        if wires.count("yellow") == 0 and odd_serial:
            return "Cut the third wire"
        elif wires.count("yellow") == 1 and wires.count("white") > 1:
            return "Cut the fourth wire"
        elif wires.count("red") == 0:
            return "Cut the last wire"
        else:
            return "Cut the fourth wire"