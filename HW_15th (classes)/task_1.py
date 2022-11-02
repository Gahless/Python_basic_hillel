
class Human:

    def __init__(self, surname: str, name: str, age: int, phone: str, address: str):
        self.surname = surname
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        return {
            'surname': self.surname,
            'name': self.name,
            'age': self.age,
            'phone': self.phone,
            'address': self.address
        }

    def call(self, phone_number):
        print(self.phone, 'вызывает абонента', phone_number)


spongesob_s = Human('Squarepants', 'SpongeBob', 26, '707-663-4279', '124 Conch St., Bikini Bottom')
james_n = Human('Neves', 'James', 27, '757-581-3169', '3466 Daffodil Lane')
sarah_b = Human('Burns', 'Sarah', 22, '360-551-7044', '1658 Chardonnay Drive')

print(spongesob_s.get_info())
print(james_n.get_info())
print(sarah_b.get_info())
