from __future__ import print_function
import torch
x = torch.rand(5, 3)
print(x)

x = torch.empty(5, 3)
print(x)

# 构造一个随机初始化的矩阵：
x = torch.rand(5, 3)
print(x)

# 构造一个矩阵全为 0，而且数据类型是 long.
x = torch.zeros(5, 3, dtype=torch.long)
print(x)

# 构造一个张量，直接使用数据：
x = torch.tensor([5.5, 3])
print(x)

# 创建一个 tensor 基于已经存在的 tensor
x = x.new_ones(5, 3, dtype=torch.double)
# new_* methods take in sizes
print(x)
x = torch.randn_like(x, dtype=torch.float)

# override dtype!
print(x)

# 获取维度信息
print(x.size())

# 加法操作
y = torch.rand(5, 3)
x + y
torch.add(x, y)
## in place
y.add_(x)

# 改变大小
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())

# 获取元素的值
x = torch.randn(1)
print(x)
print(x.item())