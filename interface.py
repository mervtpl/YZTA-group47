import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # Pillow kütüphanesi gerekiyor: pip install pillow
import os

import gemini_handler

root = tk.Tk()
root.title("EcoStory - Geri Dönüşüm Hikayeleri")
root.geometry("1000x1000")
root.configure(bg="#f0f9ff")

selected_item = tk.StringVar()


tk.Label(root, text="EcoStory'ye Hoş Geldin!", bg="#f0f9ff", fg="#333",
         font=("Comic Sans MS", 24, "bold")).pack(pady=10)

tk.Label(root, text="Bir geri dönüşüm nesnesi seç:", bg="#f0f9ff", fg="#555",
         font=("Comic Sans MS", 14)).pack()


frame = tk.Frame(root, bg="#f0f9ff")
frame.pack(pady=20)


items = {
    "Plastik Şişe": "images/plastic.png",
    "Kağıt": "images/paper.png",
    "Teneke Kutu": "images/can.png",
    "Cam Şişe": "images/glass.png",
    "Karton Kutu": "images/cardboard.png"
}

images = {}
col = 0
for name, path in items.items():
    if os.path.exists(path):
        img = Image.open(path).resize((80, 80))
        photo = ImageTk.PhotoImage(img)
        images[name] = photo
        rb = tk.Radiobutton(
            frame, text=name, image=photo, compound="top", variable=selected_item, value=name,
            indicatoron=0, bg="#e0f7fa", font=("Comic Sans MS", 10),
            selectcolor="#aed581", width=100, height=120
        )
        rb.grid(row=0, column=col, padx=10, pady=10)
        col += 1


story_box = tk.Text(root, wrap="word", width=90, height=12, bg="#fffde7",
                    fg="#333", font=("Comic Sans MS", 11))
story_box.pack(pady=10)




def olustur():
    item = selected_item.get()
    if not item:
        messagebox.showwarning("Uyarı", "Lütfen bir nesne seçin.")
        return
    try:

        story = gemini_handler.generate_story(item)

        if not story:
            messagebox.showerror("Hata", "Hikaye üretilemedi.")
            return
        story_box.insert(tk.END, story)


        import vertex_handler
        vertex_handler.generate_image(story)  # Bu fonksiyon output.png üretmeli


        gen_img = Image.open("output.png").resize((300, 200))
        gen_photo = ImageTk.PhotoImage(gen_img)
        generating_image_label.config(image=gen_photo)
        generating_image_label.image = gen_photo

    except Exception as e:
        messagebox.showerror("Hata", f"Hikaye veya görsel oluşturulamadı:\n{e}")

    except Exception as e:
        messagebox.showerror("Hata", f"Hikaye veya görsel yüklenemedi:\n{e}")



btn_frame = tk.Frame(root, bg="#f0f9ff")
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="Hikaye Oluştur", command=olustur).grid(row=0, column=0, padx=10)
ttk.Button(btn_frame, text="Kaydet (PDF)", ).grid(row=0, column=1, padx=10)

generating_image_label = tk.Label(root, bg="#f0f9ff")
generating_image_label.pack(pady=10)

root.mainloop()