from pyspark.sql import SparkSession
from pyspark.sql.functions import col, coalesce
spark = SparkSession.builder.master("local[*]").appName("Tic_Kids_Analise").getOrCreate()

dataset = spark.read.csv('../tratamento_dados/arquivos_gerados/dados_tic_kids_geral.csv', header=True, inferSchema=True, multiLine=True, escape='"')

# dataset.printSchema()

dataset_unificado = dataset.withColumn(
    "uso_rede_social",
    coalesce(
        col(dataset.columns[4]),
        col(dataset.columns[10]),
        col(dataset.columns[12]),
    )
)

dataset_unificado = dataset_unificado.withColumn(
    "freq_rede_social",
    coalesce(
        col(dataset.columns[5]),
        col(dataset.columns[7]),
        col(dataset.columns[11]),
        col(dataset.columns[13]),
    )
)

# dataset_unificado.select("ano", "uso_rede_social", "freq_rede_social", "Em que ano a criança/adolescente está na escola?").show(5, truncate=False)

# ensino_medio = dataset_unificado.filter(
#     col("Em que ano a criança/adolescente está na escola?").contains("Ensino Médio")
# )

# ensino_medio.select("ano", "Em que ano a criança/adolescente está na escola?", "uso_rede_social", "freq_rede_social"
# ).show(10, truncate=False)

spark.stop()