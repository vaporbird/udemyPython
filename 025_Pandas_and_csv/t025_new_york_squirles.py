import pandas as pd

data = pd.read_csv("./squirles_data.csv")

#fur_color = data["Primary Fur Color"]

#fur_dict = fur_color.value_counts().to_dict()
#print("\n")
#print(fur_dict)

black = len(data[data["Primary Fur Color"] == "Black"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray = len(data[data["Primary Fur Color"] == "Gray"])


print(f"Black Squrles: {black}")
print(f"Red Squirles: {red}")
print(f"Gray Squirles: {gray}")


my_data_dict = {
	"Fur Color": ["Black", "red", "Gray"],
	"Count": [black, red, gray],
}

my_df = pd.DataFrame.from_dict(my_data_dict)
print(my_df)

my_df.to_csv("my_squirel_count.csv")
