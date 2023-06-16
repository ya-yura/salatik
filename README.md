# Проект SALATIK 

> Нужен для того, чтобы заказать себе салат!

В приложении будет часть, где администраторы могут регулировать доступные ингредиенты для салатов и их наличие (склад), указывать стоимость компонентов, отслеживать заказы, их статусы. Часть для курьеров с интеграцией яндекс-карт. И пользовательская часть, где можно выбрать ингредиенты для салата, указать их количество и порядок закладки, а также оформить заказ себе домой.


# Техническое задание

## Введение

**Цель проекта**

Разработать приложение заказа салата с доставкой для администратора, пользователей и курьеров.

<details>  
<summary>1. Основные функциональные требования</summary>

  
-   Администратор должен иметь возможность управлять компонентами, их наличием и статусом заказов.    
-   Пользователь должен иметь возможность выбирать компоненты, указывать количество и порядок их закладывания, оформлять заказ и просматривать свои заказы.    
-   Курьер должен иметь возможность просматривать данные о заказе, местоположение клиента на карте и обновлять статус заказа.
</details> 
  
  
<details>  
<summary>2. Требования к функциональности</summary>

  
**2.1. Администраторская часть**

-   Авторизация администратора
-   Управление компонентами  
-- *Добавление, редактирование и удаление компонентов с указанием названия, фотографии, описания и массы в наличии.*  
-- *Просмотр списка компонентов с указанием их текущего количества.*
-   Управление заказами
-- *Просмотр списка заказов с указанием статуса и деталей заказа.*
-- *Изменение статуса заказа (например, «в обработке», «готовится», «доставляется», «доставлен», «отменён»).*

**2.2. Пользовательская часть**

- Регистрация и аутентификация пользователей.    
- Просмотр списка доступных компонентов с указанием их массы в наличии.    
- Выбор компонентов, указание количества и порядка их закладывания в салат.    
- Оформление заказа с указанием адреса доставки и выбором оплаты.    
- Просмотр списка собственных заказов с указанием статуса и деталей заказа.

**2.3. Курьерская часть**

- Авторизация курьера.    
- Просмотр списка заказов, которые требуется доставить.    
- Просмотр подробной информации о заказе, включая адрес доставки и контактные данные клиента.    
- Обновление статуса заказа (например, «взят в доставку», «доставлен клиенту»).
</details>


<details>
<summary>3. Технические требования</summary>

  
- Фреймворк: Django.    
- Язык программирования: Python.    
- База данных: PostgreSQL.

- Интерфейс администратора должен быть реализован с использованием специальных представлений (views) и шаблонов (templates).
- Возможность добавления, редактирования и удаления компонентов, указание их наличия (массы на складе), цены (за единицу массы).    
- Возможность управления заказами (просмотр и редактирование статусов).
-  Пользовательский интерфейс должен быть разработан с использованием HTML, CSS и JavaScript. Для упрощения разработки пользовательского интерфейса можно использовать фреймворк Bootstrap или другие CSS-фреймворки.    
- Реализация функциональности выбора компонентов и оформления заказа должна быть выполнена с помощью Django-форм или JavaScript для динамического добавления и удаления компонентов.    
- Для отображения местоположения клиента на карте в курьерской части можно использовать интеграцию с сервисами карт, такими как Google Maps или Яндекс.Карты.    
- Для обработки платежей можно использовать платежные шлюзы, такие как ЮMoney, Сбер или ВК. Интеграция с выбранным платежным шлюзом должна быть выполнена в соответствии с их документацией.    
- Для обновления статуса заказа и отслеживания его выполнения в реальном времени можно использовать WebSocket-соединения или технологию Server-Sent Events (SSE).    
- Приложение должно быть развернуто на сервере с использованием соответствующих настроек и конфигурации для Django приложений.


</details>

## Архитектура проекта

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="http://4qd.ru/architecture.png">
  <source media="(prefers-color-scheme: light)" srcset="http://4qd.ru/architecture.png">
  <img alt="Architcture of app scheme." src="http://4qd.ru/architecture.png">
</picture>


## Схема базы данных

```mermaid
erDiagram
    USER {
        username CharField
        email EmailField
        password CharField
        first_name CharField
        last_name CharField
        bio TextField
    }
    ROLE {
        name CharField
        users ManyToManyField
    }
    INGREDIENT_TYPE {
        name CharField
        slug SlugField
        is_available BooleanField
        created_at DateTimeField
        updated_at DateTimeField
    }
    INGREDIENTS {
        name CharField
        slug SlugField
        photo ImageField
        type ForeignKey
        price_per_unit DecimalField
        protein FloatField
        fat FloatField
        carbohydrates FloatField
        energy FloatField
        is_available BooleanField
        created_at DateTimeField
        updated_at DateTimeField
    }
    SALAD {
        name CharField
        slug SlugField
        description TextField
        is_available BooleanField
        created_at DateTimeField
        updated_at DateTimeField
        creator ForeignKey
    }
    COMPONENT {
        salad ForeignKey
        slug SlugField
        ingredient ForeignKey
        weight DecimalField
        order IntegerField
        is_available BooleanField
        created_at DateTimeField
        updated_at DateTimeField
    }
    ORDER {
        user ForeignKey
        salad ForeignKey
        status ForeignKey
        total_price DecimalField
        created_at DateTimeField
        updated_at DateTimeField
    }
    STATUS {
        name CharField
    }
    PAYMENT {
        order ForeignKey
        amount DecimalField
        timestamp DateTimeField
    }
    DELIVERY {
        order ForeignKey
        courier ForeignKey
        address CharField
        status CharField
        delivery_fee DecimalField
        created_at DateTimeField
        updated_at DateTimeField
    }

    PAYMENT ||--|| ORDER : for
    DELIVERY ||--|| ORDER : for
    DELIVERY ||--|| USER : for
    ORDER ||--|| USER : by
    ORDER ||--|{ SALAD : for
    ORDER ||--|| STATUS : of
    COMPONENT ||--|| SALAD : of
    COMPONENT ||--|{ INGREDIENTS : with
    SALAD ||--|| USER : by
    INGREDIENTS ||--|| INGREDIENT_TYPE : of
    USER }|--|{ ROLE : of
```





 - [x] trewtrewy
 - [ ] wetret
 - [ ] List item


```
код
код
код
```

[Contribution guidelines for this project](docs/CONTRIBUTING.md)



1. First list item
   - First nested list item
     - Second nested list item










|                |ASCII                          |HTML                         |
|----------------|-------------------------------|-----------------------------|
|Single backticks|`'Isn't this fun?'`            |'Isn't this fun?'            |
|Quotes          |`"Isn't this fun?"`            |"Isn't this fun?"            |
|Dashes          |`-- is en-dash, --- is em-dash`|-- is en-dash, --- is em-dash|


## KaTeX

You can render LaTeX mathematical expressions using [KaTeX](https://khan.github.io/KaTeX/):

The *Gamma function* satisfying $\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$ is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

> You can find more information about **LaTeX** mathematical expressions [here](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference).


## UML diagrams

You can render UML diagrams using [Mermaid](https://mermaidjs.github.io/). For example, this will produce a sequence diagram:


And this will produce a flow chart:

```mermaid
flowchart TB
    c1-->a2
    subgraph one 
    a1-->a2
    end
    subgraph two 
    b1-->b2
    end
    subgraph three
    id1{{c1}}-->id2[/c2/]
    end
    id4>one] --> id5(two)
    three --> id5(two)
    id5(two) --> c2
    style a2 fill:#f9f,stroke:#333,stroke-width:4px
```

```mermaid
stateDiagram
   direction TB

   accTitle: This is the accessible title
   accDescr: This is an accessible description

   classDef notMoving fill:white
   classDef movement font-style:italic;
   classDef badBadEvent fill:#f00,color:white,font-weight:bold,stroke-width:2px,stroke:yellow

   [*] --> Still:::notMoving
   Still --> [*]
   Still --> Moving:::movement
   Moving --> Still
   Moving --> Crash:::movement
   Crash:::badBadEvent --> [*]
```



```mermaid
journey
    title My working day
    section Go to work
      Make tea: 5: Me
      Go upstairs: 3: Me
      Do work: 1: Me, Cat
    section Go home
      Go downstairs: 5: Me
      Sit down: 5: Me
```


```mermaid
timeline
    title Timeline of Industrial Revolution
    section 17th-20th century
        Industry 1.0 : Machinery, Water power, Steam <br>power
        Industry 2.0 : Electricity, Internal combustion engine, Mass production
        Industry 3.0 : Electronics, Computers, Automation
    section 21st century
        Industry 4.0 : Internet, Robotics, Internet of Things
        Industry 5.0 : Artificial intelligence, Big data,3D printing

```
