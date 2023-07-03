# lists ,its ordered amd changeable
cars=["mercedes","Nissan","Toyota","Range"]
cars[1]="Subaru"
cars.append("nisssan")
cars.insert(2,"BMW")
cars.pop()
cars.sort()
cars.copy()
cars.count("BMW")
cars.append("nissan")
print(cars)
print(cars)

# this is a tuple
# ordered its unchangeable,cannot have the same obj
fruits=("mangoes","oranges","bananas","appples")
for x in fruits:
    print(x)
print(fruits)
# sets data structure are unodered-takes no index
countries={"Kenya","Uganda","Tanzania","Burundi","Ethiopia"}
print(countries)
# dictionaries
matunda={
    "amount":40,
    "jina":"Ndizi",
    "rangi":"yellow",
}
matunda["size"]="large"
matunda.pop("jina")
print(matunda)
