from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode_outer


spark = SparkSession.builder \
    .appName("DataFrame_Test") \
    .getOrCreate()


data_for_products = spark.createDataFrame([
    (1, 'Apple'),
    (2, 'Banana'),
    (3, 'Orange'),
    (4, 'Carrot'),
    (5, 'Lettuce'),
    (6, 'Tomato'),
    (7, 'Potato'),
    (8, 'Broccoli'),
    (9, 'Grapes'),
    (10, 'Strawberry')],
    ['id', 'product_name', ]
)


data_for_categories = spark.createDataFrame([
    (1, 'Fruits'),
    (2, 'Vegetables'),
    (3, 'Berries'),
    (4, 'Root Vegetables'),
    (5, 'Leafy Greens'),
    (6, 'Citrus Fruits'),
    (7, 'Tubers'),
    (8, 'Tree Fruits'),
    (9, 'Climbing Plants'),
    (10, 'Allium Vegetables'), ],
    ['id', 'category_name', ]
)


data = [
    (1, [1]),
    (2, [1, 8]),
    (3, [1, 6, 8]),
    (4, [2, 4]),
    (5, []),
    (6, [8]),
    (7, []),
    (8, [2]),
    (9, [3, 9]),
    (10, [3])
]


data_for_connect = spark.createDataFrame(
    data,
    ["id_product", "id_category"]
)


pairs_of_data = data_for_connect.select(
    col('id_product'),
    explode_outer(col('id_category')).alias('id_category')
)


pairs_of_data_filter = pairs_of_data.filter(
    pairs_of_data.id_category.isNotNull()
)


empty_categories = pairs_of_data.filter(
    col('id_category').isNull()
).select('id_product')

pairs_of_data_filter.show()
empty_categories.show()

spark.stop()