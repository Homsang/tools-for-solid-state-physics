import numpy as np


class Material:

    def __init__(self, name):
        self.name = name
        self.comp = []
        self.pos = []
        self.elec = []
        self.n = 0
    
    def add(self, comp, pos, e):
    	# 元胞信息导入
        if 1 in pos:
            raise Exception('Wrong Input')
        self.comp.append(comp)
        self.pos.append(pos)
        self.elec.append(e)
        self.n += 1
    
    def centerize(self, n):
    	# 以 n 为中心，构建单胞
        dx, dy, dz = self.pos[n] - np.array([0.5,0.5,0.5])
        self.cubepos = []
        self.cubeelec = []
        self.cubefrac = []
        self.e = self.elec[n]
        self.nn = 0
        for i in range(self.n):
            px, py, pz = self.pos[i]
            for sx in [-1,0,1]:
                for sy in [-1,0,1]:
                    for sz in [-1,0,1]:
                        x = px + sx - dx
                        y = py + sy - dy
                        z = pz + sz - dz
                        if 0 <= x <= 1 and 0 <= y <= 1 and 0 <= z <= 1:
                            self.cubepos.append(np.array([x,y,z]))
                            self.cubeelec.append(self.elec[i])
                            ct = sum(1 for w in [x,y,z] if w in [0,1])
                            self.cubefrac.append(np.power(1/2,ct))
                            self.nn += 1

    def alpha(self, n, Max=5):
    	# 利用以 n 为中心单胞，计算马德隆常数
        self.centerize(n)
        f = 0
        for i in range(self.nn):
            x, y, z = self.cubepos[i] - np.array([0.5,0.5,0.5])
            e = self.cubeelec[i]*self.cubefrac[i]
            for xls in np.arange(-Max,Max+1):
                xx = (x + xls)**2 
                for yls in np.arange(-Max,Max+1):
                    yy = (y + yls)**2
                    for zls in np.arange(-Max,Max+1):
                        zz = (z + zls)**2
                        r = np.sqrt(xx + yy + zz)
                        if r < 0.01:
                            continue
                        f += e/r
        return -f*self.e


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
