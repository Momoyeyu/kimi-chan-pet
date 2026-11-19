# 署名、来源与许可边界

## 本项目不是官方形象

“Kimi 娘 · Q 版”是社区同人桌宠，不是 Moonshot AI／月之暗面的官方角色、官方素材或官方背书。Kimi、Moonshot AI 及相关商标归各自权利人所有。

`assets/petfetch.svg` 中的 Unicode 小蓝球文字画仅参考 Kimi Work 内置小蓝球及 Kimi Code 的圆形、蓝色与深色方眼特征，是由文字符号构成的非官方彩蛋，不是官方图像素材。

## 原作者与原始出处

角色形象与原始美术设计：**ZipZipPipe**。

- 哔哩哔哩：<https://space.bilibili.com/4168597>（用户 ID：4168597）
- Pixiv：<https://www.pixiv.net/users/18604994>（用户 ID：18604994）
- 原始立绘合集：<https://www.pixiv.net/artworks/148186519>（《AI娘化》，Kimi 位于第 6 页）
- Q 版设计展示：<https://www.bilibili.com/video/BV1tE9XBbErS/>（《大AI和小AI们》，约 41 秒处）
- 作者关于开放分享与再创作的说明：<https://www.bilibili.com/video/BV1bARXBYEZz/>（《“亿万”身家的她们》）

## 原作者的使用要求

ZipZipPipe 在 Pixiv《AI娘化》的原始说明中写道：

> 作为保存用，方便所有人取用，需要标注作者，不可商用。

作者在哔哩哔哩《“亿万”身家的她们》的简介中也说明，自己的图开放分享，并允许用于再创作。

作者针对 **DeepSeek 鲸鱼娘** 另行声明了 CC BY-NC-SA 4.0；那一角色特定的声明不自动等同于 Kimi 娘的许可。本项目不声称 ZipZipPipe 已为 Kimi 娘选择某个统一的标准开源许可证，只依据上述“署名、不可商用、允许再创作”的原始要求分发衍生作品。

## 本项目做了什么

本项目基于上述角色设计生成了新的 Q 版动画帧，并进行了以下技术处理：

- 将动作帧规范化为 256 × 288 像素的透明 PNG 图集；
- 制作待机、左右移动、工作、等待、失败及两组随机动作；
- 追加“长笛演奏”自定义动作；
- 提供可选的点击触发辅助脚本。

这些修改不代表原作者或 Moonshot AI 对本项目的认可、合作或背书。

## 许可分配

### 角色美术与桌宠素材

`kimi-chan/pet.json`、`kimi-chan/spritesheet.png`、`assets/` 中的角色图像和动画预览，以 **Creative Commons Attribution-NonCommercial 4.0 International（CC BY-NC 4.0）** 发布，完整条款见 `LICENSE`：

<https://creativecommons.org/licenses/by-nc/4.0/>

使用该素材时必须：

1. 保留 ZipZipPipe 的署名及上述原始出处；
2. 标明本项目所做的修改；
3. 仅用于非商业用途；
4. 保留本 `NOTICE.md` 和 `LICENSE`。

本项目的 CC BY-NC 4.0 许可只覆盖我们有权许可的新增衍生内容，不取代原作者的权利与使用要求，也不提供任何商业授权。

### 辅助代码

`scripts/` 中由本项目编写的安装与预览辅助代码以 **MIT License** 发布，见 `LICENSE-CODE`。MIT 只适用于这些代码文件，不改变角色美术的非商业限制。

## 更正与下架

如果原作者认为本项目的署名或使用方式不妥，请在仓库中提交 Issue，并附上对应素材与原始出处。核实后应及时更正署名、调整分发方式或下架相关素材。
