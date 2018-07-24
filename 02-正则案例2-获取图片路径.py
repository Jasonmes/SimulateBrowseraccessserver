# 需求: 有一个图片标签,把里面的图片路径取出来;(多个,只取第一个...)
#       思路: 使用search(); 指定符合内容的字符串就可以了...
import re

img_url = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'

# 根据re模块的高级用法,搜索search(); 查找第一个符合标准的内容
#    尽可能少的匹配.
obj = re.search(r'https://.+?\.jpg', img_url)
print(obj.group())
