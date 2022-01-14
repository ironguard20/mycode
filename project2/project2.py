#!/usr/bin/env python3
"""
Author: Robert Spring

This program takes data from the all_cars.csv (a collection of cars from autotrader),
groups the cars by Make, Model, Year, 
calculates the average price of the models
and then outputs it to group_cars.csv
"""
# import pandas
import pandas as pd

def main():

    # read csv data to pandas dataframe
    df = pd.read_csv("all_cars.csv")

    # extract relevant data to be spliced from all_cars
    data = [df["Make"], df["Model"], df["Year"], df["Price"], df["Age"]]
    headers = ["Make", "Model","Year","Price", "Age"]
    # concatenate data into new dataframe
    df2 = pd.concat(data, axis=1, keys=headers)

    # Groupby Make, Model, Year and show the average age and price for each group
    df2 = df2.groupby(['Make','Model','Year']).mean()
    # Round the data down for readability
    df2 = df2.round(2)
    # export data to csv
    df2.to_csv("grouped_cars.csv")
# call program with main
if __name__ == "__main__":
    main()
