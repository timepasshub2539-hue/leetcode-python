def make_coffee(size="medium", milk=True):
    milk_text = "with milk" if milk else "black"
    print(f"{size} coffee, {milk_text}")

make_coffee(size="large", milk=False)
