import tkinter as tk
from tkinter import messagebox
import os
from cryptography.fernet import Fernet

main_file = "pass_till"
FİLE = "pass_till\\pass.txt"



def login_pass_till():
    global key2
    global login

    login = tk.Tk()
    login.resizable(width=False, height=False)
    login.geometry("200x100")
    login.configure(background="black")
    login.title("Login")

    def kapat():
        messagebox.showinfo("Programcı Mesajı","By nyoxs iyi günler diler.😁")
        login.destroy()

    login.protocol("WM_DELETE_WINDOW",kapat)

    def check_password(key1, login_attempts):
        if key1.get() == "123456":
            login.destroy()
            pass_till()
        else:
            login_attempts[0] += 1
            remaining_attempts = 5 - login_attempts[0]
            if remaining_attempts > 0:
                messagebox.showerror("Hata", f"Yanlış Key! Kalan deneme hakkınız: {remaining_attempts}")
            else:
                messagebox.showerror("Hata", "5 kez yanlış key girdiniz. Uygulama kapatılıyor.")
                login.destroy()

                

    key1_screen = tk.Label(text="Key 1:",bg="black",fg="red")
    key1_screen.place(x=1, y=2)

    key1 = tk.StringVar()
    key1_input = tk.Entry(textvariable=key1, show='*')
    key1_input.place(x=35, y=2,width=140)

    key2_screen = tk.Label(text="Key 2:",bg="black",fg="red")
    key2_screen.place(x=1,y=31)

    key2 = tk.StringVar()
    key2_input = tk.Entry(textvariable=key2, show="*")
    key2_input.place(x=35,y=32,width=140)

    login_attempts = [0]

    login_open_button = tk.Button(text="Giriş", command=lambda: check_password(key1, login_attempts),bg="black",fg="red")
    login_open_button.place(x=35, y=70, height=20, width=120)

    login.mainloop()

def encrypted():

    def generate_key():
        global main_key
        main_key = Fernet.generate_key()
        with open("key.txt","wb") as key_save:
            key_save.write(f"key:{main_key.decode()}".encode())
            key_save.close()
        print(f"Key : {main_key}")
            
    def encrypt_file(file_name):

        fernet = Fernet(main_key)

        with open(file_name, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(file_name, "wb") as encrypted_file:
            encrypted_file.write(encrypted)

    key = generate_key()
    encrypt_file(FİLE)

def decrypted():
# Dosyayı şifre çözme
    def decrypt_file(file_name):
        try:

            fernet = Fernet(key2.get())

            with open(file_name, "rb") as encrypted_file:
                encrypted = encrypted_file.read()

            decrypted = fernet.decrypt(encrypted)

            with open(file_name, "wb") as decrypted_file:
                decrypted_file.write(decrypted)
        except ValueError:
            messagebox.showerror("HATA", "Hata,key2 yanlış lütfen dogru giriniz.")
            os._exit()

# Kullanım
    decrypt_file(FİLE)  

def pass_till():
    global main_interface
    decrypted()   
    main_interface = tk.Tk()
    main_interface.geometry("600x150")
    main_interface.resizable(width=False,height=False)
    main_interface.title("PASS TİLL")
    main_interface.configure(background="black")

    def kapat():
        messagebox.showinfo("Programcı Mesajı","Lütfen key.txt dosyasını saklayınız.\nBy nyoxs iyi günler diler.😁")
        main_interface.destroy()

    main_interface.protocol("WM_DELETE_WINDOW",kapat)

    #Başlık Giriş Kısmı
    title_screen = tk.Label(text="Başlık:",bg="black",fg="red")
    title_screen.place(x=2,y=3)

    title = tk.StringVar()
    title_input_screen = tk.Entry(textvariable=title)
    title_input_screen.place(x=39,y=3,width=161)

    #Kullanıcı İsmi giriş kısmı
    client_screen = tk.Label(text="Kullanıcı İsmi:",bg="black",fg="red")
    client_screen.place(x=2,y=30)

    client_name = tk.StringVar()
    client_name_input = tk.Entry(textvariable=client_name)
    client_name_input.place(x=78,y=30,width=122)

    #Şifre Neye Ait
    pass_screen = tk.Label(text="Şifre:",bg="black",fg="red")
    pass_screen.place(x=2,y=57)

    password = tk.StringVar()
    pass_input = tk.Entry(textvariable=password)
    pass_input.place(x=31,y=57,width=169)

    #Not al
    notes_screen = tk.Label(text="Not:",bg="black",fg="red")
    notes_screen.place(x=2,y=84)

    notes = tk.StringVar()
    notes_input = tk.Entry(textvariable=notes)
    notes_input.place(x=30,y=84,width=170)

    def password_add():
        pass_list = f"""
---------------------------------------------
Başlık:{title.get()}
Kullanıcı İsmi:{client_name.get()}
Şifre:{password.get()}
Not:{notes.get()}
---------------------------------------------
        """
        try:
            with open(FİLE, "a") as password_write:
                password_write.write(pass_list)
            messagebox.showinfo("Başarılı","Şifre Başarılı Bir Şekilde Eklendi.")
            title_input_screen.delete(0,tk.END)
            client_name_input.delete(0,tk.END)
            pass_input.delete(0,tk.END)
            notes_input.delete(0,tk.END)
        except :
            messagebox.showerror("Hata","Bilinmeyen Bir Hata Oluştu !!!")
    
    def password_list_open():
        with open(FİLE,"r") as pass_list:
            password_list = pass_list.read()
            pass_list_screen.config(state=tk.NORMAL)
            pass_list_screen.delete(1.0,tk.END)
            pass_list_screen.insert(tk.END,password_list)
            pass_list_screen.config(state=tk.DISABLED)

    pass_add_button = tk.Button(text="Verileri Ekle",command=password_add,bg="black",fg="red")
    pass_add_button.place(x=35,y=120)

    pass_list_open_button = tk.Button(text="Listeyi Yenile",command=password_list_open,bg="black",fg="red")
    pass_list_open_button.place(x=105,y=120)

    pass_list_screen = tk.Text(main_interface,bg="black",fg="red")
    pass_list_screen.place(x=220,y=3,width=370,height=140)
    pass_list_screen.config(state=tk.DISABLED)

    main_interface.mainloop()
    encrypted()

for i in range(1):
    if os.path.exists(main_file):
        login_pass_till()
    else:
        os.mkdir(main_file)
        with open(FİLE,"wb") as main_filex:
            main_filex.write(b"----------------By nyoxs sunar---------------")
            main_filex.close()
        encrypted()
        