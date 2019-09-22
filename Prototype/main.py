import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter
import view

def main():
    view.create_window()

companies = pd.read_csv("fortune1000.csv", index_col = "Company")
print(companies)
companies["Profits"].plot()
plt.show()
main()