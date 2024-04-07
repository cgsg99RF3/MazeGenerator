# Генератор Лабиринтов

***Цель*:** написать генератор лабиринтов

***Функционал:***  
 - Генерация с помощью DFS или минимального остовного дерева 
 - Возможность выбрать вариант генерации через командную строку 
 - Возможность задать размеры лабиринта через командную строку 
 - Отображение лабиринта в консоле 
 - Сохранение/загрузка лвбиринта в/из файлов 
 - Решение лабиринтов и отображение пути

***Архитектура:***

**1) Class Params** 
```python
self.width  # Высота лабиринта

self.height  # Ширина лабиринта

self.type  # Тип генерации - DFS(1)/MST(2) 
```
```python
def __init__(self, width, height, type)  
```  

**2) Class Cell**
```python
self.x # Позиция x

self.y # Позиция y

self.is_checked # Флаг, был ли алгоритм в клетке 

self.walls # List([bool]) - лист, показывает есть стена или нет
```
```python
def __init__(self, x : int, y : int)

def get_neighbours(self) -> List[Cell] # Поиск соседей

def check(self) -> bool # Проверка, нужно ли идти в клетку

@staticmetod
def is_passage(first : Cell, second : Cell) # Проверка, есть ли путь между клетками

@staticmetod
def is_wall(first : Cell, second : Cell) # Проверка, есть ли стена между клетками

@staticmetod
def connect(first : Cell, second : Cell) # Удаление стены между клетками

def load(file : _io.TextIOWrapper) # Загрузка из файла

def save(file : _io.TextIOWrapper) # Сохранение в файл
```
**3) Class Maze**
```python
self.params # Параметры лабиринта

self.grid # Поле лабиринта, List[width * height * cell()]
```
```python
def __init__(self, params : Params) # Инициализация

@abstractmetod
def draw(self) # Отрисовка лабиринта

@abstractmetod
def generate(self) # Генерация лабиринта (абстрактный метод)
```
**4) Class DFS(Maze)**
```python
def generate(self) # Реализация абстрактного метода

def draw(self) # Реализация абстрактного метода
```
**5) Class MST(Maze)**
```python
def generate(self) # Реализация абстрактного метода

def draw(self) # Реализация абстрактного метода
```
**6) Class Path**
```python
self.maze # Лабиринт, для которого ищется путь

self.path # List[Cell] - путь
```
```python
def __init__(self, maze : Maze) # Инициализация

def find(self) # Поиск пути

def draw(self) # Отрисовка пути
```