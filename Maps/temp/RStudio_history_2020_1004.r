residuals(lm.fit.linear) %>% hist(col = "darkgrey", main = "Histogram of linear model residuals")
legend(x = "topleft", legend = c(paste("mean =", mean(residuals(lm.fit.linear)))))
grid()
residuals(lm.fit.linear) %>% hist(col = "darkgrey", main = "Histogram of linear model residuals")
legend(x = "topleft", legend = c(paste("mean =", signif(mean(residuals(lm.fit.linear))))))
grid()
residuals(lm.fit.linear) %>% hist(col = "lightgrey", main = "Histogram of linear model residuals")
legend(x = "topleft", legend = c(paste("mean =", signif(mean(residuals(lm.fit.linear))))))
grid()
residuals(lm.fit.linear) %>% hist(col = "lightgrey", main = "Histogram of linear model residuals", xlab = "Residuals of linear model")
legend(x = "topleft", legend = c(paste("mean =", signif(mean(residuals(lm.fit.linear))))))
grid()
library(lmtest)
bptest.linear <- bptest(lm.fit.linear)
bptest.linear
summary(bptest.linear)
str(bptest.linear)
bptest.linear$statistic
bptest.linear$parameter
# Performing the auxiliary regression for the BP test
lm.fit.linear.residuals.squared <- lm(linear_model_residuals^2 ~ balance + dti + ltv + borrower_score + co_borrower_score + purpose + property_type + relocation + first_time, data = fannie_mae_training)
# Computing the test statistic
R_aux_sqrd <- summary(lm.fit.linear.residuals.squared)$r.squared
BP_test_statistic <- length(linear_model_residuals) * R_aux_sqrd
pchisq(BP_test_statistic, df = 13, lower.tail = FALSE)
# Plotting the distributions of the quantitative predictors
par(mfrow=c(2,2))
hist(fannie_mae_sample$borrower_score, xlab = "", ylab = "", main = "Borrower score histogram", col = "lightgrey")
hist(fannie_mae_sample$ltv, xlab = "", ylab = "", main = "LTV histogram")
hist(fannie_mae_sample$dti, xlab = "", ylab = "", main = "DTI histogram")
hist(fannie_mae_sample$balance, xlab = "", ylab = "", main = "Loan balance histogram")
# Plotting the distributions of the quantitative predictors
par(mfrow=c(2,2))
hist(fannie_mae_sample$borrower_score, xlab = "", ylab = "", main = "Borrower score histogram", col = "lightgrey")
hist(fannie_mae_sample$ltv, xlab = "", ylab = "", main = "LTV histogram", col = "lightgrey")
hist(fannie_mae_sample$dti, xlab = "", ylab = "", main = "DTI histogram", col = "lightgrey")
hist(fannie_mae_sample$balance, xlab = "", ylab = "", main = "Loan balance histogram", col = "lightgrey")
# Plotting the response as a function of the qualitative predictors
par(mfrow=c(2,2))
boxplot(fannie_mae_sample$interest ~ fannie_mae_sample$purpose, main = "Interest vs. loan purpose", sub = "C = Cash-out refi P = Purchase R = No-cash-out refi", col = "lightgrey"); grid()
boxplot(fannie_mae_sample$interest ~ fannie_mae_sample$property_type, main = "Interest vs. property type", sub = "SF = Single Family CO = Condo MH = Manufactured\n PU = Planned Urban Development CP = Co-op"); grid()
boxplot(fannie_mae_sample$interest ~ fannie_mae_sample$relocation, main = "Interest vs. relocation indicator"); grid()
boxplot(fannie_mae_sample$interest ~ fannie_mae_sample$first_time, main = "Interest vs. first-time buyer indicator"); grid()
# Plotting the response as a function of the qualitative predictors
par(mfrow=c(2,2))
boxplot(fannie_mae_sample$interest ~ fannie_mae_sample$purpose, main = "Interest vs. loan purpose", sub = "C = Cash-out refi P = Purchase R = No-cash-out refi", col = "lightgrey"); grid()
boxplot(fannie_mae_sample$interest ~ fannie_mae_sample$property_type, main = "Interest vs. property type", sub = "SF = Single Family CO = Condo MH = Manufactured\n PU = Planned Urban Development CP = Co-op", col = "lightgrey"); grid()
boxplot(fannie_mae_sample$interest ~ fannie_mae_sample$relocation, main = "Interest vs. relocation indicator", col = "lightgrey"); grid()
boxplot(fannie_mae_sample$interest ~ fannie_mae_sample$first_time, main = "Interest vs. first-time buyer indicator", col = "lightgrey"); grid()
# Plotting the distributions of the quantitative predictors
par(mfrow=c(2,2))
hist(fannie_mae_sample$borrower_score, xlab = "", ylab = "", main = "Borrower score histogram", col = "lightgrey"); grid()
hist(fannie_mae_sample$ltv, xlab = "", ylab = "", main = "LTV histogram", col = "lightgrey")
hist(fannie_mae_sample$dti, xlab = "", ylab = "", main = "DTI histogram", col = "lightgrey")
hist(fannie_mae_sample$balance, xlab = "", ylab = "", main = "Loan balance histogram", col = "lightgrey")
# Plotting the distributions of the quantitative predictors
par(mfrow=c(2,2))
hist(fannie_mae_sample$borrower_score, xlab = "", ylab = "", main = "Borrower score histogram", col = "lightgrey"); grid()
hist(fannie_mae_sample$ltv, xlab = "", ylab = "", main = "LTV histogram", col = "lightgrey"); grid()
hist(fannie_mae_sample$dti, xlab = "", ylab = "", main = "DTI histogram", col = "lightgrey"); grid()
hist(fannie_mae_sample$balance, xlab = "", ylab = "", main = "Loan balance histogram", col = "lightgrey"); grid()
library(caTools)
# set.seed(1000) # reproducibility
# split <- sample.split(th$Severity, SplitRatio = 0.7)
# mammo_data_train <- subset(mammo_data, split==TRUE)
# mammo_data_test <- subset(mammo_data, split==FALSE)
?sample.split
library(MASS)
data(cats)
cats
summary(cats)
thyroid <- read.csv("thyroid.dat", header = FALSE, skip = 26)
colnames(thyroid) <- c("age", "sex", "on_thyroxine", "query_on_thyroxine", "antithyroid_medication", "sick", "pregnant", "thyroid_surgery", "I131_treatment", "query_hypothyroid", "query_hyperthyroid", "lithium", "goitre", "tumor", "hypopituitary", "psych", "TSH", "T3", "TT4", "T4U", "FTI","class")
str(thyroid)
split <- sample.split(thyroid$class, SplitRatio = 0.7)
?split
data_split <- sample.split(thyroid$class, SplitRatio = 0.7)
?data_split
summary(data_split)
summary(thyroid$class)
table(thyroid$class)
thyroid_train <- subset(thyroid, split==TRUE)
table(thyroid_train$class)
6666*0.7
368*0.7
166*.7
?read.csv
thyroid <- read.csv("thyroid.dat", header = FALSE, skip = 26)
colnames(thyroid) <- c("age", "sex", "on_thyroxine", "query_on_thyroxine", "antithyroid_medication", "sick", "pregnant", "thyroid_surgery", "I131_treatment", "query_hypothyroid", "query_hyperthyroid", "lithium", "goitre", "tumor", "hypopituitary", "psych", "TSH", "T3", "TT4", "T4U", "FTI","class")
str(thyroid)
# Changle "class" to factor
thyroid$class <- factor(thyroid$class)
# Multiply "age" by 100
thyroid$age <- 100 * thyroid$age
library(caTools)
set.seed(1000) # reproducibility
split <- sample.split(thyroid$class, SplitRatio = 0.7)
thyroid_train <- subset(thyroid, split==TRUE)
thyroid_test <- subset(thyroid, split==FALSE)
library(rpart)
library(rpart.plot)
# Building a tree with a minimum of 10 observations on each leaf
thyroid_tree <- rpart(class ~ ., data = thyroid_train, control=rpart.control(minbucket=50))
prp(thyroid_tree)
# Building a tree with a minimum of 10 observations on each leaf
thyroid_tree <- rpart(class ~ ., data = thyroid_train, control=rpart.control(minbucket=10))
prp(thyroid_tree)
# Building a tree with a minimum of 10 observations on each leaf
thyroid_tree <- rpart(class ~ ., data = thyroid_train, control=rpart.control(minbucket=1))
prp(thyroid_tree)
table(thyroid$on_thyroxine)
table(thyroid$query_on_thyroxine)
table(thyroid$query_hypothyroid)
table(thyroid$query_hyperthyroid)
table(thyroid$antithyroid_medication)
table(thyroid$sick)
table(thyroid$pregnant)
table(thyroid$thyroid_surgery)
table(thyroid$I131_treatment)
table(thyroid$query_hypothyroid)
table(thyroid$query_hyperthyroid)
table(thyroid$lithium)
table(thyroid$goitre)
table(thyroid$tumor)
summary(thyroid)
thyroid <- read.csv("thyroid.dat", header = FALSE, skip = 26) # skipping the first 26 lines
colnames(thyroid) <- c("age", "sex", "on_thyroxine", "query_on_thyroxine", "antithyroid_medication", "sick", "pregnant", "thyroid_surgery", "I131_treatment", "query_hypothyroid", "query_hyperthyroid", "lithium", "goitre", "tumor", "hypopituitary", "psych", "TSH", "T3", "TT4", "T4U", "FTI","class")
str(thyroid)
# Changle "class" to factor
thyroid$class <- factor(thyroid$class)
# Multiply "age" by 100
thyroid$age <- 100 * thyroid$age
library(caTools)
set.seed(1000) # reproducibility
split <- sample.split(thyroid$class, SplitRatio = 0.7)
thyroid_train <- subset(thyroid, split==TRUE)
thyroid_test <- subset(thyroid, split==FALSE)
library(rpart)
library(rpart.plot)
# Building a tree with a minimum of 10 observations on each leaf
thyroid_tree <- rpart(class ~ ., data = thyroid_train, control=rpart.control(minbucket=1))
prp(thyroid_tree)
# Building a tree with a minimum of 10 observations on each leaf
thyroid_tree <- rpart(class ~ ., data = thyroid_train, control=rpart.control(minbucket=50))
prp(thyroid_tree)
# Generate predictions on training set
PredictCART_train = predict(thyroid_tree, type = "class")
# Confusion matrix of training set
conf_matrix_train <- table(thyroid_train$class, PredictCART_train)
conf_matrix_train
sum(diag(conf_matrix_train)) / sum(conf_matrix_train)
PredictCART_test = predict(thyroid_tree, newdata = thyroid_test, type = "class")
# Confusion matrix of test set
conf_matrix_test <- table(thyroid_test$class, PredictCART_test)
conf_matrix_test
sum(diag(conf_matrix_test)) / sum(conf_matrix_test)
library(caret)
library(e1071)
# Setting cross-validation to be 10-fold
fitControl = trainControl( method = "cv", number = 10 )
# Setting cp to .01, .02, ..., 0.5
cartGrid = expand.grid( .cp = (1:50)*0.01)
train(class ~ ., data = thyroid_train, method = "rpart", trControl = fitControl, tuneGrid = cartGrid)
thyroid_tree_cv <- rpart(class ~ ., data = thyroid_train, control=rpart.control(cp=0.03))
prp(thyroid_tree_cv)
# Generate predictions on training set
PredictCART_train_cv = predict(thyroid_tree_cv, type = "class")
# Confusion matrix of training set
conf_matrix_train_cv <- table(thyroid_train$class, PredictCART_train_cv)
conf_matrix_train_cv
# Generate predictions on training set
PredictCART_train_cv = predict(thyroid_tree_cv, type = "class")
# Confusion matrix of training set
conf_matrix_train_cv <- table(thyroid_train$class, PredictCART_train_cv)
conf_matrix_train_cv
sum(diag(conf_matrix_train_cv)) / sum(conf_matrix_train_cv)
# Generate predictions on test set using cross-validated set
PredictCART_test_cv = predict(thyroid_tree_cv, type = "class")
# Confusion matrix of training set
conf_matrix_test_cv <- table(thyroid_test$class, PredictCART_test_cv)
# Generate predictions on test set using cross-validated set
PredictCART_test_cv = predict(thyroid_tree_cv, newdat = thyroid_test, type = "class")
# Confusion matrix of training set
conf_matrix_test_cv <- table(thyroid_test$class, PredictCART_test_cv)
conf_matrix_test_cv
sum(diag(conf_matrix_test_cv)) / sum(conf_matrix_test_cv)
?plot
install.packages("jpeg")
library(jpeg)
setwd("~/")
img <- readJPEG(system.file("img", "999.jpg", package="jpeg"))
img <- readJPEG(system.file("img", "0999.jpg", package="jpeg"))
getcwd()
getwd()
img <- readJPEG(system.file("img", "0999.jpg", package="jpeg"))
img <- readJPEG(system.file("img", "0999.jpg", package="jpeg"))
img <- readJPEG(system.file("img", "0999.jpg", package="jpeg"))
?readJPEG
img <- readJPEG(system.file("img", "0999.JPG", package="jpeg"))
img <- readJPEG("0999.jpg")
str(img)
plot(img)
?clearNames
?clear
img <- readJPEG("0999_gray.jpg")
str(img)
img[1,1]
?dim
dim(img)
img[1,]
img[10,]
img[148,]
q()
setwd("~/Boricuas_NCAA/Season_Summary_2019_2020/Women/")
library(ggmap)
register_google(key = "AIzaSyDV235gPhQgTX0_uHbxgCB5JqbdQkoj_L8")
geocode("University of Florida", source = "google")
source("write_csv_files.r")
colnames()all_players
colnames(all_players)
geocode(all_players$Institution, source = "google")
x <- geocode("University of Florida", source = "google")
x
str(x)
?lines
source("./../Maps/players_propsymbols.r")
setwd("./../Maps")
source("./../Maps/players_propsymbols.r")
source("players_propsymbols.r")
pr_data_join
centroids
centroids$X
c(centroids$X, centroids$Y)
?map
?maps
?get_map
x
x[1]
get_map()
ggmap(get_map())
ggmap(get_map(zoom = 3))
ggmap(get_map(zoom = 5))
ggmap(get_map(zoom = 4))
ggmap(get_map(zoom = 4, maptype = hybrid))
ggmap(get_map(zoom = 4, maptype = "hybrid"))
ggmap(get_map(zoom = 4, maptype = "terrain-background"))
ggmap(get_map(zoom = 4, source = "osm"))
?ggmap
ggmap(get_map(zoom = 4), extent = "normal")
ggmap(get_map(zoom = 4), extent = "device")
df <- data.frame(
x = rnorm(1000, -95.36258, .2),
y = rnorm(1000,  29.76196, .2)
)
ggmap(get_map(), base_layer = ggplot(aes(x = x, y = y), data = df)) +
geom_point(colour = "red")
getwd()
source("players_propsymbols_usa.r")
pr_data_join
usa_data_join
usa_shp
pr_shp
pr_shp_pr
usa_shp
!pr_shp_pr$COUNTY
pr_shp_pr[ , !(names(pr_shp_pr) %in% c("COUNTY"))]
pr_shp_pr_2 <- pr_shp_pr[ , !(names(pr_shp_pr) %in% c("COUNTY"))]
rbind(usa_shp_mainland, pr_shp_pr_2)
pr_plus_usa rbind(usa_shp_mainland, pr_shp_pr_2)
pr_plus_usa <- rbind(usa_shp_mainland, pr_shp_pr_2)
ggplot(pr_plus_usa ) + geom_sf(color = "white", fill = "light gray")
ggplot(pr_shp_pr_2  ) + geom_sf(color = "white", fill = "light gray")
usa_shp_mainland_2 <- usa_shp[usa_shp$NAME != "Alaska" & & usa_shp$NAME != "Hawaii",]
usa_shp_mainland_2 <- usa_shp[usa_shp$NAME != "Alaska" & usa_shp$NAME != "Hawaii",]
ggplot(usa_shp_mainland_2   ) + geom_sf(color = "white", fill = "light gray")
ggplot(usa_shp_mainland_2   ) + geom_sf(color = "white", fill = "light gray") + theme_map
ggplot(usa_shp_mainland_2   ) + geom_sf(color = "white", fill = "light gray") + theme_map()
install.packages("geosphere")
lat_ca <- 39.164141
lon_ca <- -121.640625
lat_me <- 45.213004
lon_me <- -68.906250
inter <- gcIntermediate(c(lon_ca, lat_ca), c(lon_me, lat_me), n=50, addStartEnd=TRUE)
lines(inter)
inter
inter <- gcIntermediate(c(lon_ca, lat_ca), c(lon_me, lat_me), n=50, addStartEnd=TRUE)
library(geosphere)
inter <- gcIntermediate(c(lon_ca, lat_ca), c(lon_me, lat_me), n=50, addStartEnd=TRUE)
lat_ca <- 39.164141
lon_ca <- -121.640625
lat_me <- 45.213004
lon_me <- -68.906250
inter <- gcIntermediate(c(lon_ca, lat_ca), c(lon_me, lat_me), n=50, addStartEnd=TRUE)
lines(inter)
inter
ggplot(usa_shp_mainland_2   ) + geom_sf(color = "white", fill = "light gray") + theme_map() + geom_path(as.data.frame(inter))
ggplot(usa_shp_mainland_2   ) + geom_sf(color = "white", fill = "light gray") + theme_map() + geom_path(as.data.frame(inter), aes(x=lon, y=lat, group=NULL))
as.data.frame(inter)
ggplot(usa_shp_mainland_2   ) + geom_sf(color = "white", fill = "light gray") + theme_map() + geom_path(as.data.frame(inter), aes(x=lon, y=lat, group=NULL))
ggplot(usa_shp_mainland_2   ) + geom_path(as.data.frame(inter), aes(x=lon, y=lat, group=NULL))
library(maps)
?map
map("world")
map("states")
map("state")
map("usa")
map("state", add = TRUE)
help(package='maps'
)
xlim <- c(-171.738281, -56.601563)
ylim <- c(12.039321, 71.856229)
map("world", col="#f2f2f2", fill=TRUE, bg="white", lwd=0.05, xlim=xlim, ylim=ylim)
map("usa")
ggplot(usa_shp_mainland_2   ) + geom_path(as.data.frame(inter), aes(x=lon, y=lat, group=NULL))
inter
str(inter)
as.data.frame(inter)
ggplot(usa_shp_mainland_2   ) + geom_path(as.data.frame(inter), aes(x=lon, y=lat))
?geom_path
ggplot(usa_shp_mainland_2   ) + geom_path(data = as.data.frame(inter), aes(x=lon, y=lat))
ggplot(usa_shp_mainland_2   ) + geom_sf(color = "white", fill = "light gray") + theme_map() + geom_path(data = as.data.frame(inter), aes(x=lon, y=lat, group=NULL))
pr_data_join
centroids
source("arcs_map.r")
?gcIntermediate
geocode("SJU")
as.vector(geocode("SJU"))
x <- as.vector(geocode("SJU"))
x
str(x)
str(geocode("SJU"))
x <- str(geocode("SJU"))
x
x <- geocode("SJU")
x
str(x)
as.vector(x)
?as.vector
str(inter)
summary(inter)
inter$lon
inter["lon"]
inter[["lon"]]
inter[["lon"]]
inter["lon"]
?str
ls.str(inter)
names(x)
x["lon"]
names(inter)
?inter
summary(inter)
str(inter)
inter[[1]]
x <- geocode("SJU")
x[1]
x[2]
str(x[2])
str(x[1,1])
x[1,1]
x[1,2]
c(x[1,1], x[1,2])
y <- c(x[1,1], x[1,2])
y
str(y)
?geom_path
x <- seq(0.01, .99, length.out = 100)
df <- data.frame(
x = rep(x, 2),
y = c(qlogis(x), 2 * qlogis(x)),
group = rep(c("a","b"),
each = 100)
)
df
x
y
c(qlogis(x), 2 * qlogis(x))
rep(c("a","b")
)
?rep
df
names(df)
p <- ggplot(df, aes(x=x, y=y, group=group))
p
p + geom_line(linetype = 2)
p + geom_line(aes(colour = group), linetype = 2)
ggplot(df, aes(x=x, y=y, group=group))
p
source("arcs_map.r")
lat_pr <- -75.23993
lon_pr <- 39.99512
geocode("SJU")
lon_pr <- -75.23993
lat_pr <- 39.99512
inter_2 <- gcIntermediate(c(lon_ca, lat_ca), c(lon_pr, lat_pr), n=50, addStartEnd=TRUE)
p + geom_path(data = as.data.frame(inter_2), aes(x=lon, y=lat, group=NULL))
lon_pr <- 18.4278
lon_pr <- -66.0156
lat_pr <- 18.4278
inter_2 <- gcIntermediate(c(lon_ca, lat_ca), c(lon_pr, lat_pr), n=50, addStartEnd=TRUE)
p + geom_path(data = as.data.frame(inter_2), aes(x=lon, y=lat, group=NULL))
all_players$Institution_Coords <- geocode(all_players$Institution, source = "google")
all_players$Institution[1]
geocode(all_players$Institution[1])
geocode(as.character(all_players$Institution[1]))
geocode(as.character(all_players$Institution[1]), messaging = FALSE)
?geocode
all_players$Institution_Coords <- geocode(as.character(all_players$Institution), source = "google")
all_players
summary(all_players)
?geom_path
summary(df)
?left_join
getwd()
source("players_propsymbols.r")
centroids
all_players_2 <- left_join(all_players, centroids, by = c('Hometown' = 'NAME'))
all_players$Hometown <- as.character(all_players$Hometown)
all_players_2 <- left_join(all_players, centroids, by = c('Hometown' = 'NAME'))
summary(all_players_2)
all_players_2["X"]
all_players_2["X", "Y"]
all_players_2[["X", "Y"]]
all_players_2[c("X", "Y")]
summary(all_players_2)
summary(all_players)
all_players$Institution_Coords <- geocode(as.character(all_players$Institution), source = "google")
summary(all_players)
all_players_2 <- left_join(all_players, centroids, by = c('Hometown' = 'NAME'))
summary(aall_players_2)
summary(all_players_2)
all_players_2$X[1]
str(all_players_2$X[1])
lat_pr
?ggcIntermediate
?gcIntermediate
str(inter)
as.data.frame(inter)
?lapply
str(all_players_2["X", "Y"])
str(all_players_2[c("X", "Y")])
all_players_2[c("X", "Y")][1]
all_players_2[c("X", "Y")][1,]
str(all_players_2[c("X", "Y")][1,])
as.vector(all_players_2[c("X", "Y")][1,]
)
str(as.vector(all_players_2[c("X", "Y")][1,]))
?data.frame()
data.frame(c(lon_ca, lon_pr))
data.frame(c(lon_ca, lon_pr), c(lat_ca,lat_pr))
df_cg <- data.frame(c(lon_ca, lon_pr), c(lat_ca,lat_pr))
names(df_cg) <- c("lon", "lat")
df_cg
df_cg <- data.frame(c(lon_ca, lon_pr, lon_me), c(lat_ca, lat_pr, lat_me), c(lon_pr, lon_me, lon_ca), c(lat_pr, lat_me, lat_ca))
df_cg
names(df_cg) <- c("p1_lon", "p1_lat", "p2_lon", "p2_lat")
df_cg
df_cg$name <- c("CA_to_PR", "PR_to_ME", "ME_to_CAR")
df_cg$name <- c("CA_to_PR", "PR_to_ME", "ME_to_CA")
df_cg
df_cg$p1_lon[1]
str(df_cg$p1_lon[1])
?lapply
lapply(c(p1_lon, p1_lat), c(p2_lon, p2_lat), FUN = gcIntermediate
)
lapply(c(df_cg$p1_lon, df_cg$p1_lat), c(df_cg$p2_lon, df_cg$p2_lat), FUN = gcIntermediate)
gcIntermediate(c(df_cg$p1_lon, df_cg$p1_lat), c(df_cg$p2_lon, df_cg$p2_lat))
rows(df_cg)
?row
row(df_cg)
nrow(df_cg)
for (idx in 1:nrow(df_cg)) {gcIntermediate(c(df_cg$p1_lon[idx], df_cg$p1_lat[idx]), c(df_cg$p2_lon[idx], df_cg$p2_lat[idx]))}
z <- for (idx in 1:nrow(df_cg)) {gcIntermediate(c(df_cg$p1_lon[idx], df_cg$p1_lat[idx]), c(df_cg$p2_lon[idx], df_cg$p2_lat[idx]))}
z
gcIntermediate(c(df_cg$p1_lon[idx], df_cg$p1_lat[idx]), c(df_cg$p2_lon[idx], df_cg$p2_lat[idx]))
for (idx in 1:nrow(df_cg)) {1}
?for
for (idx in 1:nrow(df_cg)) 1
z <- for (idx in 1:nrow(df_cg)) 1
z
?mapply
data.frame(a = 1, b = list(c("a", "b")))
data.frame(a = 1, b = I(list(c("a", "b"))))
z <- data.frame(a = 1, b = I(list(c("a", "b"))))
z
summary(z)
z$b
str(z$b)
str(z$b[1])
str(z$b[[1])
str(z$b[[1]])
for (idx in 1:nrow(df_cg)) {print(gcIntermediate(c(df_cg$p1_lon[idx], df_cg$p1_lat[idx]), c(df_cg$p2_lon[idx], df_cg$p2_lat[idx])))}
z <- data.frame()
?rbind
for (idx in 1:nrow(df_cg)) {rbind(z, gcIntermediate(c(df_cg$p1_lon[idx], df_cg$p1_lat[idx]), c(df_cg$p2_lon[idx], df_cg$p2_lat[idx])))}
z
rbind(z, gcIntermediate(c(df_cg$p1_lon[idx], df_cg$p1_lat[idx]), c(df_cg$p2_lon[idx], df_cg$p2_lat[idx])))
z
for (idx in 1:nrow(df_cg)) {z <- rbind(z, gcIntermediate(c(df_cg$p1_lon[idx], df_cg$p1_lat[idx]), c(df_cg$p2_lon[idx], df_cg$p2_lat[idx])))}
z
df_cg
df_cg[rep(1:3, 2),]
df_cg_2 <- df_cg[rep(1:3, 50),]
summary(z)
dim(z)
df_cg_2_z <- cbind(df_cg_2, z)
dim(df_cg_2)
dim(df_cg_2_z)
p <- ggplot(usa_shp_mainland_and_pr) + geom_sf(color = "white", fill = "light gray") + theme_map()
p
p + geom_path(data = df_cg_2_z, aes(x=lon, y=lat, group=name))
savehistory("~/Boricuas_NCAA/Season_Summary_2019_2020/Maps/temp/RStudio_history_2020_1004.r")
