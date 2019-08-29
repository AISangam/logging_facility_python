# logging_facility_python  

![Screenshot_log](https://user-images.githubusercontent.com/35392729/63938693-126a6580-ca83-11e9-963f-8f8a36511dec.png)

## Why logging is needed  
logs are created so that when we run our code, we can assure that each step is executed properly. If you are on the local system then you have the option of doing debugging usin various options but just realize when you are on the server and executed the cron job. Any time you can see the functionality of the code using the log file. I hope you may get more wider view why log file is needed.  

## How to use it  

First import it using the below code 
```
import logging 
```

Now you can create the log file with year-month-date hours:minutes:seconds using the below command
```
# you can choose any name
logging.basicConfig(filename='ThisFile.log',
                    level=logging.INFO,
                   format='%(asctime)s - %(message)s')
```

I hope this step is also clear. 
                   
## Use of logging in the code  

```
def logging_answers(index, answer):
    logging.info("Answer to story with index {} is {} ".format(index, answer))

logging.info("logging is over for three stores")

```  

## How to run this code  

```
python logging_facility.py
```

Thanks for reading this post

## To learn about using git, you can refer to the below tutorials  

[Getting Started with git step by step part 1 ai sangam](http://www.aisangam.com/blog/getting-started-with-git-step-by-step-part-1-ai-sangam/)  


[gitignore, git diff, checkout and reset HEAD Git Part 2 | AI Sangam](http://www.aisangam.com/blog/gitignore-git-diff-checkout-and-reset-head-git-part-2-ai-sangam/)


