import sys

def stupid_coach():
    print("I'm your coach! What are you going to do next?")
    print("> ")
    your_message = input('> ')
    if (your_message in ["I AM GOING TO WORK RIGHT NOW!", "I am going to work right now!"]):
        return "Nice... That's what I wanted to hear."
    if your_message.isupper():
        motivation = "I can feel your motivation!"
        if (your_message[-1] == "?"):
            return f"{motivation} But what a silly question, get dressed and go to work!"
        else:
            return f"{motivation} But I don't care, get dressed and go to work!"
    if (your_message[-1] == "?"):
        return f"Silly question, get dressed and go to work!"
    else:
        return f"I don't care, get dressed and go to work!"


if __name__ == '__main__':
    print("Some odd dialoge:")
    print(stupid_coach())
