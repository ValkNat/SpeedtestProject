#imports
import speedtest

st = speedtest.Speedtest()

class TestSpeed:
    def testSpeed():
        download_speed = int(st.download()) / (1024 * 1024)
        upload_speed = int(st.upload()) / (1024 * 1024)
        print(f"Download speed: {download_speed} Mb / Second")
        print(f"Upload speed: {upload_speed} Mb / Second")
    def testPing():
        servers = []
        st.get_best_server()
        ping = st.results.ping
        print(f"Ping: {ping} ms")


test_being_run = int(input("Would you like to test: speed (1) or ping (2)? "))

if test_being_run == 1:
    TestSpeed.testSpeed()

elif test_being_run == 2:
    TestSpeed.testPing()

else:
    print("Error: Please type 1 or 2")


