import matplotlib.pyplot as plt

# Sample star data: Temperature (K) vs Luminosity (Solar units)
temperature = [30000, 10000, 7500, 6000, 5000, 3500]
luminosity = [100000, 1000, 30, 1, 0.3, 0.01]
star_names = ["O", "B", "A", "G", "K", "M"]

plt.figure(figsize=(8,6))
plt.scatter(temperature, luminosity, color='orange')

for i, name in enumerate(star_names):
    plt.text(temperature[i], luminosity[i], name)

plt.gca().invert_xaxis()  # Hot stars on left
plt.yscale('log')         # Log scale for luminosity
plt.xlabel("Temperature (K)")
plt.ylabel("Luminosity (Solar Units)")
plt.title("Hertzsprung-Russell Diagram")
plt.grid(True)
plt.show()