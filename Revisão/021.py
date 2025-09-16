#Escreva um programa que tenha uma função, maior(), que receba 5 parâmetros e retorne qual é o maior deles

def maior(n1,n2,n3,n4,n5):
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        return n1
    elif n2 > n3 and n2 > n4 and n2 > n5:
        return n2
    elif n3 > n4 and n3 > n5:
        return n3
    elif n4 > n5:
        return n4
    else:
        return n5