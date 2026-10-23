from webbrowser import open

print("============ Bem Vindo(a) ao Menu de APP's ==========")
app = input("App's:\n 1.WhatsApp\n 2.Spotify\n Escolha o APP: ")
print()

if app == "1":
    open("https://web.whatsapp.com/")
elif app == "2":
    open("https://spotify.com/")