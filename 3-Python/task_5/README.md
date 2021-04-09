# Task 5

> Develop a function that takes a list of integers (by idea not in fact) as an argument and returns 
> list of top-three max integers. If passed list contains not just integers collect them and print the 
> following error message: You've passed some extra elements that I can't parse: [<"elem1", "elem2" .... >]. 
> If return value will have less than 3 elements for some reason it's ok and shouldn't cause any problem, but 
> some list should be returned in any case.

**top3Max (*list*) --> *list*, *list***

Return 2 lists: list of top 3 max numbers and list element's, that couldn't be parsed.
If no numbers or no extra elements are given, returns empty corresponding list.

## Examples:

1. Input argumets - list of numbers. Prints top 3 max numbers and doesn't print empty list of extra elements:

    ![Screenshot_7](https://user-images.githubusercontent.com/40645030/113492929-e5462a80-94e3-11eb-8526-3c04a0220b1a.png)

2. Input argumets - list of mixed numers and extra elements. Print only 2 numbers (ordered), because there is no more numbers, and prints one extra element:

    ![Screenshot_8](https://user-images.githubusercontent.com/40645030/113492935-eaa37500-94e3-11eb-8afa-ca0992e6a81a.png)

3. Input argumets - list of strings. Reports that there is no numbers in given list (returned list of top numbers is also empty) and list of extra elements:

    ![Screenshot_9](https://user-images.githubusercontent.com/40645030/113492937-eecf9280-94e3-11eb-9974-5e71330a1ce1.png)

4. Input argumets - string. Processes provided string as a *list of symbols*, reports that there is no numbers and each symbol of the string is processed as a single extra element:

    ![Screenshot_10](https://user-images.githubusercontent.com/40645030/113492940-f1ca8300-94e3-11eb-917c-28bc39aa5438.png)

5. Input argumets - number. Reports error message, because provided argument's type is not a *list*. Down below there is output of 2 returned lists: list of top 3 max numbers and list element's, that couldn't be parsed (both are empty):

    ![Screenshot_11](https://user-images.githubusercontent.com/40645030/113492944-f55e0a00-94e3-11eb-987e-5f8baedb6a1c.png)

