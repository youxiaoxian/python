from faker import Faker


class ContactInfo:
    def __init__(self):
        self.faker = Faker('zh-CN')

    def get_name(self):
        name = self.faker.name()
        return name

    def get_num(self):
        phonenum = self.faker.phone_number()
        return phonenum
