import csv
import speedtest

st = speedtest.Speedtest()

class TestSpeed:
    def testSpeed():
        download_speed = f"Download speed: {int(st.download()) / (1024 * 1024)} Mb/s"
        upload_speed = f"Upload speed: {int(st.upload()) / (1024 * 1024)} Mb/s"
        print(download_speed)
        print(upload_speed)
        log_to_file = input("Log to file? [y/n]: ")
        if log_to_file == 'y':
            TestSpeed.logToFile(download_speed, upload_speed)
        elif log_to_file == 'n':
            print("Not saving to CSV...")
        else:
            print("Format error!")
    def testPing():
        servers = []
        st.get_best_server()
        ping = f"{st.results.ping} ms"
        print(f"Ping: {ping} ms")
        log_to_file = input("Log to file? [y/n]: ")
        if log_to_file == 'y':
            TestSpeed.logToFile(ping)
        elif log_to_file == 'n':
            print("Not saving to CSV...")
        else:
            print("Format error!")

    def logToFile(*data):
        parameters = []
        with open('speed_data.csv', mode='a', encoding='UTF-8', errors='strict', buffering=1) as file:
            for i in data:
                parameters.append(i)
            for i in parameters:
                file.write(i)


test_being_run = int(input("Would you like to test: speed (1) or ping (2)? "))

if test_being_run == 1:
    TestSpeed.testSpeed()

elif test_being_run == 2:
    TestSpeed.testPing()

else:
    print("Error: Please type 1 or 2")


