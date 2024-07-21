# Who doesn't love Ya Kun breakfast?
## Overview
Generally, most Python code runs synchronously, meaning that the code executes sequentially, one statement after another. This approach is fine for small-scale, non-load-intensive applications. However, when an application becomes large-scale and load-intensive, running it synchronously can be time-consuming. There are several ways to overcome this, such as asynchronous execution, multithreading, and multiprocessing. In this repository, I will demonstrate asynchronous execution using Ya Kun breakfast as an example. I will cover multithreading and multiprocessing later.

Imagine we are running a Ya Kun store with only one worker. The signature Set A breakfast menu includes a drink, kaya butter toast, and two soft-boiled eggs. Assume it takes 3 seconds, 5 seconds, and 8 seconds to prepare these items, respectively. If a customer orders the set, it will take the worker a total of 16 seconds to make it if the items are prepared sequentially.

However, there is lead time in making the meals. This means that while waiting for the soft-boiled eggs to cook, the worker can prepare the kaya butter toast. Similarly, while waiting for the kaya butter toast to be ready, the worker can make the drink first. When the drink is ready, the toast is almost ready too. When the toast is ready, the eggs are nearly done as well. This approach saves the store a lot of time, reducing the total preparation time to 8 seconds when done asynchronously, compared to 16 seconds when done synchronously—a 50% improvement in the time taken. This is the power of asynchronous execution.

You may refer to the screenshot below for the results and the scripts in the repository for the code.

![image](https://github.com/user-attachments/assets/3d0cf8b9-17db-4b74-8f01-684cbc92ba38)


## Other example
We can also use asynchronous execution for internet requests, such as API calls. In this simple example, I show the time taken to check website status synchronously and asynchronously. It takes about 10 seconds to run synchronously and about 1.5 seconds to run asynchronously, resulting in approximately a 90% improvement in the time taken.

![image](https://github.com/user-attachments/assets/29ccf000-49c8-421b-9d81-2724a5b2424e)
