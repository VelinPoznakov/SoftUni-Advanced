from python_oop_part_2.encapsulation.exr.wild_cat_zoo.animal import Animal


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        is_enough_budget = self.__budget >= price
        is_enougt_compacity = len(self.animals) < self.__animal_capacity

        if is_enougt_compacity and is_enough_budget:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif is_enougt_compacity and not is_enough_budget:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        all_salary = sum([worker.salary for worker in self.workers])
        if all_salary <= self.__budget:
            self.__budget -= all_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        all_animal_budget = sum([animal.money_for_care for animal in self.animals])
        if all_animal_budget <= self.__budget:
            self.__budget -= all_animal_budget
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        res = f"You have {len(self.animals)} animals\n"

        lion = [animal for animal in self.animals if animal.__class__.__name__ == 'Lion']
        cheetah = [animal for animal in self.animals if animal.__class__.__name__ == 'Cheetah']
        tiger = [animal for animal in self.animals if animal.__class__.__name__ == 'Tiger']

        res += f"----- {len(lion)} Lions:\n"
        for l in lion:
            res += f"{l}\n"

        res += f"----- {len(tiger)} Tigers:\n"
        for t in tiger:
            res += f"{t}\n"

        res += f"----- {len(cheetah)} Cheetahs:\n"
        for c in cheetah:
            res += f"{c}\n"

        return res[:-1]

    def workers_status(self):
        res = f"You have {len(self.workers)} workers\n"

        keepers = [worker for worker in self.workers if worker.__class__.__name__ == 'Keeper']
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == 'Caretaker']
        vet = [worker for worker in self.workers if worker.__class__.__name__ == 'Vet']

        res += f"----- {len(keepers)} Keepers:\n"
        for k in keepers:
            res += f"{k}\n"

        res += f"----- {len(caretakers)} Caretakers:\n"
        for c in caretakers:
            res += f"{c}\n"

        res += f"----- {len(vet)} Vets:\n"
        for v in vet:
            res += f"{v}\n"

        return res[:-1]
