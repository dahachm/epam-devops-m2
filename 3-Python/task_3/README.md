# Task 3

> Self-study positional arguments for Python scripts (sys.argv). 
> Write a script that takes a list of words (or even phrases). 
> Script should ask a user to write something to stdin until 
> user won't provide one of argument phrases.



  At first stage, a dictionary of pass words and phrases is created. This dictionary contains all the words from arguments list and their 
  combination in *direct order* of any possible length. E.g., from the list **['a', 'b', 'c']** the following dictionary will be created: 
  **['a', 'a b', 'a b c', 'b c']**, so there is no **'a c'** combination as this chars don't stand together.

  Thus, any number of words (in direct order) from arguments list can be accepted as a secret word/phrase.
  
## Examples:

1. Any word from arguments list can be accepted:
  
    ![Screenshot_3](https://user-images.githubusercontent.com/40645030/113492125-3bb06a80-94de-11eb-8ae1-96e0fed930c6.png)
  
2. Some words from the list, that stand together, also can be accepted:

    ![Screenshot_4](https://user-images.githubusercontent.com/40645030/113492137-423ee200-94de-11eb-88d8-1d9d356ea63f.png)

3. Some words from the list, that do not stand together, won't be accepted:

    ![Screenshot_5](https://user-images.githubusercontent.com/40645030/113492140-49fe8680-94de-11eb-8069-44868669f1a7.png)
