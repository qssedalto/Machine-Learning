# 《机器学习》：可持续扩充的 LaTeX 研究笔记

这是一个使用 `ctexart` 的中文 LaTeX 文稿。封面采用 `\maketitle`，标题、作者与日期按约定固定为：

```tex
\documentclass{ctexart}
\title{机器学习}
\author{天国 付}
\date{November 2026}
\begin{document}
\maketitle
% 正文\ldots
\end{document}
```

## 目录结构

- `main.tex`：主文件，标题、目录、正文的 `\input` 顺序与文献输出。
- `config/preamble.tex`：字体、版式、数学环境和交叉引用。
- `chapters/*.tex`：按研究主题编排，可独立增删和修订。
- `appendices/*.tex`：符号表和修订记录。
- `code/*.py`：可单独运行的 NumPy 算例及梯度校验。
- `references.bib`：参考文献条目，按需继续扩充。

## 编译

编译器选 XeLaTeX，文献后端为 Biber。TeX Live 或 Overleaf 中在项目根目录运行：

```sh
latexmk -xelatex -interaction=nonstopmode -file-line-error main.tex
```

Overleaf：上传完整 ZIP，主文件指定 `main.tex`，编译器选择 XeLaTeX。

## 后续怎么增加主题

1. 新建 `chapters/regularization.tex`，正文以 `\section{...}` 开头。
2. 在 `main.tex` 新增 `\input{chapters/regularization}`，放在希望出现的正文位置。
3. 公式使用 `\label{eq:...}`，定理使用 `\label{prop:...}`，正文用 `\eqref{...}` 和 `\ref{...}` 交叉引用。
4. 如需新增参考资料，将对应条目写入 `references.bib`，正文使用 `\cite{...}`。
5. 在 `appendices/development_log.tex` 记录对原结论的更改。

## 已有内容与证据说明

正文的数学推导从统计学习常用定义和所列教材的相应章节展开；引用的页码并非凭空填写。多项式误差表来自此前讨论中保存的示例数据，暂未取得其原始数据文件与运行日志，因此在文中明确标记为“历史记录，待核验”。`code/` 中的脚本用于独立重现其对应的简单数学算例。所有新内容应注明前提、计算方法与数据来源。

本项目不将主题按“第几课”编排，也不设定不能修改的终稿章节数。

## 自动编译与代码检查

仓库使用 GitHub Actions 工作流 `.github/workflows/latex.yml`。
修改 `main.tex`、`chapters/`、`config/`、`appendices/`、
`references.bib` 或 `code/` 后推送到 `main`，会自动执行以下步骤：

1. 在 Python 3.12 中安装 `requirements.txt` 列出的 NumPy，并运行当前三个数值实验脚本。
2. 在 TeX Live 2026 环境中使用 XeLaTeX 与 Biber 编译 `main.tex`，并安装项目所用的 Noto 中文字体。
3. 把生成的 `main.pdf` 作为工作流产物上传至 GitHub Actions，供下载。
4. 如果 PDF 内容确有变化，且此次运行由 `main` 分支推送触发，则由 GitHub Actions 机器人更新仓库中的 `main.pdf`。

Pull Request 仅进行检查和上传构建产物，不会自动修改 `main`。也可以到仓库 **Actions** 页面手动运行工作流（`workflow_dispatch`）；手动运行只生成构建产物，不会自动提交 PDF。

初次使用时，在仓库的 **Actions** 页面查看工作流执行结果。若自动提交 PDF 失败，可检查仓库 **Settings → Actions → General → Workflow permissions**，并确保工作流有写入仓库内容的权限；PDF 构建是否成功则应以日志和产物为准。

编译过程中产生的 `.aux`、`.log` 等临时文件由 `.gitignore` 排除，已经纳入版本管理的 `main.pdf` 不会被忽略。Python 依赖统一登记在 `requirements.txt`。
