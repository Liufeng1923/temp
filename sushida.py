import pyautogui as pag
from PIL import Image
import numpy as np
from paddleocr import PaddleOCR
import keyboard  # 监听键盘按键
import time

# 初始化 PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang="en")


def render_doc_text(image):
    # 将 PIL Image 转换为 numpy array
    image_np = np.array(image)

    # OCR 识别
    result = ocr.ocr(image_np, cls=True)
    txts = [elements[1][0] for elements in result[0]]
    # 返回识别到的文本字符串，合并成一行
    return " ".join(txts)


def capture_and_ocr():
    # 使用 pyautogui 在屏幕上的某个区域进行截图
    # 例如截取屏幕的 x=90, y=230 到 x=400, y=260 的区域
    screenshot = pag.screenshot(
        region=(487, 899, 1117, 973)
    )  # (left, top, width, height)

    # OCR 识别并获取文本
    string = render_doc_text(screenshot)

    # 模拟键盘输入识别到的文本
    pag.write(string)


# 主循环监听按键 F1
while True:
    if keyboard.is_pressed("space"):  # 当按下 F1 时
        capture_and_ocr()

        # 避免频繁触发，稍微暂停一会儿
        time.sleep(0.5)
