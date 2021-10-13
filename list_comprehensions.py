def run():
    squeres = []
    for i in range(1,100):
        if i % 3 != 0:
            squeres.append(i**2)
    print(squeres)


if __name__=="__main__":
    run()