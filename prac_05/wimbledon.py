"""
Estimate: 45 minutes
Actual:   60 minutes
read/process/display wimbledon champions data
"""

FILENAME = "wimbledon.csv"
CHAMPION_INDEX = 2
COUNTRY_INDEX = 1


def main():
    """Read and process the Wimbledon file, then display the champion counts and countries."""
    data = load_data(FILENAME)
    champion_wins, champion_countries = process_data(data)
    display_results(champion_wins, champion_countries)


def load_data(filename):
    """Read the data from the given file and return it as a list of lists."""
    with open(filename, 'r', encoding='utf-8-sig') as file:
        file.readline()  # Skip the header
        return [line.strip().split(',') for line in file]


def process_data(data):
    """process data to count champion wins and collect countries."""
    champion_to_count = {}
    countries = set()

    for line in data:
        country = line[COUNTRY_INDEX]
        champion = line[CHAMPION_INDEX]
        countries.add(country)

        # Increment champion's win count
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1

    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display the champions and their win counts, along with the countries."""
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
