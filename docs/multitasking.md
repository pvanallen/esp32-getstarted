## Multitasking in Micropython

In physical computing projects it is often necessary to do more than one thing at a time -- such as blink an LED while reading a sensor. In Python, this is accomplished using the concept of "threads" which represents the idea that we can separate our project into different tasks (or threads) that run in parallel at the same time. In other words, multitasking.

We define each thread task by creating a function definition ("def") that does everything needed for that task. In our first example, we define two threads, one (blink1) which blinks an LED at one rate, and a second (blink2) which blinks a different LED at a different rate.

After defining them, we can then start each thread so it runs in the background using the "start\_new\_thread" function.

Note that these examples use the \_thread module of Python rather than Threads module. This is because \_thread is standard for Microphython, while Threads is not.

### [blink\_2leds.py](examples/blink_2leds.py)

This example demonstrates the use of two different functions that become threads and run independently. They use a single argument to determine the time for each blink. They terminate when the corresponding variable is set to false (either blink1_running or blink2_running).

Once the two different LED blink threads are started, the main line code "does work" by counting to 10. Once complete, it terminates the threads.

### [fade\_2leds.py](examples/fade_2leds.py)

This example is similar to the above, but uses PWM to fade leds up and down at a variable rate. It also using a single function fade() for both LEDs, simplifying the code.

The resulting threads are terminated differently though. Instead of using a simple variable, the code uses a function to determine when the thread should terminate.
