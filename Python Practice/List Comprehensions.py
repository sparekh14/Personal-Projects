# ------------------------- READ COMMENTS ------------------------- #

class List_Comp():

    def Family(self):
        family = ["Jimi", "Hemali"]

        # This is using a simple for-loop
        l = []
        for person in family:
            l.append(person)
        print("Using for-loop: ", end="")
        print(l)

        # This will produce the same result as the for-loop, but it is done in just one line of code
        print("Using list comprehension: ", end= "")
        print([person for person in family])

    def MovieSeries(self):
        movies_ratings = {"Iron Man Movies": 7, "Thor Movies": 8, "Spider-Man Movies": 9, "Star Wars Movies": 8}

        # This is using a for-loop
        l = []
        for movie in movies_ratings:
            if movies_ratings[movie] >= 8:
                l.append(movie)
        print("Using list comprehension: ", end="")
        print(l)

        # This is using list comprehension, with a dictionary
        print([movie for movie in movies_ratings if movies_ratings[movie] >= 8])

    def Numbers(self):

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]





practice = List_Comp()

# Results in two equal lists, but with two different methods (read code)
practice.Family()

practice.MovieSeries()