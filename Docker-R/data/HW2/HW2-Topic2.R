# load and read data 
water_data  <- read.csv("datasets//Water Quality Testing.csv", header = TRUE, sep = ",")

# Inspect dataset structure
str(water_data )

#Remove the first column:
water_data_noid <- water_data[, -1]
head(water_data_noid)

#applies mean function to the columns (2) of data frame, ignoring missing values (na.rm = TRUE)
means <- apply(water_data_noid, 2, mean, na.rm = TRUE)
#applies sd function to the columns (2) of data frame, ignoring missing values (na.rm = TRUE)
sds <- apply(water_data_noid, 2, sd, na.rm = TRUE)

print(data.frame(means, sds))

#b.	Standardize the data (z-score)
standardized_data <- scale(water_data_noid)
#extract the principal components
pca <- prcomp(standardized_data, center=TRUE, scale=TRUE)
summary(pca)

#Scree Plot and Variance
screeplot(pca, type = "lines")


# Extract principal components
pc_data <- pca$x
pc_data

# Scatter Plot PC1 vs PC2
plot(
  pc_data[, 1], pc_data[, 2],
  xlab = "Principal Component 1",
  ylab = "Principal Component 2",
  main = "Scatter Plot: PC1 vs PC2",
  col = "blue",
  pch = 19
)

# 3D Scatter Plot using the first three principal components
scatterplot3d(
  x = pc_data[, 1],  # PC1
  y = pc_data[, 2],  # PC2
  z = pc_data[, 3],  # PC3
  xlab = "Principal Component 1",
  ylab = "Principal Component 2",
  zlab = "Principal Component 3",
  main = "3D Scatter Plot: PC1, PC2, and PC3",
  color = "blue",
  pch = 19
)
