import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a DataFrame
df = pd.read_csv('/home/lasso/github/personal_py_repo/EXTRA/stravaAPI/data/my_activity_data=20240507114610.csv')


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='distance', y='total_elevation_gain', hue='start_date', palette='viridis')
plt.title('Distance vs. Total Elevation Gain')
plt.xlabel('Distance (m)')
plt.ylabel('Total Elevation Gain (m)')
plt.legend(title='Date', loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.show()

