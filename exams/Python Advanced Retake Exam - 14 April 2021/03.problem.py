def flights(*args):
    a = 1
    dict_flights = {}
    for i in range(0, len(args), 2):
        current = args[i]
        if current == "Finish":
            return dict_flights
        if i % 2 == 0:
            if current not in dict_flights:
                dict_flights[current] = 0
            dict_flights[current] += int(args[i + 1])
    return dict_flights






print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))