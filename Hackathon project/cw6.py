#შექმენით რაიმე string ტიპის ცვლადი და დათვალეთ რამდენი ხმოვანია ამ string'ში
string = input("enter string here: " )
total=0
for i in string:
    if i in ["ა","ე","ი","ო","უ"]:
        total += 1
print(total)


