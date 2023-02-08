def convert(amount, fromm, too):
    exchange_rates = {'US_dollar': 1.0, 'France_euro': 0.93, 'Mexico_peso': 18.87,
                      'Japan_yen': 131.19, 'Canada_dollar': 1.34, 'India_rupee':82.5}
    
    initial_amount = exchange_rates[too]/exchange_rates[fromm]
    target_amount =  initial_amount*z
    
    
    return target_amount
q=input("Welcome to Currency Converter! Would you like to convert? Yes:No")
while q!="No":
    
    z=int(input("type amount:   "))
    y=input("select a currency?: US_dollar, France_euro, Mexico_peso, Japan_yen, Canada_dollar, India_rupee:----->")
    f=input("What would you like to convert to?:US_dollar, France_euro, Mexico_peso, Japan_yen, Canada_dollar, India_rupee:------>    ")
    

    v=(convert(z,y,f))
    print("you now have "+str(v)+" "+str(f))
    q=input("Welcome to Currency Converter! Would you like to convert? Yes:No")

print("Thank You")
        
