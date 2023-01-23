from BankAccount import BankAccount

ba = BankAccount("John Doe", 55)
ba.deposit(17.52)
ba.withdraw(30)
print(ba.get_balance())
