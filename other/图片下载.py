from urllib import request

img_url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1510994968332&di=7120cb95aebfc40e0a76079fb7bc96c6&imgtype=0&src=http%3A%2F%2Fimage.tianjimedia.com%2FuploadImages%2F2015%2F215%2F45%2F04L5VRR21C5W.jpg'
img_url2 = 'http://imgsrc.baidu.com/forum/pic/item/03a4462309f79052204229be04f3d7ca7acbd5d5.jpg'


def download_image(url):
    request.urlretrieve(url, 'D:\\test.jpg')


download_image(img_url2)
