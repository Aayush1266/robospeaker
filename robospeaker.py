import os


if __name__ == '__main__':
    print("Welcome to robospeaker 1.1 created by Aayush")
    while True:
        x = input("Enter what you want me to speak")
        if x =='q':
            break
        command = f"say {x}"
        os.system(command)

