from faker import Faker

# Crea un'istanza di Faker
fake = Faker("it_IT")

# Genera una password con il metodo password()
fgf = fake.name()

print(fgf)
