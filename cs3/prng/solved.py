numBuckets = 10


def showHistogram(buckets):
    for index, count in enumerate(buckets):
        scale = 20 / max(buckets)
        bar = "#" * round(scale * count)
        print(
            f"{index / numBuckets:.2f} - {(index + 1) / numBuckets:.2f} : {count:6} : {bar}"
        )


def testRandoms(values):
    valBuckets = [0] * numBuckets
    gapBuckets = [0] * numBuckets

    for index, n in enumerate(values):
        valBuckets[int(n * numBuckets)] += 1
        diff = (n - values[index - 1]) % 1
        gapBuckets[int(diff * numBuckets)] += 1

    print("value bins:\n")
    showHistogram(valBuckets)

    print("\nvalue spacing:\n")
    showHistogram(gapBuckets)


numVals = 1000000


def randomNums():
    n = 17
    m = 2**32
    a = 1664525
    c = 1013904223

    result = []

    for _ in range(numVals):
        result.append(n / m)
        n = (n * a + c) % m

    return result


values = randomNums()
testRandoms(values)
