from PIL import Image, ImageDraw, ImageFont


def save_image():
    img = Image.new('RGB', (200, 200), (255, 0, 0))
    img.save('D:\\test.png', 'png')


def write_text_to_image():
    # 载入图片
    img = Image.open('D:\\test.png')
    # 载入字体及大小
    font = ImageFont.truetype('data/神韵哈天随性体.ttf', 30)
    # 获取图片宽度和高度
    w, h = img.size
    # 创建图像
    draw = ImageDraw.Draw(img)
    # 写入文字
    draw.text((0.5 * w, 0.2 * h), '中文', font=font, fill=(0, 0, 255))
    # 保存图像
    img.save('D:\\deal.png', 'png')


def show_image_in_plt():
    # 载入图片
    img = Image.open('E:\\我的图片\\QQ图片20170914200717.jpg')
    # 载入字体及大小
    font = ImageFont.truetype('data/神韵哈天随性体.ttf', 100)
    # 获取图片宽度和高度
    w, h = img.size
    # 创建图像
    draw = ImageDraw.Draw(img)
    # 写入文字
    draw.text((0.5 * w, 0.2 * h), '程序猿', font=font, fill=(255, 0, 0))
    # 显示图像
    # plt.imshow(img)
    # plt.axis('off')
    # plt.show()
    img.show()


show_image_in_plt()
