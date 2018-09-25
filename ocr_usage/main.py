import pytesseract
from PIL import Image

# 识别汉字
image = Image.open("hanzi.png")
image.show()    # 打开图片
text = pytesseract.image_to_string(image, lang='chi_sim')   # 使用简体中文解析图片
print(text)


# 识别数字
# def get_bin_table(threshold=230):
#     # 获取灰度转二值的映射table
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#     return table
#
#
# image = Image.open('number.png')
# gray_image = image.convert('L')
# gray_image.show()
# table = get_bin_table()
# text = pytesseract.image_to_string(gray_image, config='digits')
# filter_text = filter(str.isdigit, text)
# print(''.join(filter_text))
