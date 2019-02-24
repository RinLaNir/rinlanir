import datetime

class employee():

    def __init__(self, surname, name, education):
        self.surname = surname
        self.name = name
        self.start_work = 9.00
        self.education = education
        self.base = 0

class Tester(employee):

    def __init__(self, surname, name, education, years):
        employee.__init__(self, surname, name, education)
        self.base = 2000
        self.years = years

    def calculateSalary(self):
        salary = self.base*(1+self.years/5)
        return salary

    def showinginf(self):
        print("Surname: {}".format(self.surname)+'\n'+"Name: {}".format(self.name)+'\n'+" Time start: {}".format(self.start_work)+'\n'
        +"Education: {}".format(self.education)+'\n'+"Base Salary: {}".format(self.base)+'\n'+"Years of working: {}".format(self.years))

class Engineer(employee):

    def __init__(self, surname, name, education, years, qualification):
        employee.__init__(self, surname, name, education)
        self.base = 3000
        self.years = years
        self.qualification = qualification

    def calculateSalary(self):
        salary = self.qualification*self.base*(1+self.years/10)
        return salary

    def showinginf(self):
        print("Surname: {}".format(self.surname)+'\n'+"Name: {}".format(self.name)+'\n'+"Time start: {}".format(self.start_work)+'\n'
        +"Education: {}".format(self.education)+'\n'+"Base Salary: {}".format(self.base)+'\n'+"Years of working: {}".format(self.years)+'\n'
        "Qualification: {}".format(self.qualification))

class Worker2(employee):

    def __init__(self, surname, name, education, years):
        employee.__init__(self, surname, name, education)
        self.base = 2500
        self.years = years

    def calculateSalary(self):
        salary = self.base*(1+0.1*round(self.years/3))
        return salary

    def showinginf(self):
        print("Surname: {}".format(self.surname)+'\n'+"Name: {}".format(self.name)+'\n'+" Time start: {}".format(self.start_work)+'\n'
        +"Education: {}".format(self.education)+'\n'+"Base Salary: {}".format(self.base)+'\n'+"Years of working: {}".format(self.years))

class Company():

    def __init__(self,worker1,worker2,worker3):
        self.worker1 = worker1
        self.worker2 = worker2
        self.worker3 = worker3

    def hire_workers(self,prog, tester, worker):
        work = input('Кого ви хочете зарахувати? -- ')
        if work == 'програміст':
            surname = input('Призвіще: ')
            name = input("Ім'я: ")
            education = input('Освіта: ')
            years = int(input('Досвід: '))
            qualification = int(input('Кваліфікація: '))
            prog.append(self.worker1(surname, name, education, years, qualification))
        if work == 'тестувальник':
            surname = input('Призвіще: ')
            name = input("Ім'я: ")
            education = input('Освіта: ')
            years = int(input('Досвід: '))
            tester.append(self.worker2(surname, name, education, years))
        if work == 'відділ кадрів':
            surname = input('Призвіще: ')
            name = input("Ім'я: ")
            education = input('Освіта: ')
            years = int(input('Досвід: '))
            tester.append(self.worker3(surname, name, education, years))

    def firing_workers(self,prog,tester,worker):
        work=input('Кого ви хочете звільнити? -- ')
        if work=='програміст':
            surname=input('Призвище:')
            name=input('Імя:')
            names = [i.name for i in prog]
            surnames = [i.surname for i in prog]
            for i in range(len(prog)):
                if name in names:
                    if surname in surnames:
                        del prog[i]
                        break
        if work=='ввіділ кадрів':
            surname=input('Призвище:')
            name=input('Імя:')
            names = [i.name for i in worker]
            surnames = [i.surname for i in worker]
            for i in range(len(worker)):
                if name in names:
                    if surname in surnames:
                        del worker[i]
                        break
        if work=='тестувальник':
            surname=input('Призвище:')
            name=input('Імя:')
            names = [i.name for i in tester]
            surnames = [i.surname for i in tester]
            for i in range(len(tester)):
                if name in names:
                    if surname in surnames:
                        del tester[i]
                        break

    def time(sekf,year, month):
        now = datetime.datetime.now()
        holidays = {datetime.date(year, 8, 14)} # you can add more here
        businessdays = 0
        for i in range(1, 32):
            try:
                thisdate = datetime.date(year, month, i)
            except(ValueError):
                break
            if thisdate.weekday() < 5 and thisdate not in holidays: # Monday == 0, Sunday == 6
                businessdays += 1
        return businessdays

    def show(self,prog,tester,worker):
        print('Програмісти: ')
        for i in range (len(prog)):
            prog[i].showinginf()
        print('\n')
        print('Тестери: ')
        for i in range (len(tester)):
            tester[i].showinginf()
        print('\n')
        print('Відділ кадрів: ')
        for i in range (len(worker)):
            worker[i].showinginf()
        print('\n')

    def all_salary(self,prog,tester,worker,year, month):
        sum=0
        for i in range(len(prog)):
            sum+=prog[i].calculateSalary()*self.time(year, month)
        for i in range(len(worker)):
            sum+=worker[i].calculateSalary()*self.time(year, month)
        for i in range(len(tester)):
            sum+=tester[i].calculateSalary()*self.time(year, month)
        print('Всього видатків: {}'.format(sum))

    def nologi(self,prog,tester,worker,year, month):
        sum=0
        for i in range(len(prog)):
            sum+=prog[i].calculateSalary() *0.2*self.time(year, month)
        for i in range(len(worker)):
            sum+=worker[i].calculateSalary() *0.2*self.time(year, month)
        for i in range(len(tester)):
            sum+=tester[i].calculateSalary()*0.2*self.time(year, month)
        print('Всього податків: {}'.format(sum))

    def zarp(self,prog,tester,worker,year, month):
        sum=0
        for i in range(len(prog)):
            sum = sum + (prog[i].calculateSalary() - prog[i].calculateSalary()*0.2)*self.time(year, month)
        for i in range(len(worker)):
            sum = sum + (worker[i].calculateSalary() - worker[i].calculateSalary()*0.2)*self.time(year, month)
        for i in range(len(tester)):
            sum = sum + (tester[i].calculateSalary() - tester[i].calculateSalary()*0.2)*self.time(year, month)
        print('Всього отримали робітники: {}'.format(sum))
