class Category(object):
    def __init__(self, category):
        self._cat = category
        self._amount = 0.0
        self._desc = ""
        self._ledger = list(dict())

    def deposit(self, amount, desc=""):
        self._amount = amount
        self._desc = desc[:23]
        self._ledger.append({"amount": self._amount, "description": self._desc})


    def withdraw(self, amount, desc=""):
        if self.check_funds(amount):
            self._amount = -amount
            self._desc = desc[:23]
            self._ledger.append({"amount": self._amount, "description": self._desc})
            return True
        else: return False


    def transfer(self, amount, another_ledger):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {another_ledger.cat}')
            another_ledger.deposit(amount, f'Transfer from {self._cat}')
            return True
        else: return False

    def check_funds(self, amount=0):
        self._total = 0
        for dict_item in self._ledger:
            self._total += dict_item['amount']
        if self._total >= amount:
            return True
        else: return False

    @property
    def cat(self):
        return self._cat
    def ledger(self):
        return self._ledger
    def get_balance(self):
        self.check_funds()
        return self._total

    def display(self):
        print(self._cat.center(31, '*'))
        for dict_item in self._ledger:
            print(dict_item['description'].ljust(23, ' '), str("{:.2f}".format(dict_item['amount']))[:7].rjust(7, ' '))
        print(f'Total: {self.get_balance()}')

def create_spend_chart(cat_list):
    mylist = cat_list
    mychart = list(dict())
    total_spent = 0
    for obj in mylist:
        spent = 0
        for objdict in obj.ledger():
            if objdict['amount'] < 0 and "Transfer" not in objdict['description'] :
                spent += objdict['amount']
        mychart.append({"name":obj.cat, "spent":spent, "percentage": 0})
        total_spent += spent

    for obj in mychart:
        obj['percentage'] = int((obj['spent'] / total_spent ) * 100) // 10 *10


    print(mychart)
    print("Percentage spent by category")
    for i in range(100, -10, -10):
        print(f'{str(i).rjust(3)}|', end='')
        for obj in mychart:
            if obj['percentage'] >= i :
                print(' o ', end='')
            else: print ('   ', end='')
        print()
    print(''.rjust(3),'-'*(len(mylist)*3+1))

    newlist = [ x.cat for x in mylist]
    full_len = 0
    for x in mylist:
        full_len += len(x.cat)

    str1 = ''
    for i in range(len(mylist) + 2):
        for j in range(int(full_len / len(mylist)) + 1):
            try:
                if newlist[j][i]:
                    str1 += newlist[j][i] + "  "
            except IndexError:
                str1 += '   '
        print(''.rjust(5), end='')
        print(str1)
        str1 = ''

def main():
    # food, clothing, and entertainment
    food = Category('Food')
    clothing = Category("Clothing")
    entertainment = Category("Entertainment")
    food.deposit(1000, "Initial Deposit")
    food.withdraw(10.15, "Groceries")
    food.withdraw(15.89, "Restaurant and more food")
    food.transfer(50, clothing)
    food.display()


    clothing.display()

    entertainment.deposit(88234980908, "This is a test deposit to check printing format")
    entertainment.display()

    auto = Category("Auto")
    auto.deposit(100, "Test Deposit")
    auto.withdraw(30, "Test Withdrawal")
    auto.display()

    create_spend_chart([food, clothing, auto])


if __name__ == "__main__":
    main()

