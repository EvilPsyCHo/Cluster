# Affinity Propagation

```text

# 整个算法的思想好像是基于置信传播（Belief Propagation）和对应的sum-product algorithm
# 将亲和传播算法看成选举
# s(similarities matrix), s(i,k)就相当于i对选k这个人的一个固有的偏好程度
# r(responsibility matrix), r(i,k)表示用s(i,k)减去最强竞争者的评分，可以理解为k在对i这个选民的竞争中的优势程度
# a(availability matrix), a(i, k)相当于选民i通过网上关于k的民意调查看到：有很多人（即i'们）都觉得k不错（r(i',k)>0），那么选民i也就会相应地觉得k不错，是个可以相信的选择

解释：可以用一个比喻来理解这两个量和其之间交替过程：选举。
将聚类过程看成选举：
所有人都参加选举（大家都是选民也都是参选人），要选出几个作为代表
	s(i,k)就相当于i对选k这个人的一个固有的偏好程度
    r(i,k)表示用s(i,k)减去最强竞争者的评分，可以理解为k在对i这个选民的竞争中的优势程度
    r(i,k)的更新过程对应选民i的各个参选人的挑选（越出众越有吸引力）
    a(i,k)：从公式里可以看到，所有r(i',k)>0的值都对a有正的加成。对应到我们这个比喻中，就相当于选民i通过网上关于k的民意调查看到：有很多人（即i'们）都觉得k不错（r(i',k)>0），那么选民i也就会相应地觉得k不错，是个可以相信的选择
    a(i,k)的更新过程对应关于参选人k的民意调查对于选民i的影响（已经有了很多跟随者的人更有吸引力）
    两者交替的过程也就可以理解为选民在各个参选人之间不断地比较和不断地参考各个参选人给出的民意调查。
    r(i,k)的思想反映的是竞争，a(i,k)则是为了让聚类更成功。
    
```

+ 参数
  + damping，阻尼系数，防止全部更新造成的数值震荡
  + convergence_iter，迭代中止轮数阀值
  + preference，样本偏好

+ Reference

[Brendan J. Frey and Delbert Dueck, "Clustering by Passing MessagesBetween Data Points", Science Feb. 2007]()

https://www.zhihu.com/question/25384514/answer/47636054