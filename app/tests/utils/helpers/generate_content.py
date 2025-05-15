from faker import Faker

faker = Faker()


def generate_factory_content(min_length=300, max_length=1000):
    content = ""
    while len(content) < min_length:
        content += " " + faker.paragraph()
    return content[:max_length]
