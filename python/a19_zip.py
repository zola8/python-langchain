def separate_dicts_example_1():
    names = {"UCaiL2GDNpLYH6Wokkk1VNcg": "mCoding",
             "UC7_gcs09iThXybpVgjHZ_7g": "PBS Space Time",
             "UCxHAlbZQNFU2LgEtiqd2Maw": "Cᐩᐩ Weekly With Jason Turner"}
    sub_counts = {"UCaiL2GDNpLYH6Wokkk1VNcg": 122_000,
                  "UC7_gcs09iThXybpVgjHZ_7g": 2_630_000,
                  "UCxHAlbZQNFU2LgEtiqd2Maw": 85_000}

    print()
    for cid in names:
        name = names[cid]
        sub_count = sub_counts[cid]
        print(f'{name} has {sub_count} subscribers! Watch here: youtube.com/channel/{cid}')


def separate_dicts_example_2():
    names = {"UCaiL2GDNpLYH6Wokkk1VNcg": "mCoding",
             "UC7_gcs09iThXybpVgjHZ_7g": "PBS Space Time",
             "UCxHAlbZQNFU2LgEtiqd2Maw": "Cᐩᐩ Weekly With Jason Turner"}
    sub_counts = {"UCaiL2GDNpLYH6Wokkk1VNcg": 122_000,
                  "UC7_gcs09iThXybpVgjHZ_7g": 2_630_000,
                  "UCxHAlbZQNFU2LgEtiqd2Maw": 85_000}

    print("\n\n-- separate_dicts_example_2")
    for cid, name in names.items():
        sub_count = sub_counts[cid]
        print(f'{name} has {sub_count} subscribers! Watch here: youtube.com/channel/{cid}')


def plain_zip_example():
    ids = ["UCaiL2GDNpLYH6Wokkk1VNcg", "UC7_gcs09iThXybpVgjHZ_7g", "UCxHAlbZQNFU2LgEtiqd2Maw"]
    names = ["mCoding", "PBS Space Time", "Cᐩᐩ Weekly With Jason Turner"]
    sub_counts = [122_000, 2_630_000, 85_000]

    print("\n\n-- plain_zip_example")
    for cid, name, sub_count in zip(ids, names, sub_counts, strict=True):
        print(f'{name} has {sub_count} subscribers! Watch here: youtube.com/channel/{cid}')


def dict_zip(*dicts):
    if not dicts:
        return

    n = len(dicts[0])
    if any(len(d) != n for d in dicts):
        raise ValueError('arguments must have the same length')

    for key, first_val in dicts[0].items():
        yield key, first_val, *(other[key] for other in dicts[1:])


def separate_dicts_example_3():
    names = {"UCaiL2GDNpLYH6Wokkk1VNcg": "mCoding",
             "UC7_gcs09iThXybpVgjHZ_7g": "PBS Space Time",
             "UCxHAlbZQNFU2LgEtiqd2Maw": "Cᐩᐩ Weekly With Jason Turner"}
    sub_counts = {"UCaiL2GDNpLYH6Wokkk1VNcg": 122_000,
                  "UC7_gcs09iThXybpVgjHZ_7g": 2_630_000,
                  "UCxHAlbZQNFU2LgEtiqd2Maw": 85_000}

    print("\n\n-- separate_dicts_example_3")
    for cid, name, sub_count in dict_zip(names, sub_counts):
        print(f'{name} has {sub_count} subscribers! Watch here: youtube.com/channel/{cid}')


if __name__ == '__main__':
    separate_dicts_example_1()
    separate_dicts_example_2()
    plain_zip_example()
    separate_dicts_example_3()