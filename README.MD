This is an MVP version of library that download amazon order to json file. Currently, this version just support login when
amazon not let client login by captcha.
# Installation
First you should clone this project to you mac or widonws. And you should install python3 and pip3.  
````
git clone 
````
# Usage
You can use command to start run this program.
```
python3 main.py your_email your_password
```
Here is a example. It will auto login and down orders to assert dir.
![img.png](assert/img.png)
![img.png](assert/storage.png)
# TODO
As i say, this is just a MVP version. There are still many features to be done.  
- [ ] login with captcha
- [ ] abstract code with form class to support login
- [ ] add logging to replace print
- [ ] query orders use page number
- [ ] extract more info about order info
- [ ] add conf file support config some features
- [ ] add unit tests
- [ ] support logout
- [ ] process exception
# Tech Design