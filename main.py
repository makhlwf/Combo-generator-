import random
import sys
import string
import os
from tqdm import tqdm

def generate_proxy():
    # Generate four random numbers for the IP address parts
    ip_parts = [str(random.randint(0, 255)) for _ in range(4)]
    # Generate a random port number with higher probability for 443, 80, 7575, 8080, and 4545
    port = random.choice([443, 80, 7575, 8080, 4545] + [random.randint(1, 65535)] * 5)

    # Combine the parts into the desired format
    proxy = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.{ip_parts[3]}:{port}"

    return proxy

def generate_and_save_proxies(filename, num_proxies):
    generated_proxies = set()  # To store unique proxies
    with open(filename, 'w') as file:
        for i in range(1, num_proxies + 1):
            proxy = generate_proxy()
            while proxy in generated_proxies:
                proxy = generate_proxy()
            generated_proxies.add(proxy)
            sys.stdout.write(f"\rGenerated {i} of {num_proxies} proxies: {proxy}")
            sys.stdout.flush()
            file.write(proxy + '\n')
        print("\nProxy generation complete.")

def generate_email_password(num_pairs, password_length):
    email_password_pairs = set()
    for _ in range(num_pairs):
        email = f"{''.join(random.choice(string.ascii_lowercase) for _ in range(10))}@gmail.com"
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(password_length))
        email_password_pairs.add(f"{email}:{password}")
    return email_password_pairs

def main():
    print("Welcome to the Combined Generator Tool by MAKHLWF")
    print("Copyright © 2023. All rights reserved.")
    print("Author: @makhlwf on Telegram - https://t.me/makhlwf")
    print("Important Instructions:")
    print("This script is compatible with systems supporting Python.")
    
    while True:
        print("\nOptions:")
        print("1. Proxy Generator")
        print("2. Email and Password Generator")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            filename = input("Enter the filename with txt or db or json, etc.: ")
            num_proxies = int(input("Enter the number of proxies to generate: "))
            generate_and_save_proxies(filename, num_proxies)
        elif choice == '2':
            num_pairs = int(input("Enter the number of email/password pairs to generate: "))
            password_length = int(input("Enter the desired password length: "))
            filename = input("Enter the name of the file to save the pairs (extension .txt will be automatically added): ")
            filename += ".txt"
            if os.path.exists(filename):
                response = input("The file already exists. Do you want to overwrite it? (yes/no): ")
                if response.lower() != 'yes':
                    print("Aborted. The existing file was not overwritten.")
                    continue
            pairs = generate_email_password(num_pairs, password_length)
            with open(filename, 'w') as file:
                with tqdm(total=num_pairs) as pbar:
                    for pair in pairs:
                        file.write(pair + '\n')
                        pbar.update(1)
            print(f"{num_pairs} email/password pairs with {password_length}-character strong passwords generated and saved to {filename}.")
        elif choice == '3':
            print("Exiting the Combined Generator Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

if __name__ == "__main__":
    main()
