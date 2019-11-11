# This example is to use cudf (cuda dataframe) to load csv and basic data processing 
# We will download a CSV then uses GPU to parse it into rows and columns and run calculation

import cudf, io, requests
from io import StringIO

url="https://github.com/plotly/datasets/raw/master/tips.csv"
content = requests.get(url).content.decode('utf-8')

tip_df = cudf.read_csv(StringIO(content))
tip_df['tip_percentage'] = tip_df['tip']/tip_df['total_bill']*100

# display average tip by dining party size
print(tips_df.groupby('size').tip_percentage.mean())