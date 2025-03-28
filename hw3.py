def get_fixed_price(discount_rate, discounted_price) :
    original_price=discounted_price*(100/(100-discount_rate))
    return original_price

discount_rate=int(input('할인율은?'))
discounted_price_A=int(input('A상품의 할인된 가격은?'))
discounted_price_B=int(input('B상품의 할인된 가격은?'))

original_price_A=int(get_fixed_price(discount_rate, discounted_price_A))
original_price_B=int(get_fixed_price(discount_rate, discounted_price_B))

print('A 상품의 정가는', original_price_A, '원')
print('B 상품의 정가는', original_price_B, '원')