library(ggplot2)
library(dplyr)

car_data <- data.frame(
  Horsepower = c(130, 150, 180, 200, 110, 140, 170),
  Weight = c(2100, 1950, 3050, 4000, 2700, 2900, 3200),
  ltper100km = c(8.5, 7.9, 11, 13, 9, 9.8, 12),
  Price = c(20000, 23000, 27000, 30000, 19000, 21000, 26000)
)
# Print the dataset
print(car_data)

model <- lm(Price ~ Horsepower + Weight + ltper100km, data = car_data)
summary(model)
residuals <- resid(model); round(residuals, 2)

# Predict car price for a new car with specific features
predicted_price <- predict(model, data.frame(Horsepower=170, Weight=3150, ltper100km=12))
predicted_price


ggplot(car_data, aes(x = Horsepower, y = Weight, color = Price)) +
  geom_point(size = 4) +
  scale_color_gradient(low = "blue", high = "red") +
  theme_minimal()

# ----------------- #
  
# Dataset with 2 features (x1, x2) and binary labels (y)
X <- cbind(c(0, 1, 0, 1, 1, 2), c(0, 0, 1, 1, 2, 1))
y <- c(0, 0, 0, 1, 1, 1)


# Update weights and bias function
update_w <- function(X, delta, w, b, learning_rate) {
  # Gradient for weights (one per feature)
  dw <- rep(0, ncol(X))  # Gradient for each feature's weight
  db <- 0  # Gradient for bias
  
  # Calculate the gradients
  for (i in 1:nrow(X)) {
    dw <- dw + delta[i] * X[i, ]  
    db <- db + delta[i]
  }
  
  # Update weights and bias
  w <- w + learning_rate * dw
  b <- b + learning_rate * db 
  
  return(list(w = w, b = b))
}


# Define the ReLU activation function
relu <- function(x) {
  return(pmax(0, x))
}

# Function to compute the predicted output using ReLU activation
neuron_calc <- function(x, w, b) {
  return(relu(x %*% w + b))  # safer and faster
}


# Update weights and bias function
update_w <- function(X, delta, w, b, learning_rate) {
  dw <- rep(0, ncol(X))  # Gradient for each feature
  db <- 0  # Gradient for bias
  
  for (i in 1:nrow(X)) {
    dw <- dw + delta[i] * X[i, ]         
    db <- db + delta[i]                  
  }
  
  w <- w + learning_rate * dw            
  b <- b + learning_rate * db            
  
  return(list(w = w, b = b))
}


# Initialize weights and bias
set.seed(42)
w <- matrix(runif(2, -0.1, 0.1), ncol = 1)  # Random weights for two features 
b <- runif(1, -0.1, 0.1)  # Random bias 
learning_rate <- 0.01
epochs <- 100

# Training loop
for (epoch in 1:epochs) {
  predictions <- apply(X, 1, function(row) neuron_calc(row, w, b))
  delta <- y - predictions                          
  result <- update_w(X, delta, w, b, learning_rate)  
  w <- result$w
  b <- result$b
  
  # Print values for key epochs
  if (epoch %in% c(10, 30, 90)) {
    cat("Epoch", epoch, "-> w1:", round(w[1], 3),
        "w2:", round(w[2], 3), "b:", round(b, 3), "\n")
  }
}


test_X <- cbind(1,2)  # Test point (1, 2)
prediction <- neuron_calc(test_X, w, b)
step_function(prediction)
cat("Prediction for test point (1, 2):", round(prediction,1), "\n")



