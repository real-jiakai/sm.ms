# S.EE（原SM.MS）图床备份工具

## 说明

本仓库代码用于备份S.EE（原SM.MS）图床图片。代码改编自[下载自己在 SM.MS 图床上的所有图片](https://blog.baoshuo.ren/post/download-smms-image/)。

SM.MS 已迁移至 [S.EE](https://s.ee)，API 端点和文件命名规则均有变化：

| 对比项 | SM.MS（旧） | S.EE（新） |
|---|---|---|
| API 端点 | `/api/v1/file/upload_history` | `/api/v1/files` |
| 文件命名 | 随机字母组合（如 `xELWwcToDpkbePy.webp`） | 时间戳格式（如 `20260211080408912.webp`） |
| API 文档 | 已下线 | [S.EE API Docs](https://s.ee/docs/api/GetFileHistory/) |

3-2-1 备份原则：

+ 备份 3 份，1 份主要文件，2 份备份文件。
+ 文件存放在 2 种不同的备份媒介。
+ 其中 1 份备份要存放异地（家庭或事业场所以外的地方）。

例如：S.EE 一份、本地一份、Cloudflare R2 一份（当然你也可以直接将图片上传至 GitHub，然后借助 jsDelivr CDN 来加速）。

## 脚本说明

| 脚本 | 保存目录 | 文件命名 | 用途 |
|---|---|---|---|
| `index.py` | `./images/` | `storename`（兼容旧 SM.MS 随机命名） | 增量备份，兼容历史数据 |
| `index_see.py` | `./see/` | `filename`（S.EE 时间戳命名） | 全量重新下载，文件名更直观 |

两个脚本均内置限流重试机制，触发 429 后会自动退避重试。

## 使用说明

```bash
# 克隆本仓库
git clone https://github.com/real-jiakai/sm.ms.git

# 进入文件夹
cd sm.ms

# 安装依赖
pip install -r requirements.txt

# 方式一：增量备份（兼容旧数据，保存到 images 目录）
python index.py your_s.ee_api_token

# 方式二：全量下载（时间戳命名，保存到 see 目录）
python index_see.py your_s.ee_api_token
```

API Token 获取方式：登录 [S.EE Dashboard](https://s.ee/user/dashboard/)，在设置中获取 API Key。

## 补充：上传至 Cloudflare R2

```shell
# 1、Cloudflare 界面 R2 -> Create bucket
# 2、创建名为 blog 的 bucket
# 3、下载 rclone https://rclone.org/install/
# 4、依据官方文档对 rclone 进行配置
# CF 文档地址：https://developers.cloudflare.com/r2/examples/rclone/
# rclone 文档地址：https://rclone.org/docs/

# 创建配置文件
rclone config file

# 将本地的 images 文件夹上传至 R2 存储桶
# 示例：rclone copy "./images" blog:blog/images
rclone copy "your_local_images_folder" blog:blog/images
```
