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
      print(BColors.HEADER + str(log) + BColors.ENDC)
   def okblue( self, log: object ):
      print(BColors.OKBLUE + str(log) + BColors.ENDC)
   def okcyan( self, log: object ):
      print(BColors.OKCYAN + str(log) + BColors.ENDC)
   def okgreen( self, log: object ):
      print(BColors.OKGREEN + str(log) + BColors.ENDC)
   def warn( self, log: object ):
      print(BColors.WARNING + str(log) + BColors.ENDC)
   def underline( self, log: object ):
      print(BColors.UNDERLINE + str(log) + BColors.ENDC)
   def fail( self, log: object ):
      print(BColors.FAIL + str(log) + BColors.ENDC)
   def bold( self, log: object ):
      print(BColors.BOLD + str(log) + BColors.ENDC)
   def new_work(self, number_at_work: int):
      self.header(f"#### ЗАДАНИЕ {number_at_work} ####")

def input_number() -> int:
    while True:
        x = input("Введите число: ")
        try:
            return int(x)
        except ValueError: 
            print("Вы не ввели корректное число. Попробуйте еще раз.")
      

