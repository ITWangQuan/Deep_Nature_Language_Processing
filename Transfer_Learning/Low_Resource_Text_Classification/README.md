# Low Resource Text Classification
This project will deal with data from the Equal Community Foundation:  http://ecf.org.in/. They work with adolescent boys in India to support them in becoming gender equitable adults. They have developed and implement behaviour change programmes and their mission is to raise every boy in India to be gender equitable. In order to extend their programs, they need a way to automatically measure the impact of their interventions. They have developed a survey which consists of ten questions which probe the boys' attitude to violence, masculinity and gender roles. The boys answer these questions with free text, usually a couple of sentences and these sentences are graded from 0 to 3 in terms of how aware and how egalitarian their attitudes are. The grading of these answers needs to be automated but there is very little training data. This project will investigate how to adapt low-resource deep learning techniques such as transfer learning and curriculum learning to this task.


**Requirements:**

* Python 3
* TensorFlow >= 1.4
* nltk


**1. pre train word embedding(optional):**
  ```
  python train_skip.py
  ```
**2. pre train C-LSTMs:**
  ```
  python main.py --pretrain true
  ```

**3. fine tune C-LSTMs:**
  ```
  python main.py --pretrain false
  ```
