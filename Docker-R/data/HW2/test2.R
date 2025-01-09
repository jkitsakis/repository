
  # Gradient Descent function
  LR_GradientDescent <- function(xx, yy, r, m, b, N)
    # xx => independent values
    # yy => dependent values
    # r => learning rate
    # m => initial value of m (slope)
    # b => initial value of b (intercept)
  {
    n <- length(xx)
    # ten iterations
    for( i in 1:N )
    {
      # Predicted values
      y_pred <- m * xx + b
      
      # Calculate gradients
      grad_m <- -sum((yy - y_pred) * xx) / n
      grad_b <- -sum(yy - y_pred) / n

# Update parameters
m <- m - r * grad_m
b <- b - r * grad_b

# Calculate and store the cost (Sum Squared Error)
cost <- sum((yy - y_pred)^2) / 2

# print information
cat("\niteration = ")
print(i)
cat("cost = ")
print(round(cost,3))
cat(" slope = ")
print(round(m,3))
cat(" intercept = ")
print(round(b,3))
    }
    rval <- list("slope" = m, "intercept" = b, "cost" = cost)
    return(rval) 
  }
  # our data
  x_data <- longley$Year
  y_data <- longley$GNP
  # data scaling
  xx <- scale(x_data)
  yy <- scale(y_data)
  # Linear Regression with Gradient Descent
  lr_gd = LR_GradientDescent(xx, yy, 0.01, 1, 1, 10)
  # plot data & gradient descent line
  # Extract the slope and intercept from the results 
  slope <- lr_gd$slope 
  intercept <- lr_gd$intercept 
  
  # Predicted values based on the final slope and intercept 
  y_pred <- slope * xx + intercept 
  
  # Plot the data points 
  plot(xx, yy, main = "Linear Regression Using Gradient Descent", xlab = "Year (scaled)", ylab = "GNP (scaled)", col = "blue", pch = 16) 
  # Plot the best-fit line 
  lines(xx, y_pred, col = "red", lwd = 2)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  