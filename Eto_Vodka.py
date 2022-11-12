orderlist = str(["tea", "hot chocolate", "coffee"])
print("[You enter a coffee shop.]")
name = input("(Barista): Hello! Welcome to my coffee shop!!!!1!!!1 \n \n What is your name? \n")

order = input(f"\n(Barista): So, {name}, what would you like? Coffee(£4.99), tea(£1.99), or hot chocolate(£0.99)?\n\n(You): I would like ")
while orderlist not in order:
    order = input("Sorry, we don't serve that (or you typed it wrong). Please try again. \n \n (You): I would like ")
    break

amt_order = int(input(f"(Barista): How many {order}s would you like? \n \n"))
if order == "hot chocolate":
    total_cost = amt_order*0.99
elif order == "tea":
    total_cost = amt_order*1.99
elif order == "coffee":
    total_cost = amt_order*4.99

if amt_order > 1:
    print(f"(Barista): 'Aight my G I'll get you those {order}s in a bit.")
else:
    print(f"(Barista): 'Aight my G I'll get you that {order} in a bit.")

import time
time.sleep(2.1)

if amt_order > 1:
    print(f"(Barista): 'Aight my G here are your {order}s.")
else:
    print(f"(Barista): 'Aight my G here is your {order}.")

payment_method = input(f"(Barista): Alright, that'll be £{total_cost}, how will you like to pay? Card, cash, or Ohio? \n \n")

if payment_method == "card":
    print(f"(Barista): Please PayPal Codrut £{total_cost} now, {name}")
elif payment_method == "cash":
    print(f"(Barista): Hand Codrut £{total_cost} when you next see him, {name}.")
elif payment_method == "Ohio" or "ohio":
    print("https://open.spotify.com/track/7o8cvobGNd2IbhCz7J0DvB?si=eff1a02dbe074d80") # a song on spotify

else:
    print(f"(Barista): Sorry, we don't accept that. Buuuuuuuuuuuuuuuuuuuuuut, you're getting them for free, {name}. You lucky son of a bi- [You leave at the right moment.]") #I am too lazy to do it everywhere
time.sleep(2.3712659852) #Very Specific
print(f"[You reach home. You drink your {order}(s) in peace. What a vibe.]")
time.sleep(3.1415926535897932384626433)# More specific
print("[What a vibe.]")
time.sleep(3)
exit()
