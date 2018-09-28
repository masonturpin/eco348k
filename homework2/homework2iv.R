data <- read.csv("data/CARD.csv", stringsAsFactors = FALSE)
data$exper2 <- data$exper^2

model <- lm(lwage ~ educ + exper + exper2 + black + smsa + south, data)
summary(model)

first_stage <- lm(educ ~ nearc4 + exper + exper2 + black + smsa + south, data)
data$D_hat <- first_stage$fitted.values

second_stage <- lm(lwage ~ D_hat + exper + exper2 + black + smsa + south, data)
summary(second_stage)

X <- model.matrix(~ educ + exper + exper2 + black + smsa + south, data)
Z <- model.matrix(~ nearc4 + exper + exper2 + black + smsa + south, data)
Y <- data$lwage

first <- lm(X ~ Z)
X_hat <- fitted(first)
second <- lm(Y ~ X_hat)
summary(second)

library(AER)
iv <- ivreg(lwage ~ educ + exper + exper2 + black + smsa + south |. - educ + nearc4, data = data)
summary(iv)

