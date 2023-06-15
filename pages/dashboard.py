import pandas as pd
import numpy as np
from raceplotly.plots import barplot

df=pd.read_csv('/fortune500.csv')
df.replace('-', np.nan, inplace=True)
df['Revenue']=df['Revenue'].astype(float)
df=df.sort_values(by='Year')

#Create bar race animation
my_raceplot = barplot(df,  item_column='Name', value_column='Revenue', time_column='Year',top_entries=10)
fig=my_raceplot.plot(item_label = 'Top 10 Companies', value_label = 'Revenue', frame_duration = 200, date_format='%Y',orientation='horizontal')

#Add chart title, format the chart, etc.
fig.update_layout(
      title='Top 10 U.S. Companies Based on Revenue (1955-2021)',
      title_x=0.15,
      width=800,
      height=550,
      paper_bgcolor="lightgray",
      )
