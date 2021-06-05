from PIL import Image
import cv2
import psutil
import time
from matplotlib import pyplot as plt


def cancel_img_show(time_of_cancel=3):
    time.sleep(time_of_cancel)
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()


def show_original_image(picture_name):
    img = Image.open(picture_name)
    img.show()
    return img


def show_left_image(picture_name):
    img = Image.open(picture_name)
    rotate_left_img = img.rotate(90)
    rotate_left_img.show()
    return rotate_left_img


def show_right_image(picture_name):
    img = Image.open(picture_name)
    rotate_right_img = img.rotate(-90)
    rotate_right_img.show()
    return rotate_right_img


def show_gray_image(picture_name):
    img = Image.open(picture_name)
    img = img.convert('LA')
    img.show()
    return img


#
# # ---------------------------------
# img3=cv2.imread('girl.jpg', 0)
# # 灰階大於127 轉 255
# ret, th1 = cv2.threshold(img3, 127, 255, cv2.THRESH_BINARY)
#
# titles=['original', 'rotate_right', 'rotate_left', 'black','BINARY']
# images = [img1, rotate_right_img, rotate_left_img, img2, th1]
#
# for i in range(5):
#     plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#
#     # plt.yticks([]), plt.xticks([])
#
# plt.show()

# ------------------------------------------------

# 引入套件
import tkinter as tk

# 建立主視窗和 Frame（把元件變成群組的容器）
window = tk.Tk()
top_frame = tk.Frame(window)

# 將元件分為 top/bottom 兩群並加入主視窗
top_frame.pack()

bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)


# 建立事件處理函式（event handler），透過元件 command 參數存取


def event_by_red_button():
    show_left_image('girl.jpg')
    cancel_img_show()


def event_by_green_button():
    show_right_image('girl.jpg')
    cancel_img_show()


def event_by_blue_button():
    show_gray_image('girl.jpg')
    cancel_img_show()


def event_by_black_button():
    show_original_image('girl.jpg')
    cancel_img_show()


# 以下為 top 群組
first_button = tk.Button(top_frame, text='原圖', fg='black', command=event_by_black_button)
# 讓系統自動擺放元件，預設為由上而下（靠左）
first_button.pack(side=tk.LEFT)

left_button = tk.Button(top_frame, text='左轉90', fg='red', command=event_by_red_button)
# 讓系統自動擺放元件，預設為由上而下（靠左）
left_button.pack(side=tk.LEFT)

right_button = tk.Button(top_frame, text='右轉90', fg='green', command=event_by_green_button)
right_button.pack(side=tk.LEFT)

# # 以下為 bottom 群組
gray_button = tk.Button(bottom_frame, text='彩色轉灰階', fg='gray', command=event_by_blue_button)
gray_button.pack(side=tk.LEFT)

# 讓系統自動擺放元件（靠下方）
# bottom_button.pack(side=tk.BOTTOM)

# 運行主程式
window.mainloop()
