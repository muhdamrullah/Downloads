Emotion-Recog
=======

_Recognizing emotional states in faces_

----------------------------------------------

Authors: Muhd Amrullah

Contributors: Jonathan Leo

Development Status: Experimental 

Copyleft: [CC-BY-NC 2013](http://creativecommons.org/licenses/by-nc/3.0/)

----------------------------------------------

## Goal
This project aims to recognize main facial expressions (neutral, anger, disgust, fear, joy, sadness, surprise) in image
sequences using the approaches described in:

* [Dynamics of Facial Expression Extracted Automatically from Video](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=1384873)
* [Fully Automatic Facial Action Recognition in Spontaneous Behavior](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=1613024)

## References

Here is listed some interesting material about machine learning, opencv, gabor transforms and other
stuff that could be useful to get in this topic:

 * [AdaBoost and the Super Bowl of Classifiers](http://www.inf.fu-berlin.de/inst/ag-ki/rojas_home/documents/tutorials/adaboost4.pdf)
 * [Tutorial on Gabor Filters](http://mplab.ucsd.edu/tutorials/gabor.pdf)
 * [Gabor wavelet transform and its application](http://disp.ee.ntu.edu.tw/~pujols/Gabor%20wavelet%20transform%20and%20its%20application.pdf)
 * [Gabor Filter Visualization](http://www.cs.umd.edu/class/spring2005/cmsc838s/assignment-projects/gabor-filter-visualization/report.pdf)
 * [Meta-Analyis of the First Facial Expression Recognition Challenge](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6222016)

## Project Structure

    Emotions
      \-->Angry 		 jpg photos training for Anger
      \-->Disgust 	 jpg photos training for Disgust
      \-->Fear		   jpg photos training for Fear
      \-->Happy 		 jpg photos training for Happy
      \-->Neutral    jpg photos training for Neutral
      \-->Sad        jpg photos training for Sad
      \-->Surprise   jpg photos training for Surprise
    faceRecogEmotion            
      \-->Angry.py 		 Python script to send to GA for Anger
      \-->Disgust.py 	 Python script to send to GA for Disgust
      \-->Fear.py		   Python script to send to GA for Fear
      \-->Happy.py 		 Python script to send to GA for Happy
      \-->Neutral.py   Python script to send to GA for Neutral
      \-->Sad.py       Python script to send to GA for Sad
      \-->Surprise.py  Python script to sent to GA for Surprise
      emotion.csv      A self-generated csv file to categorise emotions and to be trained on
      faceReco.cpp     C++ code that contains the emotion recognition script
      reco             Executable Program
      CMakeFiles       An important CMAKE folder that is generated during compiling
      CMakeLists.txt   A .txt file that contains the compile code to be used for cmake .


## Build

Dependencies:

* `CMake >= 2.8`
* `Python >= 2.7, < 3.0`
* `OpenCV >= 2.4.5`

Compiling on linux:

* `cd Downloads`
* `git clone git://github.com/bytefish/libfacerec`
* `cmake .`
* `make`
* `cd faceRecogEmotion`
* `cmake .` - now the reco file should be generated

### Usage

Video gui:

    ./reco emotion.csv 4500   
    <executable file> <.csv of choice> <prediction number where the number goes from 100 - 10000>


### Dataset

The [Cohn-Kanade database](http://www.consortium.ri.cmu.edu/ckagree/) is one of the most used faces database. Its extended version (CK+) contains also [FACS](http://en.wikipedia.org/wiki/Facial_Action_Coding_System)
code labels (aka Action Units) and emotion labels (neutral, anger, contempt, disgust, fear, happy, sadness, surprise).

## ~~Validation~~ (old, check v1.2 release page)

_First, rough evaluation of the performance of the system_ 
Validation test involved the whole system `face detector + emotion classifier`, so should not be considered relative to the _emotion classifier_ itself. 

Of course, a more fine validation shuld be tackled in order to evaluate emotion classifier alone.
For the sake of completeness the reader have to know that the haarcascade_frontalface face model is a good face locator rather than detector, roughly speaking it detects less but is more precise.

Following results are commented with my personal - totally informal - evaluation after live webcam session.

```text
multicalss method: Eigen Face Recognizer 
face detector:     haarcascade_frontalface_alt.xml
eye correction:    no 
width:             48
height:            48 
nwidths:           3 
nlambdas:          5
nthetas:           4

Sadness                   <-- Not good in live webcam sessions too
  sadness -> 0.67%
  surprise -> 0.17%
  anger -> 0.17%
Neutral                   <-- Good in live webcam sessions
  neutral -> 0.90%
  contempt -> 0.03%
  anger -> 0.03%
  fear -> 0.02%
  surprise -> 0.01%
Disgust                   <-- Good in live webcam sessions
  disgust -> 1.00%
Anger                     <-- Good in live webcam sessions
  anger -> 0.45%
  neutral -> 0.36%
  disgust -> 0.09%
  contempt -> 0.09%
Surprise                  <-- Good in live webcam sessions
  surprise -> 0.94%
  neutral -> 0.06%
Fear                      <-- Almost Good in live webcam sessions
  fear -> 0.67%
  surprise -> 0.17%
  happy -> 0.17%
Contempt                  <-- Not good in live webcam sessions
  neutral -> 0.50%
  contempt -> 0.25%
  anger -> 0.25%
Happy                     <-- Good in live webcam sessions
  happy -> 1.00%
```

```text
multicalss method: Fisher Face Recognizer
face detector:     haarcascade_frontalface_alt.xml
eye correction:    no 
width:             48
height:            48 
nwidths:           3 
nlambdas:          5
nthetas:           4

Sadness                   <-- Not good in live webcam sessions too
  unknown -> 0.50%
  sadness -> 0.33%
  fear -> 0.17%
Neutral                   <-- Good in live webcam sessions 
  neutral -> 0.73%
  unknown -> 0.24%
  surprise -> 0.01%
  fear -> 0.01%
  contempt -> 0.01%
Disgust                   <-- Good in live webcam sessions
  disgust -> 0.82%
  unknown -> 0.18%
Anger                     <-- Almost sufficient in live webcam sessions
  anger -> 0.36%
  neutral -> 0.27%
  unknown -> 0.18%
  disgust -> 0.09%
  contempt -> 0.09%
Surprise                  <-- Good in live webcam sessions
  surprise -> 0.94%
  neutral -> 0.06%
Fear                      <-- Sufficient in live webcam sessions
  fear -> 0.67%
  surprise -> 0.17%
  happy -> 0.17%
Contempt                  <-- Not good in live webcam sessions too
  unknown -> 1.00%
Happy                     <-- Good in live webcam sessions 
  happy -> 1.00%
```

Also main difference between the Eigen Face Recognizer and the Fisher Face Recognizer mode experimented in livecam sessions are related to the amount of unknown states registered and the stability of the detected states.
In detail Fisher Face Recognizer multiclass method provide more less noisy detections during a live web-cam session, Eigen Face Recognizer mode instead is able to always predict a valid state for each frame processed, but sometimes it result to be more unstable during the expression transition.


Sorry for the lack of fine tuning and detail, but it is a spare time project at the moment..
If you have any idea or suggestion feel free to write us!


## Further Development

* Tuning GaborBank parameters for accuracy enhancement.
* Tuning image sizes for better real-time performance.
* Better handle illumination, detections are good when frontal light is in place (keep it in mind when you use it with your camera).
