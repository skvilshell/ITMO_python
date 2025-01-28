class Room:
   def __init__(self, number, room_type, max_people, price_per_night):
      self.number = number
      self.room_type = room_type
      self.max_people = max_people
      self.price_per_night = price_per_night
      self.is_available = True

# Бронирование с проверкой
   def book(self):
      if self.is_available:
         self.is_available = False
         print(f"Комната {self.number} забронирована")
      else:
         print(f"Комната {self.number} уже имеет бронь")

# Освобождение комнаты
   def release(self):
      self.is_available = True
      print(f"Комната {self.number} стала свободна")

class LuxuryRoom(Room):
   def __init__(self, number, max_people, price_per_night, balcony, mini_bar):
   #   Добавляем из класса Room
      super().__init__(number, "Luxury", max_people, price_per_night)
      self.balcony = balcony
      self.mini_bar = mini_bar

# Бронирование с класса Room
   def book(self):
      super().book()
      print("Дополнительные роскошные услуги включены")

class StandardRoom(Room):
    def __init__(self, number, max_people, price_per_night, bed_count):
        super().__init__(number, "Standard", max_people, price_per_night)
        self.bed_count = bed_count

    def release(self):
        super().release()
        print("Идет стандартная уборка номера")

class EconomyRoom(StandardRoom):
    def release(self):
        super().release()
        print("Проверяем, все ли гости выехали")

class Guest:
    def __init__(self, name, phone, booking_id=None):
        self.name = name
        self.phone = phone
        self.booking_id = booking_id

    def book_room(self, room):
        if room.is_available:
            room.book()
            self.booking_id = room.number
            print(f"Гость {self.name} забронил комнату {room.number}")
        else:
            print("Комната занята")

class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def find_room_by_number(self, number):
        for room in self.rooms:
            if room.number == number:
                return room
        return None

    def all_available_rooms(self):
        return [room for room in self.rooms if room.is_available]

    def find_room_for_people(self, people_count):
        return [room for room in self.rooms if room.max_people >= people_count and room.is_available]

# # Test script
# hotel = Hotel()
# hotel.add_room(LuxuryRoom(101, 2, 150, True, True))
# hotel.add_room(StandardRoom(102, 3, 100, 2))
# hotel.add_room(EconomyRoom(103, 4, 50, 3))

# guest1 = Guest("Alice", "1234567890")
# guest1.book_room(hotel.find_room_by_number(101))

# guest2 = Guest("Bob", "0987654321")
# guest2.book_room(hotel.find_room_by_number(102))

# print("Доступные номера после бронирования:", [room.number for room in hotel.all_available_rooms()])
# hotel.find_room_by_number(101).release()
# print("Доступные комнаты после выпуска 101:", [room.number for room in hotel.all_available_rooms()])

class TreeNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _create_node(self, value, parent):
        return TreeNode(value, parent)

    def insert(self, value):
        if not self.root:
            self.root = self._create_node(value, None)
            print(f"Вставленный корневой узел: {value}")
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left:
                self._insert_recursive(current.left, value)
            else:
                current.left = self._create_node(value, current)
                print(f"Вставлено {value} как левый узел {current.value}")
        elif value > current.value:
            if current.right:
                self._insert_recursive(current.right, value)
            else:
                current.right = self._create_node(value, current)
                print(f"Вставлено {value} как правый узел {current.value}")
        else:
            print(f"Значение {value} уже существует в дереве")

    def find(self, value):
        return self._find_recursive(self.root, value)

    def _find_recursive(self, current, value):
        if not current:
            return None
        if value == current.value:
            return current
        elif value < current.value:
            return self._find_recursive(current.left, value)
        else:
            return self._find_recursive(current.right, value)

    def delete(self, value):
        node = self.find(value)
        if node:
            self._delete_node(node)
            print(f"Удален узел со значением: {value}")
        else:
            print(f"Значение {value} не найдено")

    def _delete_node(self, node):
        if not node.left and not node.right:  # Leaf node
            self._replace_node_in_parent(node, None)
        elif node.left and node.right:  # Two children
            successor = self._find_min(node.right)
            node.value = successor.value
            self._delete_node(successor)
        else:  # One child
            child = node.left if node.left else node.right
            self._replace_node_in_parent(node, child)

    def _replace_node_in_parent(self, node, new_node):
        if node.parent:
            if node == node.parent.left:
                node.parent.left = new_node
            else:
                node.parent.right = new_node
        if new_node:
            new_node.parent = node.parent
        if node == self.root:
            self.root = new_node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def print_tree(self):
        self._print_recursive(self.root, 0)

    def _print_recursive(self, current, depth):
        if current:
            self._print_recursive(current.right, depth + 1)
            print("    " * depth + f"{current.value}")
            self._print_recursive(current.left, depth + 1)

def start_bin():

   bst = BinarySearchTree()

   while True:
      command = input("Введите команду (insert, find, delete, print, exit): ").strip().lower()

      if command == "insert":
         try:
               value = int(input("Введите значение для вставки:"))
               bst.insert(value)
         except ValueError:
               print("Неверный ввод. Пожалуйста, введите номер.")

      elif command == "find":
         try:
               value = int(input("Введите значение, чтобы найти:"))
               node = bst.find(value)
               if node:
                  print(f"Найден узел со значением: {node.value}")
               else:
                  print("Значение не найдено в дереве")
         except ValueError:
               print("Неверный ввод. Пожалуйста, введите номер")

      elif command == "delete":
         try:
               value = int(input("Введите значение для удаления:"))
               bst.delete(value)
         except ValueError:
               print("Неверный ввод. Пожалуйста, введите номер")

      elif command == "print":
         print("Текущее состояние дерева:")
         bst.print_tree()

      elif command == "exit":
         print("Выход")
         break

      else:
         print("Не понятно")


# start_bin()