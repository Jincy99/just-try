# Bus seating chart

chart=""
for row in range(1,8):
    for seat in range(1,5):
        amount=int(input("Tell us the amount you have: "))
        if amount>=250:
            print("your seat number is: ",row,seat)
            chart+="$"
        else:
            chart+="#"
    chart+="\n"
print(chart)
                      
