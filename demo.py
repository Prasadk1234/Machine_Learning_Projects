import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('job.csv')

prof = ProfileReport(df)
prof.to_file(output_files='output.html')