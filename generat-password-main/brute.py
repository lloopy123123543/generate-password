from Password import Password

from next_array import next_array


password = Password()

count_symbols = input("Введите количество символов в пароле: ")
pin_code = input("Введите PIN CODE для шифрования пароля (4 цифры): ")

if not pin_code.isdigit():
    pin_code = None

if count_symbols.isdigit():
    password.generation(int(count_symbols), pin_code)
else:
    password.generation(None, None)


print (password.password)
print(password.check_summa)

password_array = [0 for i in range(0, password.count_symbols)]

password_array = next_array(password_array, len(password.ARRAY_SYMBOLS))
print(password_array)

password_string = ''
for i in password_array:
    password_string += password.get_symbols(i)

print (password_string)

check_summa = hashlib.sha512(f'{password}{self.pin_code}'.encode()).hexdigest()
print(check_summa)
count_variant = ''
import time
import os
    start_time = time.time()
    count_variant = 0

    while True:
        count_variant += 1

        password = Password()
        password.generation(int(count_symbols), pin_code)

        typer.echo(f'Проверяем пароль: {password.password}')

        if check_summa == password.check_summa:
            typer.echo(f'Совпадение: {password.password}')
            typer.echo(f'Количество пройденных вариантов: {count_random}')
            typer.echo(f'Время перебора составило: {time.time() - start_time}')
            break
