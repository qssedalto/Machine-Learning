# 机器学习｜精简学习笔记

一份面向初学者的中文机器学习笔记，重点是**核心概念、常用公式和简单算例**。不追求堆砌定理；先理解每个方法解决什么问题、怎样计算、有哪些限制。

**阅读成品：**[main.pdf](main.pdf)（自动编译可能稍有延迟）  
**编辑正文：**[chapters/](chapters/)  
**主文件：**[main.tex](main.tex)

## 内容

| 章节 | 重点 |
| --- | --- |
| [基本概念](chapters/foundations.tex) | 回归、分类、损失函数 |
| [线性回归](chapters/least_squares.tex) | 最小二乘法与直线拟合 |
| [梯度下降](chapters/gradient_methods.tex) | 参数更新与学习率 |
| [逻辑回归](chapters/logistic_regression.tex) | Sigmoid、交叉熵、二分类 |
| [模型评价](chapters/generalization.tex) | 过拟合、交叉验证、分类指标 |
| [算例与代码](chapters/experiments.tex) | 用 Python 检查基本方法 |
| [后续方向](chapters/open_questions.tex) | 可以继续学习的主题 |

## 项目文件

- `main.tex`：标题、目录和章节入口；`main.pdf`：生成的阅读版本。
- `chapters/`：正文，每个主题一个 `.tex` 文件。
- `code/`：线性回归、逻辑回归梯度检查、多项式比较三个小实验。
- `config/preamble.tex`：排版与公式设置。
- `references.bib`：参考书目；`appendices/`：符号和修订记录。
- `.github/workflows/latex.yml`：自动检查 Python 并编译 PDF。

## 运行

需要 Python 和 NumPy。进入仓库目录后运行：

```sh
python -m pip install -r requirements.txt
python code/linear_regression_demo.py
python code/logistic_gradient_check.py
python code/polynomial_comparison.py
```

编译中文 PDF 需要 XeLaTeX、latexmk 与 Biber：

```sh
latexmk -xelatex -interaction=nonstopmode -file-line-error main.tex
```

## 写作原则

只保留关键概念和实际常用的公式；数学结论注明必要的成立条件；用日常语言解释符号，不为形式完整而重复证明。新增内容以**容易理解、方便复习**为先。