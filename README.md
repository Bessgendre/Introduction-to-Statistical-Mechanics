# 统计力学笔记

## 前言

&emsp;&emsp;本文写于中国科学技术大学化学物理系所开设的统计力学 2023 春的课堂，授课老师是徐瑞雪、侯中怀两位教授。在笔记中，作者不仅追求将二位老师的课堂内容完整地记录下来，更期望能对统计力学的内在逻辑联系与脉络予以清晰的表达。作者主要参考了帕斯里亚、朗道、费曼以及钱德勒的相关专著，希望能融会贯通。

&emsp;&emsp;统计力学将热力学问题归结于 **概率与统计推断** ，以等概率假设与遍历性假设为基础，建立起一整套关于微观-宏观相互联系的桥梁。通过一定的统计推断，我们可以从众多自由度中提取出一些重要信息，而忽视一些细节，或者无关紧要的部分。

&emsp;&emsp;虽然我们打算忽略一些细节，但是还是得来看看这些细节都是怎么一回事。经典力学以相空间和哈密顿函数为基础，以 **正则变量** 的时间演化给出力学系统的时间演化。这些正则变量服从哈密顿方程：

$$
\begin{aligned}
    \dot{q_i} &= \frac{\partial H}{\partial p_i} \\
    \dot{p_i} &= -\frac{\partial H}{\partial q_i}
\end{aligned}
$$

&emsp;&emsp;不过，要想求解如此庞大的耦合微分方程系统是很困难的一件事——例如采样，而且是对 $10^{23}$ 量级的粒子数！既然庞加莱早已证明，连最简单的三体问题都没有解析解，且对初值敏感， **我们又有什么信心认为对于 $10^{23}$ 量级的结果是可靠的呢？**

&emsp;&emsp;好消息是，统计力学的遍历性假设将会让这些烦人的细节从我们的面前消失。考虑一个宏观小而微观大的子系统，它与周围的环境进行着复杂紊乱的相互作用，所以我们有理由认为：在足够长的时间间隔内子系统在自身所有可能的状态中经历足够多的次数。同时，这一假设也让我们相信：某个子系统的统计分布与同一系统的其他任意小部分的初始状态无关，因为从任何初始状态出发，这个系统总是将所有可能的状态都走了足够多遍，以至于这种初始状态的影响在足够长的时间内，被系统其余的、更为广大的部分的影响所完全消除。换句话说， **每一个状态都可以取为初始状态** 。

&emsp;&emsp;所以我们看到，统计力学对一个物理系统的预言具有概率的特征。但必须指出的一点是，这样的概率绝非系统所固有，而是因为得到这些结论所依据的条件远比完整的力学描述所需要的少得多——例如我们可以仅用三个宏观可测的状态参量就能完全确定一个宏观系统，还能确定系统其他的状态参量的值，**而这三个自由度实际上将天文数字的微观自由度都统摄其下**。

&emsp;&emsp;另一个问题是 **微观可逆性与宏观不可逆性的矛盾** ——如果用 $-t$ 替代求解结果中的 $t$ （做一个时间反演，或者说把录像带倒着放）仍然是演化方程的一个可能的解，但我们从来没有观察到滴进池塘的墨水又重新聚集成刚滴进去时的形状。这样一来， **时间的流逝似乎就有了确定的方向。** 这样的“热力学时间”和我们其他地方作为正则变换参量（Hamilton-Jacobi 理论）或者酉变换参量（量子力学传播子）所引入的时间有什么差别？

&emsp;&emsp;总之，统计力学是作者本科以来最喜欢的一门理论课，它是一个关于“大”的理论。固然对“小”的研究也同样迷人（量子力学、第一性原理计算、单分子反应机理的探究等等），对这些细节的研究加深了我们对自然界的微观认识，使得我们对自然界究竟是怎样运转的有了更多的了解，甚至于在原子、电子、夸克尺度上让基本力服从我们的意志，但我仍然坚信：**More is Different** 。具有巨大自由度数目的系统虽然系统与单一粒子遵循同样的力学规律，但是自由度的巨大却导致性质上的全新规律性。而这样的规律，是在微观层面意识不到的。

&emsp;&emsp;不识庐山真面目，只缘身在此山中。进入大数据时代，甚至现在的 new bing 和 ChatGPT 所引领的大语言模型时代，科学界的主要矛盾也在变化。这是统计语言大放光彩的时代，也是科技革命的浪潮之巅。

&emsp;&emsp;统计力学将会爆发出的能量，我想是不言而喻的。



