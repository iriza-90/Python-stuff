def set_alarm():
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    alarm_hour, alarm_minute = map(int, alarm_time.split(":"))

    while True:
        current_time = input("Enter the current time in HH:MM format: ")
        current_hour, current_minute = map(int, current_time.split(":"))

        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("Time to wake up!")
            for _ in range(10):  # Play 10 beeps as the alarm sound
                print("\a")  # This will create a beep sound on most systems
            break
        else:
            print("Not yet time for the alarm. Keep waiting...")

set_alarm()
