def buy(shopping_bag):
    item = input("상품명? ")
    if item == "":  
        return False
    quantity = int(input("수량은? "))
    if item in shopping_bag:
        shopping_bag[item] += quantity
    else:
        shopping_bag[item] = quantity
    print(f"장바구니에 {item} {quantity}개가 담겼습니다.\n")
    return True

def show(shopping_bag):
    print("\n>>> 장바구니 보기:", shopping_bag)

def find(shopping_bag):
    item = input("\n장바구니에서 확인하고자 하는 상품은? ")
    if item in shopping_bag:
        print(f"{item}(은)는 {shopping_bag[item]}개 담겨 있습니다.")
    else:
        print(f"장바구니에 {item}(은)는 없습니다.")


shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break

show(shopping_bag)
find(shopping_bag)