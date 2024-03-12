class CurrencyConverter:
    @staticmethod
    def convert(amount, from_currency, to_currency):
        conversion_rates = {
            ('USD', 'EUR'): 0.93,
            ('EUR', 'USD'): 1.07,
            ('USD', 'GBP'): 0.82,
            ('GBP', 'USD'): 1.22,
            # Add more conversion rates as needed
        }

        # Construct the key for the conversion rates dictionary
        conversion_key = (from_currency, to_currency)

        # Check if the conversion rate exists
        if conversion_key in conversion_rates:
            return amount * conversion_rates[conversion_key]
        else:
            raise ValueError("Conversion rate not found.")

# Converting 100 USD to EUR
print(CurrencyConverter.convert(300, 'USD', 'EUR'))

# Converting 50 EUR to USD
print(CurrencyConverter.convert(50, 'EUR', 'USD'))
