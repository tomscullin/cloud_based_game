import random

# --- Player Stats ---
storage = 256  # GB
integrity = 80  # %
money = 20  # SoulCredits
subscription_days = 3

# --- Display Status ---
def display_status():
    print("\n--- Cloud Based Status ---")
    print(f"Storage: {storage} GB")
    print(f"Memory Integrity: {integrity}%")
    print(f"SoulCredits: {money}")
    print(f"Subscription Days Left: {subscription_days}")
    print("--------------------------")

# --- Events ---
def memory_corruption():
    global storage, integrity, money
    print("\n📂 A childhood memory is corrupted!")
    print("1. Delete it (+10 GB, -10% integrity)")
    print("2. Pay 5 SoulCredits to restore it")
    choice = input("Choose (1 or 2): ")
    if choice == "1":
        storage += 10
        integrity -= 10
        print("You deleted the memory. You feel emptier...")
    elif choice == "2":
        if money >= 5:
            money -= 5
            print("You restored the memory. It cost you.")
        else:
            print("You don’t have enough SoulCredits!")
    else:
        print("You did nothing. The memory is lost.")

def relative_cancels():
    global subscription_days
    print("\n💬 Your mother canceled her subscription payment.")
    print("1. Guilt-trip her (extend subscription by 1 day)")
    print("2. Respect her choice (-1 subscription day)")
    choice = input("Choose (1 or 2): ")
    if choice == "1":
        subscription_days += 1
        print("You guilt-tripped your mom. You get one more day.")
    elif choice == "2":
        subscription_days -= 1
        print("You let her go. Time is running out.")
    else:
        print("You did nothing. The subscription continues to drain.")

def ad_offer():
    global integrity, money
    print("\n📺 CloudCorp offers to run ads in your dreams.")
    print("1. Accept (+10 SoulCredits, -5% integrity)")
    print("2. Decline (Nothing happens)")
    choice = input("Choose (1 or 2): ")
    if choice == "1":
        money += 10
        integrity -= 5
        print("You accepted. Sweet cash, but nightmares incoming.")
    elif choice == "2":
        print("You declined. Silence in the void.")
    else:
        print("No response. The offer expires.")

# --- Random Event Selection ---
def trigger_event():
    events = [memory_corruption, relative_cancels, ad_offer]
    event = random.choice(events)
    event()

# --- End Conditions ---
def check_end():
    if subscription_days <= 0:
        print("\n☠️ Your subscription expired. You fade into digital oblivion.")
        return True
    if integrity <= 0:
        print("\n🧠 You’ve lost all memory integrity. You no longer exist as yourself.")
        return True
    return False

# --- Game Loop ---
print("🌩️ Welcome to Cloud Based! 🌩️\n")

game_over = False

while not game_over:
    display_status()
    trigger_event()
    subscription_days -= 1
    game_over = check_end()

print("\nGAME OVER")
