"""
კითხები ჩაწერილია questions.txt ფაილში. შემდეგი ფორმატით: კითხვა;A;B;C;D;სწორი პასუხი.
ჩვენ ეს მონაცემები უნდა წავიკითხოთ და უნდა ჩავწეროთ ჩვენთვის საჭირო მონაცემთა სტრუქტურაში.
მომხმარებელს ეკრანიდან შემოაქვს საკუთარი სახელი და კითხვების ოდენობა.
შემთხვევითი ავარჩიოთ სასურველი ოდენობის კითხვებს.
შევამოწმოთ მომხმარებლის პასუხები სწორია.
საბოლოო შედეგს ჩავწერთ data.txt ფაილში.
"""
import random
class test:
    def name_questions(self):
        print("Test Started")
        self.name = input('write your name: ')
        self.questions = []
        self.n = int(input('number of questions = '))

    def readquestions(self):
        f = open('questions.txt', 'r')
        N = int(f.readline())
        for i in range(0,N+1):
            self.questions.append(f.readline().replace('\n',''))

    def testing(self):
        # choosing random numbers and counter for question numbers and correct questions
        question_numbers = random.sample(range(0, len(self.questions)), self.n)
        cnt = 0 # სწორი პასუხების მთვლელი
        qnum = 1 # კითხვების დასანომრი

        f = open(f'{self.name}.txt', 'w')
        f.write(f'{self.name}\n{self.n} questions:\n\n')

        # getting questions and answers
        for i in question_numbers:
            q, a, b, c, d, v = self.questions[i].split(';')
            answer_choices = {'a': a, 'b': b, 'c': c, 'd': d}
            question = (f'\n{qnum}) {q}\na. {a}\nb. {b}\nc. {c}\nd. {d}\n')
            answer = input(f'{question}\nyour choice: ')

            f.write(f'{question}\nchoosed answer: {answer}\ncorrect answer: {v}\n')

            if answer in answer_choices and answer_choices[answer] == v:
                print("Correct!\n")
                cnt += 1
            else:
                print("Incorrect.\n")
            qnum += 1
        f.close()

        # Calculating the score
        percentage = (cnt / self.n) * 100
        results = f'{self.name}: {percentage}% ({cnt}/{self.n})'
        print(results)
        #saving result to file
        s = open('data.txt', 'a')
        s.write(f'{results}\n')
        s.close()

test = test()
test.name_questions()
test.readquestions()
test.testing()
