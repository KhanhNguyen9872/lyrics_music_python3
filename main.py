#!/bin/python3

def clear():
    if (os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

def main():
    clear()
    user_input=str(input("Input name: "))
    try:
        exec(f"{user_input}=sound.{user_input}")
    except:
        print("Music not found!")
        exit()
    if (eval(user_input)['lyrics'] == user_input):
        print(f"Lyrics must not same [{user_input}]")
        exit()
    else:
        exec(f"global {eval(user_input)['lyrics']}; {eval(user_input)['lyrics']}=lyrics.{eval(user_input)['lyrics']}")
    exec(f"play(user_input,{user_input}['name'],{user_input}['author'],{user_input}['file'],{user_input}['lyrics'],{user_input}['min'],{user_input}['max'])")

def play(user_input, name, author, file, lyric, min, max):
    time=float(min)
    clear()
    print("Name: {}\nMusic: {}\nAuthor: {}\n[Ctrl + C] to exit!\n".format(user_input, name, author))
    try:
        playsound.playsound(file, False)
    except:
        print("File not found or playsound version is not 1.2.2")
        exit()
    try:
        while 1:
            print(f"\r{time}\r", end="", flush=True)
            try:
                temp=eval(lyric)[f"{time}"]
                if (temp == ""):
                    print(f"\r{time}                                                                                \r", end="", flush=True)
                else:
                    print(f"\r{time}  {temp}\r", end="", flush=True)
            except:
                pass
            sleep(0.1)
            if (str(time) == str(max)):
                exit()
            else:
                time=round(float(time + 0.1), 1)
    except:
        pass
    print("Stopping...")
    exit()


if (__name__=='__main__'):
    try:
        import os, playsound
    except:
        import os
        if (os.name == 'nt'):
            os.system('python -m pip install playsound==1.2.2')
        else:
            os.system('python3 -m pip install playsound==1.2.2')
        import playsound
    from time import sleep
    import sound, lyrics
    main()