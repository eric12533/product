import os

def read_file(filename):
	product = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name,price = line.strip().split(',')
			product.append([name, price])
	return product

#讓使用者輸入
def user_input(product):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		product.append([name, price])
	print(product)
	return product

#印出所有購買紀錄
def print_product(product):
	for p in product:
		print(p[0],'的價格是',p[1])


#寫入檔案
def write_file(filename, product):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		f.write('商品,價格\n')
		for p in product:
			f.write(p[0] + ',' + p[1] + '\n')


def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('存在檔案!')
		product = read_file(filename)
	else:
		print('沒有檔案')
	product = user_input(product)
	print_product(product)
	write_file('products.csv', product)

main()

