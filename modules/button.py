# Button
def button(colour, text, batteries, car, frk):
    """Uses the instructions from the manual
    to defuse the button module."""
    if colour == "blue" and text == "abort":
        return "Hold the button and look at strip colour"
    elif text == "detonate" and batteries > 1:
        return "Press the button"
    elif colour == "white" and car:
        return "Hold the button and look at strip colour"
    elif batteries > 2 and frk:
        return "Press the button"
    elif colour == "yellow":
        return "Hold the button and look at strip colour"
    elif colour == "red" and text == "hold":
        return "Press the button"
    else:
        return "Hold the button and look at strip colour"

def button_strip(colour):
    if colour == "blue":
        return "Release on a 4"
    elif colour == "yellow":
        return "Release on a 5"
    else:
        return "Release on a 1"