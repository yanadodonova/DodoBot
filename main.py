
import math
class DodoBot:
    def __init__(self):
        self.topics = {
            'фізика': self._handle_physics,
            'математика': self._handle_math,
            'філологія': self._handle_philology,
            'географія': self._handle_geography,
            'астрономія': self._handle_astronomy,
            'інше': self._handle_other
        }
        self.G = 9.8

    def start(self):
        while True:
            print('Вітаю, мене звати DodoBot\nВи можете задати мені питання з наступних тем:\nфізика, математика, філологія, географія, астрономія або інше''')
            topic = input().lower()
            if topic in self.topics:
                self.topics[topic]()
            else:
                print('Вибачте, я не розумію цю тему')

#-------ФІЗИКА----------
    def _handle_physics(self):
        while True:
            print('Ось мої функції у фізиці:')
            print('Знайти F, знайти за законом Ома, знайти за законом Бойля-Маріотта чи повернутися назад?')
            sub_topic = input().lower()
            if sub_topic == 'назад':
                break
            elif sub_topic == 'знайти f':
                while True:
                    m1 = float(input('Введіть m1 = '))
                    m2 = float(input('Введите m2 = '))
                    r = float(input('Введіть r = '))
                    result = self._newton(m1, m2, r)
                    print(f'F = {result}')
                    repeat = input(
                        'Чи хочете ви повторити? Так/Ні\n').lower()
                    if repeat == 'ні':
                        break
            elif sub_topic == 'знайти за законом ома':
                while True:
                    sub_sub_topic = input(
                        'Що ви хочете знайти: I, V, R\n').lower()
                    if sub_sub_topic == 'i':
                        v = float(input('Введіть V = '))
                        r = float(input('Введіть R = '))
                        result = self._ohms_law_current(v, r)
                        print(f'I = {result}')
                    elif sub_sub_topic == 'v':
                        i = float(input('Введіть I = '))
                        r = float(input('Введіть R = '))
                        result = self._ohms_law_voltage(i, r)
                        print(f'V = {result}')
                    elif sub_sub_topic == 'r':
                        v = float(input('Введіть V = '))
                        i = float(input('Введіть I = '))
                        result = self._ohms_law_resistance(v, i)
                        print(f'R = {result}')
                    else:
                        print(
                            'Вибачте, я не розумію цей запит')
                        continue
                    repeat = input(
                        'Чи хочете ви повторити? Так/Ні\n').lower()
                    if repeat == 'ні':
                        break
            elif sub_topic == 'знайти за законом бойля-маріотта':
                while True:
                    sub_sub_topic = input(
                        'Що ви хочете знайти: P1, V1\n').lower()
                    if sub_sub_topic == 'p1':
                        V1 = float(input('Введіть V1 = '))
                        P2 = float(input('Введіть P2 = '))
                        V2 = float(input('Введіть V2 = '))
                        result = self._boyles_law_p1(V1, P2, V2)
                        print(f'P1 = {result}')
                    elif sub_sub_topic == 'v1':
                        P1 = float(input('Введіть P1 = '))
                        V2 = float(input('Введіть V2 = '))
                        P2 = float(input('Введіть P2 = '))
                        result = self._boyles_law_v1(P1, V2, P2)
                        print(f'V1 = {result}')
                    else:
                        print(
                            'Вибачте, я не розумію цей запит')
                        continue
                    repeat = input(
                        'Чи хочете ви повторити? Так/Ні\n').lower()
                    if repeat == 'ні':
                        break
            else:
                print('Вибачте, я не розумію цю тему')
                continue


#-------МАТЕМАТИКА------
    def _handle_math(self):
        while True:
            print('Ось мої функції у математиці:')
            print('''Формула векторного добутку векторів, формула скалярного добутку векторів,\nплоща кола, площа трапеції, або назад''')
            sub_topic = input().lower()
            if sub_topic == 'назад':
                break
            elif sub_topic == 'формула векторного добутку векторів':
                while True:
                    A = input('Введіть перший вектор у форматі x, y, z = ')
                    A = tuple(map(float, A.split(', ')))
                    B = input('Введіть другий вектор у форматі x, y, z = ')
                    B = tuple(map(float, B.split(', ')))
                    result = self._cross_product(A, B)
                    print(f'Векторний добуток = {result}')
                    repeat = input(
                        'Чи хочете ви повторити? Так/Ні\n').lower()
                    if repeat == 'ні':
                        break
            elif sub_topic == 'формула скалярного добутку векторів':
                while True:
                    A = input('Введіть перший вектор у форматі x, y, z = ')
                    A = tuple(map(float, A.split(', ')))
                    B = input('Введіть другий вектор у форматі x, y, z = ')
                    B = tuple(map(float, B.split(', ')))
                    result = self._dot_product(A, B)
                    print(f'Скалярний добуток = {result}')
                    repeat = input(
                        'Чи хочете ви повторити? Так/Ні\n').lower()
                    if repeat == 'ні':
                        break
            elif sub_topic == 'площа кола':
                while True:
                    radius = float(input('Введіть радіус кола = '))
                    result = self._area_of_circle(radius)
                    print(f'Площа кола = {result}')
                    repeat = input(
                        'Чи хочете ви повторити? Так/Ні\n').lower()
                    if repeat == 'ні':
                        break
            elif sub_topic == 'площа трапеції':
                while True:
                    a = float(input('Введіть а трапеції = '))
                    b = float(input('Введіть b трапеції = '))
                    h = float(input('Введіть висоту трапеції = '))
                    result = self._area_of_trapezoid(a, b, h)
                    print(f'Площа трапеції = {result}')
                    repeat = input(
                        'Чи хочете ви повторити? Так/Ні\n').lower()
                    if repeat == 'ні':
                        break
            else:
                print('Вибачте, я не розумію цю тему')
                continue

    

    def _handle_geography(self):
        while True:
            print('Ось мої функції у географии:')
            print('''найбільше озеро в світі за площею, 5 найвищих гір в світі, держави, які мають найбільшу кількість водосховищ в світі, або назад''')
            sub_topic = input().lower()
            if sub_topic == 'назад':
                break
            elif sub_topic == 'найбільше озеро в світі за площею':
                print('--------\nКаспійське море або Каспій\n--------')
            elif sub_topic == '5 найвищих гір в світі':
                print('----------\n1. Еверест 8848 м\n2. Чогорі 8614 м\n3. Канченджанга 8586 м\n4. Лхоцзе 8516 м\n5. Макалу 8485 м\n-------')
            elif sub_topic == 'держави, які мають найбільшу кількість водосховищ в світі':
                print('--------\nСаудівська Аравія\n--------')
            elif sub_topic == 'держави, які мають найбільшу кількість водосховищ в світі':
                print('США та Китай')
                    



    def _handle_philology(self):
        print('Функції у філологія: TBD')
        
    def _handle_astronomy(self):
        print('Функції у астрономії: TBD')

    def _handle_other(self):
        print('Функції у інше: TBD')

#---------ФУНКЦІЇ ФІЗИКИ--------
    def _newton(self, m1, m2, r):
        F = self.G * (m1 * m2) / r**2
        return F

    def _ohms_law_voltage(self, I, R):
        V = I * R
        return V

    def _ohms_law_current(self, V, R):
        I = V / R
        return I

    def _ohms_law_resistance(self, V, I):
        R = V / I
        return R

    def _boyles_law_p1(self, V1, P2, V2):
        P1 = P2 * V2 / V1
        return P1

    def _boyles_law_v1(self, P1, V2, P2):
        V1 = V2 * P2 / P1
        return V1
#------ФУНКЦІЇ МАТЕМАТИКИ------- 
    def _cross_product(self, A, B):
        Ax, Ay, Az = A
        Bx, By, Bz = B
        return (Ay*Bz - Az*By, Az*Bx - Ax*Bz, Ax*By - Ay*Bx)

    def _dot_product(self, A, B):
    
        # Обчислити величини векторів
        mag_A = math.sqrt(sum([n**2 for n in A]))
        mag_B = math.sqrt(sum([n**2 for n in B]))

        # Обчислити косинус кута між векторами
        cos_theta = sum([A[i] * B[i] for i in range(3)]) / (mag_A * mag_B)

        # Обчислити точковий добуток
        dot_product = mag_A * mag_B * cos_theta

        return dot_product
    
    
    def _area_of_circle(self, radius):
        
        return math.pi * radius ** 2
    

    def _area_of_trapezoid(self, a, b, h):
    
        return 0.5 * (a + b) * h
#----------------------------

if __name__ == '__main__':
    bot = DodoBot()
    bot.start()