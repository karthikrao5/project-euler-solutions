
# palins = []
# largest = 0
# for i in range(1000):
#     for j in range(1000):
#         product = i * j
#         if str(product)[::-1] == str(product) and product not in palins and product > largest:
#             palins.append(product)
#             largest = product
#         j+=1
#     i+=1
# print(palins[-9:])
MAX = 1000

def palin():
    a, b = 1, 1
    while a < MAX and b < MAX:
        yield a * b

if __name__ == "__main__":

