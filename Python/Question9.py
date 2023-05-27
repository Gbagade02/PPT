import pandas as pd

data = pd.read_csv("/config/workspace/Electric_Vehicle_Population_Data.csv")

#Q1. Get all the cars and their types that do not qualify for clean alternative fuel vehicle

data["Eligibility"] = data["Clean Alternative Fuel Vehicle (CAFV) Eligibility"].astype('category')
data["Eligibility"] = data["Eligibility"].cat.codes
cars = data.loc[data["Eligibility"] != 0, ["Make", "Model"]]

#Q2. Get all TESLA cars with the model year, and model type made in Bothell City.

Tesla = data.loc[data["Make"] == "TESLA", ["Model Year", "Model", "City"]]
Tesla = Tesla.loc[Tesla["City"] == "Bothell"]

#Q3. Get all the cars that have an electric range of more than 100, and were made after 2015

High_range_cars = data.loc[data["Electric Range"] >= 100]
High_range_cars = High_range_cars.loc[High_range_cars["Model Year"] > 2015]

#Q4. Q4. Draw plots to show the distribution between city and electric vehicle type

import matplotlib.pyplot as plt
grouped_data = data.groupby(['Make', 'Electric Vehicle Type']).size().unstack()
grouped_data.plot(kind='bar', stacked=True)
plt.title('Distribution of Electric Vehicle Types by City')
plt.xlabel('City')
plt.ylabel('Count')
plt.show()