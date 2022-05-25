# Gerekli olan kütüphane ve modüller

from tkinter import *
from tkinter.messagebox import showinfo
import pyttsx3
import speech_recognition as sr

# Python metinden konuşmaya ve konuşmadan metne işlevleri oluşturma


def speak(text: str):
    engine = pyttsx3.init()
    engine.setProperty('rate', 10)
    engine.setProperty('volume', 100)
    engine.say(text)
    engine.runAndWait()

# Dinleme adımlarını giriyoruz.


def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 2
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="tr-tr")
        except Exception as e:
            showinfo(title="Error!", message="SİZİ ANLAYAMADIM!")

            return "Nothing"
        return query

# Ana STT (Speech-to-Text --Konuşmadan Metme--) fonksiyonlarını ve talimat fonksiyonlarını oluşturma


def STT():
    stt_wn = Toplevel(root)
    stt_wn.title('STT (Konuşmadan Metne Dönüştürme')
    stt_wn.geometry("350x200")
    stt_wn.configure(bg='#f1efef')
    Label(stt_wn, text='Konuşmadan Metne Dönüştürme',
          font=("Lato", 16), bg='#f1efef').place(x=20)
    text = Text(stt_wn, font=12, height=3, width=30)
    text.place(x=7, y=100)
    record_btn = Button(stt_wn, text='Kayıt', bg='#fff6da',
                        command=lambda: text.insert(END, record()))
    record_btn.place(x=150, y=50)


def instruction():
    instructions = '''
Talimatlar:
1. Bir süre bekleyin çünkü STT dönüşümleri biraz zaman alır.
2. STT dönüşümünde ifadenizi bitirmek için 2 saniye duraklayın, çünkü bu, pause_threshold miktarıdır.
'''
    showinfo("Başlamadan Önce Bilinmesi Gerekenler", instructions)

# Main GUI penceresinin oluşturulması


root = Tk()
root.title('TARHAN -_- STT')
root.geometry('350x350')
root.resizable(0, 0)
root.configure(bg='#d3bab2')

# Tüm bileşenlerin yerleştirilmesi

Label(root, text='Tarhan SESİ METNE DÖNÜŞTÜRME (STT) Uygulaması',
      font=('Lato', 16), bg='#d3bab2', wrap=True, wraplength=300).place(x=65, y=5)

stt_btn = Button(root, text='Sesi Metne Dönüştürme', font=(
    'Helvetica', 16), bg='#e3d4d6', command=STT)
stt_btn.place(x=50, y=200)
instruction_btn = Button(root, text='NASIL ÇALIŞIR?', font=('Helvetica', 16), bg='#e3d4d6',
                         command=instruction)
instruction_btn.place(x=80, y=250)

# Main pencerenin güncellenmesi

root.update()
root.mainloop()

