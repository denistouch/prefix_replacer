# replace - Программа по замене префикса в именах файлов в каталоге
Проверено на `Python 3.9.6`
## Описание
Утилита совершает поиск файлов в папке, содержащих указанный префикс в имени и заменяет его на установленное значение(по умолчанию пустая строка), 
позволяет сделать замену имени для группы файлов. 
## Сценарий использования.
Вы съездили вдвоём в отпуск и каждый из вас сделал большое количество фотографий и видео. Логично было бы предположить, что вы захотели разместить их где-то, в хронологическом порядке, чтобы удобно делиться с окружающими.
Но вот незадача, производитель вашего устройства решил, что видеофайлы будут начинаться с "VID_" а фото с "IMG_" и вы уже не можете отсортировать их по имени в каком нибудь облачном хранилище, а поставщик вашего облака совершенно не умеет в сортировку по дате создания. 
Тут то вам и поможет эта программа.
## Пример
У вас есть каталог, куда вы сохранили весь заснятый материал с вашего отпуска со всех ваших девайсов, для примера пусть он будет такой `/Users/denistouch`.
Так же вам повезло и все файлы содержат в имени дату и время съёмки, но они идут следом за каким то кодовым словом, в вашем случае это префиксы `VID_`,`IMG_` или `PANO_`
В таком случае использование программы будет выглядеть следующим образом
`python3 main.py --in=/Users/denistouch --prefix=VID_` - для переименования всех видео
`python3 main.py --in=/Users/denistouch --prefix=IMG_` - для переименования всех фото
`python3 main.py --in=/Users/denistouch --prefix=PANO_` - для переименования всех панорам
## Использование
```
usage: replace.py [-h] --in IN --prefix PREFIX [--to TO]

Программа по массовому отрезанию префикса от файлов в каталоге

optional arguments:
  -h, --help       show this help message and exit
  --in IN          Каталог в котором будет происходить переименование
  --prefix PREFIX  Префикс, который по которому будут отбираться файлы для переименования
  --to TO          Строка на которую будет заменён префикс, в переименовываемом файле
```
