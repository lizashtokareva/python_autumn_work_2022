# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами
#  A и B (коэффициент A не равен 0).
A = int(input())
B = int(input())
def main(A, B):
    x = -B/A
    return x

print(main(A, B))
