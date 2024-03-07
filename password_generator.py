import random
import string

class Password_generator:
    def get_user_length(self):
        len=int(input("Enter length of password:"))
        return len
    def generate_random_password(self):
        len=self.get_user_length()
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        return password
##    def print_password(self):
##        pass=self.generate_random_password()
    
        

# Example usage:
#password_length = 12  # Specify the desired length of the password
generator = Password_generator
password = generator.generate_random_password(12)
print("Generated Password:", password)
print("Generated Password:", password)


