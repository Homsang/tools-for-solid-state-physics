# Introduction to the usage

Here the specific method of calling the tool and some calculation examples are given. Everyone can pick it up very quickly.

## Madelung constant

$\mathrm{C_{60}}$ and are synthetic football shaped macromolecules composed of 60 carbon atoms. The crystal composed of CO has an approximate fcc structure, and the lattice constant is a = 1.424nm. It is an insulator. When CA crystal grits have three K atoms to form K and C6o, one K (1) atom is in the octahedron position and the other two K (2) atoms are in the tetrahedron position (as shown in the figure), the crystal material has a superconducting transition temperature of 18K. If K, CO crystal
The volume can be approximately regarded as an ionic crystal composed of K + ions and C0 ions. Try programming to calculate K (1)
The Madelung constants of K (2) and C0 ions are 2.9195, 4.0707 and 33.1830 respectively
```python
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
