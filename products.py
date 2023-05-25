import os  # 操作系统

# 读取文件
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# 用户输入
def user_input(products):
    while True:
        name = input('请输入商品名称：')
        if name == 'q':
            break
        price = input('请输入商品价格：')
        products.append([name, price])
    print(products)
    return products

# 打印所有购买记录
def print_products(products):
    for p in products:
        print(p[0], '的价格是', p[1])

# 写入文件
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('找到文件了！')
        products = read_file('products.csv')
    else:
        print('找不到文件')
        products = []
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()
