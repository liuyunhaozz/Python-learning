from PIL import Image, ImageFont
 
from handright import Template, handwrite
 
import docx
 
# 自动缩进排版，如果已在word里设置缩进可以注释本段
# indent_size控制缩进,file_path文档路径
def get_text(file_path, indent_size=4):  
    doc = docx.Document(file_path)
    texts = []
    indent = ''
    for i in range(0, indent_size):
        indent = indent + ' '
    for paragraph in doc.paragraphs:
        texts.append(indent + paragraph.text)
    return '\n'.join(texts)
 
# 根目录下的word文档
text = get_text('demo.docx') 
 
 
template = Template(
    background=Image.open('back.jpg'),  # 自定义背景图片
    # font_size=100,
    font=ImageFont.truetype("D:/DUT/home/Handright/tests/fonts/Bo Le Locust Tree Handwriting Pen Chinese Font-Simplified Chinese Fonts.ttf", size=10), # 字体选择手写体
    line_spacing=150,
    fill=(0, 0, 0),  # 字体颜色，括号内为RGB的值
    left_margin=100,
    top_margin=100,
    right_margin=100,
    bottom_margin=100,
    word_spacing=15,
    line_spacing_sigma=6,  # 行间距随机扰动
    font_size_sigma=20,  # 字体大小随机扰动
    word_spacing_sigma=3,  # 字间距随机扰动
    end_chars="，。",  # 防止特定字符因排版算法的自动换行而出现在行首
    perturb_x_sigma=4,  # 笔画横向偏移随机扰动
    perturb_y_sigma=4,  # 笔画纵向偏移随机扰动
    perturb_theta_sigma=0.05,  # 笔画旋转偏移随机扰动
)
images = handwrite(text, template)
for i, im in enumerate(images):
    assert isinstance(im, Image.Image)
    im.show()
    im.save("{}.jpg".format(i))  # 生成的图片生成在当前目录下