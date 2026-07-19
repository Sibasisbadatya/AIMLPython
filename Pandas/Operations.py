import pandas as pd
# Operations
# --------------

var = pd.DataFrame({
    "A":[1,2,3],
    "B":[3,4,5]
})
var["C"] = var["A"]+var["B"]
print(var)

# Logical operations

var["lessthan2"] = var["A"]<2
print(var)

# Delete and Insert Data
var = pd.DataFrame({
    "A":[1,2,3],
    "B":[3,4,5]
})

var.insert(2,"C",var["B"]*2) # position , column name,elements (passed as elements array or previous columns elements)
# make sure to insert the elements array should be of equal length of the existing element length
print(var)


# Copying
# ------------

var["D"] = var["C"][:2]  # here there should not cause any problem for length (NaN ) will be default placeholder
print(var)


# Delete
# -----------
var.pop("A")
print(var)

# or

del var["B"]
print(var)