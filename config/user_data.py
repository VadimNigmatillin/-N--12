class User:
    def __init__(self, title, username, email, password, birth_year, birth_month, birth_day, 
                 first_name, last_name,
                 company, address, address2, country, state, city, zipcode,
                 phone, sub_email):
        self.title = title
        self.username = username
        self.email = email
        self.password = password
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address = address
        self.address2 = address2 
        self.country = country
        self.state = state
        self.city = city
        self.zipcode = zipcode
        self.phone = phone
        self.sub_email = sub_email
        
'''
На веб-странице значения атрибута value в элементах <option> используются для представления месяцев. 
Например, значение 1 соответствует месяцу 'January', значение 2 соответствует месяцу 'February' и так далее.

birth_month="1" -> "January"
birth_month="2" -> "February"
birth_month="3" -> "March"
birth_month="4" -> "April"
birth_month="5" -> "May"
birth_month="6" -> "June"
birth_month="7" -> "July"
birth_month="8" -> "August"
birth_month="9" -> "September"
birth_month="10" -> "October"
birth_month="11" -> "November"
birth_month="12" -> "December"
'''

'''
Список доступных стран: "India", "United States", "Canada", "Australia", "Israel", "New Zealand", "Singapore"
'''


user1 = User(
    title="Mr.",
    username="Vadim",
    email="example1qwertq@mail.ru",
    password="Vadim",
    birth_year="2002",
    birth_month="4",
    birth_day="22",
    first_name="Vadim",
    last_name="Nigmatullin",
    company="Positive Technologies",
    address="st. Pushkina, house 10",
    address2="",
    country="Canada",
    state="Leningrad region",
    city="Saint-Petersburg",
    zipcode="123456",
    phone="79991234567",
    sub_email="sub_email@mail.ru"
)
