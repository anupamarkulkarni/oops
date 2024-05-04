from details import keerthi, anu, ayesha

def main():
    Keerthi = keerthi("sbi", 123, 1)
    Anu = anu("karnataka", 1234, 2)
    Ayesha = ayesha("indian",12345, 3)

    Keerthi.display_details()
    print("\n")
    Anu.display_details()
    print("\n")
    Ayesha.display_details()

if __name__ == "__main__":
    main()
