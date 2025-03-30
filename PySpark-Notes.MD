# PySpark Notes

## Structure Field

## How to grab the data from file
- df['age']
- df.select('age').show()
- df.createorReplaceTemplateView() `This changes the view to sql type`

## Spark Data Frame Operations
- from pyspark.sql import SparkSession
- df.filter()
- df.filter((df['close'] < 200) & (df['Open'] > 200)).show()
- df.filter().collect()
- GroupBy and Aggregate Functions
  - df.groupBy()
  - df.agg({'sales':'sum'}).show()
- How to Import functions in pyspark.sql.functions
  - average
  - stddev `standard deviation`
  - countDistinct
  - format_number('name of colum',decimal places)
  - 