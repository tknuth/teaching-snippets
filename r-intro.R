getwd()

?plot
??plot
help("[")
help.start()

objects()
?rm

x <- c(4.1, 3.2, 5.7, 4.5)
assign("x", c(4.1, 3.2, 5.7, 4.5) * 2)

1/x
x > 10
mean(x)
sqrt(x)

y <- c(1, 2)
v <- x * y

1:10
seq(-10, 10, by=.5)
seq(length=30, from=-10, by=.5)
rep(1:3, times=5)
rep(1:3, each=5)

z <- c(x, NA)
is.na(z)

z[!is.na(z)]

x == v
any(x == v)
all(x == v)

as.integer(v)
round(v)
as.character(v)

trees
trees$Girth

attach(trees)
Girth
detach()
Girth

fruit <- c(1, 2, 3)
names(fruit) <- c("apple", "banana", "grapefruit")
barplot(fruit, 1)

n <- 50
x <- 1:n
y <- 1:n + rnorm(n, sd=5)

plot(x, y, "p")
plot(x, y, pch=19)
plot(x, y, "l")

plot(x, y)
lines(x, y, col="orange")
points(x, y, pch=19)

plot(x, y, "l", col="orange")
points(x, y, pch=21, bg="white")

plot(x, y)
for (i in -5:5) {
  if (i %% 2) {
    abline(3*i, 1, col="blue", lty="dotdash")
  } else {
    abline(3*i, 1, col="red", lty="dashed")
  }
}

