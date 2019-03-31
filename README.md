# miniScheduler

## Demo
First, prepare a text file, e.g. [`todo_list.txt`](./todo_list.txt), which contains your tasks and their prerequisites.
To schedule the tasks listed in [`todo_list.txt`](./todo_list.txt), run the following command:
```shell
python3 scheduler.py < todo_list.txt
```
which should give the following result:
```shell
Independent Task Group 1:
  A
  B
  C
Independent Task Group 2:
  1
  2
  3
```

## Code Style
In this repo, we adopt [PEP 8](https://www.python.org/dev/peps/pep-0008/) as our code style and use [`pylint`](https://www.pylint.org) to check the conformance. 
