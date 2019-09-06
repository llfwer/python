from time import sleep

import uiautomator2 as u2

d = u2.connect('192.168.1.103')

# 启动App
d.app_start("org.chromium.webview_shell")

# 搜索
d(resourceId="org.chromium.webview_shell:id/url_field").wait(timeout=10.0)
d(resourceId="org.chromium.webview_shell:id/url_field").set_text("https://www.baidu.com/")
d(description=u"Load URL").click()

# 输入关键字
d(resourceId="index-kw").wait(timeout=10.0)
d(resourceId="index-kw").set_text("奥巴马")
d(resourceId="index-bn").click()

# 搜索按钮
d(description="奥巴马_百度百科").wait(timeout=10.0)
d(description="奥巴马_百度百科").click()

sleep(5)

# 停止app
d.app_stop("org.chromium.webview_shell")
