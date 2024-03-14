class Expense:
    def __init__(self,payer_id,amount,participants,expense_type,values=None):
        self.payer_id = payer_id
        self.amount = amount
        self.participants = participants
        self.expense_type = expense_type
        self.values = values if values else []
