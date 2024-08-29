import random

print("Press Enter key to generate IPs (Ctrl+C to exit).")

def generate_random_ip():
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

while True:
    input() 
    print(generate_random_ip())