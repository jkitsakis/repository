# load and read data 
water_data  <- read.csv("datasets//Water Quality Testing.csv", header = TRUE, sep = ",")

# Inspect dataset structure
str(water_data )

#Remove the first column:
water_data_noid <- water_data[, -1]
water_data_noid