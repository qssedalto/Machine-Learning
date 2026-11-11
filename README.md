# 机器学习 · LaTeX 项目文件指南

> **这个仓库放的是什么？** 一份可持续扩展的中文机器学习研究笔记：用 LaTeX 排版数学推导，用 Python 保存数值实验，用 BibLaTeX 管理参考文献。  
> **从哪里开始？** 要读成品看 [main.pdf](main.pdf)；要改正文进入 [chapters/](chapters/)；要改版式打开 [config/preamble.tex](config/preamble.tex)；要改摘要打开 [main.tex](main.tex)。

## 项目是怎样组成的

`main.tex` 是入口，但**不承载全部正文**。编译器从中依次读取章节、附录与文献，再生成 PDF。

```text
Machine-Learning/
├── main.tex                       主文件：标题、摘要、目录、章节装配
├── main.pdf                       已提交的 PDF 成品
├── README.md                      本文件：目录索引与维护说明
├── references.bib                 文献数据库
├── requirements.txt               Python 实验依赖
├── .gitignore                     忽略临时文件的规则
├── .github/
│   └── workflows/
│       └── latex.yml              自动检查 Python 并编译 PDF
├── config/
│   ├── preamble.tex               全局版式、字体、公式和代码样式
│   └── titlepage.tex              备用独立封面（当前未启用）
├── chapters/
│   ├── preface.tex                引言
│   ├── foundations.tex            从数据到优化问题
│   ├── least_squares.tex          线性回归与最小二乘估计
│   ├── gradient_methods.tex       梯度下降与步长
│   ├── logistic_regression.tex    逻辑回归与对数损失
│   ├── generalization.tex         模型评价、过拟合和泛化
│   ├── experiments.tex            数值算例与代码展示
│   └── open_questions.tex         后续研究方向
├── code/
│   ├── linear_regression_demo.py  解析最小二乘 vs. 梯度下降
│   ├── logistic_gradient_check.py 逻辑回归解析梯度的数值校验
│   └── polynomial_comparison.py   多项式模型复杂度对比
└── appendices/
    ├── notation.tex               符号与记号约定
    └── development_log.tex        修订记录
```

## 01 / 根目录：文档的入口与输出

| 文件 | 它负责什么 | 什么时候编辑 |
| --- | --- | --- |
| [`main.tex`](main.tex) | **总装配文件**：定义文档类；加载 `config/preamble.tex`；设置标题、作者、日期；写入**摘要与关键词**；生成目录；以 `\input` 按顺序加入各章节和附录；最后输出参考文献。 | 调整文章结构、摘要、关键词或章节顺序时。 |
| [`main.pdf`](main.pdf) | 已纳入版本管理的 PDF 阅读版，是编译**产物**，不是正文源文件。 | 通常不手工编辑；由编译流程更新。它可能暂时落后于源代码，以实际构建结果为准。 |
| [`README.md`](README.md) | 你正在阅读的项目地图，解释每个文件的职责与维护方法。 | 新增、删除或调整项目文件时同步更新。 |
| [`references.bib`](references.bib) | 以 BibTeX/BibLaTeX 条目保存教材与著作等文献信息；正文用 `\cite{条目键}` 引用。 | 添加、核对或修订文献元数据时。 |
| [`requirements.txt`](requirements.txt) | Python 数值实验的依赖清单；当前列出 NumPy 版本范围。 | 实验确实引入新依赖时。 |
| [`.gitignore`](.gitignore) | 排除 `.aux`、`.log`、`.bbl` 等 LaTeX 辅助文件，以及 Python 缓存、虚拟环境和编辑器临时文件；**不忽略** `main.pdf`。 | 调整哪些生成文件需要跟踪时。 |
| [`.github/workflows/latex.yml`](.github/workflows/latex.yml) | GitHub Actions 工作流：安装 Python 依赖、运行三个实验脚本，在 TeX Live 环境中用 XeLaTeX/Biber 构建 PDF，上传构建产物；满足条件时把变化后的 `main.pdf` 提交回 `main`。 | 修改 CI、编译环境、自动检查或 PDF 发布流程时。 |

## 02 / config：全文排版与封面

| 文件 | 具体职责 | 当前状态 |
| --- | --- | --- |
| [`config/preamble.tex`](config/preamble.tex) | 设置 A4 页边距、西文字体、宏包、章节标题颜色与间距、页眉页脚、定理环境、数学符号快捷命令、Python 代码框、图表及 GB/T 7714 文献样式。 | **正在使用**，由 `main.tex` 加载。中文字体交给 `ctexart` 的内置 Fandol 字体映射管理，避免在科技云重复覆盖字体。 |
| [`config/titlepage.tex`](config/titlepage.tex) | 设计独立封面：主副标题、分隔线、版本和编译日期等。 | **目前未启用**：`main.tex` 使用 `\maketitle`，没有 `\input{config/titlepage}`。修改这个文件不会改变当前 PDF 的封面。 |

## 03 / chapters：八个正文章节

每个文件对应一个研究主题，章节内容通过 `main.tex` 中的 `\input{chapters/文件名}` 进入最终文档。

| 文件 | 正文内容 | 主要关注点 |
| --- | --- | --- |
| [`chapters/preface.tex`](chapters/preface.tex) | 引言、研究范围、写作思路和教材来源。 | 区分模型拟合、参数求解与泛化能力。 |
| [`chapters/foundations.tex`](chapters/foundations.tex) | 数据、模型族、损失函数、经验风险和学习任务的定义。 | 怎样从数据建模走向一个可求解的优化问题。 |
| [`chapters/least_squares.tex`](chapters/least_squares.tex) | 线性回归、残差平方和、正规方程与相关条件。 | 最小二乘解从哪里来、何时存在或唯一。 |
| [`chapters/gradient_methods.tex`](chapters/gradient_methods.tex) | 方向导数、负梯度、步长选择及一阶方法的性质。 | 为何下降、何时收敛、步长为什么重要。 |
| [`chapters/logistic_regression.tex`](chapters/logistic_regression.tex) | Logistic 概率模型、伯努利似然、交叉熵及梯度。 | 分类损失如何由概率假设推导出来。 |
| [`chapters/generalization.tex`](chapters/generalization.tex) | 训练与测试风险、过拟合、偏差—方差以及评价方法。 | 为什么训练误差低不保证新数据表现好。 |
| [`chapters/experiments.tex`](chapters/experiments.tex) | 解析算例、数值结果的说明及源代码片段。 | **实验的书面解释**，并使用 `\lstinputlisting` 从 `code/` 读取 Python 代码。 |
| [`chapters/open_questions.tex`](chapters/open_questions.tex) | 正则化、进一步的数值优化、统计推断等待扩展议题。 | 记录尚未展开的研究问题，而非把它们当作已证明结论。 |

## 04 / code：三个独立的 Python 实验

这些脚本用于核对算法思想；**LaTeX 编译不会自动执行 Python**。GitHub Actions 会单独运行它们。

| 文件 | 做了什么 | 对应正文 |
| --- | --- | --- |
| [`code/linear_regression_demo.py`](code/linear_regression_demo.py) | 用 NumPy 的最小二乘求解与手写全批量梯度下降比较回归参数。 | `least_squares.tex`、`gradient_methods.tex`、`experiments.tex` |
| [`code/logistic_gradient_check.py`](code/logistic_gradient_check.py) | 通过中心差分近似梯度，检查逻辑回归负对数似然的解析梯度。 | `logistic_regression.tex` |
| [`code/polynomial_comparison.py`](code/polynomial_comparison.py) | 在固定随机种子的构造数据上比较不同次数多项式回归的误差。 | `generalization.tex`、`experiments.tex` |

> **区分两种工作**：编辑 `code/*.py` 改变的是实验程序；编辑 `chapters/experiments.tex` 改变的是 PDF 中对实验的描述。若增删代码行，还需要检查 `\lstinputlisting` 的行号范围。

## 05 / appendices：正文之外的辅助材料

| 文件 | 它的作用 |
| --- | --- |
| [`appendices/notation.tex`](appendices/notation.tex) | 统一列出 `m`、`p`、`X`、`J(θ)`、经验风险等数学符号及其约定，减少跨章节歧义。 |
| [`appendices/development_log.tex`](appendices/development_log.tex) | 记录文稿版本、修订时间与内容变更；目前含 v0.1 的初始记录。 |

## 常见修改：该打开哪个文件？

| 你想做的事 | 打开这里 |
| --- | --- |
| 改摘要或关键词 | [`main.tex`](main.tex) 的 `abstract` 环境及后续关键词行 |
| 改作者、标题、日期 | [`main.tex`](main.tex) 的 `\author`、`\title`、`\date` |
| 改中文排版或全局字体 | [`config/preamble.tex`](config/preamble.tex)；先检查 `ctexart` 的默认设置，避免重复定义 |
| 改页边距、标题样式、代码框 | [`config/preamble.tex`](config/preamble.tex) |
| 改某一节数学推导 | 对应的 [`chapters/`](chapters/) 文件 |
| 改实验算法与数据 | 对应的 [`code/`](code/) 脚本，并同步核对正文说明 |
| 加一条参考文献 | [`references.bib`](references.bib)，并在正文中引用 |
| 增加数学符号解释 | [`appendices/notation.tex`](appendices/notation.tex) |
| 记录修改历史 | [`appendices/development_log.tex`](appendices/development_log.tex) |
| 增加全新章节 | 新建 `chapters/新主题.tex`，并在 [`main.tex`](main.tex) 加入对应的 `\input` |

## 编译与同步

**中国科技云 / 其他在线 LaTeX 编辑器**

1. 上传**完整项目**并保留文件夹层级；不能只上传 `main.tex`。
2. 将 `main.tex` 设为主文档，编译器选 **XeLaTeX**。
3. 项目采用 `biblatex` + **Biber**。参考文献未更新时，检查平台的 Biber 处理是否完成，然后再次编译。
4. 出现缺字或字体替代警告时，优先查看编译日志与 `config/preamble.tex`；不要把字体问题误认为章节未上传。

**本地运行**

```sh
python -m pip install -r requirements.txt
python code/linear_regression_demo.py
python code/logistic_gradient_check.py
python code/polynomial_comparison.py
latexmk -xelatex -interaction=nonstopmode -file-line-error main.tex
```

最后一条命令需要完整的 TeX Live、XeLaTeX、latexmk 和 Biber 环境。

**GitHub 自动构建**

- 修改正文、配置、附录、代码、依赖、文献或工作流文件，推送到 `main` 后会触发 [自动构建](.github/workflows/latex.yml)；单独修改本 README **不触发**该工作流。
- 工作流会检查三个 Python 实验并生成 PDF，上传为 Actions 构建产物。
- 由 `main` 分支的 `push` 触发时，如 PDF 有变化，工作流尝试自动更新仓库中的 `main.pdf`；Pull Request 和手动触发不会自动回写 PDF。
- GitHub Actions 的系统字体与中国科技云可能不同。当前工作流仍安装 Noto 字体包，但正文使用的中文字体由 `ctexart` 设置，不再依赖手动指定 Noto 字体名称。

---

**维护原则**：论文内容写在 `chapters/`，排版规则放在 `config/`，可运行实验放在 `code/`，文献条目放在 `references.bib`。修改数学结论时，保留成立条件与证据；新增文件时，及时更新这份指南。
