## 说明

本仓库代码用于备份sm.ms图床图片。代码改编自[下载自己在 SM.MS 图床上的所有图片](https://blog.baoshuo.ren/post/download-smms-image/)。

SM.MS一份、本地一份、Cloudflare R2一份（当然你也可以直接将图片上传至GitHub，然后借助jsdeliver cdn来加速）。

3-2-1备份原则：

+ 备份 3 份，1 份主要文件，2 份备份文件。

+ 文件存放在 2 种不同的备份媒介。

+ 其中 1 份备份要存放异地（家庭或事业场所以外的地方）。

## 使用说明

```bash
# 克隆本仓库
git clone https://github.com/real-jiakai/sm.ms.git
# 进入文件夹
cd sm.ms
# 新建images文件夹
mkdir images
# 安装依赖
pip install -r requirements.txt
# 运行脚本，其中your_sm.ms_api替换为sm.ms账号的api
python index.py your_sm.ms_api
```

## 补充

```shell
# 1、cloudflare界面R2—>Create bucket
# 2、创建名为blog的bucket
# 3、下载rclone https://rclone.org/install/
# 4、依据官方文档对rclone进行配置
# cf文档地址：https://developers.cloudflare.com/r2/examples/rclone/
# rclone文档地址：https://rclone.org/docs/

# 创建配置文件
.\rclone.exe config file
# 将本地的images文件夹上传至R2存储桶中的images文件夹中
# example: .\rclone.exe copy "D:\project\python\sm.ms\images" blog:blog/images
.\rclone.exe copy "you_sm.ms_images_folder_location" blog:blog/images
```

## 注意点

请务必让sm.ms网址走代理。

![sm.ms走clash代理](https://vip2.loli.io/2023/03/23/gT6IHi72GdaLfMl.webp)
