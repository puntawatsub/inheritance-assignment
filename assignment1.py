class Person:
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self) -> str:
        return f"I am {self.name}, {self.age} years old, {self.gender}"

class Member(Person):
    def __init__(self, name: str, age: int, gender: str, membership_id: str) -> None:
        Person.__init__(Person, name, age, gender)
        self.membership_id = membership_id
    
    def introduce(self) -> str:
        return super().introduce() + f", with membership ID {self.membership_id}"

class Author(Person):
    def __init__(self, name: str, age: int, gender: str, books_written: list[str]) -> None:
        Person.__init__(Person, name, age, gender)
        self.books_written = books_written
    
    def list_books(self) -> str:
        return f"Books written: {', '.join(self.books_written)}"

class AuthorMember(Member, Author):
    def __init__(self, name: str, age: int, gender: str, membership_id: str, books_written: list[str]) -> None:
        Member.__init__(self, name, age, gender, membership_id)
        Author.__init__(self, name, age, gender, books_written)
    
    def introduce(self) -> str:
        return f"I am {self.name}, {self.age} years old, {self.gender}, with membership ID: {self.membership_id}. Books written: {', '.join(self.books_written)}"

# Example usage
authorMember1 = AuthorMember("Amir", 200, 'Male', '12345A', ['How to Python', 'How to Java', 'How to JavaScript', 'How to Rust', "How to C", "How to Teach Your Boss"])
print(authorMember1.introduce())
