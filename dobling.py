import math


def main():
    print("=== Dobling av investering ===\n")

    while True:
        try:
            rente = float(input("Oppgi forventet årlig rente (i prosent, f.eks. 7): "))
            if rente <= 0:
                print("Renten må være større enn 0. Prøv igjen.\n")
                continue
            break
        except ValueError:
            print("Ugyldig inndata. Skriv inn et tall.\n")

    regel_72 = 72 / rente
    eksakt = math.log(2) / math.log(1 + rente / 100)

    print(f"\nVed {rente}% årlig rente:")
    print(f"  Regel av 72 (estimat):  {regel_72:.1f} år")
    print(f"  Eksakt beregning:       {eksakt:.2f} år")
    print(f"  Avvik:                  {abs(regel_72 - eksakt):.2f} år")


if __name__ == "__main__":
    main()
