import requests
import os
import json
import pathlib
import sys

# 获取图片上传历史信息的函数。
def getUploadedImages(token,i):
    url = "https://sm.ms/api/v2/upload_history"
    headers = {"Authorization": token}
    params = {"page": i}
    return requests.get(url, headers=headers,params=params).text

# 获取数据页数。
pageNum = json.loads(getUploadedImages(sys.argv[1],1))["TotalPages"]
print("数据页数为 %s" % pageNum)

# 循环页数，下载图片至data文件夹下。
for i in range(1,pageNum):
    data = json.loads(getUploadedImages(sys.argv[1],i))
    for img in data["data"]:
        path = "./images/" + img["storename"]
        if not pathlib.Path(path).is_file():
            pic = requests.get(img["url"]).content
            f = open(path, "wb")
            f.write(pic)
            f.close()
            del pic
            print("Successfully get "+img["storename"]+" .")
        else:
            print(""+img["storename"]+" is already exists.")