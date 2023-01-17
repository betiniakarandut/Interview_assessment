# Mapping list to synonyms

map_list = [
{"Dg set": "Diesel generator"},
{"Organization": "Organisation"},
{"Group": "Organisation"},
{"Orange": "Kinnu"},
{"Orange": "narangi"}
]

new_list = []
# print(map_list[2])

for i in map_list:
    for prop, value in i.items():
        # print(prop, value)
        listed = False
        for group in new_list:
            if prop in group or value in group:
                group.add(prop)
                group.add(value)
                listed = True
            break
        if not listed:
            group = set()
            group.add(prop)
            group.add(value)
            new_list.append(group)
print(new_list)
