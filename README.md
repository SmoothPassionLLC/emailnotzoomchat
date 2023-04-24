# emailnotzoomchat
EmailNotZoomChat: Enjoy Shorter Video Calls!
Introducing EmailNotZoomChat, a Python program designed for those who appreciate concise work-related video calls. This program helps manage the duration of Zoom and Google Meet calls by sending friendly reminders to wrap up the call and automatically closing it if it goes beyond the set duration. Supporting Zoom, Google Meet in Firefox, and Google Meet in Brave browsers, it's perfect for keeping your video calls short and sweet.

A Delightful Experience with EmailNotZoomChat
EmailNotZoomChat offers a range of features to keep your video calls on track:

Always on the lookout for Zoom and Google Meet calls
Sends a gentle reminder to close the video call after the specified time
Closes the video call with a smile if it overstays its welcome
Suggests using email for those longer conversations
Reopens the Zoom application with a spring in its step after wrapping up a call
Welcomes Zoom, Google Meet on Firefox, and Google Meet on Brave browsers with open arms
How EmailNotZoomChat Spreads Joy
The program constantly scans for open video call windows. When it finds one, it counts down the specified duration before sending a friendly reminder to close the call. If the video call window remains open past the additional waiting period, the program cheerfully closes the window, kindly proposing the user switch to email for those longer chats.

EmailNotZoomChat is a versatile friend, handling Zoom and Google Meet calls with ease. For Google Meet, it can detect and close calls in Firefox and Brave browsers.

Let the Fun Begin
To join the EmailNotZoomChat party, simply run the Python script. The program will start monitoring for video call windows and gracefully take action based on the specified durations and intervals.

Make EmailNotZoomChat Your Own
You can personalize the program by adjusting the following variables in the main() function:

video_call_check_interval: The frequency, in seconds, of checking for video call windows
reminder_duration: The countdown, in seconds, before sending a reminder notification to close the video call
time_to_wait: The total waiting time, in seconds, before automatically closing the video call window
reopen_delay: The pause, in seconds, before reopening the Zoom application or restarting the monitoring loop
You can also extend a warm welcome to other browsers by adding their names and titles to the browsers list.
