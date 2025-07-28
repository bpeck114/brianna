# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.

def print_star_names():
    for name in targets:
        print(name)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_name_and_spectral_type():
    for name, info in targets.items():
        print(f"{name}: {info['Spectral Type']}")

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def stars_with_mag_gt_0_1():
    for name, info in targets.items():
        if info["Magnitude"] > 0.1:
            print(f"{name}: {info['Magnitude']}")


# 4) Look up another target, add all the necessary information to the targets list. 
targets["Altair"] = {
    "RA": "19h 50m 47.0s",
    "Dec": "+08° 52′ 06″",
    "Magnitude": 0.77,
    "Spectral Type": "A7V"
}

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# Students don't have to have this much complexity, but this is just for clarity.
def parse_dec(dec_str):
    #Convert Dec string like '+38° 47′ 01″' to float degrees
    dec_str = dec_str.replace('−', '-').replace('+', '')

    parts = dec_str.replace('°', ' ').replace('′', ' ').replace('″', ' ').split()
    degrees = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])

    sign = -1 if degrees < 0 else 1
    degrees = abs(degrees) 
    return sign * (degrees + minutes / 60 + seconds / 3600)


def find_brightest_closest_to_20():
    closest_star = None
    min_distance = float('inf')
    for name, info in targets.items():
        dec_deg = parse_dec(info["Dec"])
        distance = abs(dec_deg - 20)
        if closest_star is None or (
            distance < min_distance or (
                distance == min_distance and info["Magnitude"] < targets[closest_star]["Magnitude"]
            )
        ):
            closest_star = name
            min_distance = distance
    print(f"Closest to 20° and brightest: {closest_star} ({targets[closest_star]['Dec']}, Mag: {targets[closest_star]['Magnitude']})")

# 6) What is your favorite constellation?
# :) Orion
