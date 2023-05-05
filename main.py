from random import choice
from datetime import date, datetime
from math import pi, sqrt
class DodoBot:
    def __init__(self):
        self.topics = {
            'фізика': self._handle_physics,
            'математика': self._handle_math,
            'філологія': self._handle_philology,
            'географія': self._handle_geography,
            'астрономія': self._handle_astronomy,
            'інше': self._handle_other,
            'help': self._handle_help
        }
        self.G = 9.8

    def start(self):
        while True:
            print('\033[1;32mВітаю, мене звати DodoBot\nВи можете задати мені питання з наступних тем:\nфізика, математика, філологія, географія, астрономія, інше\nабо help\nабо вийти щоб закрити програму\033[0m')
            topic = input().lower()
            if topic == 'вийти':
                print('\033[1;32mДо побачення!\033[0m')
                return
            elif topic in self.topics:
                self.topics[topic]()
            else:
                print('\033[1;32mВибачте, я не розумію цю тему\033[0m')

#------ХЕЛП МИ--------
    def _handle_help(self):
            while True:
                print('\033[34mПісля запуску програми ви побачите наступне повідомлення:\nВітаю, мене звати DodoBo\nВи можете задати мені питання з наступних тем\nфізика, математика, філологія, географія, астрономія або інш\nВведіть тему, про яку ви хочете дізнатися більше, наприклад "фізика".\nПісля цього програма запропонує вам вибрати одну з наступних під\nОсь мої функції у фізиці\nЗнайти F, знайти за законом Ома, знайти за законом Бойля-Маріотта чи повернутися назад\nВведіть підтему, наприклад "Знайти F", і слідуйте інструкціям на екрані.\nПісля виконання запиту програма запропонує повторити операцію або повернутися на попередній рівень меню.\033[0m')
                break


#-------ФІЗИКА----------
    def _handle_physics(self):
        while True:
            print('\033[1;32mОсь мої функції у фізиці:\nЗнайти F,\nзнайти за законом Ома,\nзнайти за законом Бойля-Маріотта\nчи повернутися назад?\033[0m')
            sub_topic = input().lower()
            if sub_topic == 'назад':
                break
            elif sub_topic == 'знайти f':
                while True:
                    m1 = float(input('Введіть m1 = '))
                    m2 = float(input('Введите m2 = '))
                    r = float(input('Введіть r = '))
                    result = self._newton(m1, m2, r)
                    print('\033[1;32mF = {}\033[0m'.format(result))
                    repeat = input(
                        'Чи хочете ви повторити? Так/Ні\n ').lower()
                    if repeat == 'ні':
                        break
            elif sub_topic == 'знайти за законом ома':
                while True:
                    sub_sub_topic = input(
                        'Що ви хочете знайти: I, V, R ').lower()
                    if sub_sub_topic == 'i':
                        v = float(input('Введіть V = '))
                        r = float(input('Введіть R = '))
                        result = self._ohms_law_current(v, r)
                        print('\033[1;32mI = {}\033[0m'.format(result))
                    elif sub_sub_topic == 'v':
                        i = float(input('Введіть I = '))
                        r = float(input('Введіть R = '))
                        result = self._ohms_law_voltage(i, r)
                        print('\033[1;32mV = {}\033[0m'.format(result))
                    elif sub_sub_topic == 'r':
                        v = float(input('Введіть V = '))
                        i = float(input('Введіть I = '))
                        result = self._ohms_law_resistance(v, i)
                        print('\033[1;32mR = {}\033[0m'.format(result))
                    else:
                        print(
                            '\033[1;32mВибачте, я не розумію цей запит\033[0m')
                        continue
                    repeat = input(
                        'Чи хочете ви повторити? Так/Ні\n ').lower()
                    if repeat == 'ні':
                        break
            elif sub_topic == 'знайти за законом бойля-маріотта':
                while True:
                    sub_sub_topic = input(
                        'Що ви хочете знайти: P1, V1\n ').lower()
                    if sub_sub_topic == 'p1':
                        V1 = float(input('Введіть V1 = '))
                        P2 = float(input('Введіть P2 = '))
                        V2 = float(input('Введіть V2 = '))
                        result = self._boyles_law_p1(V1, P2, V2)
                        print('\033[1;32mP1 = {}\033[0m'.format(result))
                    elif sub_sub_topic == 'v1':
                        P1 = float(input('Введіть P1 = '))
                        V2 = float(input('Введіть V2 = '))
                        P2 = float(input('Введіть P2 = '))
                        result = self._boyles_law_v1(P1, V2, P2)
                        print('\033[1;32mV1 = {}\033[0m'.format(result))
                    else:
                        print(
                            '\033[1;32mВибачте, я не розумію цей запит\033[0m')
                        continue
                    repeat = input(
                        'Чи хочете ви повторити? Так/Ні\n').lower()
                    if repeat == 'ні':
                        break
            else:
                print('\033[1;32mВибачте, я не розумію цю тему\033[0m')
                continue


#-------МАТЕМАТИКА------
    def _handle_math(self):
        while True:
            print('\033[1;32mОсь мої функції у математиці:\033[0m')
            print('\033[1;32mФормула векторного добутку векторів,\nформула скалярного добутку векторів,\nплоща кола, площа трапеції,\nабо назад\033[0m')
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
                    print(f'\033[1;32mВекторний добуток = {result}\033[0m')
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
                    print(f'\033[1;32mСкалярний добуток = {result}\033[0m')
                    repeat = input(
                        'Чи хочете ви повторити? Так/Ні\n').lower()
                    if repeat == 'ні':
                        break
            elif sub_topic == 'площа кола':
                while True:
                    radius = float(input('Введіть радіус кола = '))
                    result = self._area_of_circle(radius)
                    print(f'\033[1;32mПлоща кола = {result}\033[0m')
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
                    print(f'\033[1;32mПлоща трапеції = {result}\033[0m')
                    repeat = input(
                        'Чи хочете ви повторити? Так/Ні\n').lower()
                    if repeat == 'ні':
                        break
            else:
                print('\033[1;32mВибачте, я не розумію цю тему\033[0m')
                continue

    
#--------ГЕОГРАФИЯ-------------
    def _handle_geography(self):
        while True:
            print('\033[1;32mОсь мої функції у географії:\033[0m')
            print('\033[1;32mнайбільше озеро в світі за площею,\n5 найвищих гір в світі,\nдержави, які мають найбільшу кількість водосховищ в світі,\nкраїна, в якій знаходиться найбільша пустеля після Сахари.\nабо назад\033[0m')
            sub_topic = input().lower()
            if sub_topic == 'назад':
                break
            elif sub_topic == 'найбільше озеро в світі за площею':
                print('\033[1;32m--------\nКаспійське море або Каспій\n--------\033[0m')
            elif sub_topic == '5 найвищих гір в світі':
                print('\033[1;32m----------\n1. Еверест 8848 м\n2. Чогорі 8614 м\n3. Канченджанга 8586 м\n4. Лхоцзе 8516 м\n5. Макалу 8485 м\n-------\033[0m')
            elif sub_topic == 'країна, в якій знаходиться найбільша пустеля після сахари':
                print('\033[1;32m--------\nСаудівська Аравія\n--------\033[0m')
            elif sub_topic == 'держави, які мають найбільшу кількість водосховищ в світі':
                print('\033[1;32mСША та Китай\033[0m')
            else:
                print('\033[1;32mВибачте, я не розумію цю тему\033[0m')
                continue


#---------ФІЛОЛОГІЯ--------------
    def _handle_philology(self):
        while True:
            print('\033[1;32mОсь мої функції у філології:\033[0m')
            print('\033[1;32mЯка різниця між Some та Any\nЯк утворити PassiveVoice в PresentSimple,\nабо назад\033[0m')
            sub_topic = input().lower()
            if sub_topic == 'назад':
                break
            elif sub_topic == 'яка різниця між some та any':
                print('\033[1;32m--------\n"Some" використовується, коли ми говоримо про кількість предметів, що існують, і ми зафіксовані на позитивному аспекті.\n"Any" використовується, коли ми говоримо про кількість предметів, яку ми не знаємо, і ми зафіксовані на негативному аспекті.\n--------\033[0m')
            elif sub_topic == 'як утворити passivevoice в presentsimple':
                print('\033[1;32m----------\nПредмет/людина + am/are/is + 3-тя форма неправильного дієслова або правильний дієслово з закінченням -ed.\n-------\033[0m')
            else:
                print('\033[1;32mВибачте, я не розумію цю тему\033[0m')
                continue
        
#-------АСТРОНОМИЯ----------
    def _handle_astronomy(self):
        while True:
            print('\033[1;32mОсь мої функції у астрономії:\033[0m')
            print('\033[1;32mЯкі планети нашої Сонячної системи є газовими гігантами\nЩо таке космічне випромінювання\nЯкі процеси відбуваються на Сонці та як вони впливають на Землю\nЩо таке чорні діри та як вони виникають\nабо назад\033[0m')
            sub_topic = input().lower()
            if sub_topic == 'назад':
                break
            elif sub_topic == 'які планети нашої сонячної системи є газовими гігантами':
                print('\033[1;32m--------\nЮпітер, Сатурн, Уран та Нептун\n--------\033[0m')
            elif sub_topic == 'що таке космічне випромінювання':
                print('\033[1;32m----------\nКосмічне випромінювання - це потік сильно енергетичних частинок і фотонів, що походять від різних джерел у космосі, таких як сонце, зірки, блазари, галактики та інші космічні об`єкти. Він може бути дуже шкідливим для живих організмів, що можуть перебувати в космосі, включаючи космонавтів, тому що він може викликати радіаційну хворобу та інші прояви радіаційного впливу. Крім того, космічне випромінювання може впливати на електроніку та іншу техніку, що знаходиться в космосі, що може призвести до її збоїв або відмови.\n-------\033[0m')
            elif sub_topic == 'які процеси відбуваються на сонці та як вони впливають на землю':
                print('\033[1;32m--------\nСонце є джерелом енергії для Землі і нашої планети залежить від різних процесів, що відбуваються на ньому. Наприклад, на Сонці відбуваються ядерні реакції, які створюють енергію, що потім передається у формі світла та тепла на Землю.\n\nТакож на Сонці відбуваються корональні викиди та сонячні бурі, що можуть впливати на електромагнітне поле Землі і можуть викликати різні ефекти, такі як підрив електричних мереж, перешкоди в роботі супутників та інші проблеми.\n\nКрім того, Земля також отримує вплив вітру сонячної системи, який складається з плазми, що виходить з Сонця. Цей вітер може створювати різні геомагнітні явища на Землі, такі як Полярні сяйва та інші види сяйв.\n--------\033[0m')
            elif sub_topic == 'що таке чорні діри та як вони виникають':
                print('\033[1;32m-----------\nЧорна діра - це область простору, де гравітаційне поле настільки сильне, що навіть світло не може виходити з неї. Чорні діри виникають в результаті зіткнення гігантських зір або колапсу зір після того, як вони вичерпають свої запаси палива і перестають випромінювати енергію світла. Гравітаційне поле у таких зір набуває фантастичної сили, що притягує до центру зір маси ядра зірки, стискаючи його до крайніх меж. Якщо ця маса перевищує критичний поріг, створюється область, в якій гравітація настільки сильна, що навіть світло не може вибратися з цієї області. Таким чином утворюється чорна діра.\n--------------\033[0m')
            else:
                print('\033[1;31mВибачте, я не розумію цю тему\033[0m')
                continue

#-------ДРУГЕ---------
    def _handle_other(self):
        while True:
            print('\033[1;32mОсь мої функції в темі "Інше":\033[0m')
            print('''\033[1;32mЯкий зараз місяць\nЯк тебе звати\nРозповісти анекдот,\nгра історія,\nскільки днів до літа\nяка тварина цього року\nякий колір цього року\nвизначити ваш знак зодіаку\nабо назад\033[0m''')
            sub_topic = input().lower()
            if sub_topic == 'назад':
                break
            elif sub_topic == 'який зараз місяць':
                print(f'\033[1;32m------------\nЗараз {self.current_month_ukr()}\n----------\033[0m')
            elif sub_topic == 'як тебе звати':
                print('\033[1;32m-----------------\nМене звуть DodoBot! Я допомагаю в різних уроках\n-------------------\033[0m')
            elif sub_topic == 'розповісти анекдот':
                joke = self.get_joke()
                print(f'\033[1;32m---------------\n{joke}\n----------------\033[0m')
            elif sub_topic == 'гра історія':
                while True:
                    self.history_game()
                    repeat = input(
                        'Чи хочете ви повторити? Так/Ні\n').lower()
                    if repeat == 'ні':
                        break
            elif sub_topic == 'скільки днів до літа':
                result = self.plural_days(self.summer())
                print(f'\033[1;32m-----------\n{result} до літа\n----------\033[0m')
            elif sub_topic == 'яка тварина цього року':
                yeara = int(input('Введіть поточний рік: '))
                result = self.animal_of_the_year(yeara)
                print(f'\033[1;32m-----------\n{result}\n----------\033[0m')
            elif sub_topic == 'який колір цього року':
                yearb = int(input('Введіть поточний рік: '))
                result = self.color_of_the_year(yearb)
                print(f'\033[1;32m-----------\n{result}\n----------\033[0m')
            elif sub_topic == 'визначити ваш знак зодіаку':
                day = int(input('Введіть день коли ви народилися: '))
                month = int(input('Введіть місяць, коли ви народилися: '))
                result = self.zodiac_sign(day, month)
                print(f'\033[1;32m-----------\n{result}\n----------\033[0m')
            else: 
                print('\033[1;32mВибачте, я не розумію цю тему\033[0m')
                continue

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
        mag_A = sqrt(sum([n**2 for n in A]))
        mag_B = sqrt(sum([n**2 for n in B]))

        # Обчислити косинус кута між векторами
        cos_theta = sum([A[i] * B[i] for i in range(3)]) / (mag_A * mag_B)

        # Обчислити точковий добуток
        dot_product = mag_A * mag_B * cos_theta

        return dot_product
    
    
    def _area_of_circle(self, radius):
        
        return pi * radius ** 2
    

    def _area_of_trapezoid(self, a, b, h):
    
        return 0.5 * (a + b) * h
#---------ФУНКЦІЯ ІНШЕ---------
    def current_month_ukr(self):
        now = datetime.now()
        ukr_month_names = [
            "січень", "лютий", "березень", "квітень",
            "травень", "червень", "липень", "серпень",
            "вересень", "жовтень", "листопад", "грудень"
        ]
        month_num = now.month - 1
        return ukr_month_names[month_num]

    def get_joke(self):
        jokes = [
            'Штірліц довго дивився на одну крапку. Потім перевів погляд на іншу крапку. “Двокрапка” — здогадався Штірліц.',
            'лист із центра до Штірліца не дійшов. Він перечитав його ще раз — однаково не дійшов.',
            'Штірліц сидів дома. З вікна дуло. Штірліц натиснув Alt+F4 — вікно зникло.',
            'Штірліц читав книгу біля вікна, з вікна дуло. Штірліц закрив вікно — дуло пропало.',
            'Штірліц всю ніч топив камін.  На ранок камін потонув.'
        ]
        return choice(jokes)

    def color_of_the_year(self, year_new):
        color = {0: 'Белый (Металл)', 1: 'Белый (Металл)', 2: 'Черный (Вода)', 3: 'Черный (Вода)', 4: 'Голубой (Дерево)',
                5: 'Голубой (Дерево)', 6: 'Красный (Огонь)', 7: 'Красный (Огонь)', 8: 'Желтый (Земля)', 9: 'Желтый (Земля)'}
        k = year_new % 10
        return color[k]

    def history_game(self):
        templates = [
            "У {1} в {2} році {0} {3} {4}.",
            "{0} {3} {4} у {1} у {2} році.",
            "{0} зробив {4} у {2} році у {1}, щоб {3}.",
            "{0} {3} {4} в {1} у місці під назвою {2}.",
            "{0} {3} {4} у {1} тому часі, коли {2} було важливим місцем."
        ]

        prompts = ["Хто?", "Де?", "Коли?", "Навіщо?", "Що?"]
        answers = []

        for prompt in prompts:
            answer = input(prompt + " ")
            answers.append(answer)

        template = choice(templates)
        text = template.format(*answers)
        print(text)

    def plural_days(self, n):  # выбирает окончание слова
        days = ['день', 'дня', 'днів']

        if n % 10 == 1 and n % 100 != 11:
            p = 0
        elif 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20):
            p = 1
        else:
            p = 2

        return str(n) + ' ' + days[p]

    def summer(self):  # визначає скільки днів до літа
        now = date.today()
        reachday = date(2023, 6, 1)
        result = (reachday - now).days  # ЗАЛИШАЄ ТІЛЬКИ ДНІ!!!
        
        return result


    def animal_of_the_year(self, year_new):
        year = ['Щур', 'Буйвол', 'Тигр',
                'Кролик (Кіт)', 'Дракон', 'Змія', 'Кінь', 'Вівця', 'Мавпа', 'Півень', 'Собака', 'Свиня']
        k = year_new % 10
        yk = abs((year_new - 2020) % 12)
        return year[yk]

    def zodiac_sign(self, day, month):
        # Визначаємо знак зодіаку за датою народження
        if month == 12:
            sign = 'Стрілець' if (day < 22) else 'Козеріг'
        elif month == 1:
            sign = 'Козеріг' if (day < 20) else 'Водолій'
        elif month == 2:
            sign = 'Водолій' if (day < 19) else 'Риби'
        elif month == 3:
            sign = 'Риби' if (day < 21) else 'Овен'
        elif month == 4:
            sign = 'Овен' if (day < 20) else 'Телець'
        elif month == 5:
            sign = 'Телець' if (day < 21) else 'Близнюки'
        elif month == 6:
            sign = 'Близнюки' if (day < 21) else 'Рак'
        elif month == 7:
            sign = 'Рак' if (day < 23) else 'Лев'
        elif month == 8:
            sign = 'Лев' if (day < 23) else 'Діва'
        elif month == 9:
            sign = 'Діва' if (day < 23) else 'Терези'
        elif month == 10:
            sign = 'Терези' if (day < 23) else 'Скорпіон'
        elif month == 11:
            sign = 'Скорпіон' if (day < 22) else 'Стрілець'

        return sign
#----------------------------

if __name__ == '__main__':
    bot = DodoBot()
    bot.start()