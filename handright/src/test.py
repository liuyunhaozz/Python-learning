# coding: utf-8
from PIL import Image, ImageFont

from handright import Template, handwrite


with open('text.txt', 'r', encoding='utf8') as f:
    text = f.read()
# print(text)

# text = "「初次见面，我叫做雪之下雪乃，是比企谷同学的......什么呢?我们既不是同学，也不是朋友....非常遗憾，应该算是认识的人吧?」「有道理.... 那么，容我更正一下。非常遗憾，我是跟比企谷同学念同一间学校的雪之下雪乃」"



template = Template(
    background=Image.new(mode="1", size=(2100, 3200), color=1),  # 调整 size 进行适应
    font=ImageFont.truetype("assets/Bo Le Locust Tree Handwriting Pen Chinese Font-Simplified Chinese Fonts.ttf", size=100),
)
images = handwrite(text, template)
for index, im in enumerate(images):
    assert isinstance(im, Image.Image)
    im.show()
    # im.save(f"{index + 1}.jpg")  # 生成的图片生成在当前目录下