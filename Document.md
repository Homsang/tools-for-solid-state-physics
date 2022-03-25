# A Brief Introduction

Here the specific method of calling the tool and some calculation examples are given. Everyone can pick it up very quickly.

## Madelung constant

C_60_ is a synthetic football shaped macromolecule composed of 60 carbon atoms. The crystal composed of C_60_ has an approximate fcc structure. When C_60_ crystal is doped with three K atoms to form K_3_C_60_, one K(1) atom is in the octahedral position and the other two K(2) atoms are in the tetrahedral position. K_3_C_60_ crystal can be approximately regarded as an ionic crystal composed of K^+^ ions and C_60_^3-^.

The Madelung constants for three ions in K_3_C_60_ crystal using file `Madelung.py` is shown below.
```python
from Madelung import Material

# 实例化对象
K3C60 = Material('K3C60')

# 导入元胞信息
# 面心立方位置
K3C60.add('C60',np.array([0,0,0]),-3)
K3C60.add('C60',np.array([0,0.5,0.5]),-3)
K3C60.add('C60',np.array([0.5,0,0.5]),-3)
K3C60.add('C60',np.array([0.5,0.5,0]),-3)

# 八面体位置
K3C60.add('K1',np.array([0.5,0,0]),1)
K3C60.add('K1',np.array([0,0.5,0]),1)
K3C60.add('K1',np.array([0,0,0.5]),1)
K3C60.add('K1',np.array([0.5,0.5,0.5]),1)

# 四面体位置
K3C60.add('K2',np.array([0.25,0.25,0.25]),1)
K3C60.add('K2',np.array([0.25,0.25,0.75]),1)
K3C60.add('K2',np.array([0.25,0.75,0.25]),1)
K3C60.add('K2',np.array([0.75,0.25,0.25]),1)
K3C60.add('K2',np.array([0.75,0.75,0.25]),1)
K3C60.add('K2',np.array([0.75,0.25,0.75]),1)
K3C60.add('K2',np.array([0.25,0.75,0.75]),1)
K3C60.add('K2',np.array([0.75,0.75,0.75]),1)

# 使用方法计算马德隆常数
print('C60:\t', K3C60.alpha(0), '\nK1:\t', K3C60.alpha(7), '\nK2:\t', K3C60.alpha(-1))
```
The results are as below.
```
C60:     42.60291890523868 
K1:      -0.22047811795502253 
K2:      7.210725543108959
```
