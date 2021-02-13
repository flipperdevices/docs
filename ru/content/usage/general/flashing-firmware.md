## Установка dfu-util

Сейчас для прошивки Flipper Zero через USB-C порт необходима утилита `dfu-util`.

Вы можете пропустить эту часть, если у вас `dfu-util` уже установлен.

### Windows

#### Подготовка
Для прошивки Flipper Zero на Windows нам понадобится программа `DfuSeDemo` и актуальная прошивка в `*.dfu` формате.

Загружаем свежую сборку `*.dfu` прошивки [здесь](https://update.flipperzero.one/master/firmware/firmware.dfu).
Загружаем DfuSeDemo с сайта [STM](https://www.st.com/en/development-tools/stsw-stm32080.html).
Это совершенно бесплатно, но необходимо зарегистрироваться в процессе загрузки.

#### Прошивка

Переводим Flipper One в режим DFU и подключаем к ПК.

В диспетчере устройств наш Flipper One отображается, как `DFU in FS Mode` и для него необходимо установить драйвер.
![](../../assets/1-win-ru-deviceManager.png)

Идём в Центр обновления Windows -> Посмотреть необязательные обновления.
![](../../assets/2-win-ru-checkingUpdate.png)

Находим драйвер `STMicroelectronics`, отмечаем галочкой и нажимаем «Загрузить».
![](../../assets/assets/3-win-ru-chooseDriver.png)

После загрузки и установки драйвера название в диспетчере устройств изменится на `STM Device in DFU Mode`.
Иногда может потребоваться перезагрузка ПК.
![](../../assets/4-win-ru-checkDevice.png)

Теперь нам необходимо установить и запустить скачанный ранее DfuSeDemo.
В окне программы вверху справа убедимся, что выбранно устройство `STM Device in DFU Mode`.
Далее в таблице выбираем раздел для установки прошивки `00  Internal Flash  256 sectors…`.
После нажимаем кнопку «Choose» внизу окна программы и выбираем скачанный файл прошивки.
![](../../assets/6-win-ru-chooseFirm.png)

Перепроверяем, что выбран раздел `00  Internal Flash  256 sectors…`, нажимаем `Upgrade` и во всплывающем окне нажимаем «Да».
![](../../assets/7-win-ru-flashFirm.png)

После появления сообщения об успешной прошивке, отключаем и перезагружаем Flipper.
![](../../assets/9-win-ru-doneReboot.png)

### macOS

Установите [Homebrew](https://brew.sh), если у вас его нет:
``` sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Установите `dfu-util`:
``` sh
brew install dfu-util
```

### Linux

Выберите ваш дистрибутив для установки из пакетного менеджера или [соберите утилиту из исходников](http://dfu-util.sourceforge.net/build.html).

=== "Ubuntu/Debian"
    ``` sh
    sudo apt-get install dfu-util
    ```
=== "Fedora"
    ``` sh
    sudo yum install dfu-util
    ```
=== "Arch"
    ``` sh
    sudo pacman -Sy dfu-util
    ```

## Прошивка

### Скачивание свежей прошивки

Кликните на картинку, чтобы скачать свежую сборку полной прошивки:
[![](https://update.flipperzero.one/latest-firmware-banner.png){: width="400"}](https://update.flipperzero.one/full_firmware_latest.bin)

### Вход в режим DFU

DFU означает Device Firmware Update.

{{ gif("/assets/how-to-dfu.mp4") }}

Чтобы войти в режим DFU:

1. Нажмите и удержите :flp-btn-left: + :flp-btn-back: как при перезагрузке, подождите секунду
2. Отпустите :flp-btn-back:, но продолжайте держать :flp-btn-left: ещё на секунду
3. Отпустите :flp-btn-left:

Дисплей погаснет, а светодиод загорится синим, что означает успешный вход в режим DFU.

Подключите ваш Flipper Zero к компьютеру с помощью USB-кабеля.

### Загрузка прошивки

Запустите эту команду в терминале, чтобы загрузить прошивку на устройство:
``` sh
dfu-util -a 0 -s 0x08000000 -D full_firmware_latest.bin
```

!!! warning "Внимание"
    При скачивании прошивки по ссылке выше вы получаете единый бинарный файл, содержащий как загрузчик, так и саму прошивку.

    Однако если вы хотите прошить файл, **не содержащий загрузчика**, используйте `0x08008000` в параметре `-s` утилиты `dfu-util`. В норме вам это не пригодится.

### Перезагрузка

После установки прошивки [перезагрузитесь](rebooting.md), чтобы выйти из режима DFU.

USB-кабель можно вытаскивать как до перезагрузки, так и после.
