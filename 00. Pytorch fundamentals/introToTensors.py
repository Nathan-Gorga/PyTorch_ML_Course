import torch



# Creating tensors
# scalar
scalar = torch.tensor(7)

print(scalar)

# get tensor back as Python int
print(scalar.item())


#vector

vector = torch.tensor([7,7])

print(vector)

# shape

print(vector.shape)



# matrix

matrix = torch.tensor([[7,8],
                       [9,10]])

print(matrix)


#tensor

tensor = torch.tensor([[[1,2,3],
                        [4,5,6],
                        [7,8,9]]])


print(tensor.shape)