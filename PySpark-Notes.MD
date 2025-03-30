# PySpark Notes
- Python Spark API to help analysing the data
- Distributed Over Multiple Machines/Nodes To execute the tasks on Large Data Sets
- Scalability,Extensibility,Availability,Resource Management etc..

## Structure Field

## How to grab the data from file
- df['age']
- df.select('age').show()
- df.createorReplaceTemplateView() `This changes the view to sql type`

## Spark Data Frame Operations
- Creating a Spark Session:
- `spark = SparkSession.Builder.master("local").appName("name").config("spark.some.config.option","some-value").getOrCreate()`

- `spark = SparkSession.Builder.remote("sc://localhost").appName("app").config("some.config.option","some-value").getOrCreate()`

- df.select(mean("Column-Name"))
- df.select(max('Volume'),Min('Volume))
- df.filter('Column-Name' < 60).count()
- df.filter(df['close']< 60).count()
- (df.filter(df['High']>80).count()/df.count()) * 100
- average functions

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
  - desc()
  - asc()
- Missing Data Frames
  - df.na.drop(how='all').show()
  - df.na.drop(thresh=2).show()
- Date and Time Stamps:
  - df.head(1)
  - dayofmonth,hour,dayofyear,month,weekofyear,format_number,date_format
  - df.select(dayofmonth(df['Date'])).show()

## Spark Streaming Platforms:(Data-Pipelines)
- 