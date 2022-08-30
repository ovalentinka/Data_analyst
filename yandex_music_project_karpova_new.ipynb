{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "E0vqbgi9ay0H"
   },
   "source": [
    "# Музыка больших городов"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "VUC88oWjTJw2"
   },
   "source": [
    "Сравнение Москвы и Петербурга окружено мифами. Например:\n",
    " * Москва — мегаполис, подчинённый жёсткому ритму рабочей недели;\n",
    " * Петербург — культурная столица, со своими вкусами.\n",
    "\n",
    "На данных Яндекс.Музыки мы сравним поведение пользователей двух столиц.\n",
    "\n",
    "**Цель исследования** — проверьте три гипотезы:\n",
    "1. Активность пользователей зависит от дня недели. Причём в Москве и Петербурге это проявляется по-разному.\n",
    "2. В понедельник утром в Москве преобладают одни жанры, а в Петербурге — другие. Так же и вечером пятницы преобладают разные жанры — в зависимости от города. \n",
    "3. Москва и Петербург предпочитают разные жанры музыки. В Москве чаще слушают поп-музыку, в Петербурге — русский рэп.\n",
    "\n",
    "**Ход исследования**\n",
    "\n",
    "Данные о поведении пользователей мы получили из файла `yandex_music_project.csv`. О качестве данных ничего не известно. Поэтому перед проверкой гипотез понадобится обзор данных. \n",
    "\n",
    "Мы проверим данные на ошибки и оценим их влияние на исследование. Затем, на этапе предобработки поищем возможность исправить самые критичные ошибки данных.\n",
    " \n",
    "Таким образом, исследование пройдёт в три этапа:\n",
    " 1. Обзор данных.\n",
    " 2. Предобработка данных.\n",
    " 3. Проверка гипотез.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Ml1hmfXC_Zcs"
   },
   "source": [
    "## Обзор данных\n",
    "\n",
    "Составим первое представление о данных Яндекс.Музыки.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "AXN7PHPN_Zcs"
   },
   "outputs": [],
   "source": [
    "import pandas as pd # импорт библиотеки pandas"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "SG23P8tt_Zcs"
   },
   "source": [
    "Прочитаем файл `yandex_music_project.csv` и сохраним его в переменной `df`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "id": "fFVu7vqh_Zct"
   },
   "outputs": [],
   "source": [
    "df = pd.read_csv(r'C:\\Dev\\Jupyter\\dist\\projects\\yandex_music_project.csv') # чтение файла с данными и сохранение в df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "rDoOMd3uTqnZ"
   },
   "source": [
    "Выведем на экран первые десять строк таблицы:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "id": "oWTVX3gW_Zct"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>userID</th>\n",
       "      <th>Track</th>\n",
       "      <th>artist</th>\n",
       "      <th>genre</th>\n",
       "      <th>City</th>\n",
       "      <th>time</th>\n",
       "      <th>Day</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>FFB692EC</td>\n",
       "      <td>Kamigata To Boots</td>\n",
       "      <td>The Mass Missile</td>\n",
       "      <td>rock</td>\n",
       "      <td>Saint-Petersburg</td>\n",
       "      <td>20:28:33</td>\n",
       "      <td>Wednesday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>55204538</td>\n",
       "      <td>Delayed Because of Accident</td>\n",
       "      <td>Andreas Rönnberg</td>\n",
       "      <td>rock</td>\n",
       "      <td>Moscow</td>\n",
       "      <td>14:07:09</td>\n",
       "      <td>Friday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>20EC38</td>\n",
       "      <td>Funiculì funiculà</td>\n",
       "      <td>Mario Lanza</td>\n",
       "      <td>pop</td>\n",
       "      <td>Saint-Petersburg</td>\n",
       "      <td>20:58:07</td>\n",
       "      <td>Wednesday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>A3DD03C9</td>\n",
       "      <td>Dragons in the Sunset</td>\n",
       "      <td>Fire + Ice</td>\n",
       "      <td>folk</td>\n",
       "      <td>Saint-Petersburg</td>\n",
       "      <td>08:37:09</td>\n",
       "      <td>Monday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>E2DC1FAE</td>\n",
       "      <td>Soul People</td>\n",
       "      <td>Space Echo</td>\n",
       "      <td>dance</td>\n",
       "      <td>Moscow</td>\n",
       "      <td>08:34:34</td>\n",
       "      <td>Monday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>842029A1</td>\n",
       "      <td>Преданная</td>\n",
       "      <td>IMPERVTOR</td>\n",
       "      <td>rusrap</td>\n",
       "      <td>Saint-Petersburg</td>\n",
       "      <td>13:09:41</td>\n",
       "      <td>Friday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>4CB90AA5</td>\n",
       "      <td>True</td>\n",
       "      <td>Roman Messer</td>\n",
       "      <td>dance</td>\n",
       "      <td>Moscow</td>\n",
       "      <td>13:00:07</td>\n",
       "      <td>Wednesday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>F03E1C1F</td>\n",
       "      <td>Feeling This Way</td>\n",
       "      <td>Polina Griffith</td>\n",
       "      <td>dance</td>\n",
       "      <td>Moscow</td>\n",
       "      <td>20:47:49</td>\n",
       "      <td>Wednesday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>8FA1D3BE</td>\n",
       "      <td>И вновь продолжается бой</td>\n",
       "      <td>NaN</td>\n",
       "      <td>ruspop</td>\n",
       "      <td>Moscow</td>\n",
       "      <td>09:17:40</td>\n",
       "      <td>Friday</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>E772D5C0</td>\n",
       "      <td>Pessimist</td>\n",
       "      <td>NaN</td>\n",
       "      <td>dance</td>\n",
       "      <td>Saint-Petersburg</td>\n",
       "      <td>21:20:49</td>\n",
       "      <td>Wednesday</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     userID                        Track            artist   genre  \\\n",
       "0  FFB692EC            Kamigata To Boots  The Mass Missile    rock   \n",
       "1  55204538  Delayed Because of Accident  Andreas Rönnberg    rock   \n",
       "2    20EC38            Funiculì funiculà       Mario Lanza     pop   \n",
       "3  A3DD03C9        Dragons in the Sunset        Fire + Ice    folk   \n",
       "4  E2DC1FAE                  Soul People        Space Echo   dance   \n",
       "5  842029A1                    Преданная         IMPERVTOR  rusrap   \n",
       "6  4CB90AA5                         True      Roman Messer   dance   \n",
       "7  F03E1C1F             Feeling This Way   Polina Griffith   dance   \n",
       "8  8FA1D3BE     И вновь продолжается бой               NaN  ruspop   \n",
       "9  E772D5C0                    Pessimist               NaN   dance   \n",
       "\n",
       "             City        time        Day  \n",
       "0  Saint-Petersburg  20:28:33  Wednesday  \n",
       "1            Moscow  14:07:09     Friday  \n",
       "2  Saint-Petersburg  20:58:07  Wednesday  \n",
       "3  Saint-Petersburg  08:37:09     Monday  \n",
       "4            Moscow  08:34:34     Monday  \n",
       "5  Saint-Petersburg  13:09:41     Friday  \n",
       "6            Moscow  13:00:07  Wednesday  \n",
       "7            Moscow  20:47:49  Wednesday  \n",
       "8            Moscow  09:17:40     Friday  \n",
       "9  Saint-Petersburg  21:20:49  Wednesday  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10) # получение первых 10 строк таблицы df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "EO73Kwic_Zct"
   },
   "source": [
    "Одной командой получаем общую информацию о таблице:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "id": "DSf2kIb-_Zct"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 65079 entries, 0 to 65078\n",
      "Data columns (total 7 columns):\n",
      " #   Column    Non-Null Count  Dtype \n",
      "---  ------    --------------  ----- \n",
      " 0     userID  65079 non-null  object\n",
      " 1   Track     63848 non-null  object\n",
      " 2   artist    57876 non-null  object\n",
      " 3   genre     63881 non-null  object\n",
      " 4     City    65079 non-null  object\n",
      " 5   time      65079 non-null  object\n",
      " 6   Day       65079 non-null  object\n",
      "dtypes: object(7)\n",
      "memory usage: 3.5+ MB\n"
     ]
    }
   ],
   "source": [
    "df.info()# получение общей информации о данных в таблице df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "TaQ2Iwbr_Zct"
   },
   "source": [
    "Итак, в таблице семь столбцов. Тип данных во всех столбцах — `object`.\n",
    "\n",
    "Согласно документации к данным:\n",
    "* `userID` — идентификатор пользователя;\n",
    "* `Track` — название трека;  \n",
    "* `artist` — имя исполнителя;\n",
    "* `genre` — название жанра;\n",
    "* `City` — город пользователя;\n",
    "* `time` — время начала прослушивания;\n",
    "* `Day` — день недели.\n",
    "\n",
    "В названиях колонок видны три нарушения стиля:\n",
    "1. Строчные буквы сочетаются с прописными.\n",
    "2. Встречаются пробелы.\n",
    "3. Используется CamelCase.\n",
    "\n",
    "\n",
    "\n",
    "Количество значений в столбцах различается. Значит, в данных есть пропущенные значения.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "MCB6-dXG_Zct"
   },
   "source": [
    "**Выводы**\n",
    "\n",
    "В каждой строке таблицы — данные о прослушанном треке. Часть колонок описывает саму композицию: название, исполнителя и жанр. Остальные данные рассказывают о пользователе: из какого он города, когда он слушал музыку. \n",
    "\n",
    "Предварительно можно утверждать, что, данных достаточно для проверки гипотез. Но встречаются пропуски в данных, а в названиях колонок — расхождения с хорошим стилем.\n",
    "\n",
    "Чтобы двигаться дальше, нужно устранить проблемы в данных."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "SjYF6Ub9_Zct"
   },
   "source": [
    "## Предобработка данных\n",
    "Исправим стиль в заголовках столбцов, исключим пропуски. Затем проверим данные на дубликаты."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "dIaKXr29_Zct"
   },
   "source": [
    "### Стиль заголовков\n",
    "Выведем на экран названия столбцов:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "id": "oKOTdF_Q_Zct"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['  userID', 'Track', 'artist', 'genre', '  City  ', 'time', 'Day'], dtype='object')"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns  # перечень названий столбцов таблицы df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "zj5534cv_Zct"
   },
   "source": [
    "Приведем названия в соответствие с хорошим стилем:\n",
    "* несколько слов в названии запишем в «змеином_регистре»,\n",
    "* все символы сделаем строчными,\n",
    "* устраним пробелы.\n",
    "\n",
    "Для этого переименум колонки так:\n",
    "* `'  userID'` → `'user_id'`;\n",
    "* `'Track'` → `'track'`;\n",
    "* `'  City  '` → `'city'`;\n",
    "* `'Day'` → `'day'`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "id": "ISlFqs5y_Zct"
   },
   "outputs": [],
   "source": [
    "df = df.rename(columns={'  userID':'user_id', 'Track':'track', '  City  ':'city', 'Day':'day'})# переименование столбцов"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "1dqbh00J_Zct"
   },
   "source": [
    "Проверка результата:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "id": "d4NOAmTW_Zct"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['user_id', 'track', 'artist', 'genre', 'city', 'time', 'day'], dtype='object')"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns # проверка результатов - перечень названий столбцов"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5ISfbcfY_Zct"
   },
   "source": [
    "### Пропуски значений\n",
    "Подсчитаем, сколько в таблице пропущенных значений. Для этого достаточно двух методов `pandas`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "RskX29qr_Zct"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "user_id       0\n",
       "track      1231\n",
       "artist     7203\n",
       "genre      1198\n",
       "city          0\n",
       "time          0\n",
       "day           0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isna().sum() # подсчёт пропусков"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "qubhgnlO_Zct"
   },
   "source": [
    "Не все пропущенные значения влияют на исследование. Так в `track` и `artist` пропуски не важны для нашей работы. Достаточно заменить их явными обозначениями.\n",
    "\n",
    "Но пропуски в `genre` могут помешать сравнению музыкальных вкусов в Москве и Санкт-Петербурге. На практике было бы правильно установить причину пропусков и восстановить данные. Такой возможности нет в учебном проекте. Придётся:\n",
    "* заполнить и эти пропуски явными обозначениями,\n",
    "* оценить, насколько они повредят расчётам. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "fSv2laPA_Zct"
   },
   "source": [
    "Заменим пропущенные значения в столбцах `track`, `artist` и `genre` на строку `'unknown'`. Для этого создадим список `columns_to_replace`, переберем его элементы циклом `for` и для каждого столбца выполним замену пропущенных значений:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "id": "KplB5qWs_Zct"
   },
   "outputs": [],
   "source": [
    "columns_to_replace = ['track', 'artist', 'genre'] # создаем список столбцов, пропущенные значения которых будут обновлены\n",
    "\n",
    "for colunm in columns_to_replace:\n",
    "    df[colunm] = df[colunm].fillna('unknown')# перебор названий столбцов в цикле и замена пропущенных значений на 'unknown'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Ilsm-MZo_Zct"
   },
   "source": [
    "Убеждаемся, что в таблице не осталось пропусков. Для этого ещё раз посчитаем пропущенные значения."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "id": "Tq4nYRX4_Zct"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "user_id    0\n",
       "track      0\n",
       "artist     0\n",
       "genre      0\n",
       "city       0\n",
       "time       0\n",
       "day        0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isna().sum() # подсчёт пропусков"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "BWKRtBJ3_Zct"
   },
   "source": [
    "### Дубликаты\n",
    "Считаем явные дубликаты в таблице одной командой:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "id": "36eES_S0_Zct"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3826"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum() # подсчёт явных дубликатов"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Ot25h6XR_Zct"
   },
   "source": [
    "Вызываем специальный метод `pandas`, чтобы удалить явные дубликаты:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "id": "exFHq6tt_Zct"
   },
   "outputs": [],
   "source": [
    "df = df.drop_duplicates().reset_index(drop=True) # удаление явных дубликатов (с удалением старых индексов и формированием новых)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Im2YwBEG_Zct"
   },
   "source": [
    "Ещё раз считаем явные дубликаты в таблице и убеждаемся, что полностью от них избавились:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "id": "-8PuNWQ0_Zct"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum() # проверка на отсутствие дубликатов"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "QlFBsxAr_Zct"
   },
   "source": [
    "Теперь избавляемся от неявных дубликатов в колонке `genre`. Например, название одного и того же жанра может быть записано немного по-разному. Такие ошибки тоже повлияют на результат исследования."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "eSjWwsOh_Zct"
   },
   "source": [
    "Выведим на экран список уникальных названий жанров, отсортированный в алфавитном порядке. Для этого:\n",
    "* извлекаем нужный столбец датафрейма, \n",
    "* применим к нему метод сортировки,\n",
    "* для отсортированного столбца вызовем метод, который вернёт уникальные значения из столбца."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "id": "JIUcqzZN_Zct",
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['acid',\n",
       " 'acoustic',\n",
       " 'action',\n",
       " 'adult',\n",
       " 'africa',\n",
       " 'afrikaans',\n",
       " 'alternative',\n",
       " 'alternativepunk',\n",
       " 'ambient',\n",
       " 'americana',\n",
       " 'animated',\n",
       " 'anime',\n",
       " 'arabesk',\n",
       " 'arabic',\n",
       " 'arena',\n",
       " 'argentinetango',\n",
       " 'art',\n",
       " 'audiobook',\n",
       " 'author',\n",
       " 'avantgarde',\n",
       " 'axé',\n",
       " 'baile',\n",
       " 'balkan',\n",
       " 'beats',\n",
       " 'bigroom',\n",
       " 'black',\n",
       " 'bluegrass',\n",
       " 'blues',\n",
       " 'bollywood',\n",
       " 'bossa',\n",
       " 'brazilian',\n",
       " 'breakbeat',\n",
       " 'breaks',\n",
       " 'broadway',\n",
       " 'cantautori',\n",
       " 'cantopop',\n",
       " 'canzone',\n",
       " 'caribbean',\n",
       " 'caucasian',\n",
       " 'celtic',\n",
       " 'chamber',\n",
       " 'chanson',\n",
       " 'children',\n",
       " 'chill',\n",
       " 'chinese',\n",
       " 'choral',\n",
       " 'christian',\n",
       " 'christmas',\n",
       " 'classical',\n",
       " 'classicmetal',\n",
       " 'club',\n",
       " 'colombian',\n",
       " 'comedy',\n",
       " 'conjazz',\n",
       " 'contemporary',\n",
       " 'country',\n",
       " 'cuban',\n",
       " 'dance',\n",
       " 'dancehall',\n",
       " 'dancepop',\n",
       " 'dark',\n",
       " 'death',\n",
       " 'deep',\n",
       " 'deutschrock',\n",
       " 'deutschspr',\n",
       " 'dirty',\n",
       " 'disco',\n",
       " 'dnb',\n",
       " 'documentary',\n",
       " 'downbeat',\n",
       " 'downtempo',\n",
       " 'drum',\n",
       " 'dub',\n",
       " 'dubstep',\n",
       " 'eastern',\n",
       " 'easy',\n",
       " 'electronic',\n",
       " 'electropop',\n",
       " 'emo',\n",
       " 'entehno',\n",
       " 'epicmetal',\n",
       " 'estrada',\n",
       " 'ethnic',\n",
       " 'eurofolk',\n",
       " 'european',\n",
       " 'experimental',\n",
       " 'extrememetal',\n",
       " 'fado',\n",
       " 'fairytail',\n",
       " 'film',\n",
       " 'fitness',\n",
       " 'flamenco',\n",
       " 'folk',\n",
       " 'folklore',\n",
       " 'folkmetal',\n",
       " 'folkrock',\n",
       " 'folktronica',\n",
       " 'forró',\n",
       " 'frankreich',\n",
       " 'französisch',\n",
       " 'french',\n",
       " 'funk',\n",
       " 'future',\n",
       " 'gangsta',\n",
       " 'garage',\n",
       " 'german',\n",
       " 'ghazal',\n",
       " 'gitarre',\n",
       " 'glitch',\n",
       " 'gospel',\n",
       " 'gothic',\n",
       " 'grime',\n",
       " 'grunge',\n",
       " 'gypsy',\n",
       " 'handsup',\n",
       " \"hard'n'heavy\",\n",
       " 'hardcore',\n",
       " 'hardstyle',\n",
       " 'hardtechno',\n",
       " 'hip',\n",
       " 'hip-hop',\n",
       " 'hiphop',\n",
       " 'historisch',\n",
       " 'holiday',\n",
       " 'hop',\n",
       " 'horror',\n",
       " 'house',\n",
       " 'hymn',\n",
       " 'idm',\n",
       " 'independent',\n",
       " 'indian',\n",
       " 'indie',\n",
       " 'indipop',\n",
       " 'industrial',\n",
       " 'inspirational',\n",
       " 'instrumental',\n",
       " 'international',\n",
       " 'irish',\n",
       " 'jam',\n",
       " 'japanese',\n",
       " 'jazz',\n",
       " 'jewish',\n",
       " 'jpop',\n",
       " 'jungle',\n",
       " 'k-pop',\n",
       " 'karadeniz',\n",
       " 'karaoke',\n",
       " 'kayokyoku',\n",
       " 'korean',\n",
       " 'laiko',\n",
       " 'latin',\n",
       " 'latino',\n",
       " 'leftfield',\n",
       " 'local',\n",
       " 'lounge',\n",
       " 'loungeelectronic',\n",
       " 'lovers',\n",
       " 'malaysian',\n",
       " 'mandopop',\n",
       " 'marschmusik',\n",
       " 'meditative',\n",
       " 'mediterranean',\n",
       " 'melodic',\n",
       " 'metal',\n",
       " 'metalcore',\n",
       " 'mexican',\n",
       " 'middle',\n",
       " 'minimal',\n",
       " 'miscellaneous',\n",
       " 'modern',\n",
       " 'mood',\n",
       " 'mpb',\n",
       " 'muslim',\n",
       " 'native',\n",
       " 'neoklassik',\n",
       " 'neue',\n",
       " 'new',\n",
       " 'newage',\n",
       " 'newwave',\n",
       " 'nu',\n",
       " 'nujazz',\n",
       " 'numetal',\n",
       " 'oceania',\n",
       " 'old',\n",
       " 'opera',\n",
       " 'orchestral',\n",
       " 'other',\n",
       " 'piano',\n",
       " 'podcasts',\n",
       " 'pop',\n",
       " 'popdance',\n",
       " 'popelectronic',\n",
       " 'popeurodance',\n",
       " 'poprussian',\n",
       " 'post',\n",
       " 'posthardcore',\n",
       " 'postrock',\n",
       " 'power',\n",
       " 'progmetal',\n",
       " 'progressive',\n",
       " 'psychedelic',\n",
       " 'punjabi',\n",
       " 'punk',\n",
       " 'quebecois',\n",
       " 'ragga',\n",
       " 'ram',\n",
       " 'rancheras',\n",
       " 'rap',\n",
       " 'rave',\n",
       " 'reggae',\n",
       " 'reggaeton',\n",
       " 'regional',\n",
       " 'relax',\n",
       " 'religious',\n",
       " 'retro',\n",
       " 'rhythm',\n",
       " 'rnb',\n",
       " 'rnr',\n",
       " 'rock',\n",
       " 'rockabilly',\n",
       " 'rockalternative',\n",
       " 'rockindie',\n",
       " 'rockother',\n",
       " 'romance',\n",
       " 'roots',\n",
       " 'ruspop',\n",
       " 'rusrap',\n",
       " 'rusrock',\n",
       " 'russian',\n",
       " 'salsa',\n",
       " 'samba',\n",
       " 'scenic',\n",
       " 'schlager',\n",
       " 'self',\n",
       " 'sertanejo',\n",
       " 'shanson',\n",
       " 'shoegazing',\n",
       " 'showtunes',\n",
       " 'singer',\n",
       " 'ska',\n",
       " 'skarock',\n",
       " 'slow',\n",
       " 'smooth',\n",
       " 'soft',\n",
       " 'soul',\n",
       " 'soulful',\n",
       " 'sound',\n",
       " 'soundtrack',\n",
       " 'southern',\n",
       " 'specialty',\n",
       " 'speech',\n",
       " 'spiritual',\n",
       " 'sport',\n",
       " 'stonerrock',\n",
       " 'surf',\n",
       " 'swing',\n",
       " 'synthpop',\n",
       " 'synthrock',\n",
       " 'sängerportrait',\n",
       " 'tango',\n",
       " 'tanzorchester',\n",
       " 'taraftar',\n",
       " 'tatar',\n",
       " 'tech',\n",
       " 'techno',\n",
       " 'teen',\n",
       " 'thrash',\n",
       " 'top',\n",
       " 'traditional',\n",
       " 'tradjazz',\n",
       " 'trance',\n",
       " 'tribal',\n",
       " 'trip',\n",
       " 'triphop',\n",
       " 'tropical',\n",
       " 'türk',\n",
       " 'türkçe',\n",
       " 'ukrrock',\n",
       " 'unknown',\n",
       " 'urban',\n",
       " 'uzbek',\n",
       " 'variété',\n",
       " 'vi',\n",
       " 'videogame',\n",
       " 'vocal',\n",
       " 'western',\n",
       " 'world',\n",
       " 'worldbeat',\n",
       " 'ïîï',\n",
       " 'электроника']"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted(df['genre'].unique()) # Просмотр уникальных названий жанров"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "qej-Qmuo_Zct"
   },
   "source": [
    "Видим неявные дубликаты названия `hiphop`. Это могут быть названия с ошибками или альтернативные названия того же жанра:\n",
    "* *hip*,\n",
    "* *hop*,\n",
    "* *hip-hop*.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "id": "YN5i2hpmSo09"
   },
   "outputs": [],
   "source": [
    "# Устранение неявных дубликатов\n",
    "\n",
    "df['genre'] = df['genre'].replace(['hip', 'hop', 'hip-hop'], 'hiphop')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "zQKF16_RG15m"
   },
   "source": [
    "Проверим, что заменили неправильные названия:\n",
    "\n",
    "*   hip\n",
    "*   hop\n",
    "*   hip-hop\n",
    "\n",
    "Выведем отсортированный список уникальных значений столбца `genre`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "id": "wvixALnFG15m"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['acid',\n",
       " 'acoustic',\n",
       " 'action',\n",
       " 'adult',\n",
       " 'africa',\n",
       " 'afrikaans',\n",
       " 'alternative',\n",
       " 'alternativepunk',\n",
       " 'ambient',\n",
       " 'americana',\n",
       " 'animated',\n",
       " 'anime',\n",
       " 'arabesk',\n",
       " 'arabic',\n",
       " 'arena',\n",
       " 'argentinetango',\n",
       " 'art',\n",
       " 'audiobook',\n",
       " 'author',\n",
       " 'avantgarde',\n",
       " 'axé',\n",
       " 'baile',\n",
       " 'balkan',\n",
       " 'beats',\n",
       " 'bigroom',\n",
       " 'black',\n",
       " 'bluegrass',\n",
       " 'blues',\n",
       " 'bollywood',\n",
       " 'bossa',\n",
       " 'brazilian',\n",
       " 'breakbeat',\n",
       " 'breaks',\n",
       " 'broadway',\n",
       " 'cantautori',\n",
       " 'cantopop',\n",
       " 'canzone',\n",
       " 'caribbean',\n",
       " 'caucasian',\n",
       " 'celtic',\n",
       " 'chamber',\n",
       " 'chanson',\n",
       " 'children',\n",
       " 'chill',\n",
       " 'chinese',\n",
       " 'choral',\n",
       " 'christian',\n",
       " 'christmas',\n",
       " 'classical',\n",
       " 'classicmetal',\n",
       " 'club',\n",
       " 'colombian',\n",
       " 'comedy',\n",
       " 'conjazz',\n",
       " 'contemporary',\n",
       " 'country',\n",
       " 'cuban',\n",
       " 'dance',\n",
       " 'dancehall',\n",
       " 'dancepop',\n",
       " 'dark',\n",
       " 'death',\n",
       " 'deep',\n",
       " 'deutschrock',\n",
       " 'deutschspr',\n",
       " 'dirty',\n",
       " 'disco',\n",
       " 'dnb',\n",
       " 'documentary',\n",
       " 'downbeat',\n",
       " 'downtempo',\n",
       " 'drum',\n",
       " 'dub',\n",
       " 'dubstep',\n",
       " 'eastern',\n",
       " 'easy',\n",
       " 'electronic',\n",
       " 'electropop',\n",
       " 'emo',\n",
       " 'entehno',\n",
       " 'epicmetal',\n",
       " 'estrada',\n",
       " 'ethnic',\n",
       " 'eurofolk',\n",
       " 'european',\n",
       " 'experimental',\n",
       " 'extrememetal',\n",
       " 'fado',\n",
       " 'fairytail',\n",
       " 'film',\n",
       " 'fitness',\n",
       " 'flamenco',\n",
       " 'folk',\n",
       " 'folklore',\n",
       " 'folkmetal',\n",
       " 'folkrock',\n",
       " 'folktronica',\n",
       " 'forró',\n",
       " 'frankreich',\n",
       " 'französisch',\n",
       " 'french',\n",
       " 'funk',\n",
       " 'future',\n",
       " 'gangsta',\n",
       " 'garage',\n",
       " 'german',\n",
       " 'ghazal',\n",
       " 'gitarre',\n",
       " 'glitch',\n",
       " 'gospel',\n",
       " 'gothic',\n",
       " 'grime',\n",
       " 'grunge',\n",
       " 'gypsy',\n",
       " 'handsup',\n",
       " \"hard'n'heavy\",\n",
       " 'hardcore',\n",
       " 'hardstyle',\n",
       " 'hardtechno',\n",
       " 'hiphop',\n",
       " 'historisch',\n",
       " 'holiday',\n",
       " 'horror',\n",
       " 'house',\n",
       " 'hymn',\n",
       " 'idm',\n",
       " 'independent',\n",
       " 'indian',\n",
       " 'indie',\n",
       " 'indipop',\n",
       " 'industrial',\n",
       " 'inspirational',\n",
       " 'instrumental',\n",
       " 'international',\n",
       " 'irish',\n",
       " 'jam',\n",
       " 'japanese',\n",
       " 'jazz',\n",
       " 'jewish',\n",
       " 'jpop',\n",
       " 'jungle',\n",
       " 'k-pop',\n",
       " 'karadeniz',\n",
       " 'karaoke',\n",
       " 'kayokyoku',\n",
       " 'korean',\n",
       " 'laiko',\n",
       " 'latin',\n",
       " 'latino',\n",
       " 'leftfield',\n",
       " 'local',\n",
       " 'lounge',\n",
       " 'loungeelectronic',\n",
       " 'lovers',\n",
       " 'malaysian',\n",
       " 'mandopop',\n",
       " 'marschmusik',\n",
       " 'meditative',\n",
       " 'mediterranean',\n",
       " 'melodic',\n",
       " 'metal',\n",
       " 'metalcore',\n",
       " 'mexican',\n",
       " 'middle',\n",
       " 'minimal',\n",
       " 'miscellaneous',\n",
       " 'modern',\n",
       " 'mood',\n",
       " 'mpb',\n",
       " 'muslim',\n",
       " 'native',\n",
       " 'neoklassik',\n",
       " 'neue',\n",
       " 'new',\n",
       " 'newage',\n",
       " 'newwave',\n",
       " 'nu',\n",
       " 'nujazz',\n",
       " 'numetal',\n",
       " 'oceania',\n",
       " 'old',\n",
       " 'opera',\n",
       " 'orchestral',\n",
       " 'other',\n",
       " 'piano',\n",
       " 'podcasts',\n",
       " 'pop',\n",
       " 'popdance',\n",
       " 'popelectronic',\n",
       " 'popeurodance',\n",
       " 'poprussian',\n",
       " 'post',\n",
       " 'posthardcore',\n",
       " 'postrock',\n",
       " 'power',\n",
       " 'progmetal',\n",
       " 'progressive',\n",
       " 'psychedelic',\n",
       " 'punjabi',\n",
       " 'punk',\n",
       " 'quebecois',\n",
       " 'ragga',\n",
       " 'ram',\n",
       " 'rancheras',\n",
       " 'rap',\n",
       " 'rave',\n",
       " 'reggae',\n",
       " 'reggaeton',\n",
       " 'regional',\n",
       " 'relax',\n",
       " 'religious',\n",
       " 'retro',\n",
       " 'rhythm',\n",
       " 'rnb',\n",
       " 'rnr',\n",
       " 'rock',\n",
       " 'rockabilly',\n",
       " 'rockalternative',\n",
       " 'rockindie',\n",
       " 'rockother',\n",
       " 'romance',\n",
       " 'roots',\n",
       " 'ruspop',\n",
       " 'rusrap',\n",
       " 'rusrock',\n",
       " 'russian',\n",
       " 'salsa',\n",
       " 'samba',\n",
       " 'scenic',\n",
       " 'schlager',\n",
       " 'self',\n",
       " 'sertanejo',\n",
       " 'shanson',\n",
       " 'shoegazing',\n",
       " 'showtunes',\n",
       " 'singer',\n",
       " 'ska',\n",
       " 'skarock',\n",
       " 'slow',\n",
       " 'smooth',\n",
       " 'soft',\n",
       " 'soul',\n",
       " 'soulful',\n",
       " 'sound',\n",
       " 'soundtrack',\n",
       " 'southern',\n",
       " 'specialty',\n",
       " 'speech',\n",
       " 'spiritual',\n",
       " 'sport',\n",
       " 'stonerrock',\n",
       " 'surf',\n",
       " 'swing',\n",
       " 'synthpop',\n",
       " 'synthrock',\n",
       " 'sängerportrait',\n",
       " 'tango',\n",
       " 'tanzorchester',\n",
       " 'taraftar',\n",
       " 'tatar',\n",
       " 'tech',\n",
       " 'techno',\n",
       " 'teen',\n",
       " 'thrash',\n",
       " 'top',\n",
       " 'traditional',\n",
       " 'tradjazz',\n",
       " 'trance',\n",
       " 'tribal',\n",
       " 'trip',\n",
       " 'triphop',\n",
       " 'tropical',\n",
       " 'türk',\n",
       " 'türkçe',\n",
       " 'ukrrock',\n",
       " 'unknown',\n",
       " 'urban',\n",
       " 'uzbek',\n",
       " 'variété',\n",
       " 'vi',\n",
       " 'videogame',\n",
       " 'vocal',\n",
       " 'western',\n",
       " 'world',\n",
       " 'worldbeat',\n",
       " 'ïîï',\n",
       " 'электроника']"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted(df['genre'].unique()) # Проверка на неявные дубликаты"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "jz6a9-7HQUDd"
   },
   "source": [
    "**Выводы**\n",
    "\n",
    "Предобработка обнаружила три проблемы в данных:\n",
    "\n",
    "- нарушения в стиле заголовков,\n",
    "- пропущенные значения,\n",
    "- дубликаты — явные и неявные.\n",
    "\n",
    "Мы исправили заголовки, чтобы упростить работу с таблицей. Без дубликатов исследование станет более точным.\n",
    "\n",
    "Пропущенные значения мы заменили на `'unknown'`. Ещё предстоит увидеть, не повредят ли исследованию пропуски в колонке `genre`.\n",
    "\n",
    "Теперь можно перейти к проверке гипотез. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "WttZHXH0SqKk"
   },
   "source": [
    "## Проверка гипотез"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Im936VVi_Zcu"
   },
   "source": [
    "### Сравнение поведения пользователей двух столиц"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "nwt_MuaL_Zcu"
   },
   "source": [
    "Первая гипотеза утверждает, что пользователи по-разному слушают музыку в Москве и Санкт-Петербурге. Проверим это предположение по данным о трёх днях недели — понедельнике, среде и пятнице. Для этого:\n",
    "\n",
    "* Разделим пользователей Москвы и Санкт-Петербурга\n",
    "* Сравним, сколько треков послушала каждая группа пользователей в понедельник, среду и пятницу.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "8Dw_YMmT_Zcu"
   },
   "source": [
    "Выполним каждый из расчётов по отдельности. \n",
    "\n",
    "Оценим активность пользователей в каждом городе. Сгруппируем данные по городу и посчитаем прослушивания в каждой группе.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "id": "0_Qs96oh_Zcu"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>city</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Moscow</th>\n",
       "      <td>42741</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Saint-Petersburg</th>\n",
       "      <td>18512</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  user_id\n",
       "city                     \n",
       "Moscow              42741\n",
       "Saint-Petersburg    18512"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Подсчёт прослушиваний в каждом городе\n",
    "\n",
    "city_grouping = df.groupby('city')[['user_id']].count()\n",
    "city_grouping\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "dzli3w8o_Zcu"
   },
   "source": [
    "В Москве прослушиваний больше, чем в Петербурге. Из этого не следует, что московские пользователи чаще слушают музыку. Просто самих пользователей в Москве больше.\n",
    "\n",
    "Теперь сгруппируем данные по дню недели и подсчитаем прослушивания в понедельник, среду и пятницу. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "id": "uZMKjiJz_Zcu"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>day</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Friday</th>\n",
       "      <td>21840</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Monday</th>\n",
       "      <td>21354</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Wednesday</th>\n",
       "      <td>18059</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           user_id\n",
       "day               \n",
       "Friday       21840\n",
       "Monday       21354\n",
       "Wednesday    18059"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Подсчёт прослушиваний в каждый из трёх дней\n",
    "\n",
    "city_grouping = df.groupby('day')[['user_id']].count()\n",
    "city_grouping"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "cC2tNrlL_Zcu"
   },
   "source": [
    "В среднем пользователи из двух городов менее активны по средам. Но картина может измениться, если рассмотреть каждый город в отдельности."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "POzs8bGa_Zcu"
   },
   "source": [
    "Напишем функцию, которая объединит два эти расчёта.\n",
    "\n",
    "Создаем функцию `number_tracks()`, которая посчитает прослушивания для заданного дня и города. Ей понадобятся два параметра:\n",
    "* день недели,\n",
    "* название города.\n",
    "\n",
    "В функции сохраним в переменную строки исходной таблицы, у которых значение:\n",
    "  * в колонке `day` равно параметру `day`,\n",
    "  * в колонке `city` равно параметру `city`.\n",
    "\n",
    "Для этого применим последовательную фильтрацию с логической индексацией.\n",
    "\n",
    "Затем посчитаем значения в столбце `user_id` получившейся таблицы. Результат сохраним в новую переменную. В"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "id": "Nz3GdQB1_Zcu"
   },
   "outputs": [],
   "source": [
    "# <создание функции number_tracks()>\n",
    "# Объявляется функция с двумя параметрами: day, city.\n",
    "# В переменной track_list сохраняются те строки таблицы df, для которых \n",
    "# значение в столбце 'day' равно параметру day и одновременно значение    \n",
    "# в столбце 'city' равно параметру city (используйте последовательную фильтрацию\n",
    "# с помощью логической индексации).\n",
    "# В переменной track_list_count сохраняется число значений столбца 'user_id',\n",
    "# рассчитанное методом count() для таблицы track_list.\n",
    "# Функция возвращает число - значение track_list_count.\n",
    "\n",
    "def number_tracks(day, city):\n",
    "    track_list = df[df['day'] == day]      \n",
    "    track_list = track_list[track_list['city'] == city]                                       \n",
    "    track_list_count = track_list['user_id'].count()\n",
    "    return track_list_count\n",
    "\n",
    "# Функция для подсчёта прослушиваний для конкретного города и дня.\n",
    "# С помощью последовательной фильтрации с логической индексацией она \n",
    "# сначала получит из исходной таблицы строки с нужным днём,\n",
    "# затем из результата отфильтрует строки с нужным городом,\n",
    "# методом count() посчитает количество значений в колонке user_id. \n",
    "# Это количество функция вернёт в качестве результата"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ytf7xFrFJQ2r"
   },
   "source": [
    "Вызовем `number_tracks()` шесть раз, меняя значение параметров — так, чтобы получить данные для каждого города в каждый из трёх дней."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "id": "rJcRATNQ_Zcu"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15740"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "number_tracks('Monday', 'Moscow')# количество прослушиваний в Москве по понедельникам"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "id": "hq_ncZ5T_Zcu"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5614"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "number_tracks('Monday', 'Saint-Petersburg')# количество прослушиваний в Санкт-Петербурге по понедельникам"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "id": "_NTy2VPU_Zcu"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11056"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "number_tracks('Wednesday', 'Moscow')# количество прослушиваний в Москве по средам"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "id": "j2y3TAwo_Zcu"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7003"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "number_tracks('Wednesday', 'Saint-Petersburg')# количество прослушиваний в Санкт-Петербурге по средам"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "id": "vYDw5u_K_Zcu"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15945"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "number_tracks('Friday', 'Moscow')# количество прослушиваний в Москве по пятницам"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "id": "8_yzFtW3_Zcu"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5895"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "number_tracks('Friday', 'Saint-Petersburg')# количество прослушиваний в Санкт-Петербурге по пятницам"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "7QXffbO-_Zcu"
   },
   "source": [
    "Создайем c помощью конструктора `pd.DataFrame` таблицу, где\n",
    "* названия колонок — `['city', 'monday', 'wednesday', 'friday']`;\n",
    "* данные — результаты, которые вы получили с помощью `number_tracks`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "id": "APAcLpOr_Zcu"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>city</th>\n",
       "      <th>monday</th>\n",
       "      <th>wednesday</th>\n",
       "      <th>friday</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Moscow</td>\n",
       "      <td>15740</td>\n",
       "      <td>11056</td>\n",
       "      <td>15945</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Saint-Petersburg</td>\n",
       "      <td>5614</td>\n",
       "      <td>7003</td>\n",
       "      <td>5895</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               city  monday  wednesday  friday\n",
       "0            Moscow   15740      11056   15945\n",
       "1  Saint-Petersburg    5614       7003    5895"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Таблица с результатами\n",
    "number_track_result = [['Moscow',15740,11056, 15945], # Измерения хранятся в списке списков \n",
    "              ['Saint-Petersburg',5614, 7003, 5895]]\n",
    "\n",
    "header = ['city', 'monday', 'wednesday', 'friday'] # Заголовки\n",
    "\n",
    "output = pd.DataFrame(data=number_track_result, columns=header) \n",
    "display(output)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "-EgPIHYu_Zcu"
   },
   "source": [
    "**Выводы**\n",
    "\n",
    "Данные показывают разницу поведения пользователей:\n",
    "\n",
    "- В Москве пик прослушиваний приходится на понедельник и пятницу, а в среду заметен спад.\n",
    "- В Петербурге, наоборот, больше слушают музыку по средам. Активность в понедельник и пятницу здесь почти в равной мере уступает среде.\n",
    "\n",
    "Значит, данные говорят в пользу первой гипотезы."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "atZAxtq4_Zcu"
   },
   "source": [
    "### Музыка в начале и в конце недели"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "eXrQqXFH_Zcu"
   },
   "source": [
    "Согласно второй гипотезе, утром в понедельник в Москве преобладают одни жанры, а в Петербурге — другие. Так же и вечером пятницы преобладают разные жанры — в зависимости от города."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "S8UcW6Hw_Zcu"
   },
   "source": [
    "Сохраним таблицы с данными в две переменные:\n",
    "* по Москве — в `moscow_general`;\n",
    "* по Санкт-Петербургу — в `spb_general`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "id": "qeaFfM_P_Zcu"
   },
   "outputs": [],
   "source": [
    "# получение таблицы moscow_general из тех строк таблицы df, \n",
    "# для которых значение в столбце 'city' равно 'Moscow'\n",
    "\n",
    "moscow_general = df[df['city'] == 'Moscow']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "id": "ORaVRKto_Zcu"
   },
   "outputs": [],
   "source": [
    "# получение таблицы spb_general из тех строк таблицы df,\n",
    "# для которых значение в столбце 'city' равно 'Saint-Petersburg'\n",
    "\n",
    "spb_general = df[df['city'] == 'Saint-Petersburg']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "MEJV-CX2_Zcu"
   },
   "source": [
    "Создадим функцию `genre_weekday()` с четырьмя параметрами:\n",
    "* таблица (датафрейм) с данными,\n",
    "* день недели,\n",
    "* начальная временная метка в формате 'hh:mm', \n",
    "* последняя временная метка в формате 'hh:mm'.\n",
    "\n",
    "Функция должна вернуть информацию о топ-10 жанров тех треков, которые прослушивали в указанный день, в промежутке между двумя отметками времени."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "id": "laJT9BYl_Zcu"
   },
   "outputs": [],
   "source": [
    "# Объявление функции genre_weekday() с параметрами table, day, time1, time2,\n",
    "# которая возвращает информацию о самых популярных жанрах в указанный день в\n",
    "# заданное время:\n",
    "# 1) в переменную genre_df сохраняются те строки переданного датафрейма table, для\n",
    "#    которых одновременно:\n",
    "#    - значение в столбце day равно значению аргумента day\n",
    "#    - значение в столбце time больше значения аргумента time1\n",
    "#    - значение в столбце time меньше значения аргумента time2\n",
    "#    Используйте последовательную фильтрацию с помощью логической индексации.\n",
    "# 2) сгруппировать датафрейм genre_df по столбцу genre, взять один из его\n",
    "#    столбцов и посчитать методом count() количество записей для каждого из\n",
    "#    присутствующих жанров, получившийся Series записать в переменную\n",
    "#    genre_df_count\n",
    "# 3) отсортировать genre_df_count по убыванию встречаемости и сохранить\n",
    "#    в переменную genre_df_sorted\n",
    "# 4) вернуть Series из 10 первых значений genre_df_sorted, это будут топ-10\n",
    "#    популярных жанров (в указанный день, в заданное время)\n",
    "\n",
    "def genre_weekday(table, day, time1, time2):  #1\n",
    "    \n",
    "    genre_df = table[table['day'] == day]\n",
    "    genre_df = genre_df[genre_df['time'] > time1]\n",
    "    genre_df = genre_df[genre_df['time'] < time2]\n",
    "    \n",
    "    genre_df_count = genre_df.groupby('genre')['artist'].count()  #2\n",
    "    \n",
    "    genre_df_sorted = genre_df_count.sort_values(ascending=False)  #3\n",
    "    \n",
    "    return genre_df_sorted.head(10)  #4\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "la2s2_PF_Zcu"
   },
   "source": [
    "Cравним результаты функции `genre_weekday()` для Москвы и Санкт-Петербурга в понедельник утром (с 7:00 до 11:00) и в пятницу вечером (с 17:00 до 23:00):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "id": "yz7itPUQ_Zcu"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "genre\n",
       "pop            781\n",
       "dance          549\n",
       "electronic     480\n",
       "rock           474\n",
       "hiphop         286\n",
       "ruspop         186\n",
       "world          181\n",
       "rusrap         175\n",
       "alternative    164\n",
       "unknown        161\n",
       "Name: artist, dtype: int64"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# вызов функции для утра понедельника в Москве (вместо df — таблица moscow_general)\n",
    "# объекты, хранящие время, являются строками и сравниваются как строки\n",
    "# пример вызова: genre_weekday(moscow_general, 'Monday', '07:00', '11:00')\n",
    "\n",
    "genre_weekday(moscow_general, 'Monday', '07:00', '11:00')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "id": "kwUcHPdy_Zcu"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "genre\n",
       "pop            218\n",
       "dance          182\n",
       "rock           162\n",
       "electronic     147\n",
       "hiphop          80\n",
       "ruspop          64\n",
       "alternative     58\n",
       "rusrap          55\n",
       "jazz            44\n",
       "classical       40\n",
       "Name: artist, dtype: int64"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# вызов функции для утра понедельника в Петербурге (вместо df — таблица spb_general)\n",
    "\n",
    "genre_weekday(spb_general, 'Monday', '07:00', '11:00')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "id": "EzXVRE1o_Zcu"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "genre\n",
       "pop            713\n",
       "rock           517\n",
       "dance          495\n",
       "electronic     482\n",
       "hiphop         273\n",
       "world          208\n",
       "ruspop         170\n",
       "alternative    163\n",
       "classical      163\n",
       "rusrap         142\n",
       "Name: artist, dtype: int64"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# вызов функции для вечера пятницы в Москве\n",
    "\n",
    "genre_weekday(moscow_general, 'Friday', '17:00', '23:00')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "id": "JZaEKu5v_Zcu"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "genre\n",
       "pop            256\n",
       "electronic     216\n",
       "rock           216\n",
       "dance          210\n",
       "hiphop          97\n",
       "alternative     63\n",
       "jazz            61\n",
       "classical       60\n",
       "rusrap          59\n",
       "world           54\n",
       "Name: artist, dtype: int64"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# вызов функции для вечера пятницы в Петербурге\n",
    "\n",
    "genre_weekday(spb_general, 'Friday', '17:00', '23:00')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "wrCe4MNX_Zcu"
   },
   "source": [
    "**Выводы**\n",
    "\n",
    "Если сравнить топ-10 жанров в понедельник утром, можно сделать такие выводы:\n",
    "\n",
    "1. В Москве и Петербурге слушают похожую музыку. Единственное отличие — в московский рейтинг вошёл жанр “world”, а в петербургский — джаз и классика.\n",
    "\n",
    "2. В Москве пропущенных значений оказалось так много, что значение `'unknown'` заняло десятое место среди самых популярных жанров. Значит, пропущенные значения занимают существенную долю в данных и угрожают достоверности исследования.\n",
    "\n",
    "Вечер пятницы не меняет эту картину. Некоторые жанры поднимаются немного выше, другие спускаются, но в целом топ-10 остаётся тем же самым.\n",
    "\n",
    "Таким образом, вторая гипотеза подтвердилась лишь частично:\n",
    "* Пользователи слушают похожую музыку в начале недели и в конце.\n",
    "* Разница между Москвой и Петербургом не слишком выражена. В Москве чаще слушают русскую популярную музыку, в Петербурге — джаз.\n",
    "\n",
    "Однако пропуски в данных ставят под сомнение этот результат. В Москве их так много, что рейтинг топ-10 мог бы выглядеть иначе, если бы не утерянные  данные о жанрах."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "JolODAqr_Zcu"
   },
   "source": [
    "### Жанровые предпочтения в Москве и Петербурге\n",
    "\n",
    "Гипотеза: Петербург — столица рэпа, музыку этого жанра там слушают чаще, чем в Москве.  А Москва — город контрастов, в котором, тем не менее, преобладает поп-музыка."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "DlegSvaT_Zcu"
   },
   "source": [
    "Сгруппируем таблицу `moscow_general` по жанру и посчитаем прослушивания треков каждого жанра методом `count()`. Затем отсортируем результат в порядке убывания и сохраним его в таблице `moscow_genres`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "id": "r19lIPke_Zcu"
   },
   "outputs": [],
   "source": [
    "# одной строкой: группировка таблицы moscow_general по столбцу 'genre', \n",
    "# подсчёт числа значений 'genre' в этой группировке методом count(), \n",
    "# сортировка получившегося Series в порядке убывания и сохранение в moscow_genres\n",
    "\n",
    "moscow_general = moscow_general.groupby('genre')['genre'].count().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "6kMuomxTiIr8"
   },
   "source": [
    "Выведем на экран первые десять строк `moscow_genres`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "id": "WhCSooF8_Zcv"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>genre</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>genre</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>pop</th>\n",
       "      <td>5892</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>dance</th>\n",
       "      <td>4435</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>rock</th>\n",
       "      <td>3965</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>electronic</th>\n",
       "      <td>3786</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hiphop</th>\n",
       "      <td>2096</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>classical</th>\n",
       "      <td>1616</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>world</th>\n",
       "      <td>1432</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>alternative</th>\n",
       "      <td>1379</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ruspop</th>\n",
       "      <td>1372</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>rusrap</th>\n",
       "      <td>1161</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             genre\n",
       "genre             \n",
       "pop           5892\n",
       "dance         4435\n",
       "rock          3965\n",
       "electronic    3786\n",
       "hiphop        2096\n",
       "classical     1616\n",
       "world         1432\n",
       "alternative   1379\n",
       "ruspop        1372\n",
       "rusrap        1161"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "moscow_general.to_frame().head(10) # просмотр первых 10 строк moscow_genres"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "cnPG2vnN_Zcv"
   },
   "source": [
    "Теперь повторим то же и для Петербурга.\n",
    "\n",
    "Сгруппируем таблицу `spb_general` по жанру. Посчитаем прослушивания треков каждого жанра. Результат отсортируем в порядке убывания и сохраним в таблице `spb_genres`:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "id": "gluLIpE7_Zcv"
   },
   "outputs": [],
   "source": [
    "# одной строкой: группировка таблицы spb_general по столбцу 'genre', \n",
    "# подсчёт числа значений 'genre' в этой группировке методом count(), \n",
    "# сортировка получившегося Series в порядке убывания и сохранение в spb_genres\n",
    "\n",
    "spb_general = spb_general.groupby('genre')['genre'].count().sort_values(ascending=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5Doha_ODgyQ8"
   },
   "source": [
    "Выведем на экран первые десять строк `spb_genres`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "id": "uaGJHjVU_Zcv"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>genre</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>genre</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>pop</th>\n",
       "      <td>5892</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>dance</th>\n",
       "      <td>4435</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>rock</th>\n",
       "      <td>3965</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>electronic</th>\n",
       "      <td>3786</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hiphop</th>\n",
       "      <td>2096</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>classical</th>\n",
       "      <td>1616</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>world</th>\n",
       "      <td>1432</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>alternative</th>\n",
       "      <td>1379</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ruspop</th>\n",
       "      <td>1372</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>rusrap</th>\n",
       "      <td>1161</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             genre\n",
       "genre             \n",
       "pop           5892\n",
       "dance         4435\n",
       "rock          3965\n",
       "electronic    3786\n",
       "hiphop        2096\n",
       "classical     1616\n",
       "world         1432\n",
       "alternative   1379\n",
       "ruspop        1372\n",
       "rusrap        1161"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "moscow_general.to_frame().head(10)  # просмотр первых 10 строк spb_genres"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "RY51YJYu_Zcv"
   },
   "source": [
    "**Выводы**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "nVhnJEm__Zcv"
   },
   "source": [
    "Гипотеза частично подтвердилась:\n",
    "* Поп-музыка — самый популярный жанр в Москве, как и предполагала гипотеза. Более того, в топ-10 жанров встречается близкий жанр — русская популярная музыка.\n",
    "* Вопреки ожиданиям, рэп одинаково популярен в Москве и Петербурге. \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ykKQ0N65_Zcv"
   },
   "source": [
    "## Итоги исследования"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "tjUwbHb3_Zcv"
   },
   "source": [
    "Мы проверили три гипотезы и установили:\n",
    "\n",
    "1. День недели по-разному влияет на активность пользователей в Москве и Петербурге. \n",
    "\n",
    "Первая гипотеза полностью подтвердилась.\n",
    "\n",
    "2. Музыкальные предпочтения не сильно меняются в течение недели — будь то Москва или Петербург. Небольшие различия заметны в начале недели, по понедельникам:\n",
    "* в Москве слушают музыку жанра “world”,\n",
    "* в Петербурге — джаз и классику.\n",
    "\n",
    "Таким образом, вторая гипотеза подтвердилась лишь отчасти. Этот результат мог оказаться иным, если бы не пропуски в данных.\n",
    "\n",
    "3. Во вкусах пользователей Москвы и Петербурга больше общего чем различий. Вопреки ожиданиям, предпочтения жанров в Петербурге напоминают московские.\n",
    "\n",
    "Третья гипотеза не подтвердилась. Если различия в предпочтениях и существуют, на основной массе пользователей они незаметны.\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "ExecuteTimeLog": [
   {
    "duration": 354,
    "start_time": "2022-01-30T16:36:05.029Z"
   },
   {
    "duration": 308,
    "start_time": "2022-01-30T16:36:19.337Z"
   },
   {
    "duration": 524,
    "start_time": "2022-01-30T16:37:45.850Z"
   },
   {
    "duration": 343,
    "start_time": "2022-01-30T16:38:19.745Z"
   },
   {
    "duration": 601,
    "start_time": "2022-01-30T16:39:16.539Z"
   },
   {
    "duration": 532,
    "start_time": "2022-01-30T16:39:48.258Z"
   },
   {
    "duration": 461,
    "start_time": "2022-01-30T16:40:00.498Z"
   },
   {
    "duration": 345,
    "start_time": "2022-01-30T16:44:08.982Z"
   },
   {
    "duration": 557,
    "start_time": "2022-01-30T16:44:29.753Z"
   },
   {
    "duration": 289,
    "start_time": "2022-01-30T16:45:16.782Z"
   },
   {
    "duration": 298,
    "start_time": "2022-01-30T16:45:46.533Z"
   },
   {
    "duration": 391,
    "start_time": "2022-01-30T16:48:22.163Z"
   },
   {
    "duration": 820,
    "start_time": "2022-01-30T16:48:30.101Z"
   },
   {
    "duration": 176,
    "start_time": "2022-01-30T16:48:30.923Z"
   },
   {
    "duration": 39,
    "start_time": "2022-01-30T16:48:31.102Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-30T16:48:31.144Z"
   },
   {
    "duration": 13,
    "start_time": "2022-01-30T16:48:31.150Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-30T16:48:31.166Z"
   },
   {
    "duration": 12,
    "start_time": "2022-01-30T16:48:31.176Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-30T16:48:31.192Z"
   },
   {
    "duration": 6,
    "start_time": "2022-01-30T16:48:31.203Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-30T16:48:31.212Z"
   },
   {
    "duration": 7,
    "start_time": "2022-01-30T16:48:31.235Z"
   },
   {
    "duration": 6,
    "start_time": "2022-01-30T16:48:31.244Z"
   },
   {
    "duration": 12,
    "start_time": "2022-01-30T16:48:31.252Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-30T16:48:31.266Z"
   },
   {
    "duration": 7,
    "start_time": "2022-01-30T16:48:31.277Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-30T16:48:31.286Z"
   },
   {
    "duration": 6,
    "start_time": "2022-01-30T16:48:31.297Z"
   },
   {
    "duration": 10,
    "start_time": "2022-01-30T16:48:31.305Z"
   },
   {
    "duration": 14,
    "start_time": "2022-01-30T16:48:31.333Z"
   },
   {
    "duration": 12,
    "start_time": "2022-01-30T16:48:31.349Z"
   },
   {
    "duration": 10,
    "start_time": "2022-01-30T16:48:31.363Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-30T16:48:31.376Z"
   },
   {
    "duration": 10,
    "start_time": "2022-01-30T16:48:31.401Z"
   },
   {
    "duration": 12,
    "start_time": "2022-01-30T16:48:31.414Z"
   },
   {
    "duration": 12,
    "start_time": "2022-01-30T16:48:31.429Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-30T16:48:31.443Z"
   },
   {
    "duration": 7,
    "start_time": "2022-01-30T16:48:31.454Z"
   },
   {
    "duration": 18,
    "start_time": "2022-01-30T16:48:31.464Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-30T16:48:31.485Z"
   },
   {
    "duration": 7,
    "start_time": "2022-01-30T16:48:31.495Z"
   },
   {
    "duration": 10,
    "start_time": "2022-01-30T16:48:31.505Z"
   },
   {
    "duration": 11,
    "start_time": "2022-01-30T16:48:31.517Z"
   },
   {
    "duration": 18,
    "start_time": "2022-01-30T16:48:31.533Z"
   },
   {
    "duration": 15,
    "start_time": "2022-01-30T16:48:31.554Z"
   },
   {
    "duration": 25,
    "start_time": "2022-01-30T16:48:31.571Z"
   },
   {
    "duration": 15,
    "start_time": "2022-01-30T16:48:31.599Z"
   },
   {
    "duration": 14,
    "start_time": "2022-01-30T16:48:31.617Z"
   },
   {
    "duration": 18,
    "start_time": "2022-01-30T16:48:31.633Z"
   },
   {
    "duration": 318,
    "start_time": "2022-01-30T16:49:16.561Z"
   },
   {
    "duration": 31,
    "start_time": "2022-01-30T16:49:38.865Z"
   },
   {
    "duration": 5,
    "start_time": "2022-01-30T16:52:34.855Z"
   },
   {
    "duration": 102,
    "start_time": "2022-01-30T16:57:21.751Z"
   },
   {
    "duration": 28,
    "start_time": "2022-01-30T16:57:38.713Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-30T16:57:59.263Z"
   },
   {
    "duration": 28,
    "start_time": "2022-01-30T17:08:08.208Z"
   },
   {
    "duration": 22,
    "start_time": "2022-01-30T17:08:23.679Z"
   },
   {
    "duration": 5,
    "start_time": "2022-01-30T17:08:33.949Z"
   },
   {
    "duration": 29,
    "start_time": "2022-01-30T17:18:36.571Z"
   },
   {
    "duration": 326,
    "start_time": "2022-01-30T17:23:56.824Z"
   },
   {
    "duration": 321,
    "start_time": "2022-01-30T17:24:26.996Z"
   },
   {
    "duration": 23,
    "start_time": "2022-01-30T17:25:00.627Z"
   },
   {
    "duration": 29,
    "start_time": "2022-01-30T17:25:30.883Z"
   },
   {
    "duration": 297,
    "start_time": "2022-01-31T08:31:53.232Z"
   },
   {
    "duration": 248,
    "start_time": "2022-01-31T08:32:28.850Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T08:32:47.061Z"
   },
   {
    "duration": 260,
    "start_time": "2022-01-31T08:32:51.271Z"
   },
   {
    "duration": 252,
    "start_time": "2022-01-31T08:32:57.179Z"
   },
   {
    "duration": 558,
    "start_time": "2022-01-31T08:33:07.085Z"
   },
   {
    "duration": 123,
    "start_time": "2022-01-31T08:33:07.644Z"
   },
   {
    "duration": 16,
    "start_time": "2022-01-31T08:33:07.769Z"
   },
   {
    "duration": 24,
    "start_time": "2022-01-31T08:33:07.787Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T08:33:07.812Z"
   },
   {
    "duration": 21,
    "start_time": "2022-01-31T08:33:07.817Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T08:33:07.840Z"
   },
   {
    "duration": 40,
    "start_time": "2022-01-31T08:33:07.844Z"
   },
   {
    "duration": 15,
    "start_time": "2022-01-31T08:33:07.887Z"
   },
   {
    "duration": 21,
    "start_time": "2022-01-31T08:33:07.904Z"
   },
   {
    "duration": 77,
    "start_time": "2022-01-31T08:33:07.926Z"
   },
   {
    "duration": 1,
    "start_time": "2022-01-31T08:33:08.005Z"
   },
   {
    "duration": 6,
    "start_time": "2022-01-31T08:33:08.008Z"
   },
   {
    "duration": 5,
    "start_time": "2022-01-31T08:33:08.015Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T08:33:08.022Z"
   },
   {
    "duration": 6,
    "start_time": "2022-01-31T08:33:08.027Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T08:33:08.034Z"
   },
   {
    "duration": 7,
    "start_time": "2022-01-31T08:33:08.044Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T08:33:08.052Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T08:33:08.062Z"
   },
   {
    "duration": 10,
    "start_time": "2022-01-31T08:33:08.072Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T08:33:08.084Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T08:33:08.093Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T08:33:08.102Z"
   },
   {
    "duration": 7,
    "start_time": "2022-01-31T08:33:08.112Z"
   },
   {
    "duration": 11,
    "start_time": "2022-01-31T08:33:08.121Z"
   },
   {
    "duration": 6,
    "start_time": "2022-01-31T08:33:08.135Z"
   },
   {
    "duration": 7,
    "start_time": "2022-01-31T08:33:08.142Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T08:33:08.151Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T08:33:08.160Z"
   },
   {
    "duration": 11,
    "start_time": "2022-01-31T08:33:08.169Z"
   },
   {
    "duration": 10,
    "start_time": "2022-01-31T08:33:08.181Z"
   },
   {
    "duration": 11,
    "start_time": "2022-01-31T08:33:08.192Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T08:33:08.204Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T08:33:08.214Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T08:33:08.224Z"
   },
   {
    "duration": 6,
    "start_time": "2022-01-31T08:33:08.234Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T08:33:08.242Z"
   },
   {
    "duration": 68,
    "start_time": "2022-01-31T08:34:11.549Z"
   },
   {
    "duration": 46,
    "start_time": "2022-01-31T08:34:29.108Z"
   },
   {
    "duration": 18,
    "start_time": "2022-01-31T08:36:10.862Z"
   },
   {
    "duration": 11769,
    "start_time": "2022-01-31T08:36:28.721Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T08:37:04.491Z"
   },
   {
    "duration": 6,
    "start_time": "2022-01-31T08:37:17.994Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T08:37:37.238Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T09:02:37.923Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T09:03:03.279Z"
   },
   {
    "duration": 271,
    "start_time": "2022-01-31T09:03:09.727Z"
   },
   {
    "duration": 516,
    "start_time": "2022-01-31T09:03:29.260Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T09:05:04.926Z"
   },
   {
    "duration": 510,
    "start_time": "2022-01-31T09:05:09.252Z"
   },
   {
    "duration": 581,
    "start_time": "2022-01-31T09:07:06.510Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T09:08:20.260Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T09:08:25.905Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T09:08:34.020Z"
   },
   {
    "duration": 254,
    "start_time": "2022-01-31T09:18:12.201Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T09:19:35.972Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T09:19:40.718Z"
   },
   {
    "duration": 13,
    "start_time": "2022-01-31T09:20:31.445Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T09:20:35.445Z"
   },
   {
    "duration": 10,
    "start_time": "2022-01-31T09:21:15.058Z"
   },
   {
    "duration": 2,
    "start_time": "2022-01-31T09:21:20.619Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-31T09:21:38.685Z"
   },
   {
    "duration": 15,
    "start_time": "2022-01-31T09:21:45.100Z"
   },
   {
    "duration": 19,
    "start_time": "2022-01-31T09:21:51.331Z"
   },
   {
    "duration": 48,
    "start_time": "2022-01-31T09:21:55.296Z"
   },
   {
    "duration": 52,
    "start_time": "2022-01-31T09:22:02.378Z"
   },
   {
    "duration": 58,
    "start_time": "2022-01-31T09:22:07.201Z"
   },
   {
    "duration": 51,
    "start_time": "2022-01-31T09:22:11.608Z"
   },
   {
    "duration": 10,
    "start_time": "2022-01-31T09:22:22.910Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T09:22:28.937Z"
   },
   {
    "duration": 156,
    "start_time": "2022-01-31T09:22:28.941Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T09:22:29.099Z"
   },
   {
    "duration": 29,
    "start_time": "2022-01-31T09:22:29.109Z"
   },
   {
    "duration": 17,
    "start_time": "2022-01-31T09:22:29.140Z"
   },
   {
    "duration": 15,
    "start_time": "2022-01-31T09:22:29.158Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T09:22:29.175Z"
   },
   {
    "duration": 21,
    "start_time": "2022-01-31T09:22:29.180Z"
   },
   {
    "duration": 15,
    "start_time": "2022-01-31T09:22:29.202Z"
   },
   {
    "duration": 19,
    "start_time": "2022-01-31T09:22:29.218Z"
   },
   {
    "duration": 70,
    "start_time": "2022-01-31T09:22:29.238Z"
   },
   {
    "duration": 51,
    "start_time": "2022-01-31T09:22:29.310Z"
   },
   {
    "duration": 48,
    "start_time": "2022-01-31T09:22:29.363Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T09:22:29.412Z"
   },
   {
    "duration": 2,
    "start_time": "2022-01-31T09:22:29.422Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T09:22:29.426Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T09:22:29.437Z"
   },
   {
    "duration": 27,
    "start_time": "2022-01-31T09:22:29.446Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T09:22:29.476Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T09:22:29.481Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T09:22:29.486Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T09:22:29.495Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T09:22:29.504Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T09:22:29.514Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T09:22:29.524Z"
   },
   {
    "duration": 11,
    "start_time": "2022-01-31T09:22:29.534Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T09:22:29.546Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T09:22:29.555Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T09:22:29.565Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T09:22:29.575Z"
   },
   {
    "duration": 11,
    "start_time": "2022-01-31T09:22:29.585Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T09:22:29.597Z"
   },
   {
    "duration": 11,
    "start_time": "2022-01-31T09:22:29.607Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T09:22:29.619Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T09:22:29.628Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T09:22:29.639Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T09:22:29.649Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T09:22:29.659Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T09:24:42.453Z"
   },
   {
    "duration": 49,
    "start_time": "2022-01-31T09:25:03.125Z"
   },
   {
    "duration": 11,
    "start_time": "2022-01-31T09:25:36.533Z"
   },
   {
    "duration": 266,
    "start_time": "2022-01-31T09:28:06.853Z"
   },
   {
    "duration": 11,
    "start_time": "2022-01-31T09:41:04.476Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T10:02:32.374Z"
   },
   {
    "duration": 560,
    "start_time": "2022-01-31T10:11:57.771Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T10:12:24.760Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-31T10:12:29.669Z"
   },
   {
    "duration": 18,
    "start_time": "2022-01-31T10:12:35.211Z"
   },
   {
    "duration": 19,
    "start_time": "2022-01-31T10:12:40.083Z"
   },
   {
    "duration": 18,
    "start_time": "2022-01-31T10:12:43.148Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-31T10:12:46.606Z"
   },
   {
    "duration": 13,
    "start_time": "2022-01-31T10:12:49.932Z"
   },
   {
    "duration": 289,
    "start_time": "2022-01-31T10:13:03.221Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-31T10:14:14.455Z"
   },
   {
    "duration": 19,
    "start_time": "2022-01-31T10:14:18.952Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-31T10:14:24.210Z"
   },
   {
    "duration": 17,
    "start_time": "2022-01-31T10:14:28.269Z"
   },
   {
    "duration": 21,
    "start_time": "2022-01-31T10:14:33.377Z"
   },
   {
    "duration": 17,
    "start_time": "2022-01-31T10:14:36.345Z"
   },
   {
    "duration": 19,
    "start_time": "2022-01-31T10:15:22.536Z"
   },
   {
    "duration": 17,
    "start_time": "2022-01-31T10:15:26.700Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-31T10:16:47.277Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-31T10:17:39.703Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-31T10:17:45.329Z"
   },
   {
    "duration": 17,
    "start_time": "2022-01-31T10:17:48.313Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-31T10:17:52.285Z"
   },
   {
    "duration": 18,
    "start_time": "2022-01-31T10:17:56.465Z"
   },
   {
    "duration": 19,
    "start_time": "2022-01-31T10:19:25.205Z"
   },
   {
    "duration": 18,
    "start_time": "2022-01-31T10:19:30.782Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T10:19:33.269Z"
   },
   {
    "duration": 47,
    "start_time": "2022-01-31T10:19:39.074Z"
   },
   {
    "duration": 30,
    "start_time": "2022-01-31T10:19:52.182Z"
   },
   {
    "duration": 51,
    "start_time": "2022-01-31T10:20:51.234Z"
   },
   {
    "duration": 51,
    "start_time": "2022-01-31T10:20:55.477Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T10:21:19.005Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-31T10:21:22.437Z"
   },
   {
    "duration": 17,
    "start_time": "2022-01-31T10:21:25.389Z"
   },
   {
    "duration": 21,
    "start_time": "2022-01-31T10:21:30.558Z"
   },
   {
    "duration": 17,
    "start_time": "2022-01-31T10:21:35.174Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T10:23:08.983Z"
   },
   {
    "duration": 554,
    "start_time": "2022-01-31T10:23:13.602Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T10:28:23.030Z"
   },
   {
    "duration": 22,
    "start_time": "2022-01-31T10:28:27.331Z"
   },
   {
    "duration": 26,
    "start_time": "2022-01-31T10:28:31.469Z"
   },
   {
    "duration": 21,
    "start_time": "2022-01-31T10:28:35.949Z"
   },
   {
    "duration": 21,
    "start_time": "2022-01-31T10:30:08.243Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T10:33:19.045Z"
   },
   {
    "duration": 528,
    "start_time": "2022-01-31T10:33:23.182Z"
   },
   {
    "duration": 532,
    "start_time": "2022-01-31T10:34:28.331Z"
   },
   {
    "duration": 569,
    "start_time": "2022-01-31T10:44:01.003Z"
   },
   {
    "duration": 526,
    "start_time": "2022-01-31T10:44:59.420Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T10:50:59.132Z"
   },
   {
    "duration": 62,
    "start_time": "2022-01-31T10:51:02.471Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T10:52:06.395Z"
   },
   {
    "duration": 21,
    "start_time": "2022-01-31T10:52:12.485Z"
   },
   {
    "duration": 19,
    "start_time": "2022-01-31T10:52:17.644Z"
   },
   {
    "duration": 7,
    "start_time": "2022-01-31T10:53:30.200Z"
   },
   {
    "duration": 566,
    "start_time": "2022-01-31T10:53:33.505Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T10:54:45.301Z"
   },
   {
    "duration": 1382,
    "start_time": "2022-01-31T10:54:50.229Z"
   },
   {
    "duration": 557,
    "start_time": "2022-01-31T10:57:02.718Z"
   },
   {
    "duration": 627,
    "start_time": "2022-01-31T11:00:56.025Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T11:01:46.107Z"
   },
   {
    "duration": 24,
    "start_time": "2022-01-31T11:01:49.816Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-31T11:01:57.505Z"
   },
   {
    "duration": 22,
    "start_time": "2022-01-31T11:02:01.840Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T11:03:06.596Z"
   },
   {
    "duration": 61,
    "start_time": "2022-01-31T11:03:12.398Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T11:04:08.489Z"
   },
   {
    "duration": 54,
    "start_time": "2022-01-31T11:04:13.145Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T11:05:08.373Z"
   },
   {
    "duration": 50,
    "start_time": "2022-01-31T11:05:12.570Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T11:06:29.452Z"
   },
   {
    "duration": 556,
    "start_time": "2022-01-31T11:06:32.394Z"
   },
   {
    "duration": 643,
    "start_time": "2022-01-31T11:07:12.258Z"
   },
   {
    "duration": 535,
    "start_time": "2022-01-31T11:08:51.684Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T11:09:09.961Z"
   },
   {
    "duration": 547,
    "start_time": "2022-01-31T11:09:13.849Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T11:13:54.617Z"
   },
   {
    "duration": 16,
    "start_time": "2022-01-31T11:13:58.529Z"
   },
   {
    "duration": 14,
    "start_time": "2022-01-31T11:14:01.509Z"
   },
   {
    "duration": 15,
    "start_time": "2022-01-31T11:14:02.733Z"
   },
   {
    "duration": 14,
    "start_time": "2022-01-31T11:14:03.560Z"
   },
   {
    "duration": 16,
    "start_time": "2022-01-31T11:14:04.276Z"
   },
   {
    "duration": 13,
    "start_time": "2022-01-31T11:14:04.988Z"
   },
   {
    "duration": 296,
    "start_time": "2022-01-31T11:14:52.006Z"
   },
   {
    "duration": 246,
    "start_time": "2022-01-31T11:23:21.847Z"
   },
   {
    "duration": 303,
    "start_time": "2022-01-31T11:23:32.170Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T11:23:42.337Z"
   },
   {
    "duration": 7,
    "start_time": "2022-01-31T11:24:08.561Z"
   },
   {
    "duration": 11,
    "start_time": "2022-01-31T12:36:03.114Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T12:36:06.489Z"
   },
   {
    "duration": 112,
    "start_time": "2022-01-31T12:50:14.889Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T12:50:29.714Z"
   },
   {
    "duration": 256,
    "start_time": "2022-01-31T12:53:53.660Z"
   },
   {
    "duration": 17,
    "start_time": "2022-01-31T12:54:21.945Z"
   },
   {
    "duration": 13,
    "start_time": "2022-01-31T12:55:08.105Z"
   },
   {
    "duration": 16,
    "start_time": "2022-01-31T12:55:24.557Z"
   },
   {
    "duration": 13,
    "start_time": "2022-01-31T12:55:34.753Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T13:04:16.765Z"
   },
   {
    "duration": 10,
    "start_time": "2022-01-31T13:05:39.827Z"
   },
   {
    "duration": 10,
    "start_time": "2022-01-31T13:05:42.965Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T13:05:47.746Z"
   },
   {
    "duration": 10,
    "start_time": "2022-01-31T13:06:58.768Z"
   },
   {
    "duration": 6,
    "start_time": "2022-01-31T13:07:05.000Z"
   },
   {
    "duration": 5,
    "start_time": "2022-01-31T13:07:08.887Z"
   },
   {
    "duration": 5,
    "start_time": "2022-01-31T13:08:09.250Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T13:08:24.710Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T13:14:00.041Z"
   },
   {
    "duration": 5,
    "start_time": "2022-01-31T13:14:15.760Z"
   },
   {
    "duration": 19,
    "start_time": "2022-01-31T13:14:30.607Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T13:14:48.479Z"
   },
   {
    "duration": 115,
    "start_time": "2022-01-31T13:14:48.483Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T13:14:48.600Z"
   },
   {
    "duration": 21,
    "start_time": "2022-01-31T13:14:48.610Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T13:14:48.633Z"
   },
   {
    "duration": 40,
    "start_time": "2022-01-31T13:14:48.637Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T13:14:48.679Z"
   },
   {
    "duration": 22,
    "start_time": "2022-01-31T13:14:48.685Z"
   },
   {
    "duration": 14,
    "start_time": "2022-01-31T13:14:48.708Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-31T13:14:48.723Z"
   },
   {
    "duration": 73,
    "start_time": "2022-01-31T13:14:48.745Z"
   },
   {
    "duration": 60,
    "start_time": "2022-01-31T13:14:48.819Z"
   },
   {
    "duration": 44,
    "start_time": "2022-01-31T13:14:48.881Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T13:14:48.927Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T13:14:48.937Z"
   },
   {
    "duration": 30,
    "start_time": "2022-01-31T13:14:48.946Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T13:14:48.977Z"
   },
   {
    "duration": 18,
    "start_time": "2022-01-31T13:14:48.987Z"
   },
   {
    "duration": 20,
    "start_time": "2022-01-31T13:14:49.007Z"
   },
   {
    "duration": 5,
    "start_time": "2022-01-31T13:14:49.029Z"
   },
   {
    "duration": 30,
    "start_time": "2022-01-31T13:14:49.036Z"
   },
   {
    "duration": 19,
    "start_time": "2022-01-31T13:14:49.067Z"
   },
   {
    "duration": 17,
    "start_time": "2022-01-31T13:14:49.087Z"
   },
   {
    "duration": 16,
    "start_time": "2022-01-31T13:14:49.106Z"
   },
   {
    "duration": 16,
    "start_time": "2022-01-31T13:14:49.124Z"
   },
   {
    "duration": 16,
    "start_time": "2022-01-31T13:14:49.142Z"
   },
   {
    "duration": 14,
    "start_time": "2022-01-31T13:14:49.160Z"
   },
   {
    "duration": 25,
    "start_time": "2022-01-31T13:14:49.175Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T13:14:49.202Z"
   },
   {
    "duration": 15,
    "start_time": "2022-01-31T13:14:49.212Z"
   },
   {
    "duration": 31,
    "start_time": "2022-01-31T13:14:49.228Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T13:14:49.261Z"
   },
   {
    "duration": 12,
    "start_time": "2022-01-31T13:14:49.272Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T13:14:49.286Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T13:14:49.296Z"
   },
   {
    "duration": 5,
    "start_time": "2022-01-31T13:14:49.306Z"
   },
   {
    "duration": 11,
    "start_time": "2022-01-31T13:14:49.313Z"
   },
   {
    "duration": 7,
    "start_time": "2022-01-31T13:14:49.325Z"
   },
   {
    "duration": 21,
    "start_time": "2022-01-31T13:15:23.831Z"
   },
   {
    "duration": 45,
    "start_time": "2022-01-31T13:15:37.476Z"
   },
   {
    "duration": 2,
    "start_time": "2022-01-31T13:16:29.802Z"
   },
   {
    "duration": 135,
    "start_time": "2022-01-31T13:16:29.806Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T13:16:29.943Z"
   },
   {
    "duration": 38,
    "start_time": "2022-01-31T13:16:29.954Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T13:16:29.994Z"
   },
   {
    "duration": 12,
    "start_time": "2022-01-31T13:16:30.000Z"
   },
   {
    "duration": 4,
    "start_time": "2022-01-31T13:16:30.013Z"
   },
   {
    "duration": 54,
    "start_time": "2022-01-31T13:16:30.019Z"
   },
   {
    "duration": 17,
    "start_time": "2022-01-31T13:16:30.075Z"
   },
   {
    "duration": 31,
    "start_time": "2022-01-31T13:16:30.093Z"
   },
   {
    "duration": 66,
    "start_time": "2022-01-31T13:16:30.126Z"
   },
   {
    "duration": 57,
    "start_time": "2022-01-31T13:16:30.194Z"
   },
   {
    "duration": 70,
    "start_time": "2022-01-31T13:16:30.252Z"
   },
   {
    "duration": 8,
    "start_time": "2022-01-31T13:16:30.324Z"
   },
   {
    "duration": 3,
    "start_time": "2022-01-31T13:16:30.334Z"
   },
   {
    "duration": 14,
    "start_time": "2022-01-31T13:16:30.339Z"
   },
   {
    "duration": 15,
    "start_time": "2022-01-31T13:16:30.371Z"
   },
   {
    "duration": 10,
    "start_time": "2022-01-31T13:16:30.388Z"
   },
   {
    "duration": 9,
    "start_time": "2022-01-31T13:16:30.399Z"
   },
   {
    "duration": 2,
    "start_time": "2022-01-31T13:16:30.410Z"
   },
   {
    "duration": 24,
    "start_time": "2022-01-31T13:16:30.413Z"
   },
   {
    "duration": 36,
    "start_time": "2022-01-31T13:16:30.439Z"
   },
   {
    "duration": 27,
    "start_time": "2022-01-31T13:16:30.479Z"
   },
   {
    "duration": 12,
    "start_time": "2022-01-31T13:16:30.508Z"
   },
   {
    "duration": 24,
    "start_time": "2022-01-31T13:16:30.521Z"
   },
   {
    "duration": 30,
    "start_time": "2022-01-31T13:16:30.547Z"
   },
   {
    "duration": 10,
    "start_time": "2022-01-31T13:16:30.579Z"
   },
   {
    "duration": 16,
    "start_time": "2022-01-31T13:16:30.591Z"
   },
   {
    "duration": 13,
    "start_time": "2022-01-31T13:16:30.609Z"
   },
   {
    "duration": 10,
    "start_time": "2022-01-31T13:16:30.624Z"
   },
   {
    "duration": 31,
    "start_time": "2022-01-31T13:16:30.636Z"
   },
   {
    "duration": 29,
    "start_time": "2022-01-31T13:16:30.668Z"
   },
   {
    "duration": 16,
    "start_time": "2022-01-31T13:16:30.698Z"
   },
   {
    "duration": 11,
    "start_time": "2022-01-31T13:16:30.716Z"
   },
   {
    "duration": 14,
    "start_time": "2022-01-31T13:16:30.729Z"
   },
   {
    "duration": 5,
    "start_time": "2022-01-31T13:16:30.744Z"
   },
   {
    "duration": 15,
    "start_time": "2022-01-31T13:16:30.751Z"
   },
   {
    "duration": 6,
    "start_time": "2022-01-31T13:16:30.772Z"
   },
   {
    "duration": 598,
    "start_time": "2022-02-09T15:43:42.147Z"
   },
   {
    "duration": 152,
    "start_time": "2022-02-09T15:43:42.747Z"
   },
   {
    "duration": 20,
    "start_time": "2022-02-09T15:43:42.902Z"
   },
   {
    "duration": 30,
    "start_time": "2022-02-09T15:43:42.924Z"
   },
   {
    "duration": 5,
    "start_time": "2022-02-09T15:43:42.956Z"
   },
   {
    "duration": 50,
    "start_time": "2022-02-09T15:43:42.963Z"
   },
   {
    "duration": 3,
    "start_time": "2022-02-09T15:43:43.015Z"
   },
   {
    "duration": 35,
    "start_time": "2022-02-09T15:43:43.021Z"
   },
   {
    "duration": 19,
    "start_time": "2022-02-09T15:43:43.059Z"
   },
   {
    "duration": 38,
    "start_time": "2022-02-09T15:43:43.080Z"
   },
   {
    "duration": 65,
    "start_time": "2022-02-09T15:43:43.120Z"
   },
   {
    "duration": 84,
    "start_time": "2022-02-09T15:43:43.187Z"
   },
   {
    "duration": 74,
    "start_time": "2022-02-09T15:43:43.272Z"
   },
   {
    "duration": 12,
    "start_time": "2022-02-09T15:43:43.348Z"
   },
   {
    "duration": 4,
    "start_time": "2022-02-09T15:43:43.363Z"
   },
   {
    "duration": 35,
    "start_time": "2022-02-09T15:43:43.369Z"
   },
   {
    "duration": 26,
    "start_time": "2022-02-09T15:43:43.406Z"
   },
   {
    "duration": 14,
    "start_time": "2022-02-09T15:43:43.434Z"
   },
   {
    "duration": 13,
    "start_time": "2022-02-09T15:43:43.450Z"
   },
   {
    "duration": 4,
    "start_time": "2022-02-09T15:43:43.466Z"
   },
   {
    "duration": 41,
    "start_time": "2022-02-09T15:43:43.472Z"
   },
   {
    "duration": 21,
    "start_time": "2022-02-09T15:43:43.515Z"
   },
   {
    "duration": 18,
    "start_time": "2022-02-09T15:43:43.540Z"
   },
   {
    "duration": 47,
    "start_time": "2022-02-09T15:43:43.561Z"
   },
   {
    "duration": 17,
    "start_time": "2022-02-09T15:43:43.610Z"
   },
   {
    "duration": 17,
    "start_time": "2022-02-09T15:43:43.629Z"
   },
   {
    "duration": 10,
    "start_time": "2022-02-09T15:43:43.647Z"
   },
   {
    "duration": 11,
    "start_time": "2022-02-09T15:43:43.698Z"
   },
   {
    "duration": 10,
    "start_time": "2022-02-09T15:43:43.711Z"
   },
   {
    "duration": 4,
    "start_time": "2022-02-09T15:43:43.723Z"
   },
   {
    "duration": 42,
    "start_time": "2022-02-09T15:43:43.729Z"
   },
   {
    "duration": 30,
    "start_time": "2022-02-09T15:43:43.773Z"
   },
   {
    "duration": 19,
    "start_time": "2022-02-09T15:43:43.804Z"
   },
   {
    "duration": 14,
    "start_time": "2022-02-09T15:43:43.825Z"
   },
   {
    "duration": 10,
    "start_time": "2022-02-09T15:43:43.841Z"
   },
   {
    "duration": 5,
    "start_time": "2022-02-09T15:43:43.854Z"
   },
   {
    "duration": 8,
    "start_time": "2022-02-09T15:43:43.899Z"
   },
   {
    "duration": 4,
    "start_time": "2022-02-09T15:43:43.909Z"
   },
   {
    "duration": 11,
    "start_time": "2022-02-09T15:44:14.239Z"
   },
   {
    "duration": 16,
    "start_time": "2022-02-09T15:46:28.895Z"
   },
   {
    "duration": 325,
    "start_time": "2022-02-09T15:48:34.053Z"
   },
   {
    "duration": 11,
    "start_time": "2022-02-09T15:48:41.152Z"
   },
   {
    "duration": 319,
    "start_time": "2022-02-10T07:16:45.538Z"
   },
   {
    "duration": 172,
    "start_time": "2022-02-10T07:17:00.049Z"
   },
   {
    "duration": 261,
    "start_time": "2022-02-10T07:24:31.511Z"
   },
   {
    "duration": 168,
    "start_time": "2022-02-10T07:24:32.363Z"
   },
   {
    "duration": 403,
    "start_time": "2022-02-10T07:30:50.367Z"
   },
   {
    "duration": 830,
    "start_time": "2022-02-10T07:30:57.862Z"
   },
   {
    "duration": 187,
    "start_time": "2022-02-10T07:30:58.695Z"
   },
   {
    "duration": 38,
    "start_time": "2022-02-10T07:30:58.885Z"
   },
   {
    "duration": 14,
    "start_time": "2022-02-10T07:30:58.927Z"
   },
   {
    "duration": 45,
    "start_time": "2022-02-10T07:30:58.943Z"
   },
   {
    "duration": 14,
    "start_time": "2022-02-10T07:30:58.991Z"
   },
   {
    "duration": 49,
    "start_time": "2022-02-10T07:30:59.008Z"
   },
   {
    "duration": 7,
    "start_time": "2022-02-10T07:30:59.060Z"
   },
   {
    "duration": 34,
    "start_time": "2022-02-10T07:30:59.073Z"
   },
   {
    "duration": 22,
    "start_time": "2022-02-10T07:30:59.123Z"
   },
   {
    "duration": 29,
    "start_time": "2022-02-10T07:30:59.147Z"
   },
   {
    "duration": 108,
    "start_time": "2022-02-10T07:30:59.178Z"
   },
   {
    "duration": 109,
    "start_time": "2022-02-10T07:30:59.289Z"
   },
   {
    "duration": 81,
    "start_time": "2022-02-10T07:30:59.401Z"
   },
   {
    "duration": 14,
    "start_time": "2022-02-10T07:30:59.485Z"
   },
   {
    "duration": 22,
    "start_time": "2022-02-10T07:30:59.502Z"
   },
   {
    "duration": 14,
    "start_time": "2022-02-10T07:30:59.526Z"
   },
   {
    "duration": 16,
    "start_time": "2022-02-10T07:30:59.542Z"
   },
   {
    "duration": 16,
    "start_time": "2022-02-10T07:30:59.561Z"
   },
   {
    "duration": 58,
    "start_time": "2022-02-10T07:30:59.581Z"
   },
   {
    "duration": 23,
    "start_time": "2022-02-10T07:30:59.642Z"
   },
   {
    "duration": 5,
    "start_time": "2022-02-10T07:30:59.667Z"
   },
   {
    "duration": 58,
    "start_time": "2022-02-10T07:30:59.674Z"
   },
   {
    "duration": 20,
    "start_time": "2022-02-10T07:30:59.735Z"
   },
   {
    "duration": 20,
    "start_time": "2022-02-10T07:30:59.759Z"
   },
   {
    "duration": 52,
    "start_time": "2022-02-10T07:30:59.781Z"
   },
   {
    "duration": 21,
    "start_time": "2022-02-10T07:30:59.837Z"
   },
   {
    "duration": 19,
    "start_time": "2022-02-10T07:30:59.861Z"
   },
   {
    "duration": 43,
    "start_time": "2022-02-10T07:30:59.882Z"
   },
   {
    "duration": 16,
    "start_time": "2022-02-10T07:30:59.927Z"
   },
   {
    "duration": 13,
    "start_time": "2022-02-10T07:30:59.945Z"
   },
   {
    "duration": 6,
    "start_time": "2022-02-10T07:30:59.961Z"
   },
   {
    "duration": 64,
    "start_time": "2022-02-10T07:30:59.970Z"
   },
   {
    "duration": 17,
    "start_time": "2022-02-10T07:31:00.036Z"
   },
   {
    "duration": 22,
    "start_time": "2022-02-10T07:31:00.056Z"
   },
   {
    "duration": 49,
    "start_time": "2022-02-10T07:31:00.080Z"
   },
   {
    "duration": 13,
    "start_time": "2022-02-10T07:31:00.132Z"
   },
   {
    "duration": 7,
    "start_time": "2022-02-10T07:31:00.147Z"
   },
   {
    "duration": 12,
    "start_time": "2022-02-10T07:31:00.156Z"
   },
   {
    "duration": 11,
    "start_time": "2022-02-10T07:31:00.170Z"
   },
   {
    "duration": 42,
    "start_time": "2022-02-10T07:31:00.183Z"
   }
  ],
  "colab": {
   "collapsed_sections": [
    "E0vqbgi9ay0H",
    "VUC88oWjTJw2"
   ],
   "name": "yandex_music_project_2021.2.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": true,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {
    "height": "calc(100% - 180px)",
    "left": "10px",
    "top": "150px",
    "width": "292px"
   },
   "toc_section_display": true,
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
