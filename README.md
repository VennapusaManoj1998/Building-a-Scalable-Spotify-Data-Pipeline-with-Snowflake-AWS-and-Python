
# SPOTIFY Data Pipeline Using SNOWFLAKE, AWS and PYTHON

In this project, I embarked on a journey to create a robust ETL (Extract, Transform, Load) pipeline that seamlessly integrates Spotify data with Snowflake and Amazon Web Services (AWS). The goal was to orchestrate a smooth flow of data from its source to a data warehouse for analysis, leveraging the power of Python, AWS Lambda, and Snowflake.

The first step was to harness the Spotify API using Python, enabling the extraction of diverse music data ranging from songs and albums to artist details. Python acted as the bridge between Spotify's vast music database and our pipeline, efficiently retrieving the required data.

Next, I leveraged AWS Lambda to store the extracted data in an S3 bucket, a scalable and secure storage solution provided by AWS. This step ensured that the raw data was safely stored and ready for further processing, laying the groundwork for the transformation phase.
The transformation stage was crucial in shaping the raw data into a structured and standardized format suitable for analysis. Another AWS Lambda function played a pivotal role here, meticulously applying transformation logic to harmonize the data, ensuring consistency and accuracy.

With the transformed data poised for its next chapter, Snowpipe, a feature of Snowflake, took center stage. Snowpipe seamlessly orchestrated the transfer of transformed data from the S3 bucket to Snowflake, a powerful data warehouse known for its scalability and performance.

In Snowflake, the transformed data awaited analysis, offering a treasure trove of insights into music trends, artist popularity, and user preferences. This final stage marked the culmination of the pipeline, showcasing the seamless integration of Spotify data with Snowflake and AWS, unlocking a world of possibilities for data-driven decision-making and analysis.



## Screenshots

![App Screenshot](https://github.com/VennapusaManoj1998/Data-Engineering/blob/main/Architecture.jpeg)

