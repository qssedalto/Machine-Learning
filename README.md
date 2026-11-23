# 机器学习：从直观例子到公式推导

本仓库为中文机器学习学习笔记，正文采用“直观问题—数学定义—逐步推导—手工计算—适用条件”的结构。第一至第五课保留原文，第六至第十课整理为同风格的 LaTeX 教材章节。新增章节只包括理论、例题、公式推导和说明，不包含 Python 实验。

阅读入口：[main.pdf](main.pdf)（构建产物可能暂时落后于源码）；主文件：[main.tex](main.tex)；版式：[config/preamble.tex](config/preamble.tex)；参考文献：[references.bib](references.bib)。

## 十课目录

| 课次 | 主题 | 核心内容 | 正文 |
|---|---|---|---|
| 1 | 机器学习基础 | 特征、模型、损失函数与经验风险 | [基础](chapters/foundations.tex) |
| 2 | 线性回归与最小二乘 | RSS、MSE、导数与正规方程 | [最小二乘](chapters/least_squares.tex) |
| 3 | 梯度下降法 | 学习率、迭代与梯度 | [梯度下降](chapters/gradient_methods.tex) |
| 4 | 逻辑回归 | Sigmoid、似然、交叉熵 | [逻辑回归](chapters/logistic_regression.tex) |
| 5 | 模型评价 | 泛化、交叉验证、数据泄漏 | [模型评价](chapters/generalization.tex) |
| 6 | 正则化 | Ridge、Lasso、L1/L2、参数收缩 | [正则化](chapters/regularization.tex) |
| 7 | 决策树 | 信息熵、信息增益、基尼指数、剪枝 | [决策树](chapters/decision_trees.tex) |
| 8 | Bagging 与随机森林 | Bootstrap、OOB、预测相关性与方差 | [随机森林](chapters/random_forest.tex) |
| 9 | AdaBoost | 加权错误率、指数损失、权重更新 | [AdaBoost](chapters/adaboost.tex) |
| 10 | 支持向量机 | 超平面、几何间隔、凸二次规划 | [SVM](chapters/support_vector_machines.tex) |

## 源码组织与维护

main.tex 负责标题、摘要、目录和十个章节的顺序装配。chapters/ 每个正式章节各有一个 tex 文件。config/preamble.tex 统一字体、页边距、数学公式、图表和引用设置。appendices/notation.tex 是常用符号表；appendices/development_log.tex 记录版本；references.bib 保存四种既有教材参考资料。

仓库原有的 chapters/preface.tex、chapters/experiments.tex、chapters/open_questions.tex 仍是未参与正式构建的保留文件。config/titlepage.tex 是未启用的备用封面。code/ 中原有的七个 Python 数值实验以及 requirements.txt 均未因本次新增课程而扩展或修改。第六至第十课不新增 Python 脚本、数据分析依赖或实验章节。

## 编译

项目使用 ctexart、XeLaTeX 与 Biber。保留整个目录结构，设置 main.tex 为根文件。在具备完整 LaTeX 发行版的环境中可执行：

    latexmk -xelatex -interaction=nonstopmode -file-line-error main.tex

.github/workflows/latex.yml 会在 main 分支对应源文件更新时运行原有七个 Python 数值检查、使用 XeLaTeX 构建文档、上传 PDF，并在满足既有条件时尝试更新 main.pdf。新增章节的提交与 PDF 构建是分开的；如果工作流尚未成功运行，main.pdf 可能暂时还是旧版。

所有教学数据均为构造例子；训练目标的最优值与泛化能力是不同概念。