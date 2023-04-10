# 迴圈loop （while loop，for loop) while 用在不知道多少次數的時候
products = []

while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ') # 不能縮進，要和name同階
	p = []
	p.append(name)
	p.append(price)
	# p = [name, price]
	products.append(p)
	# products.append([name, price]) 最縮寫
print(products)

products[0][0] #把第0格的商品名字拿出來
products[1][1] # 把大清單第一個商品的價格拿出來
# 2維度清單 two dimensional x, y 軸


