The content in this file is same as README.me and cmpt383.txt, you can choose one which you like.

## Guide list:
1.Quike introduction
2.Quike code compile
3.Detailed introduction
    1). Overall goal of the project
    2). Languages using
    3). Methods of communicating between languages
    4). Steps of working the project



## 1. Quike introduction

In my project, there are two parts. Part one is using C++ and Python to do a Covid-19 statistics, Part two is using 
Ruby and Python to create a Pokemon database query. Both two parts can save problems following the Polyglot, they are 
include all the requirements of the project.



## 2. Quike code compile

### The first thing is loading the vagrant.

                            vagrant up
                            vagrant ssh

### There are some packages we should install:

                            pip3 install pandas
                            pip3 install matplotlib

### Part 1:

                            cd project
                            cd swig-Covid19Stat
                            swig -python -py3 -modern  covid_stat.i
                            gcc -fPIC -c  covid_stat.c  covid_stat_wrap.c -I/usr/include/python3.6
                            ld -shared  covid_stat.o  covid_stat_wrap.o -o _covid_stat.so
                            python3 covid19stat_main.pyc
### Part 2: we need two terminal, one for Server, one for Client
                            
### On Server:

                            cd mq-PokemonQuery
                            python3 PokemonQuery_server.py

### On Client:                  

                            cd mq-PokemonQuery
                            ruby PokemonQuery_client.rb
                            
-------------------------------------------------------------------------------------------------------------------

## 3.Detailed introduction

### 1). Overall goal of the project
The overall goal of the project is using different languages cooperate to solve one or more problems.
And I would like to use some of them to solve the problems that I care about. 

Part one is using C++ and Python to do Covid-19 statistics. As we knew, Covid-19 is the biggest problem 
in the world now, it has impacted all of us. I want to do a Covid-19 statistics to see the growth in rate 
my favorite countries Canada, America, New Zealand, and the world. I'm using Python to do the data analysis 
and using the C++ to calculate the growth rate, Python can create a visualization of the growth rate for 
the 4 countries and the world. We can know the status of Covid-19 in this year.

Part two is using Ruby and Python to create a Pokemon database query. I am a big Pokemon fan, thus the reason 
I choose to do this problem. In this part, I am using RabbitMQ to solve the problem. I choose Python as my 
server and Ruby as my client, there is a pokemon database in the Python-server, and my Ruby_client query the 
Pokemon in this bi-directional channel. This is a good experience for me to work with Pokemon.

### 2). Languages using
Part one(Covid-19 statistics): C++, Python
Part two(Pokemon database query): Python, Ruby

### 3). Methods of communicating between languages
Part one(Covid-19 statistics): The foreign function interface by SWIG
Part two(Pokemon database query): RabbitMQ

### 4). Steps of working the project
#### Step1: The first thing is loading the vagrant.
                            vagrant up
                            vagrant ssh

#### Step2: There are some packages we should install:
                            pip3 install pandas
                            pip3 install matplotlib

#### Step3: Part 1:
                            cd project
                            cd swig-Covid19Stat
                            swig -python -py3 -modern  covid_stat.i
                            gcc -fPIC -c  covid_stat.c  covid_stat_wrap.c -I/usr/include/python3.6
                            ld -shared  covid_stat.o  covid_stat_wrap.o -o _covid_stat.so
                            python3 covid19stat_main.py

Then we can get two pnd files of total case number and the growth rate.
![Image](/image/All_total_cases.png)
![Image](/image/all_growth_rate.png)

#### Step4: Part 2: we need two terminal, one for Server, one for Client
##### On Server:
                            
                            cd mq-PokemonQuery
                            python3 PokemonQuery_server.py


##### On Client:                  
                            cd mq-PokemonQuery
                            ruby PokemonQuery_client.rb

In this part, I implement many guide line for you to do a query.

##### for example: 
At the biginning of query, it will ask you to choose key-word:
1. Please enter the pokemon's key words:
2. Name  (Example: Pikachu)
3. Index number  (Example: 25)
4. type  (Example: Grass)
5. Ablity  (Example: =600, >300, <100, >=500, <=80, != 600)
6. Legendary  (Example: legendary, not legendary)


After your query, it will ask you next step:
What do you want to do?
1. I love Pokemon! Do it again!
2. Cheak my history.
3. Quit
4. Save This Query to txt file.
Please enter your number:)


There is no confrused for you to check it, just enjoy it. 

Thanks all of you.