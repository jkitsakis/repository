# Install required package (run only once)
# install.packages('naivebayes')

# Load the package
library(naivebayes)

# Step 1: Select the CSV file interactively
file_path <- file.choose()  # Select 'naivebayes_data.csv'
class_data <- read.csv(file_path, header = TRUE, sep = ",")

# Step 2: Remove 'Day' column if present
class_data <- class_data[ , -1]

# Step 3: Train the Naive Bayes classifier
classifier <- naive_bayes(PlayTennis ~ ., data = class_data)

# Step 4: Create test instances

# D16: Sunny, Mild, High, Strong
test1 <- data.frame(
  Outlook = "Sunny",
  Temperature = "Mild",
  Humidity = "High",
  Wind = "Strong"
)

# Predict probabilities for D16
prediction1 <- predict(classifier, test1, type = "prob")
print("Probabilities for D16:")
print(round(prediction1, 3))  # Round to 3 decimals

# D17: Overcast, Mild, Normal, Weak
test2 <- data.frame(
  Outlook = "Overcast",
  Temperature = "Mild",
  Humidity = "Normal",
  Wind = "Weak"
)

# Predict probabilities for D17
prediction2 <- predict(classifier, test2, type = "prob")
print("Probabilities for D17:")
print(round(prediction2, 3))  # Round to 3 decimals
