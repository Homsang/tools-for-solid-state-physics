# Introduction to the usage

Here the specific method of calling the tool and some calculation examples are given. You can pick it up very quickly.

## Madelung constant


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
