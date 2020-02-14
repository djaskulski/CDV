library(tidyverse)
library(grid)

#dostep
sciezka <- "C:/Users/DJaskulski/Desktop/CDV_R_Projekt/data_GUS"
setwd(sciezka)

tabela = list.files(sciezka, pattern="*.csv")
pliki = list()

#petla do wczytywania
for (i in 1:length(tabela)){
  dane_rok <-  read.csv2(tabela[i], encoding = "UTF-8", header = FALSE)
  dane_rok <- as.data.frame(t(as.matrix(dane_rok)))
  if (i == 1){
    dane_rok <- dane_rok[-nrow(dane_rok), ]
    pliki[[i]] <- dane_rok 
  } else {
    dane_rok <- dane_rok[c(-1,-2, -nrow(dane_rok)), ]
    pliki[[i]] <- dane_rok 
  }
}

#sprzatanie
dane_glowne <- do.call(rbind, pliki) 
dane_glowne <- dane_glowne[-1,]
names(dane_glowne) <- as.matrix(dane_glowne[1, ])
dane_glowne <- dane_glowne[-1, ]
dane_glowne <- separate(data = dane_glowne, col = Nazwa, into = c("MIESIAC", "PRODUKT", "USUN1", "ROK", "USUN2"), sep = ";")
dane_glowne <- dane_glowne[,c(-3, -5)]
start <- which( colnames(dane_glowne)=="POLSKA" )
koniec <- which( colnames(dane_glowne)=="ZACHODNIOPOMORSKIE" )

for (i in start:koniec){
  dane_glowne[,i] <- as.numeric(as.character( sub(",", ".", dane_glowne[,i] ))) 
}
dane_glowne$ROK <- as.integer(dane_glowne$ROK)
dane_glowne$PRODUKT <- as.factor(dane_glowne$PRODUKT)

#srednia i odchylenie
zestaw = gather(dane_glowne, "OBSZAR", "CENA", POLSKA:ZACHODNIOPOMORSKIE)
sred_odchy <- zestaw %>% group_by(ROK, OBSZAR, PRODUKT) %>% summarise(SREDNIA = mean(CENA), ODCH = sd(CENA))

#wykres dla Polska
polska_box <- subset(zestaw, zestaw$OBSZAR == "POLSKA")
lista_polska_box <- list()

for (i in 1:length(unique(polska_box$PRODUKT))){
  podzestaw = subset(polska_box, polska_box$PRODUKT == unique(polska_box$PRODUKT)[i])
  lista_polska_box[[i]] <- ggplot(data = podzestaw, aes(x = as.factor(ROK), y = CENA)) +
    geom_boxplot() +
    labs(x = "ROK", y = "SREDNI KOSZT (zl)") +
    ggtitle(unique(polska_box$PRODUKT)[i])
} 
do.call(grid.arrange, c(lista_polska_box, ncol = 2))

#wykres dla wojewodztw
woj_polska <- subset(sred_odchy, sred_odchy$OBSZAR != "POLSKA")
lista_woj_pol <- list()

for (i in 1:length(unique(woj_polska$PRODUKT))){
  podzestaw = subset(woj_polska, woj_polska$PRODUKT == unique(woj_polska$PRODUKT)[i])
  lista_woj_pol[[i]] <- ggplot(data = podzestaw, aes(x = ROK, y = SREDNIA, color = OBSZAR)) +
    scale_x_continuous(breaks = seq(min(podzestaw$ROK), max(podzestaw$ROK), 1)) +
    geom_line() +
    geom_point() + 
    geom_errorbar(aes(ymin=SREDNIA - ODCH, ymax=SREDNIA + ODCH), width=0.2, size=0.5) +
    labs(x = "ROK", y = "SREDNI KOSZT (zl)") +
    ggtitle(unique(woj_polska$PRODUKT)[i])
} 
do.call(grid.arrange,c(lista_woj_pol, ncol = 2))
