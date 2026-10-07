import matplotlib.pyplot as plt

values = [40, 30, 30]
categories = ["Python", "Java", "C++"]
colors = ["red", "blue", "green"]
explode = [0, 0, 0.1]

plt.pie(
    values,
    labels=categories,
    autopct="%1.1f%%",
    colors=colors,
    explode=explode,
    shadow=True,
    startangle=90
)

plt.title("Programming Language Usage")

plt.show()