from django.shortcuts import render

# Hardcoded conversion rates
INR_TO_USD = 0.012  # 1 INR = 0.012 USD
USD_TO_INR = 82.0   # 1 USD = 82 INR

def currency_converter(request):
    converted_amount = None
    if request.method == 'POST':
        amount = request.POST.get('amount')
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')

        if not amount or not from_currency or not to_currency:
            converted_amount = 'Error: Please fill in all fields.'
        else:
            try:
                amount = float(amount)
            except ValueError:
                converted_amount = 'Error: Invalid amount.'
                return render(request, r'C:\Users\Administrator\Desktop\28-03-2025\ust-python-2025\day-21\48-app-firstwebproject\firstwebproject\firstapp\templates\firstapp\convert.html', {'converted_amount': converted_amount})

            # Conversion logic
            if from_currency == 'INR' and to_currency == 'USD':
                converted_amount = amount * INR_TO_USD
            elif from_currency == 'USD' and to_currency == 'INR':
                converted_amount = amount * USD_TO_INR
            else:
                converted_amount = 'Error: Invalid currency pair.'

    return render(request, r'C:\Users\Administrator\Desktop\28-03-2025\ust-python-2025\day-21\48-app-firstwebproject\firstwebproject\firstapp\templates\firstapp\convert.html', {'converted_amount': converted_amount})
