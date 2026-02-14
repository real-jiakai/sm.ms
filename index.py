import requests
import json
import pathlib
import sys
import time

def getUploadedImages(token, page):
    url = "https://s.ee/api/v1/files"
    headers = {"Authorization": token}
    params = {"page": page}
    return requests.get(url, headers=headers, params=params).json()


token = sys.argv[1]
page = 1

pathlib.Path("./see").mkdir(exist_ok=True)

while True:
    time.sleep(1)

    max_retries = 5
    for attempt in range(max_retries):
        resp = getUploadedImages(token, page)
        if resp.get("success"):
            break
        msg = resp.get("message", "未知错误")
        if "Too Many Requests" in msg:
            wait = 5 * (attempt + 1)
            print("触发限流，等待 %d 秒后重试... (%d/%d)" % (wait, attempt + 1, max_retries))
            time.sleep(wait)
        else:
            print("请求失败: %s" % msg)
            sys.exit(1)
    else:
        print("重试次数已用尽，退出。")
        sys.exit(1)

    data = resp.get("data", [])
    if not data:
        print("所有页面已处理完毕。")
        break

    print("正在处理第 %d 页，共 %d 条记录..." % (page, len(data)))

    for img in data:
        # 用 filename（时间戳格式）作为保存文件名。
        save_name = img["filename"]
        path = "./see/" + save_name
        if not pathlib.Path(path).is_file():
            time.sleep(0.5)
            try:
                pic = requests.get(img["url"], timeout=30).content
                with open(path, "wb") as f:
                    f.write(pic)
                print("下载完成: %s (原名: %s)" % (save_name, img["storename"]))
            except Exception as e:
                print("下载失败 %s: %s" % (save_name, e))
        else:
            print("已存在: %s" % save_name)

    if len(data) < 30:
        print("所有页面已处理完毕。")
        break

    page += 1
