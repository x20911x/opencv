from PIL import Image
import cv2
from matplotlib import pyplot as plt


def show_original_image(picture_name):
    img1 = Image.open(picture_name)
    img1.show()

def show_left_image(picture_name):
    picture_name = Image.open(picture_name)
    rotate_left_img = picture_name.rotate(90)
    rotate_left_img.show()

def show_right_image(picture_name):
    picture_name = Image.open(picture_name)
    rotate_right_img = picture_name.rotate(-90)
    rotate_right_img.show()


def show_gray_image(picture_name):

    img2 = cv2.imread('girl.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('girl.jpg', img2)
    cv2.waitKey(0)
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
def event_by_black_button():
    show_original_image('girl.jpg')

def event_by_red_button():
    show_left_image('girl.jpg')

def event_by_green_button():
    show_right_image('girl.jpg')

def event_by_blue_button():
    show_gray_image('girl.jpg')

# 以下為 top 群組
left_button = tk.Button(top_frame, text='左轉90', fg='red', command=event_by_red_button)
# 讓系統自動擺放元件，預設為由上而下（靠左）
left_button.pack(side=tk.LEFT)

middle_button = tk.Button(top_frame, text='右轉90', fg='green', command=event_by_green_button)
middle_button.pack(side=tk.LEFT)

#
# # 以下為 bottom 群組
right_button = tk.Button(top_frame, text='彩色轉灰階', fg='blue', command=event_by_blue_button)
right_button.pack(side=tk.LEFT)
#
#
# bottom_button = tk.Button(top_frame, text='顯示原圖', fg='black', command=event_by_black_button)
# bottom_button.pack(side=tk.LEFT)
#


# 讓系統自動擺放元件（靠下方）
# bottom_button.pack(side=tk.BOTTOM)

# 運行主程式
window.mainloop()