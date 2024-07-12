phone_book={'Nata': 89877655656, 'Max': 89823445645}
print(phone_book)
print(phone_book['Nata'])
phone_book['Max']=89823214534
print(phone_book['Max'])
phone_book['Rita']=89878776545
print(phone_book)
del phone_book['Max']
print(phone_book)
phone_book.update({'Sasha': 89765644534,
                   'Jeny': 89768752312})
print(phone_book)
print(phone_book.get('Nata'))
print(phone_book.get('Vanya'))