products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []         # 建立小清單，也可寫成 p = [name, price]
	p.append(name)
	p.append(price)
	products.append(p)  # 把小清單放到大清單
						# 簡潔寫法 products.append([name, price])
print(products)
