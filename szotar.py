kutya = {
    "fajta": "angol bulldog",
    "születési év": 1999,
    "szín": "barna",
    "oltás":["veszettség","rühesség", "szívféreg", "hülyeség"]
    }

print(kutya["szín"])
print(kutya["oltás"])
print("\n".join(kutya("oltás")))

kutya["nev"] = "Buksi"

print(kutya)
