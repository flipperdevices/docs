# Принципиальные схемы

![](https://cdn.flipperzero.one/flipperzero-pcb-names-inside.jpg)
Здесь находятся принципиальные схемы всех плат Flipper Zero. Они могут быть полезны разработчикам модулей и для низкоуровневой отладки. Схемы опубликованы как справочный материал и не являются точной производственной документацией.

!!! warning "Схемы сокращены"
    Ниже выложены **все схемы Flipper Zero**, однако у некоторых пассивных компонентов убраны номиналы. Это сделано для усложнения копирования устройства до официального релиза.

## Плата Main
![Flipper Zero Main PCB](https://cdn.flipperzero.one/flipperzero-main-pcb-preview.jpg)

### Общая схема блоков Main
Каждый блок вынесен отдельным документом ниже.
{{ altium("77b5e9f1-7fd1-47b2-879b-42631ccf1aeb") }}

### Power
Система питания всех компонентов.
{{ altium("a41279af-a514-4eef-b0e6-caffcecea7d5") }}

### Periphery
{{ altium("1c1704de-b682-4693-88e0-74342e87bb44") }}

### MCU STM32WB55
{{ altium("eb69a746-c7bf-4301-9a4b-906995425d9c") }}

### LCD Display
{{ altium("3ad3a937-2a28-4678-bfc4-36e5a1f72d8b") }}

### Sub-1 GHz CC1101 
{{ altium("c28de394-dc04-4c0d-8d9a-ba7cc9b5a9d8") }}

### Buttons
{{ altium("d0bcb592-ee4c-4912-9167-e34b86a9e4f9") }}

## Плата iButton
На плате iButton также размещены пьезодинамик и ИК-порт. 
![ibutton pcb](https://cdn.flipperzero.one/flipperzero-ibutton-pcb-preview.jpg)

{{ altium("3d9c4181-e623-4504-b520-bfef6ba96cef") }}

## Плата NFC
На плате находятся модули RFID 125 кГц и NFC.
![Flipper Zero NFC PCB](https://cdn.flipperzero.one/flipperzero-nfc-pcb-preview.jpg)

### Общая схема блоков NFC
{{ altium("da79a091-8e8b-46df-9398-45f1dfcffa6e") }}

### NFC
{{ altium("308a6997-56f9-40aa-825d-5b77a3d98f39") }}

### RFID PERIPHERY
{{ altium("06f61470-8f77-449f-8930-46659635d796") }}

### RFID_iBTN
{{ altium("bd11bd9a-85e3-4f0d-bd8e-9ed7057658b8") }}

## Антенная плата RFID
![Flipper Zero RFID Antenna PCB](https://cdn.flipperzero.one/flipperzero-antenna-pcb-preview.jpg)