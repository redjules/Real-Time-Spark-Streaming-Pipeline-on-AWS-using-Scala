# Build a Real-Time Spark Streaming Pipeline on AWS using Scala

# Business Overview

Analyzing and measuring data as soon as it enters the database is referred to as real-time analytics.  Thus, users gain insights or may conclude as soon as data enters their system. Businesses can react quickly using real-time analytics. They can grasp opportunities and avert issues before they occur.

On the other hand, Batch-style analytics might take hours or even days to provide findings. As a result, batch analytical systems frequently produce only static insights based on lagging indications. Real-time analytics insights may help organizations stay ahead of the competition. These pipelines for streaming data generally follow a 3 step process, i.e., Ingest, Analyze and Deliver.

We aim to build a Real-Time Spark Streaming Pipeline using AWS services like AWS S3, Amazon Lambda, Amazon Kinesis Data Streams, Amazon EMR, Amazon Kinesis Firehose, and OpenSearch.  We will also use Kibana, a part of OpenSearch, for visualization.

 

# Dataset Description

This GPS trajectory information was gathered over four years by 178 users in the (Microsoft Research) Geolife project (from April 2007 to October 2011). A GPS trajectory in this collection is represented as a series of time-stamped points, each comprising latitude, longitude, and altitude information. This dataset has 17,621 trajectories totaling 1,251,654 kilometers and 48,203 hours in time.

File format:

 

PLT file fields:

Lines 1...6 are useless in this dataset and can be ignored. Points are described in the following lines, one for each line. 

Field 1: Latitude in decimal degrees.

Field 2: Longitude in decimal degrees.

Field 3: All set to 0 for this dataset.

Field 4: Altitude in feet (-777 if not valid).

Field 5: Date - number of days (with a fractional part) that have passed since 12/30/1899.

Field 6: Date as a string.

Field 7: Time as a string.

Note that fields 5, 6, and 7 represent the same date/time in this dataset. You may use either of them.

Example: 39.906631,116.385564,0,492,40097.5864583333,2009-10-11,14:04:30

 

# Tech Stack

Language: Scala, Python

Services: AWS S3, Amazon Lambda, Amazon Kinesis Data Streams, Amazon EMR, Amazon Kinesis Firehose, Amazon DynamoDB, OpenSearch, Kibana

 

# Approach

The Amazon Lambda function will stream log files into Amazon Kinesis Data Streams.

EMR will run a spark streaming job to read from Kinesis Data Streams in real-time and load data in the required format in Kinesis Firehose

Firehose is used to collect transformed data and write to OpenSearch

We use Kibana, which is part of OpenSearch, for visualization

# Architecture Diagram

![5](https://github.com/redjules/Real-Time-Spark-Streaming-Pipeline-on-AWS-using-Scala/assets/106017493/6b7c9353-9b25-44e5-a195-d1cbab4c994d)
