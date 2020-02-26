sort_me = ["Kaunas", "Vilnius", "Alytus", "Klaipeda",
           "Varena", "Druskininkai", "Klaipeda"]
sort_me.sort(key=len)
print("Ascending: {}".format(sort_me))
sort_me.sort(key=len, reverse=True) # reverse() could be used too
print("Descending: {}".format(sort_me))
