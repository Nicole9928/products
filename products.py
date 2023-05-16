products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []         # 建立小清單，也可寫成 p = [name, price]
	p.append(name)
	p.append(price)
	price = int(price)
	products.append(p)  # 把小清單放到大清單
						# 簡潔寫法 products.append([name, price])
print(products)

for p in products:      # 用for loop來一個一個拿出來
	print(p[0], '的價格是', p[1])


with open('prosucts.csv', 'w', encoding='utf-8') as f:      # read(r)讀取模式，write(w)寫入模式
										  # csv可用excel，txt為文字檔
	f.write('商品,價格\n')
	for p in products:	
		f.write(p[0] + ',' + p[1] + '\n')
