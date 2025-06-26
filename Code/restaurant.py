def search(query, ranking=lambda r: -r.stars):
    results = [r for r in Restaurant.all if query in r.name]
    return sorted(results, key=ranking)

class Restaurant:
    all = []
    def __init__(self, name, stars):
        self.name, self.stars = name, stars
        Restaurant.all.append(self)

    def similar(self, k, similarity):
        "Return the K most similar restaurants to SELF"
        others = list(Restaurant.all)
        others.remove(self)
        return sorted(others, key=lambda r: -similarity(self, r))[:k]

    def __repr__(self):
        return '<' + self.name + '>'

Restaurant('Thai Delight', 3)
Restaurant('Thai Basil', 5)
Restaurant("Top Dog", 1)

results = search("Thai")
for r in results:
    print(r, 'is similar to', r.similar(3))