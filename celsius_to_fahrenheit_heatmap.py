import matplotlib.pyplot as plt

# September 2023 temperature data values from Athens in Celsius
celsius_temperatures = [+32, +33, +32, +28, +25, +26, +27, +27, +27, +27, +27, +29, +31, +31, +32, +33, +30, +28, +29, +31, +30, +31, +33, +32, +30, +28, +24, +25, +27, +26]

# Exercise 1: Transform temperatures from Celsius to Fahrenheit
fahrenheit_temperatures = [(temp * 1.8) + 32 for temp in celsius_temperatures]

# Exercise 2: Sort temperatures from highest to lowest and print (°C, °F) pairs
temperature_pairs = list(zip(celsius_temperatures, fahrenheit_temperatures))
sorted_temperatures = sorted(temperature_pairs, key=lambda x: x[1], reverse=True)
print("Sorted Temperatures (Highest to Lowest):")
for celsius, fahrenheit in sorted_temperatures:
    print(f"{celsius}°C, {fahrenheit}°F")

# Exercise 3: Calculate the average temperature
average_celsius = sum(celsius_temperatures) / len(celsius_temperatures)
average_fahrenheit = (average_celsius * 1.8) + 32
print(f"Average Temperature (°C): {average_celsius:.2f}°C")
print(f"Average Temperature (°F): {average_fahrenheit:.2f}°F")

# We create a heatmap using Matplotlib library.
# Dates of September
dates = ["01-9-2023", "02-9-2023", "03-9-2023", "04-9-2023", "05-9-2023",
         "06-9-2023", "07-9-2023", "08-9-2023", "09-9-2023", "10-9-2023",
         "11-9-2023", "12-9-2023", "13-9-2023", "14-9-2023", "15-9-2023",
         "16-9-2023", "17-9-2023", "18-9-2023", "19-9-2023", "20-9-2023",
         "21-9-2023", "22-9-2023", "23-9-2023", "24-9-2023", "25-9-2023",
         "26-9-2023", "27-9-2023", "28-9-2023", "29-9-2023", "30-9-2023"]

# Plotting the temperatures in a heatmap
fig, ax = plt.subplots(figsize=(18, 8))
heatmap_data = [celsius_temperatures, fahrenheit_temperatures]
im = ax.imshow(heatmap_data, cmap="YlOrRd", aspect="auto")

# Set labels and titles
ax.set_xticks(range(len(dates)))
ax.set_yticks([0, 1])
ax.set_xticklabels(dates, rotation=90, fontsize=14)
ax.set_yticklabels(["°C", "°F"])
ax.set_xlabel("Date")
ax.set_ylabel("Temperature")

# We display the values of temperature on the heatmap
for i in range(2):
    for j in range(len(dates)):
        text = ax.text(j, i, f"{heatmap_data[i][j]:.1f}", ha="center", va="center", color="black")

plt.title("Temperature Heatmap for Celsius and Fahrenheit ")
plt.tight_layout()
plt.show()