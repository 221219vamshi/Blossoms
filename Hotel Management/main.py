from datetime import date

class Hotel:
    def _init_(self):
        self.rooms = {}
        self.available_rooms = {'std': [101, 102, 103], 'delux': [201, 202, 203], 'execu': [301, 302, 303], 'suite': [401, 402, 403]}
        self.roomprice = {1: 2000, 2: 4000, 3: 5000, 4: 6000}

    def get_int_input(self, prompt, min_value=None, max_value=None):
        while True:
            try:
                value = int(input(prompt))
                if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                    print(f"Please enter a number between {min_value} and {max_value}.")
                else:
                    return value
            except ValueError:
                print("Invalid input, please enter a number.")

    def check_in(self, name, address, phone):
        roomtype = self.get_int_input('Room types: \n1. Standard \n2. Deluxe\n3. Executive\n4. Suite\nSelect a room: ', 1, 4)
        room_no = None

        if roomtype == 1 and self.available_rooms['std']:
            room_no = self.available_rooms['std'].pop(0)
        elif roomtype == 2 and self.available_rooms['delux']:
            room_no = self.available_rooms['delux'].pop(0)
        elif roomtype == 3 and self.available_rooms['execu']:
            room_no = self.available_rooms['execu'].pop(0)
        elif roomtype == 4 and self.available_rooms['suite']:
            room_no = self.available_rooms['suite'].pop(0)
        else:
            print("Sorry, selected room type is not available.")
            return

        check_in_date = self.get_date_input('Enter check-in date in day, month, year (dd mm yyyy): ')
        self.rooms[room_no] = {
            'name': name,
            'address': address,
            'phone': phone,
            'check_in_date': check_in_date,
            'room_type': roomtype,
            'food': 0
        }
        print(f"Checked in {name}, {address} to room: {room_no} on {check_in_date}")

    def get_date_input(self, prompt):
        while True:
            try:
                d, m, y = map(int, input(prompt).split())
                return date(y, m, d)
            except ValueError:
                print("Invalid date format. Please enter in the format dd mm yyyy.")

    def room_service(self, room_no):
        if room_no in self.rooms:
            print("* Blossoms Restaurant room services **")
            print("1. Need Extra Bedsheets 2. Need Extra Pillows 3. Room Cleaning 4. Exit")
            while True:
                r = self.get_int_input("Select your choice: ", 1, 4)
                if r == 1:
                    quantity = self.get_int_input("Enter quantity of bedsheets: ", 1)
                    print(f"{quantity} bedsheets will be provided.")
                elif r == 2:
                    quantity = self.get_int_input("Enter quantity of pillows: ", 1)
                    print(f"{quantity} pillows will be provided.")
                elif r == 3:
                    print("Room cleaning will be provided.")
                elif r == 4:
                    print("Exiting the system. Thank you!")
                    break
                else:
                    print("Invalid choice, please try again.")
        else:
            print("Invalid room number.")

    def display_occupied(self):
        if not self.rooms:
            print("No rooms are occupied at the moment.")
        else:
            print("Occupied Rooms: ")
            print("-----------------------")
            print('Room no.   Name   Phone')
            print("-----------------------")
            for room_number, details in self.rooms.items():
                print(f"{room_number} \t {details['name']} \t {details['phone']}")

    def check_out(self, room_number):
        if room_number in self.rooms:
            check_out_date = date.today()
            check_in_date = self.rooms[room_number]['check_in_date']
            duration = (check_out_date - check_in_date).days
            roomtype = self.rooms[room_number]['room_type']

            if roomtype == 1:
                self.available_rooms['std'].append(room_number)
            elif roomtype == 2:
                self.available_rooms['delux'].append(room_number)
            elif roomtype == 3:
                self.available_rooms['execu'].append(room_number)
            elif roomtype == 4:
                self.available_rooms['suite'].append(room_number)

            print('--------------------')
            print('Blossoms Hotel Receipt')
            print(f"Name: {self.rooms[room_number]['name']}")
            print(f"Address: {self.rooms[room_number]['address']}")
            print(f"Phone: {self.rooms[room_number]['phone']}")
            print(f'Room Number: {room_number}')
            print(f"Check-in date: {check_in_date.strftime('%d %B %Y')}")
            print(f"Check-out date: {check_out_date.strftime('%d %B %Y')}")
            print(f'No. of Days: {duration}\tPrice per day: Rs. {self.roomprice[roomtype]}')
            roombill = self.roomprice[roomtype] * duration
            print(f'Total room bill: Rs. {roombill}')
            print(f'Food bill: Rs. {self.rooms[room_number]["food"]}')
            print(f'Total bill: Rs. {roombill + self.rooms[room_number]["food"]}')
            print('--------------------')

            del self.rooms[room_number]
        else:
            print("Invalid room number.")

    def order_your_food(self, room_no):
        if room_no in self.rooms:
            print("** Blossoms Restaurant Menu...")
            print("1. Tea/Coffee: Rs.20 \n2. Dessert: Rs.70 \n3. Breakfast: Rs.100 \n4. Lunch: Rs.150 \n5. Dinner: Rs.120 \n6. Exit")
            while True:
                c = self.get_int_input("Select your choice: ", 1, 6)
                if c == 1:
                    q = self.get_int_input("Enter the quantity: ", 1)
                    self.rooms[room_no]['food'] += 20 * q
                elif c == 2:
                    q = self.get_int_input("Enter the quantity: ", 1)
                    self.rooms[room_no]['food'] += 70 * q
                elif c == 3:
                    q = self.get_int_input("Enter the quantity: ", 1)
                    self.rooms[room_no]['food'] += 100 * q
                elif c == 4:
                    q = self.get_int_input("Enter the quantity: ", 1)
                    self.rooms[room_no]['food'] += 150 * q
                elif c == 5:
                    q = self.get_int_input("Enter the quantity: ", 1)
                    self.rooms[room_no]['food'] += 120 * q
                elif c == 6:
                    break
                else:
                    print("Invalid option")
            print(f"Total food bill: Rs. {self.rooms[room_no]['food']}")
        else:
            print("Invalid room number.")

    def start_app(self):
        while True:
            print("-----------------")
            print('Welcome To Blossoms Hotel')
            print("1. Check-in")
            print("2. Room service")
            print("3. Display Occupied Rooms")
            print("4. Order your Food Check-out")
            print("5. Check-out")
            print("6. Exit")

            choice = self.get_int_input("Enter your choice (1-6): ", 1, 6)
            if choice == 1:
                name = input("Enter Client Name: ")
                address = input("Enter Address: ")
                phone = input("Enter contact no.: ")
                self.check_in(name, address, phone)
            elif choice == 2:
                room_no = self.get_int_input("Enter room number: ")
                self.room_service(room_no)
            elif choice == 3:
                self.display_occupied()
            elif choice == 4:
                room_number = self.get_int_input("Enter room number: ")
                self. order_your_food (room_number)
            elif choice == 5:
                room_no = self.get_int_input("Enter room number: ")
                self.check_out(room_no)
            elif choice == 6:
                break
            else:
                print("Invalid choice. Please try again.")

h = Hotel()
h.start_app()