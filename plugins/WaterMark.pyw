# -*- coding: utf-8 -*-
# Environment    PyCharm
# File_name   visibleWaterMark |User    Pfolg
# 2024/8/7   19:30
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from tkinter import ttk, filedialog, messagebox, colorchooser
import tkinter as tk
import os


def watermark_Image(img_path, text, pos, color="#FFFFFF", textFont="STSONG.TTF", textSize=20):
    image = Image.open(img_path)

    drawing = ImageDraw.Draw(image)

    # 加载字体文件
    font = ImageFont.truetype(font=textFont, size=textSize)

    drawing.text(pos, text, fill=color, font=font)

    image.show()
    # img.save(output_path)


# img = ".\\旅行.png"
# watermark_Image(img, ".\\output.png", 'Python', pos=(10, 10))
def visibleWaterMarkFindFile(x, text):
    win = tk.Tk()
    win.withdraw()
    file_path = filedialog.askopenfilename()
    x.set(file_path)
    try:
        image = Image.open(file_path)
        width, height = image.size
        text.set(f"图片长[{width}]，宽[{height}]")
    except BaseException:
        text.set("")
    win.destroy()


def choose_color(x):
    color = colorchooser.askcolor(title="Color")
    if color[1]:
        x["background"] = color[1]


def visibleWaterMark(frame):
    markContent, phoPath, positionX, positionY, markFont, fontSize = tk.StringVar(), tk.StringVar(), tk.IntVar(), tk.IntVar(), tk.StringVar(), tk.IntVar()

    nameList = ['内容', '颜色', '图片路径', '左上角x', '左上角y', '字体', '字体大小']
    varList = [markContent, 1, phoPath, positionX, positionY, markFont, fontSize]

    markFont.set("STSONG.TTF")
    fontSize.set(20)
    positionX.set(10)
    positionY.set(10)

    imageSize = tk.StringVar()
    ttk.Label(frame, textvariable=imageSize).place(relx=.7, rely=.42)
    ch_color = tk.Button(
        frame, width=3, relief="groove", command=lambda: choose_color(ch_color), background="#000000", text=""
    )

    for i in range(len(nameList)):
        ttk.Label(frame, text=nameList[i]).place(relx=.3, rely=.12 + i * .1)
        if i == 1:
            ch_color.place(relx=.4, rely=.12 + i * .1)
            continue
        if i == 5:
            ttk.Combobox(
                frame, textvariable=markFont, values=list(os.walk(r"C:\Windows\Fonts"))[0][2], width=17  # 浏览字体文件夹并提取字体
            ).place(relx=.4, rely=.12 + i * .1)
            continue
        tk.Entry(frame, textvariable=varList[i], width=20).place(relx=.4, rely=.12 + i * .1)
        if i == 2:
            ttk.Button(
                frame, text="浏览", width=8, command=lambda: visibleWaterMarkFindFile(varList[2], imageSize)
            ).place(relx=.6, rely=.12 + i * .1)

    ttk.Button(
        frame, text="添加水印", width=8, command=lambda: watermark_Image(
            phoPath.get(), markContent.get(), pos=(positionX.get(), positionY.get()),
            color=ch_color["background"], textFont=markFont.get(), textSize=fontSize.get()
        )).place(relx=.43, rely=.85)

    instruction = (
        "不支持图片保存；\n作者为了打游戏，并且希望用户可以有最大的自由去制作水印，位置x，y可以靠感觉做，默认左上角；\n"
        "字体设置方法：打开[C:\Windows\Fonts],右键选择喜欢的字体，右键[属性]，复制[*.ttf]，粘贴至[字体]就完成设定了；\n"
        "三个需要填入数字的输入框均只支持整数；\n"
    )
    ttk.Button(
        frame, text="Help", width=8, command=lambda: messagebox.showinfo(title="提示信息", message=instruction)
    ).place(relx=.9, rely=.8)
    ttk.Button(
        frame, text="Close", width=8, command=lambda: window.destroy()
    ).place(relx=.9, rely=.9)


if __name__ == '__main__':
    window = tk.Tk()
    window.title("WaterMark")
    screen_w, screen_h = window.winfo_screenwidth(), window.winfo_screenheight()
    w, h = int(screen_w / 2), int(screen_h / 2)
    window.geometry(f'{w}x{h}+{int(screen_w / 4)}+{int(screen_h / 4)}')
    window.resizable(False, False)
    # window.iconbitmap(".\\QkStart.ico")
    # window.attributes('-alpha', 0.9)

    f = ttk.Frame(window)
    visibleWaterMark(f)
    f.place(relx=0, rely=0, width=w, height=h)

    window.mainloop()
