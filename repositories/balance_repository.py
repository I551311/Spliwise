class BalanceRepository():
    def __init__(self):
        self.balances = {}
        self.user_balances = []

    def update_balances(self, expense, shares):
        for user_id, share in shares.items():
            if user_id != expense["payer_id"]:
                self.balances[(expense["payer_id"], user_id)] = self.balances.get((expense["payer_id"], user_id), 0) + share
                self.balances[(user_id, expense["payer_id"])] = self.balances.get((user_id, expense["payer_id"]), 0) - share

    def get_balances(self, user_id=None):
        print(self.balances)
        if not self.balances:
            return []
        
        for pair, amount in self.balances.items():
            if user_id:
                if user_id == pair[0] or user_id == pair[1]:
                    if amount < 0:
                        self.user_balances.append(f"{pair[0]} owes {pair[1]}: {-1*amount}")
                    else:
                        self.user_balances.append(f"{pair[1]} owes {pair[0]}: {amount}")
            
            else:
                if amount < 0:
                    self.user_balances.append(f"{pair[0]} owes {pair[1]}: {-1*amount}")
                else:
                    self.user_balances.append(f"{pair[1]} owes {pair[0]}: {amount}")

        self.user_balances = set(self.user_balances)
        return self.user_balances
