## 说明

本仓库用于备份博客图片。代码改编自[下载自己在 SM.MS 图床上的所有图片](https://blog.baoshuo.ren/post/download-smms-image/)。

SM.MS一份、本地一份、Cloudflare R2一份。

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
# 安装requirements库
pip install -r requirements或pip install requirements
# 运行脚本，其中your_sm.ms_api替换为sm.ms账号的api
python index.py your_sm.ms_api
```