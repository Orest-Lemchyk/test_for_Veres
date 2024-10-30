class Insects:

    def __init__(self, name = "not name", speed = 0, weight = 0,  color = "not definated",  legs_num = 0):
        print("Object is created.")
        self.set_name(name)
        self.set_speed(speed)
        self.set_weight(weight)

        self.color = color
        self.legs_num = legs_num


    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


    def set_speed(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed


    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight


    def __str__(self):
       # print("Calling __str__")
        #return f" Insects \n Name: {self.__name}\n Speed(m/s): {self.__speed}\n Weight: {self.__weight}\n Color: {self.color}\n Legs num: {self.legs_num}\n"
        return f" Insects  Name: {self.__name} Speed(m/s): {self.__speed} Weight: {self.__weight} Color: {self.color} Legs num: {self.legs_num}"


    def __repr__(self):
        print("Calling __repr__")
        return self.__str__()


    def __del__(self):
        print(f"Object {self.__name} is deleted")


ant = Insects("Ant", 5, 10, "red", 8)
beetle = Insects("Beetle", 10, 3, "yelow", 6)
chafer = Insects("Chafer", 15, 16, "brown", 6)

insects_dict = {"ant": ant, "beetle": beetle, "chafer": chafer}

while True:

    user_input = input("Enter a command (e.g., print ant, del ant, or exit): ").strip().lower()
    user_comand = user_input.split()[0]

    match user_comand:
        case "printall":
            print(insects_dict)
        case "print":
            var_name = user_input.split()[1]
            if var_name in insects_dict:
                print(insects_dict[var_name])
        case "del":
            var_name = user_input.split()[1]
            if var_name in insects_dict:
                del insects_dict[var_name]
                print(f"{var_name} is deleted")
        case "delall":
            del insects_dict
            break

        case "exit":
            break
