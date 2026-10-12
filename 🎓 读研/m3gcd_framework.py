#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""M3GCD 整体框架图 v3 —— 清爽专业，忠于论文 Fig.1 数据流"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon, Circle
import matplotlib.font_manager as fm

zh = "Noto Sans CJK SC"
for p in ["/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
          "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"]:
    try:
        fm.fontManager.addfont(p)
    except Exception:
        pass
plt.rcParams["font.family"] = zh
plt.rcParams["axes.unicode_minus"] = False

W, H = 16, 9.4
fig, ax = plt.subplots(figsize=(W, H), dpi=220)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")
# 全局浅灰淡背景角标
ax.set_facecolor("#fbfcfe")

# ---------- 颜色板 ----------
C_IN   = "#dbe7f5"   # 输入 浅蓝
C_IMG  = "#2e75b6"
C_TXT  = "#c55a11"
C_DEF  = "#70ad47"   # 主块
C_LEB  = "#ffd966"
C_CLU  = "#b4a7d6"   # 邻居/聚类
C_CD   = "#7030a0"
C_OUT  = "#c00000"
INK    = "#1a1a1a"
SUB    = "#444444"

def rbox(x, y, w, h, fc, ec="#222222", lw=1.8, rad=1.8):
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle=f"round,pad=0.25,rounding_size={rad}",
                       linewidth=lw, edgecolor=ec, facecolor=fc)
    ax.add_patch(p)
    return (x, y, w, h)

def rt(x, y, s, fs=13, color=INK, weight="normal", ha="center", va="center", ls=1.5):
    ax.text(x, y, s, ha=ha, va=va, fontsize=fs, color=color,
            weight=weight, linespacing=ls)

def arrow(x1, y1, x2, y2, color="#666666", lw=2.6, ms=20, rad=0.0, ls="-"):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=ms,
                        linewidth=lw, color=color, linestyle=ls,
                        connectionstyle=f"arc3,rad={rad}")
    ax.add_patch(a)

# ================= 标题 =================
ax.add_patch(FancyBboxPatch((16, 92.5), 68, 6.4,
             boxstyle="round,pad=0.3,rounding_size=3",
             linewidth=0, facecolor="#1f3864"))
rt(50, 95.7, "M3GCD 整体框架", fs=16, color="white", weight="bold", ha="center")
rt(50, 89.3, "图像 + 临床文本配对 ｜ 识别已知疾病 ＋ 自动发现未知新类别 ｜ 无需预设类别总数",
   fs=10.5, color=SUB, ha="center")

# ================= 输入层（最左） =================
# 输入对（图片胶囊）
rbox(2.5, 42, 13, 20, "#ffffff", ec="#8faadc", lw=2)
# 图像缩略小图标感
ax.add_patch(Circle((6.5, 55.5), 3.3, color=C_IMG, alpha=0.25))
rt(6.5, 55.2, "图像", fs=7.5, color=C_IMG, weight="bold")
ax.add_patch(Circle((6.5, 47.5), 3.3, color=C_TXT, alpha=0.25))
rt(6.5, 47.2, "文本", fs=7.5, color=C_TXT, weight="bold")

# ================= 特征提取 =================
rbox(18.5, 42, 15, 20, C_IN, ec=C_IMG, lw=2)
rt(26, 56.5, "特征提取", fs=12.5, weight="bold", color="#1f3864")
rt(26, 49.5, "图像 · ResNet-50\n文本 · BioClinicalBERT", fs=9.5, color=INK)
arrow(15.7, 55.5, 18.3, 55.5, color=C_IMG, lw=2.6, ms=18)
arrow(15.7, 47.5, 18.3, 47.5, color=C_TXT, lw=2.6, ms=18)

# ================= ① DEF（含 LEB 保护）主处理 =================
rbox(36, 30, 30, 44, C_DEF, ec="#548235", lw=2.4)
rt(51, 67.5, "① DEF · 动态专家融合", fs=13.5, weight="bold", color="white")
rt(51, 61, "Dynamic Expert Fusion", fs=9.5, color="#e7f2dc", ha="center")
rt(51, 53.5, "路由器(仿 MoE) 动态决定\n每例该更信「图像」还是「文本」,\n再加权融合成一个表示", fs=10.5, color="white")
# LEB 内嵌小卡片（DEF 内部下半）
rbox(38.5, 33.5, 25, 9.5, C_LEB, ec="#7f6000", lw=1.6, rad=1.4)
rt(51, 40.5, "ⓐ LEB 局部平衡 · 保护单模态", fs=9.5, weight="bold", color="#3f2d00")
rt(51, 36.3, "评估邻居内聚/熵 → 别把微弱关键信号平均掉", fs=8.6, color="#5c4700", ha="center")



# ================= ② 邻居/聚类分配 =================
rbox(68.5, 30, 13.5, 44, "#ffffff", ec="#8888b8", lw=2)
rt(75.3, 66.8, "② 邻居相似\n+ 软聚类分配", fs=10.5, weight="bold", color="#3a3a6b")
rt(75.3, 55.5, "把每例与最像的\n邻居聚团,\n给个软标签 q", fs=9.3, color=SUB)
rt(75.3, 35.5, "（无监督）", fs=8.6, color="#777777")

# 主链箭头: DEF -> 聚类 (只一条, 指向聚类块左缘)
arrow(66.2, 52, 68.3, 52, color="#666666", lw=3, ms=22)

# ================= ③ CD 类别扩散 =================
rbox(83.8, 30, 13.5, 44, C_CD, ec="#3f1e63", lw=2.4)
rt(90.5, 66.8, "③ CD\n类别扩散", fs=13, weight="bold", color="white")
rt(90.5, 55, "Metropolis–Hastings\n分裂–合并\n自动增删类别数", fs=9.3, color="#ecdfff")
rt(90.5, 36.5, "发现未知新类", fs=9.5, color="#ffffff", weight="bold")

arrow(82.4, 52, 83.6, 52, color="#3f1e63", lw=3, ms=22)

# ================= 输出 =================
rbox(83.8, 8.5, 13.5, 15.5, C_OUT, ec="#8b1a1a", lw=2.2)
rt(90.5, 19, "输出", fs=12, weight="bold", color="white")
rt(90.5, 14.5, "已知类：分对\n未知类：新发现病", fs=9, color="#ffe0e0")
arrow(90.5, 30, 90.5, 24.2, color="#8b1a1a", lw=3, ms=22)

# ================= 底部 损失函数 横条 =================
rbox(14, 2.2, 73, 12, "#fdf1dc", ec="#c55a11", lw=1.5, rad=1.6)
rt(16.3, 8.8, "训练：", fs=11.5, weight="bold", color="#c55a11", ha="left")
rt(27, 8.7, "总损失 L = L_align + λ1·L_sim + λ2·L_ent", fs=12.5, weight="bold",
   color="#1f3864", ha="center")
rt(50, 4.6, "L_align 聚类软标签与预测对齐 ｜ L_sim 全局权重与局部判断一致 ｜ L_ent 熵正则 · 防坍缩",
   fs=9.3, color="#5a4a00", ha="center")
# 损失横条到主链的虚线示意约束(只简短标注,不穿越图形)
ax.plot([48.5, 48.5], [14.4, 29.6], color="#c55a11", lw=1.2, ls=":")

plt.tight_layout()
out = "/root/.openclaw/workspace/nanan_profile/🎓 读研/M3GCD_整体框架图.png"
plt.savefig(out, bbox_inches="tight", facecolor="white")
print("saved:", out)
