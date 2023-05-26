class AccountBank:
    def __init__(self, number: int, name: str, type: int):
        self.number = number
        self.balance = 0
        self.name = name
        self.type = type
        self.status = False
        self.limit = [False, 0, 0] #[Status, value overdraft, balance overdraft]

    def limit_(self, values) -> int:
        if not self.limit[0]:
            self.limit[0] = True
            self.limit[1] = values
            self.limit[2] = values
            return 1
        else:
            return 0

    def deposit(self, values: float) -> None:
        if self.limit[0]:
            if self.limit[2] < self.limit[1]:
                difference = self.limit[1] - self.limit[2]
                if values > difference:
                    self.limit[2] += difference
                    values = values - difference
                    self.balance += values
                else:
                    self.limit[2] += values
            else:
                self.balance += values
        else:
            self.balance += values

    def draw(self, values: float) -> int:
        if self.status:
            if values > self.balance:
                difference = values - self.balance
                if self.limit[0]:
                    if difference < self.limit[2]:
                        self.balance = 0
                        self.limit[2] -= difference
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                self.balance -= values
                return 1
        else:
            return 0

    def activate_account(self) -> int:
        if self.status:
            return 0
        else:
            self.status = True
            return 1

    def situation_account(self) -> tuple:
        return self.status, self.balance, self.limit[0], self.limit[1], self.limit[2]

