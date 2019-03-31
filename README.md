# miniScheduler

## Requirement
Language and library facilities used in this repository are intentionally restricted within [The Python Language](https://docs.python.org/3/reference/index.html) and [The Python Standard Library](https://docs.python.org/3/library/index.html).
So, the only requirement for running and using this repository is a standard [Python 3.4+](https://www.python.org/downloads/) environment.

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
