# Stupid Furbo!

The goal of this project started as a way to make a cheaper and (maybe) better home monitoring system for your pets as an alternative to products such as Furbo. 
The eventual goal is to be able to start with a basic, pretrained TensorFlow model and be able to retrain the model based data collected while observing your pets. 

Instead of using a hosting service such as AWS or Azure to host the application, we will be setting up a raspberry pi as a local server within your house.

*NOTE* This project will only contain code for hosting this on your local network via a Flask application. Exposing this application to be public facing is totally possible, but I suggest doing some serious research on the security risks involved before doing so.

## Setup

This will show you how to get started with this project. 

### Required Hardware:

- Raspberry Pi 4
- SparkFun Pi Servo pHAT [purchase link](https://www.sparkfun.com/products/15316?gclid=EAIaIQobChMIoqTM3uLrgAMVty7UAR2TdwptEAQYAiABEgJgxfD_BwE)
- USB Camera
- Coral TPU USB Accellerator [purchase link](https://www.amazon.com/Google-Coral-Accelerator-coprocessor-Raspberry/dp/B07R53D12W/ref=asc_df_B07R53D12W/?tag=hyprod-20&linkCode=df0&hvadid=343187928868&hvpos=&hvnetw=g&hvrand=13988579024015021863&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9011657&hvtargid=pla-757749808211&psc=1&tag=&ref=&adgrpid=68968886357&hvpone=&hvptwo=&hvadid=343187928868&hvpos=&hvnetw=g&hvrand=13988579024015021863&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9011657&hvtargid=pla-757749808211)
- USB GamePad Controller (optional) I am using one of [these.](https://www.amazon.com/Controller-Compatible-iNNEXT-Raspberry-Multicolored/dp/B07MBF7FN1/ref=asc_df_B07MBF7FN1/?tag=hyprod-20&linkCode=df0&hvadid=385599530796&hvpos=&hvnetw=g&hvrand=4348866700891449236&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9011657&hvtargid=pla-802012327430&psc=1&tag=&ref=&adgrpid=76783608457&hvpone=&hvptwo=&hvadid=385599530796&hvpos=&hvnetw=g&hvrand=4348866700891449236&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9011657&hvtargid=pla-802012327430)


### Required Software:

- OpenCV 4.8.0
- Tensorflow
- Flask
- See `requirements.txt` for extensive list.
