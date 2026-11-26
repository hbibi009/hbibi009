def gugudan():
    dan = int(input("몇단을 입력할까요? "))

    print(f"{dan}단")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")


gugudan()