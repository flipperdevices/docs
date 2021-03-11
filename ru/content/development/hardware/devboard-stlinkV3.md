# Отладочная плата на базе ST-Link V3

![Flipper Zero Devboard with ST-Link V3](https://cdn.flipperzero.one/devboard-stlinkv3.png)

Отладочная плата для продвинутых разработчиков, которым нужна внутрисхемная отладка своих программ. Построена на базе обычного [ST-Link V3 Mini](https://www.st.com/en/development-tools/stlink-v3mini.html), **отличается только формфактором** и удобством подключения. Дополнительно на плату выведены неиспользуемые интерфейсы ST-Link и GPIO Flipper Zero.

!!! warning "Отладочная плата не нужна для прошивки Flipper Zero"
    Вы можете обновлять прошивку, разрабатывать и загружать свою прошивку во Flipper Zero по USB без отладочной платы! Отладочная плата нужна для внутрисхемной отладки запущенных программ, например через GDB, OpenOCD. Если вы точно не знаете, как ее использовать, эта плата вам не нужна.    

## Технические характеристики

* ST-Link V3 Mini для прошивки и внутрисхемной отладки
* Встроенный UART to USB, подключенный к UART Flipper Zero (GPIO 13, 14)
* Выводы неиспользуемых GPIO Flipper Zero для отладки и макетирования

## Схема и BOM

{{ altium("0ec64b13-433d-419c-8d70-d2e84bef7532") }}

## Исходники проекта в Altium Designer

[github.com/Flipper-Zero/flipperzero-devboard-stlinkv3](https://github.com/Flipper-Zero/flipperzero-devboard-stlinkv3)  
