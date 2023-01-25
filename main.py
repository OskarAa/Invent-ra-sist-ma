from collections import Counter
#create_inventory(items)
create_inventory = ["coal", "wood", "wood", "diamond", "diamond", "diamond"]
#{"coal":1, "wood":2, "diamond":3}
add_items = ["wood", "iron", "coal", "wood"]
print(Counter(create_inventory))
res = create_inventory + add_items
print(Counter(add_items))
print(Counter(res))
res.remove("diamond")
res.remove("coal")
res.remove("iron")
print(Counter(res))
result = res.count("wood")
if result("wood")
result = res.count("iron")
result = res.count("coal")
result = res.count("wood")