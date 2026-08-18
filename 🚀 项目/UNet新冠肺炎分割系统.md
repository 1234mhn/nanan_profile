# UNet 新冠肺炎等级分割系统

> **项目状态：** 🚧 搭建中（阶段 0）
> **目标日期：** 2026年8月1日前
> **技术栈：** PyTorch · UNet · CT 医学影像分割
> **关联学习：** 🔬实操/监督学习 ｜ 📚 读研规划（本项目是 2026 级读研规划里「2026.8.1 前」的指定任务）

---

## 🎯 任务目标

基于 PyTorch 框架，搭建「**基于 UNet 的新冠肺炎等级分割系统**」——输入胸部 CT 扫描，自动分割出肺部病灶区域（磨玻璃影 GGO / 实变）。

**参考资料：**
- GitHub: https://github.com/RiccardoBiondi/segmentation
- 微信文章: https://mp.weixin.qq.com/XMW0OhWzONQDLIo4ERr4ZkHlg

---

## 📌 项目本质（一句话）

> 教 AI 学会"看懂"肺部 CT，**逐像素**自动圈出病变区域（不是整图判断"有/没有肺炎"）。

### 关键技术点速查
| 概念 | 说明 |
|:--|:--|
| **UNet** | 编码-解码 + 跳跃连接，医学分割最经典网络 |
| **分割 Seg** | 逐像素分类，输出 mask |
| **Dice Loss / IoU** | 分割专用损失与评估指标 |
| **CT 预处理** | HU 值裁剪、归一化 |
| **ground truth** | 医生手动的标注，用于监督+评估 |

---

## 🗺️ 整体流程（流水线）

```
原始 CT → ①数据准备 → ②拆分训练/验证/测试 → ③搭UNet → ④训练
        → ⑤推理 → ⑥评估 → ⑦归档
```

---

## 📁 项目目录结构（推荐）

```
covid_unet_segmentation/
├── data/          # 数据集（raw/ 原始 + processed/ 预处理）
├── src/           # dataset.py / model.py / train.py / predict.py / evaluate.py
├── models/        # 训练权重 .pth
├── results/       # 分割结果图 + 指标
├── notebooks/     # 实验记录
├── requirements.txt
└── README.md
```

---

## 📊 进度看板

| 阶段 | 内容 | 状态 | 验收标准 | 完成日期 |
|:--|:--|:--|:--|:--|
| **0 环境** | 装 Python + 虚拟环境 + 对版本 torch | ☐ | `import torch` 成功 | |
| **1 依赖** | SimpleITK / opencv / numpy 等 | ☐ | 依赖能 import | |
| **2 数据** | 下载 + 解压 + 看懂结构 | ☐ | 读出 CT 的 shape | |
| **3 写代码** | dataset / UNet / train | ☐ | loss 下降，保存权重 | |
| **4 评估** | Dice/Sens/Spec + 画图 | ☐ | 出指标 + 对比图 | |
| **5 归档** | README + 笔记 + push | ☐ | GitHub 可见 | |

---

## 💭 个人想法（随手记）

> （这里记录你自己的思考、灵感、疑问，随时追加）

- 待补充……

---

## ❓ 不会的点 / 卡点清单

> （遇到不理解的地方记这里，逐个攻破，勾掉）

### 待解决
- [ ] 待补充……

### 已解决
- 无
