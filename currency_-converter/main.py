from currency_converter import CurrencyConverter

class Currency_Converter(object):
    def __init__(self,amount,c_from,c_to):
        self.amount = amount
        self.c_from = c_from
        self.c_to = c_to
        self.currency = CurrencyConverter()



    def __repr__(self):
        try:
            currency_result = round(self.currency.convert(self.amount,self.c_from,self.c_to), 2)
            return f"{self.amount} {self.c_from} = {currency_result}{self.c_to}"
        except ValueError:
            return "Need currency amount,current  currency and convertion currency"


if __name__=="__main__":
    currency = Currency_Converter(20,"USD","EUR")
    print(currency)