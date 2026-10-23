from webbrowser import open

print("============ Bem Vindo(a) ao Menu de APP's ==========")
app = input("App's:\n 1.WhatsApp\n 2.Spotify\n 3.YouTube\n 4.Facebook\n 5.Instagram\n 6.Calendário\n Escolha o APP: ")
print()

if app == "1":
    open("https://web.whatsapp.com/")
elif app == "2":
    open("https://spotify.com/")
elif app == "3":
    open("https://www.youtube.com/")
elif app == "4":
    open("https://www.facebook.com/")
elif app == "5":
    open("https://www.instagram.com/")
elif app == "6":
    import calendario
else:
    print("Opção inválida.")
