# install.packages('naivebayes')

library(naivebayes)

file_path <- file.choose()  # Select 'naivebayes_data.csv'
class_data <- read.csv(file_path, header = TRUE, sep = ",")

class_data <- class_data[ , -1]

classifier <- naive_bayes(PlayTennis ~ ., data = class_data)

test1 <- data.frame(
  Outlook = "Sunny",
  Temperature = "Mild",
  Humidity = "High",
  Wind = "Strong"
)

prediction1 <- predict(classifier, test1, type = "prob")
print("Probabilities for D16:")
print(round(prediction1, 3))  

test2 <- data.frame(
  Outlook = "Overcast",
  Temperature = "Mild",
  Humidity = "Normal",
  Wind = "Weak"
)

prediction2 <- predict(classifier, test2, type = "prob")
print("Probabilities for D17:")
print(round(prediction2, 3))  # Round to 3 decimals
