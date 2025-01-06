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

# Combine PC1, PC2, and PC3 in a single pairwise plot
pairs(pc_data[, 1:3],
      main = "Pairwise Scatter Plot of PC1, PC2, and PC3",
      col = "red", pch = 19)
