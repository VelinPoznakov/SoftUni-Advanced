from typing import List

# from project.clients.adult import Adult
# from project.clients.base_client import BaseClient
# from project.clients.student import Student
# from project.loans.base_loan import BaseLoan
# from project.loans.mortgage_loan import MortgageLoan
# from project.loans.student_loan import StudentLoan


class BankApp:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type == 'StudentLoan' or loan_type == 'MortgageLoan':

            if loan_type == 'StudentLoan':
                loan = StudentLoan()
            else:
                loan = MortgageLoan()

            self.loans.append(loan)
            return f"{loan_type} was successfully added."

        raise Exception("Invalid loan type!")

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):

        if self.capacity == len(self.clients):
            return "Not enough bank capacity."

        if client_type == 'Student' or client_type == 'Adult':

            if client_type == 'Student':
                client = Student(client_name, client_id, income)
            else:
                client = Adult(client_name, client_id, income)

            self.clients.append(client)
            return f"{client_type} was successfully added."

        raise Exception("Invalid client type!")

    def grant_loan(self, loan_type: str, client_id: str):
        client = [client for client in self.clients if client.client_id == client_id][0]  # student id=''
        # for client in self.clients:
        #     if client.client_id == client_id:

        if (loan_type == 'StudentLoan' and client.__class__.__name__ == 'Student') or (
                loan_type == 'MortgageLoan' and client.__class__.__name__ == 'Adult'):
            loan = [loan for loan in self.loans if loan.__class__.__name__ == loan_type][0]
            # for loan in self.loans:
            #     if loan.__class__.__name__ == loan_type:
            self.loans.remove(loan)
            client.loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client.client_id}."

        raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):

        try:
            client = [c for c in self.clients if c.client_id == client_id][0]
        except IndexError:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        counter = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                counter += 1

        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                counter += 1

        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        #clients_loans = sum([c.loans for c in self.clients])
        client_income = sum([c.income for c in self.clients])
        client_interest_rate = [c.interest for c in self.clients]
        try:
            av_rate = sum(client_interest_rate) / len(client_interest_rate)
        except ZeroDivisionError:
            av_rate = 0

        result = f'Active Clients: {len(self.clients)}\n'
        result += f'Total Income: {client_income:.2f}\n'
        result += (f'Granted Loans: {len([l.amount for c in self.clients for l in c.loans])}, Total Sum: '
                   f'{sum([l.amount for c in self.clients for l in c.loans]):.2f}\n')
        result += f'Available Loans: {len(self.loans)}, Total Sum: {sum(l.amount for l in self.loans):.2f}\n'
        result += f'Average Client Interest Rate: {av_rate:.2f}'
        return result
