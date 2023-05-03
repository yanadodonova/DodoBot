class DodoBot:
    def __init__(self):
        self.topics = {
            'фізика': self._handle_physics,
            'математика': self._handle_math,
            'філологія': self._handle_philology,
            'географія': self._handle_geography,
            'астрономія': self._handle_astronomy
        }
        self.G = 9.8

    def start(self):
        while True:
            print('''Вітаю, мене звати DodoBot 
            Ви можете задати мені питання з наступних тем: 
            фізика, математика, філологія, географія, астрономія''')
            topic = input().lower()
            if topic in self.topics:
                self.topics[topic]()
            else:
                print('Вибачте, я не розумію цю тему')

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

    def _handle_math(self):
        print('Функції у математиці: TBD')

    def _handle_philology(self):
        print('Функції у філології: TBD')

    def _handle_geography(self):
        print('Функції у географії: TBD')

    def _handle_astronomy(self):
        print('Функції у астрономії: TBD')

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


if __name__ == '__main__':
    bot = DodoBot()
    bot.start()
