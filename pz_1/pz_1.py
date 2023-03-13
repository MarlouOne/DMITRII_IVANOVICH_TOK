# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 08:31:38 2023

@author: 6 cadet
"""


#Практическое занятие № 1


#Алгоритм Сложения 1 
def algoritm_1():
    base = int(input('Введите число основание {Base}: '))

    a = input('Введите число a: ')
    b = input('Введите число b: ')
    
    return (int(a, base=base) + int(b, base=base))

#Алгоритм Вычетания 2
def algoritm_2():
    base = int(input('Введите число основание {Base}: '))

    a = input('Введите число a: ')
    b = input('Введите число b: ')
    
    return int(a, base=base) - int(b, base=base)
    
#Алгоритм Умножения 3 
def algoritm_3():
    base = int(input('Введите число основание {Base}: '))

    a = input('Введите число a: ')
    b = input('Введите число b: ')
    
    return int(a, base=base) * int(b, base=base)
    
# Алгоритм деления 4 
def algoritm_4():
    base = int(input('Введите число основание {Base}: '))

    a = input('Введите число a: ')
    b = input('Введите число b: ')
    
    return int(a, base=base) // int(b, base=base), int(a, base=base) % int(b, base=base)
    
    
    
    
    
# Алгоритм Мантгомери
def algoritm_5():
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    N = int(input('Введите N: '))
    R = int(input('Введите R: '))
    
    
    print(f"MP({a*R},1,{N},{R}) сравнимо = {(a*b)*R}mod({N})")
    return ((a*b)*R)%N

# Алгоритм 6
def algoritm_6():
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    N = int(input('Введите N: '))
    R = int(input('Введите R: '))
    
    answer = ((a+b)*R)%N
    print(f"{answer} сравнимо = ({a}+{b}){R}(mod({N}))")
    
    
    A = (a*R)%N
    B =((b)*R)%N
    
    
    return answer


# Алгоритм 7
def algoritm_7():
    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    N = int(input('Введите N: '))
    R = int(input('Введите R: '))
    B = int(input('Введите B: '))
    N_ = int(input('Введите N_: '))
    
    aR = (a*R)%N
    bR = (b*R)%N
    abR = (a*b*R)%N
    ab = (a*b)%N
    
    
    print(f"aR 'сравнимы' = {aR}(mod{N})")
    print(f"bR 'сравнимы' = {bR}(mod{N})")
    print(f"abR'сравнимы' = {abR}(mod{N})")
    print(f"ab 'сравнимы' = {ab}(mod{N})")


# Алгоритм 8
def algoritm_8():
    
    a = int(input('Введите a: '))
    n = int(input('Введите n (степень): '))
    m = int(input('Введите m (модуль): '))
    
    return (a**n)%m 



def largest_prime_factor(number : int) -> int: 
    i = 2 
    while i * i <= number: 
        if number % i: 
            i += 1 
        else: 
            number //= i 
    return number 


# Алгоритм 9
def algoritm_9() -> None:
    # M = 5
    N = 10
    # print(M, '^2 %', N, '=', (M**2)%N )
    C = 5
    
    p = largest_prime_factor(N)
    q = int( N/p )
    
    print(N , '=', p, '*', q)
        
    m_p1 = int(pow( C,(p+1)/4 ) // p)  # m_p1 - 0 
    m_q1 = int(pow( C,(q+1)/4 ) // q)  # m_q1 - 1
    m_p2 = p - m_p1                    # m_p2 - 2
    m_q2 = q - m_q1                    # m_q2 - 3

    # a = pow(p, -1,  q)
    # b = pow(q, -1,  p)
    
    a = pow(q, -1,  p) * q
    b = pow(p, -1,  q) * p
    
    m_1 = (m_p1 * a + m_q1 * b) % N
    m_2 = (m_p1 * a + m_q2 * b) % N
    m_3 = (m_p2 * a + m_q1 * b) % N
    m_4 = (m_p2 * a + m_q2 * b) % N

    print( m_1, m_2, m_3, m_4)





# print('-'*20, 'Алгоритм 1 Сложение', '-'*20)
# print(algoritm_1())

# print('-'*20, 'Алгоритм 2 Вычетание', '-'*20)
# print(algoritm_2())

# print('-'*20, 'Алгоритм 3 Умножение', '-'*20)
# print(algoritm_3())

# print('-'*20, 'Алгоритм 4 Деление', '-'*20)
# print(algoritm_4())

# print('-'*20, 'Алгоритм 5 Мантгомери', '-'*20)
# print(algoritm_5())

# print('-'*20, 'Алгоритм 6 Умножение N-вычетов', '-'*20)
# print(algoritm_6())

# print('-'*20, 'Алгоритм 7 Произведение чисел', '-'*20)
# algoritm_7()

# print('-'*20, 'Алгоритм 8 Модульное возведение в степень', '-'*20)
# print(algoritm_8())

print('-'*20, 'Алгоритм 9 Извлечение квадратного корня', '-'*20)
algoritm_9()

    
    
    
    