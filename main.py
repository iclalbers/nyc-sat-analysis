# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...
# Add as many cells as you like...

at_least_80_percent = schools[schools["average_math"] >= 640]
best_math_schools = at_least_80_percent[["school_name", "average_math"]].sort_values(
    by="average_math",
    ascending=False
)

print(at_least_80_percent)

schools["total_SAT"]=schools[["average_math","average_reading","average_writing"]].sum(axis=1)
top_10_schools=schools[["school_name","total_SAT"]].sort_values(by="total_SAT", ascending=False).head(10)

print(top_10_schools)

borough_stats = schools.groupby("borough").agg(
    num_schools=("school_name", "count"),
    average_SAT=("total_SAT", "mean"),
    std_SAT=("total_SAT", "std")
).round(2)

largest_std_dev=borough_stats.sort_values("std_SAT", ascending=False).head(1).reset_index()


largest_std_dev