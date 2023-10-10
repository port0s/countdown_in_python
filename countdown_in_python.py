#  import the time module
from time import sleep
  
# define the countdown func.
def countdown(count):
    
    while count:
        # retorna divisão inteira e módulo da divisão
        mins, secs = divmod(count, 60)
        print(f'{mins:02d}:{secs:02d}', end="\r")
        sleep(1)
        count -= 1
      
    print('Fogo na bomba!')
  
  
# input time in seconds
t = input("Números em segundos: ")
  
try:
    time_in_second = int(t)
    countdown(time_in_second)
except ValueError:
    print("Digite um número inteiro positivo.")
except KeyboardInterrupt:
    print("\nTchau tchau, Black Bird")
