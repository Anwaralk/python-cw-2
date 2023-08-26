bus_capacity = 60

ppl_inbus = int(input('how many people inside? '))
ppl_waiting = int(input('how many people want to get in? '))

empty_seats = bus_capacity - ppl_inbus

if empty_seats > ppl_waiting:
    print(f'you can ride, there are {empty_seats} seats available')
elif empty_seats >= ppl_waiting:
    print('seats are full :(')