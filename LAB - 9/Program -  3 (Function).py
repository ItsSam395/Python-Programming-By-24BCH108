def create_array(dim1, dim2, dim3, initial_value):
    array_3d = [[[initial_value for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]
    return array_3d

dim1 = 3
dim2 = 4
dim3 = 5
initial_value = 7

result_array = create_array(dim1, dim2, dim3, initial_value)

for i in range(dim1):
    print(f"Layer {i+1}:")
    for j in range(dim2):
        print(result_array[i][j])
    print()
