import speedtest

test = speedtest.Speedtest()


def Download_speed():
    speed = round(test.download() / 1_000_000, 2)
    return str(speed) + "Mbps"


def Upload_speed():
    speed = round(test.upload() / 1_000_000, 2)
    return str(speed) + "Mbps"


if __name__ == "__main__":
    print(f"Download Speed :{Download_speed()}")
    print(f"Upload Speed :{Upload_speed()}")
