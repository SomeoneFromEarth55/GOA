#დავალება 8: სტუდენტის შეფასებების სისტემა (0-100 ქულა)
#შექმენი ცვლადი score, სადაც მომხმარებელი შეიტანს მიღებულ ქულას (0-დან 100-ის ჩათვლით). if-elif-else ჯაჭვის გამოყენებით განსაზღვრე ნიშანი:
#• 91-დან 100-მდე: „A“
#• 81-დან 90-მდე: „B“
#• 71-დან 80-მდე: „C“
#• 61-დან 70-მდე: „D“
#• 51-დან 60-მდე: „E“
#• 51-ზე ნაკლები: „F (ჩაიჭრა)“
score=int(input("შეიყვანე ქულა"))
if score >91 and score <=100:
    print("A")
elif score >81 and score <90:
    print("B")
elif score >71 and score <80:
    print("C")
elif score >61 and score <70:
    print("D")
elif score >51 and score <60:
    print("E")
else:
    print("F")


