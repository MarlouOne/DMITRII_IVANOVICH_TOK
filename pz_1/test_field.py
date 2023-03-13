from math import gcd, lcm
# lcm - НОК
# При a>b => НОД(a;b) = НОД(a-b;b)
# gcd - НОД(60;48) -> 12
# gcd - НОД(61;48) -> 1
# print( gcd( number, mod) )
# print( lcm( number, mod) )


def get_comparable(number : int, mod : int) -> int: # Находим наименьшие сравнимое число
    base = number
    while( base >= mod ):
        base = base - base // mod * mod # base % mod
        
    # print( base - base // mod * mod,  base - mod )
    
    if base - base // mod * mod >= abs( base - mod ):
        return base - mod
    else:
        return base - base // mod * mod # base % mod

def get_min_degree(base : int, mod : int) -> int: # Находим наименьшие степень с наименьшим остатком
    base = abs( base )
    min_value = mod
    min_degree = -1
    for degree in range(1, 10):
        remains = abs( int( get_comparable( pow(base, degree), mod) ) )
        
        if remains < min_value: # pow(base, degree) // mod * mod
            min_value, min_degree = remains, degree
            # min_degree = degree
            
        print( min_value, min_degree, ' - ', remains, degree)
        
    return min_degree
            
        
    print( base, mod)
    print( gcd( base, mod) )
    print( lcm( base, mod) )

def algoritm_9_misha(number : int,  degree : int, mod : int) -> None:   
    # M = int(input('Введите M: ')) # Число
    # n = int(input('Введите n (степень): ')) # Степень
    # А запись N = M (mod k) означает, что числа N и M дают при делении на k равные остатки.
    # n = p * q
    print( f'Input values : {number} - number, { degree} -  degree and {mod} - module')
    
    comparable = get_comparable(number, mod)
    min_degree = get_min_degree(comparable, mod)


def largest_prime_factor(number : int) -> int: 
    i = 2 
    while i * i <= number: 
        if number % i: 
            i += 1 
        else: 
            number //= i 
    return number 



def algoritm_9() -> None:
    M = 5
    N = 10
    print(M, '^2 %', N, '=', (M**2)%N )
    C = (M**2)%N
    
    p = largest_prime_factor(N)
    q = int( N/p )
    
    
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


def main():
    
    print('-'*20, 'Алгоритм 9 Извлечение квадратного корня', '-'*20)
    # algoritm_9_misha(521, 637, 17)
    algoritm_9()
    
main()