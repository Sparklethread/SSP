import random

def spelare():
    while True:
        spelarens_val = input("sten(S), sax(X) eller påse(P): ")
        if spelarens_val in ['S', 'X', 'P']:
            return spelarens_val
        else:
            print("Ogiltigt val")

def dator():
    return random.choice(['S', 'X', 'P'])

def vinnare(spelarens_val, datorns_val):
    if spelarens_val == datorns_val:
        return None
    elif (spelarens_val == 'S' and datorns_val == 'X') or \
         (spelarens_val == 'X' and datorns_val == 'P') or \
         (spelarens_val == 'P' and datorns_val == 'S'):
        return 'Spelare'
    else:
        return 'Datorn'

def main():
    while True:
        spelarens_val = spelare()
        datorns_val = dator()
        print(f"Datorn valde: {datorns_val}")
        segrare = vinnare(spelarens_val, datorns_val)
        if segrare:
            print(f"Vinnaren är: {segrare}")
            break
        else:
            print("Oavgjort, försök igen.")

if __name__ == "__main__":
    main()
