Coach BSK API
=============

A server application for mobile app Coach BSK

## Running

Configure ```run.bash``` file with the next command:
```
./configure.bash
```

Then start server
```
./run.bash
```

## API

### List of methods
| Path             | Method | Description                |
| :--------------- | -----: | -------------------------- |
| **/book**        | POST   | *Create a new book*          |
| **/books**       | GET    | *Return all books*           |
| **/tournament**  | POST   | *Create a new tournament*    |
| **/tournaments** | GET    | *Return all tournaments*     |
---
<br>

### **/book**

Body structure:

| Key            | Type          | Description       |
| :------------- | :------------ | ----------------- |
| **gym**        | string        | *name of the gym* |
| **train_type** | string        | *type of train*   |
| **train_kind** | string        | *kind of train*   |
| **coach**      | string        | *trainer's name*  |
| **date**       | datetime      | *booking date*    |
---
<br>

### **/tournament**

Body structure:

| Key            | Type          | Description              |
| :------------- | :------------ | ------------------------ |
| **name**       | string        | *name of the tournament* |
| **team_1**     | string        | *name of team 1*         |
| **team_2**     | string        | *name of team 2*         |
| **players**    | string        | *players names*          |
| **date**       | datetime      | *tournament date*        |
---