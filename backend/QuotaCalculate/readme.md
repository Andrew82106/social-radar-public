指标计算公式：

# time quota

输入：时间序列$A=[a_1,a_2,a_3,...,a_n]$

接近度：$Dis=\frac{\sum_{i=1}^{n}(a_i-B)}{24\times 60\times 60\times n}=\frac{\sum_{i=1}^{n}(a_i-B)}{86400n}$，其中$B$为今日日期

聚合度：$C=std(A)=\sqrt{\frac{1}{n}\sum_{i=1}^n(a_i-\overline{a_i})^2}$

时间热度指标：$q_{time}=\frac{C}{Dis}$
