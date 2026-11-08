print("=== Coffee Shop Order System ===")
print("Enter drink sizes: small, medium, or large")
print("Type 'done' when finished ordering")
sum=0
cycle_stopper=1
loyalty_discount=0
while cycle_stopper==1:
    size=input("Enter drink size: ")
    if size=="small":
        sum+=3.50
        print("Price: 3.50$")
        print(f"Current total:{sum}")
    if size=="medium":
            sum+=4.50
            print("Price: 4.50$")
            print(f"Current total:{sum}")
    if size=="large":
            sum+=5.50
            print("Price: 5.50$")
            print(f"Current total:{sum}")
    if size=="done":
          cycle_stopper=0
if sum>=20:
    loyalty_discount=3
print("=== Order Summary ===")
print(f"Subtotal: {sum}")
print(f"Loyalty discount: {loyalty_discount}")
print(f"Total: {sum-loyalty_discount}")
print("Thank you for your order!")
