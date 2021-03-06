import random
import nltk.data
#nltk.download() # first time running the code: uncomment this, click on "models", scroll down to "punkt", double click it

NUM_OF_QUIZ_QUESTIONS = 4

def create_quiz(text1, text2):
    # The tokenizer can split text into sentences while dealing with edge cases like "Mr."
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences1 = tokenizer.tokenize(text1.decode('utf-8'))
    sentences2 = tokenizer.tokenize(text2.decode('utf-8'))

    for i in range(len(sentences1)):
        sentences1[i] = sentences1[i].replace('\n', '')
    for i in range(len(sentences2)):
        sentences2[i] = sentences2[i].replace('\n', '')

    if len(sentences1) < NUM_OF_QUIZ_QUESTIONS or len(sentences2) < NUM_OF_QUIZ_QUESTIONS:
        print("Corpus not long enough.")
        return

    quiz = []
    for i in range(0, NUM_OF_QUIZ_QUESTIONS):
        index1 = random.randint(0, len(sentences1) - 1)
        index2 = random.randint(0, len(sentences2) - 1)

        ele1 = sentences1.pop(index1)
        ele2 = sentences2.pop(index2)

        quiz.append((ele1, ele2))

    return quiz

#if __name__ == "__main__":
# quiz = create_quiz('f1.txt', 'f2.txt')
# pickle.dump(quiz, open('quizzes/1.txt', 'wb'))
