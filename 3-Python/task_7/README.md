# Task 7

> Develop a procedure that will have a size argument and print a table where num of columns and rows 
> will be of this size. Cells of table should contain numbers from 1 to n ** 2 placed in a spiral fashion. 
> Spiral should start from top left cell and has a clockwise direction (see the example below).
> 
> example:
> 
>  ```
>  >>>print_spiral(5)  
>  1 2 3 4 5   
>  16 17 18 19 6   
>  15 24 25 20 7   
>  14 23 22 21 8
>  13 12 11 10 9
>  ```


To use this module before calling python make following command in /bin/bash:

 ```
 export PYTHONPATH=/path/to/task_7.py
 ```
 
 ![Screenshot_13](https://user-images.githubusercontent.com/40645030/113493217-1de70380-94e6-11eb-8f3f-3bfad4ba2f7b.png)
 
Now it's available in sys.path:
 
 ![Screenshot_14](https://user-images.githubusercontent.com/40645030/113493221-23444e00-94e6-11eb-9b3e-3d0514321207.png)

 
Then in python3 (or in your python script) import it and use:
 
 ```
 >>> from task_7 import print_spiral
 >>> print_spiral(7)
 ```   
 
 ![Screenshot_15](https://user-images.githubusercontent.com/40645030/113493228-35be8780-94e6-11eb-8c2b-2cd92d6dc883.png)
