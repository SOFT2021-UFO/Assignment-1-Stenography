# UFO - Assignment Work log & Steganography Challenge
- Jonatan Bakke https://github.com/JonatanMagnusBakke
- Jonas Hein - https://github.com/Zenzus
- Thomas Ebsen - https://github.com/Srax 
- [Exercise Link](https://datsoftlyngby.github.io/soft2021spring/UFO/week-05/#1-introduction-to-exploration-and-presentation)


## Homework Assignment
In order to look at self reflection and to judge your assessment of information, you should solve the programming exercise below.

However - the important thing in this exercise is how you solved it, not the end result.

At the end of the programming exercise you should have:

* A list of all search queries you made to solve it, and timestamps (just copy it from the browser history)
* A list all pages you visited to solve it (just copy it from the browser history)
* A list of the 3 biggest stumbling blocks you came across and your reflection on why they were problematic (did you misunderstand something, was some of the info you found wrong, did you miss a detail, …)
* A brief "every 30 min" diary as explained in the slides (this is more frequent than one would normally do, and is just meant as part of the exercise)

### List of all search quaries we did to solve it
[Here is a link to all our search queries](https://docs.google.com/document/d/1m8zRuxxQiVdPDvkXZb9YRje8edSh46jnw3XctwncNTM)

### Three biggest stumbling blocks
Figuring what the problem description was telling us  
Figuring out how to use python  
Figuring out how to convert bit to byte to ascii and reversing/little-endian (Just python stuff)  

**Solutions**
The homework description was hard to read and understand.   

When we started googling the problem most of the solutions/helps to solving the problem was made with python. So since none of us had any experience using python we had an initial problem in learning python.  

When we figured out the basics of python, like how to install and run a python file we then got some help from one of our classmates. He showed us how to do some tricks with easy converting byte to ascii chars and reversing the order of arrays.     


## Diary
### 30 minutes
First 30 minutes consisted of us being confused about how exactly we were supposed to clear the stenography exercise.  
Every encoder/decoder we found did not work, which discouraged us a bit.  

### 60 minutes
After some research and conversing with a classmate we now know how we are supposed to clear the assignment.  

Since we are all python noobs, most of these 30 minutes were spent setting up python and getting a better understanding of how to use the language and setup the environment.  

## 1 hour 30 minutes
We found a python library called Pillow which can be used to process images.
With Pillow, we “open” the image, and extract all the bytes from it’s blue RGB channel into an array of bits.  

After that we take the least significant bit of all the values in the array and convert them into new objects of 8 bits each, which becomes a bytearray, because we need 8 bits for a byte.  

After that we have to reverse the byte array because Martin bamboozled us, when he encoded the image.  

To get the message from the byte array, we iterate through every byte object and convert them to binary, till we reach the null-byte “00000000”.  

We can then convert binary to ascii characters and get the message: “Congratulations, this is the secret message of the UFO class! (no, not 42)”  


## Question to be investigated
<img src="./misc/exercise.png">

## How to run
1. Clone the project
2. You need pythong to run this project, download it [here](https://www.python.org/downloads/)  
3. Open a `CMD`and navigate to the root of the project folder
4. Run command `py program.py`
5. You should now see the message: **`Congratulations, this is the secret message of the UFO class! (no, not 42)`**

