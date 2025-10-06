def chart(numbers):
    for threshold in range(max(numbers), 0, -1):
        for n in numbers:
            print("X" if n >= threshold else " ", end="")
        print()


def chart(numbers):
    print(
        "\n".join(
            "".join("X" if n >= threshold else " " for n in numbers)
            for threshold in range(max(numbers), 0, -1)
        )
    )


chart([1, 4, 2, 7, 3])
