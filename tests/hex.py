hexcode=input("input hexcode: ")
# Convert hex to RGB
rgb=tuple(int(hexcode[i:i+2],16) for i in (0, 2, 4))
print(rgb)