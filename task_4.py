class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
       email =  f"{name}@email.com"
       return cls(name, hours, rest_days, email)

        
    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment 
        
    def salary(self):
        return self.hours * EmployeeSalary.hourly_payment

    
    
    #  Проверка (прошу Вас, Алексадр Орехов, не ругайтесь за мои комментарии и мои проверки, я еще учусь, будьте снисходительнее что ли):
emp1 = EmployeeSalary.get_hours("Иван", 2, "ivan@email.com")  # rest_days=2
print(emp1.salary())  # 16000

emp2 = EmployeeSalary.get_email("Мария", 40, 1)
print(emp2.salary())  # 16000
print(emp2.email)     # Мария@email.com

EmployeeSalary.set_hourly_payment(500)
print(emp1.salary())  # 20000