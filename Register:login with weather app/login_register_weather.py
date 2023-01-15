import requests

API_KEY = "ea3a35773ab5cfe4c6d177552190646e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def log_q():
    wanna_log = input("Account created!!\nWould you like to log in? Yes(y) or No(n): ")
    if wanna_log == "y":
        login()
        home_page()
        quit()

    else:
        quit()

def file_creation(name, email, password):

    with open("register", mode='w+') as f:
        f.write("1 = ")
        f.write(name)
        f.write("\n2 = ")
        f.write(email)
        f.write("\n3 = ")
        f.write(password)
        f.close()

def check_number(og_password):
    has_number = False
    for letter in og_password:
        if letter.isdigit():
            has_number = True
    return has_number

def check_upper(og_password):
    has_upper = False
    for letter in og_password:
        if letter.isupper():
            has_upper = True
    return has_upper

def login():
    with open("register", mode='r') as f:
        data_dict = {}
        for line in f:
            k, v = line.strip().split('=')
            data_dict[k.strip()] = v.strip()
        f.close()

    while True:
        l_choice = input("Type in your name or e-mail to continue: ")
        if l_choice == data_dict['1'] or data_dict['2']:
            l_password = input("Type in your password: ")
            if l_password == data_dict['3']:
                print("YOU ARE LOGGED IN !")
                break
            else:
                print("Name or password is incorrect")
                continue

        else:
            continue

def register():

    while True:
        og_password = input("Password: ")
        has_number = check_number(og_password)
        has_upper = check_upper(og_password)
        if not has_number:
            print("No number detected:(")
            continue
        elif not has_upper:
            print("No upper detected:(")
            continue
        elif len(og_password) <= 7:
            print("Password must be at least 8 characters long:(")
            continue
        else:
            conf_password = input("Confirm your chosen password: ")
            if conf_password != og_password:
                print("Not matching with the original input")
                continue
            else:
                return og_password

def home_page():
    home_q = input("What would you like to do?\nIf you'd like to check the weather, please press 'w': ")
    if home_q == "w":
        weather_app()

def main():
    while True:
        first_q = input("If you already have an account, press 'l' to Log In, if not press 'r' to Register: ")
        if first_q == "r":
            r_name = input("Name: ")
            r_email = input("Email: ")
            r_password = register()
            file_creation(r_name, r_email, r_password)
            log_q()

        elif first_q == "l":
            login()
            home_page()
            quit()
        else:
            print("Invalid input")

def weather_app():
    city = input("Enter city name: ")
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = round(data["main"]["temp"] - 273.15, 2)

        print("Weather:", weather)
        print("Temperature:", temperature,"°C")
    else:
        print("An error occured.")


print("Welcome to our page!")


main()
