class BColors:
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKCYAN = '\033[96m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
   ENDC = '\033[0m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'

class Console:
   def header( self, log: object ):
      print(BColors.HEADER + log + BColors.ENDC)
   def okblue( log: object):
      print(BColors.OKBLUE + log + BColors.ENDC)
   def okcyan( log: object):
      print(BColors.OKCYAN + log + BColors.ENDC)
   def okgreen( log: object):
      print(BColors.OKGREEN + log + BColors.ENDC)
   def warn( log: object):
      print(BColors.WARNING + log + BColors.ENDC)
   def underline( log: object):
      print(BColors.UNDERLINE + log + BColors.ENDC)
   def fail( log: object):
      print(BColors.FAIL + log + BColors.ENDC)
   def bold( log: object):
      print(BColors.BOLD + log + BColors.ENDC)
   def new_work(self, number_at_work: int):
      self.header(f"#### ЗАДАНИЕ {number_at_work} ####")

def input_number() -> int:
    while True:
        x = input("Введите число: ")
        try:
            return int(x)
        except ValueError: 
            print("Вы не ввели корректное число. Попробуйте еще раз.")
      

