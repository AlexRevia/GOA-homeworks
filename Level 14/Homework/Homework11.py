# მომხმარებელს შეეკითხეთ რიცხვი და შეინახეთ num1 ცვლადში მთელი რიცხვის სახით.
#მომხმარებელს შეეკითხეთ რიცხვი და შეინახეთ num2 ცვლადში მთელი რიცხვის სახით.
#მომხმარებელს შეეკითხეთ რიცხვი და შეინახეთ num3 ცვლადში მთელი რიცხვის სახით.

#შექმენით შემდეგი დიაპაზონი: range(num1, num2, num3)

#გადაუარეთ ამ დიაპაზონს for ციკლით და დაბეჭდეთ საიტერაციო ცვლადის კვადრატები

num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
num3 = int(input("შეიყვანეთ მესამე რიცხვი: "))

for i in range(num1, num2, num3):
    print(i**2) 
