import csv

import matplotlib.pyplot as plt

STARTING_YEAR = 1997
data = {}
with open("guru99.com\\Co2_Emission\\data\\Emissions_full.csv", "r") as f:
    file = csv.reader(f)
    next(file)  # Skip 1st line of the table
    for row in file:
        data[row[0]] = row[1:]
    print("All data from Emissions.csv has been read into a dictionary.")


def take_user_input():
    year = int(input("Select a year to find statistics (1997-2010): "))
    if year >= STARTING_YEAR and year <= 2010:
        return year
    else:
        return None


def min_max_emission(year):
    # Substract from target year, year of the 0th element in list
    year_cell = year - STARTING_YEAR
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
    year_cell = year - STARTING_YEAR
    all_emission = 0
    for em in data:
        all_emission += float(data[em][year_cell])
    return float("{:.6f}".format(all_emission / len(data)))


def check_country_name(country):
    if country[0] == " ":
        country = country[1:]
    if not (country in data):
        print("Wrong country name")
        return "Bad_name"
    return country


def prep_data_to_visualize(country):
    """Return's tuple. [0] = years, [1] = emission, [2] = country"""
    country = check_country_name(country)
    if country == "Bad_name":
        return country
    current_year = STARTING_YEAR
    years = []
    emission = []
    for emi in data[country]:
        years.append(current_year)
        emission.append(float(emi))
        current_year += 1
    return (years, emission, country)


def draw_graph(country_1, country_2=None):
    if country_2 is None:
        country_name = country_1
        country_1 = prep_data_to_visualize(country_1)
        if country_1 == "Bad_name" or country_2 == "Bad_name":
            print(f"Wrong name of the country!")
            return
        plt.plot(country_1[0], country_1[1])
        plt.suptitle(f"Year vs Emission in {country_name}")
        plt.xlabel("Year")
        plt.ylabel(f"Emission's in {country_name}")
        plt.show()
    else:
        country_1 = prep_data_to_visualize(country_1)
        country_2 = prep_data_to_visualize(country_2)
        if country_1 == "Bad_name" or country_2 == "Bad_name":
            print(f"Wrong name of the country!")
            return
        plt.suptitle(f"Year vs Emission")
        plt.ylabel(f"Emission in {country_1[2]} and {country_2[2]}")
        plt.xlabel("Year")
        plt.plot(country_1[0], country_1[1], label=f" {country_1[2]}")
        plt.plot(country_2[0], country_2[1], label=f" {country_2[2]}")
        plt.legend()
        plt.show()


def run_app():
    year = take_user_input()
    if year is None:
        print("Sorry we don't have data for this year")
        return
    # min_em, max_em = min_max_emission(year)
    everage_em = everage_emission(year)
    minn_country, maxx_country = min_max_emission(year)
    print(
        f"In {year}, countries with minimum and maximum CO2 emission level where\
{[minn_country]} and {[maxx_country]} respectively.\
    \nAverage CO2 emission's in {year} were {everage_em}"
    )
    country_to_visualize = input("Select the country to visualize: ").title()
    draw_graph(country_to_visualize)
    pair_to_visualize = input("Write two comma-separated countries, to visualize data: ").title().split(",")
    if len(pair_to_visualize) != 2:
        draw_graph(pair_to_visualize[0])
    else:
        draw_graph(pair_to_visualize[0], pair_to_visualize[1])


run_app()
