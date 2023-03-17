# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 17:48:15 2022

@author: anil_
"""


from data import question_data as questions_dic 
from question_model import Question

question_bank = []

for question in questions_dic:
    q_text = question['text']
    q_ans = question['answer']
    new_q = Question(text=q_text, answer=q_ans)
    question_bank.append(new_q)

print(question_bank)







## Testing code
# class User:
#     def __init__(self, user_id, username):
#         print('New user is created')
#         self.id = user_id
#         self.user_name = username
#         self.followers = 0
#         self.following = 0
        
#     def follow(self, user):
#         user.followers = +1
#         self.following = +1
        

# user_1 = User('01', 'Ravi')

# user_2 = User('02', 'Raj')

# user_2.user_name = 'Raj1'

# print(user_1.id, user_1.user_name)

# print(user_2.id, user_2.user_name)

# user_1.follow(user=user_2)

# user_2.fname = 'Sri'
# print(user_2.id, user_2.user_name, user_2.fname)

# print(user_1.followers, user_1.following)

# print(user_2.followers, user_2.following)