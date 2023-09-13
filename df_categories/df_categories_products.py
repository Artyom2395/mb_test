from pyspark.sql import SparkSession

def join_products_with_categories(products_df, categories_df):
    spark = SparkSession.builder.getOrCreate()

    # Выполняем объединение данных с помощью left outer join
    joined_df = products_df.join(
        categories_df,
        products_df["product_id"] == categories_df["product_id"],
        "left_outer"
    )

    # Отбираем необходимые столбцы и переименовываем их
    result_df = joined_df.select(
        products_df["product_name"],
        categories_df["category_name"]
    ).withColumnRenamed("product_name", "Product").withColumnRenamed("category_name", "Category")

    return result_df