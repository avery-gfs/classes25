def iter_product(lists):
    results = [()]

    for itemsList in lists:
        newResults = []

        for item in itemsList:
            for result in results:
                newResults.append(result + (item,))

        results = newResults

    return results


for product in iter_product([ranks, suits]):
    print(product)


def rec_product(lists):
    if not lists:
        return [()]

    results = []

    for result in rec_product(lists[1:]):
        for item in lists[0]:
            results.append((item,) + result)

    return results


for product in rec_product([ranks, suits]):
    print(product)


def yield_product(lists):
    if not lists:
        yield ()
        return

    for result in yield_product(lists[1:]):
        for item in lists[0]:
            yield (item,) + result


for product in yield_product([ranks, suits]):
    print(product)
