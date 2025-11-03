print("Introduzca una nota para saber su calificación")
num = int(input())
match num:
    case num if num >= 0 and num < 3:
        print("Muy deficente")
    case num if num >= 3 and num < 5:
        print("Insuficiente")
    case num if num >= 5 and num < 6:
        print("Suficiente")
    case num if num >= 6 and num < 7:
        print("Bien")
    case num if num >= 7 and num < 9:
        print("Notable")
    case num if num >= 9 and num <=10:
        print("Sobresaliente")

