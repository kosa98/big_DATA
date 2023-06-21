Блок 1

Пользовался этой инструкцией по установки спарка.
https://cyanogenmods.org/ru/how-to-install-apache-spark-in-ubuntu/

А этой по установки зеппилина.
https://орел-57.рф/pages/aadress.php?page=500

А из-за того что в новых версиях нельзяустановит два вокера и одну мастер ноду, не получилось их установить.
https://stackoverflow.com/questions/66024785/how-to-start-multiple-spark-workers-on-one-machine-in-spark-2-4


Блок 2

1) parquet читается во несколько раз быстрее cvs, а так же на 40% меньше занимает места. Но этот вывод только по конкретно этим данным или пообычным даным. Я верю, что есть вариант, когда parquet занимает не сильно меньше места.

2) е) Самый популярный язык книг Английский, потом американский английский(что тоже английский), французкий, немецкий. Это связанно с распростроаненостью языков, и с тем что что Goodreads начинала и развивалась как американсий стартап

Блок 3

На этом блоке я сгорел, так как не могу нигне не могу найти такую ошибку "pyspark.sql.utils.StreamingQueryException: Wrong basePath file:/home/kosa98/archive (1)/USER_cvs1 for the root path: file:/home/kosa98/archive (1)/USER_parquet/part-00002-a00f5c72-baaa-48e9-9fa6-a77f372a8a92-c000.snappy.parquet"
Или такую "pyspark.sql.utils.StreamingQueryException: Job aborted". Пробовал убирать Null с помощью df_user.na.drop(), но не помогло
