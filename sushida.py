import pyautogui as pag
from PIL import Image
import numpy as np
from paddleocr import PaddleOCR
import keyboard  # 监听键盘按键
import time
import argparse

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


def capture_and_ocr(region):
    # 使用 pyautogui 在屏幕上的某个区域进行截图
    screenshot = pag.screenshot(region=region)

    # OCR 识别并获取文本
    string = render_doc_text(screenshot)

    # 模拟键盘输入识别到的文本
    pag.write(string)


def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="Capture screen and perform OCR.")
    parser.add_argument(
        "--region",
        type=int,
        nargs=4,
        metavar=("LEFT", "TOP", "WIDTH", "HEIGHT"),
        required=True,
        help="The region to capture in the format: LEFT TOP WIDTH HEIGHT",
    )
    args = parser.parse_args()

    region = tuple(args.region)

    # 主循环监听按键 F1
    while True:
        if keyboard.is_pressed("space"):  # 当按下空格键时
            capture_and_ocr(region)

            # 避免频繁触发，稍微暂停一会儿
            time.sleep(0.5)


if __name__ == "__main__":
    main()
