import torch

x = torch.randn(4, 512)
x = x.view(4, 8, -1) # key origin
print(x.shape)
x = x[:, :, None]
print(x.shape)

y = torch.randn(4, 1, 512)
y = y.view(4, 1, 8, -1) #key now
print(y.shape)