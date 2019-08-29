# libraries are imported
import logging
import os

# variables
current_path = os.getcwd()
file_ = os.path.join(current_path, 'qa1_single-supporting-fact_test.txt')

logging.basicConfig(filename='ThisFile.log',
                    level=logging.INFO,
                   format='%(asctime)s - %(message)s')


# function to split the question and answer
def ques_ans_split():
    question, answer, supporting = each_line.split('\t')
    return answer


# function to logging answers according to index
def logging_answers(index, answer):
    logging.info("Answer to story with index {} is {} ".format(index, answer))

fetched_story = list()
with open(file_) as f:
    story = list()
    for line in f:
        line_id, line = line.split(' ', 1)
        if int(line_id)==1:
            story = list()
        fetched_story.append(line)  
        if len(fetched_story) == 45:
            break  

# print(fetched_story)        

print("Showing the first three stories:")
print()
for index, each_line in enumerate(fetched_story):
    print(index, each_line)
    if index == 14 or index == 29:
        print("Answer to the story is:", end=" ")
        answer = ques_ans_split()
        # logging.info("Answer to story with index {} is {} ".format(index, answer))
        logging_answers(index, answer)
        print(answer)
        print()
        print("Story is completed and next is started....")
        print()
        print(100*'=')
    elif index == 44:
        print("Three stories are being completed.....")
        print()
        print(100 * '*')
        print("Answer to the Last story is:", end=" ")
        answer = ques_ans_split()
        # logging.info("Answer to story with index {} is {} ".format(index, answer))
        logging_answers(index, answer)
        print(answer)
        logging.info("logging is over for three stores")
        logging.info("************************************************************")
        
 