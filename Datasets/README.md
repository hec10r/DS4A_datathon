# Data table schema

## uber_trips_2014
Trip data (pickup times, pickup coordinates, etc.) from Uber vehicles in 2014.~4.5 million rows & 4 columns.Size: ~30MB zipped, ~200MB unzipped.

### pickup_datetime:
- Type: STRING
- Description: Time of pickup (format mm/dd/yyyy hh:mm:ss and mm/dd/yy hh:mm)

### pickup_latitude:
- Type: FLOAT
- Description: Latitude coordinate of pickup location

### pickup_longitude:
- Type: FLOAT
- Description: Longitude coordinate of pickup location

### base:
- Type: STRING
- Description: Base company affiliated with the Uber ride


## uber_trips_2015
Trip data (pickup times, pickup location IDs, etc.) from Uber vehicles in 2015.~14 million rows & 4 columns.Size: ~65MB zipped, ~550MB unzipped.FieldType 

### pickup_datetime:
- Type: STRING
- Description: Time of pickup (format yyyy-mm-dd hh:mm:ss)

### pickup_location_id:
- Type: INTEGER
- Description: Taxi zone ID of pickup location

### dispatch_base:
- Type: STRING
- Description: Base company that dispatched the Uber ride

### affiliate_base:
- Type: STRING
- Description: Base company affiliated with the Uber ride


## demographics
Demographic data (population, age, income, etc.) organized alphabetically by NTA.188 rows & 33 columns. Size: ~0.1MB.

### nta_name:
- Type: STRING
- Description: Name of NTA

### borough:
- Type: STRING
- Description: Identifying code for NTA

### population:
- Type: INTEGER
- Description: Total number of people in NTA

### age brackets (14 total):
- Type: INTEGER
- Description: Number of people in given age bracket

### median_age:
- Type: FLOAT
- Description: Median age of people in NTA

### people_per_acre
- Type: INTEGER
- Description: Number of people per acre

### households:
- Type: INTEGER
- Description: Total number of households in NTA

### income brackets (10 total):
- Type: INTEGER
- Description: Number of households in given income bracket

### median_income:
- Type: INTEGER
- Description: Median household income

### mean_income:
- Type: INTEGER
- Description: Mean household income


## geographic
Data about the shape of each NTA (latitude and longitude coordinates, in order).9,302 rows & 195 columns. Size: ~4MB.

### nta_code sections (195 total):
- Type: FLOAT
-Description: Alternating longitude and latitude coordinates, in order, of the vertices of the polygon shape that define the boundaries of the given NTA code


## green_trips
Trip data (pickup/dropoff times, pickup/dropoff locations) from NYC green boro taxis. Note: in order to keep the dataset size manageable, the provided data is a 20% unbiased sample of the raw data. If using trip count metrics, remember to multiply quantities by 5 to approximate the actual data.~3.5 million rows & 9 columns. Size: ~140MB zipped, ~400MB unzipped.

### pickup_datetime:
- Type: STRING
- Description: Time of pickup (format yyyy-mm-dd hh:mm:ss)

### dropoff_datetime:
- Type: STRING
- Description: Time of dropoff (format yyyy-mm-dd hh:mm:ss)

### pickup_longitude:
- Type: FLOAT
- Description: Longitude coordinate of pickup location
### pickup_latitude:
- Type: FLOAT
- Description: Latitude coordinate of pickup location

### dropoff_longitude:
- Type: FLOAT
- Description: Longitude coordinate of dropoff location

### dropoff_latitude:
- Type: FLOAT
- Description: Latitude coordinate of dropoff location

### passenger_count:
- Type: INTEGER
- Description: Number of passengers on the ride 

### trip_distance:
- Type: FLOAT
- Description: Miles traveled during ride in miles

### total_amount:
- Type: FLOAT
- Description: Dollars spent on ride


## mta_trips
Trip data (time intervals, entries, exits, etc.) from NYC public subway turnstiles.~7.5 million rows & 10 columns. Size: ~50MB zipped, ~700MB unzipped.

### station:
- Type: STRING
- Description: Name of station

### line_name:
- Type: STRING
- Description: Name of subway 

### linedivision:
- Type: STRING
- Description: Transit company that line originally belonged to

### audit_type
- Type: STRING
- Description: Measurement type –default is “REGULAR”

### unit_id:
- Type: STRING
- Description: Unique ID of the turnstile measurement unit/device

### datetime:
- Type: STRING
- Description: Time of measurement (format mm/dd/yyyy hh:mm:ss zzz)

### new_entries:
- Type: INTEGER
- Description: Turnstile entrances in given four-hour period

### new_exits:
- Type: INTEGER
- Description: Turnstile exits in given four-hour period

### latitude:
- Type: FLOAT
- Description: Latitude coordinate of turnstile

### longitude:
- Type: FLOAT
- Description: Longitude coordinate of turnstile


## weather
Temperature and precipitation data for three areas in the NYC metropolitan area.2,190 rows & 10 columns. Size: ~0.1MB

### date:
- Type: STRING
- Description: Date of measurement (format mm/dd/yy)

### max_temp:
- Type: INTEGER
- Description: Maximum temperature in Fahrenheit

### min_temp:
- Type: INTEGER
- Description: Minimum temperature in Fahrenheit

### avg_temp:
- Type: FLOAT
- Description: Average temperature in Fahrenheit

### precipitation:
- Type: FLOAT
- Description: Total precipitation in inches when reduced to liquid form

### snowfall:
- Type: FLOAT
- Description: Total snowfall in inches

### snow_depth:
- Type: INTEGER
- Description: Depth of snow on the ground in inches

### location:
- Type: STRING
- Description: Name of area

### latitude:
- Type: FLOAT
- Description: Latitude of area

### longitude:
- Type: FLOAT
- Description: Longitude of area


## yellow_trips
Trip data (pickup/dropoff times, pickup/dropoff locations) from NYC yellow medallion taxis. 
*Note:* in order to keep the dataset size manageable, the provided data is a 5% unbiased sample of the raw data. If using trip count metrics, remember to multiply quantities by 20 to approximate the actual data.~8 million rows & 9 columns. Size: ~260MB zipped, ~800MB unzipped.

### pickup_datetime:
- Type: STRING
- Description: Time of pickup (format yyyy-mm-dd hh:mm:ss)

### dropoff_datetime:
- Type: STRING
- Description: Time of dropoff (format yyyy-mm-dd hh:mm:ss)

### pickup_longitude:
- Type: FLOAT
- Description: Longitude coordinate of pickup location

### pickup_latitude:
- Type: FLOAT
- Description: Latitude coordinate of pickup location

### dropoff_longitude:
- Type: FLOAT
- Description: Longitude coordinate of dropoff location

### dropoff_latitude:
- Type: FLOAT
- Description: Latitude coordinate of dropoff location

### passenger_count:
- Type: INTEGER
- Description: Number of passengers on the ride

### trip_distance:
- Type: FLOAT
- Description: Miles traveled during ride in miles

### total_amount:
- Type: FLOAT
- Description: Dollars spent on ride


## zones 
Information about each ride pickup zone in the NYC metropolitan area.263 rows & 5 columns. Size: ~0.1MB.

### location_id:
- Type: INTEGER
- Description: ID of zone

### borough:
- Type: STRING
- Description: Name of borough zone is located in

### zone:
- Type: STRING
- Description: Name of zone

### service_zone:
- Type: STRING
- Description: Primary car service in given zone

### nta_code:
- Type: STRING
- Description: Code of NTA that zone is located in
