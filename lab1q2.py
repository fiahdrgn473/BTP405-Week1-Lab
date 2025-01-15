import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
rainfall = [ 75, 60, 100, 125, 175, 200, 225, 210, 180, 140, 90, 80 ]

plt.figure(figsize=(10,6))
plt.bar(months, rainfall, color="red", edgecolor="black")
plt.xlabel("Months")
plt.ylabel("Rainfall")
plt.title("Monthly Rainfall Districution", fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()