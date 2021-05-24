import csv

data = {}
with open("guru99.com\\Co2_Emission\\data\\Emissions_full.csv", "r") as f:
    file = csv.reader(f)
    next(file)  # Skip 1st line of the table
    for row in file:
        data[row[0]] = row[1:]
    print("All data from Emissions.csv has been read into a dictionary.")


def take_user_input():
    year = int(input("Select a year to find statistics (1997-2010): "))
    if year >= 1997 and year <= 2010:
        return year
    else:
        return None


def min_max_emission(year):
    # Substract from target year, year of the 0th element in list
    year_cell = year - 1997
    minn = float("inf")
    maxx = float("-inf")
    minn_country = ""
    maxx_country = ""

    for country, emission in data.items():
        emi = float(emission[year_cell])
        if emi <= minn:
            minn = emi
            minn_country = country
        elif emi >= maxx:
            maxx = emi
            maxx_country = country
    return (minn_country, maxx_country)


def everage_emission(year):
    year_cell = year - 1997
    all_emission = 0
    for em in data:
        all_emission += float(data[em][year_cell])
    return float("{:.6f}".format(all_emission / len(data)))


def run_app():
    year = take_user_input()
    if year is None:
        print("Sorry we don't have data for this year")
        return
    # min_em, max_em = min_max_emission(year)
    everage_em = everage_emission(year)
    minn_country, maxx_country = min_max_emission(year)
    print(
        f"In {year}, countries with minimum and maximum CO2 emission level where {[minn_country]} and {[maxx_country]} respectively.\
\nAverage CO2 emission's in {year} were {everage_em}"
    )


run_app()
