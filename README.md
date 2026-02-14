# S.EE（原SM.MS）图床备份工具

## 说明

本仓库代码用于备份 [S.EE](https://s.ee)（原SM.MS）图床图片。代码改编自[下载自己在 SM.MS 图床上的所有图片](https://blog.baoshuo.ren/post/download-smms-image/)。

SM.MS 已迁移至 S.EE，API 文档参见 [S.EE API Docs](https://s.ee/docs/api/GetFileHistory/)。

3-2-1 备份原则：

+ 备份 3 份，1 份主要文件，2 份备份文件。
+ 文件存放在 2 种不同的备份媒介。
+ 其中 1 份备份要存放异地（家庭或事业场所以外的地方）。

例如：S.EE 一份、本地一份、Cloudflare R2 一份（当然你也可以直接将图片上传至 GitHub，然后借助 jsDelivr CDN 来加速）。

## 使用说明

```bash
# 克隆本仓库
git clone https://github.com/real-jiakai/sm.ms.git

# 进入文件夹
cd sm.ms

# 安装依赖
pip install -r requirements.txt

# 运行脚本，图片将保存至 see 目录，your_s.ee_api_token 替换为你的 S.EE API Token
python index.py your_s.ee_api_token
```

API Token 获取方式：登录 [S.EE Dashboard](https://s.ee/user/dashboard/)，在设置中获取 API Key。

脚本内置限流重试机制，触发 429 后会自动退避重试，支持增量备份（已下载的文件会自动跳过）。
