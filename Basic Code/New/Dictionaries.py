info = {
    "B21": "Shwadheen",
    "B22": "Shawon",
    "B23": "Nayon",
    24: "Mohan",
    25: "Tuhin",
    26: True
}

print(info["B22"])
print(info[24])
print("\n")

print(info.get("B23"))
print(info.get(25))
print(info.get("B26"))
print(info.get("B25", "Not found !!!"))
print(info.get("B21", "Not found !!!"))

info["B24"] = "Araf"
print(info)

removeValue = info.pop(24)
print(removeValue)
print(info)

info.clear()
print(info)
