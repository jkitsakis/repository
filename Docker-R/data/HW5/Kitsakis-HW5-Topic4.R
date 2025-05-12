# Aggelou-Topic4.R
# Topic 4: Multiple Regression and Neural Networks

library(ggplot2)
library(dplyr)

car_data <- data.frame(
  Horsepower = c(130, 150, 180, 200, 110, 140, 170),
  Weight = c(2100, 1950, 3050, 4000, 2700, 2900, 3200),
  ltper100km = c(8.5, 7.9, 11, 13, 9, 9.8, 12),
  Price = c(20000, 23000, 27000, 30000, 19000, 21000, 26000)
)
model <- lm(Price ~ Horsepower + Weight + ltper100km, data = car_data)
summary(model)
residuals <- resid(model); round(residuals, 2)
predict(model, data.frame(Horsepower=170, Weight=3150, ltper100km=12))

ggplot(car_data, aes(x = Horsepower, y = Weight, color = Price)) +
  geom_point(size = 4) +
  scale_color_gradient(low = "blue", high = "red") +
  theme_minimal()

relu <- function(x) pmax(0, x)
neuron_calc <- function(x, w, b) { relu(sum(x * w) + b) }
update_w <- function(X, delta, w, b, learning_rate) {
  dw <- rep(0, ncol(X)); db <- 0
  for (i in 1:nrow(X)) {
    dw <- dw + delta[i] * X[i, ]
    db <- db + delta[i]
  }
  w <- w + learning_rate * dw
  b <- b + learning_rate * db
  return(list(w = w, b = b))
}

X <- cbind(c(0,1,0,1,1,2), c(0,0,1,1,2,1))
y <- c(0, 0, 0, 1, 1, 1)
set.seed(42)
w <- runif(2, -0.1, 0.1)
b <- runif(1, -0.1, 0.1)
learning_rate <- 0.01
epochs <- 100

for (epoch in 1:epochs) {
  predictions <- apply(X, 1, function(row) neuron_calc(row, w, b))
  delta <- y - predictions
  result <- update_w(X, delta, w, b, learning_rate)
  w <- result$w
  b <- result$b
  if (epoch %in% c(10, 30, 90)) {
    cat("Epoch", epoch, "Weights:", round(w,3), "Bias:", round(b,3), "\n")
  }
}

test_X <- c(1, 2)
prediction <- neuron_calc(test_X, w, b)
step_function <- function(x) ifelse(x > 0.5, 1, 0)
cat("Prediction for test point (1, 2):", step_function(prediction), "\n")
