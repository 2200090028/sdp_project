while True:
    try:
        n = int(input("Please enter an integer"))
        m = int(input("Please enter an integer"))
        z = n / m
        break

    except Exception as e:
        print("Not an integer! Please again 123")
        print(e)
    except ValueError:
        print("Not an integer! Please again 456")
    finally:
        print("You succesfully enter an integer")