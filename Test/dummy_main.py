def infect(human):
    try:
        health = human["health"]
        protein = human["protein"]
    except Exception:
        print("Incorrect data")
        return None

    if protein == "A" and health < 90:
        return True
    else:
        print("Didn't infect")
        return False



def main():
    pass


if __name__ == "__main__":
    main()
