## Slide 1
IoT network & service
HardCopyWorld.com 
3장. Part1. 클래식 블루투스


## Slide 2
3장. Part1. 클래식 블루투스

  3-1. 블루투스 소개
  3-2. 모바일 – 센서장치 classic BT 통신
  3-3. 센서장치 – 서버 classic BT 통신
  3-4. 모바일 – 모바일 classic BT 통신
Contents


## Slide 3
블루투스 소개
블루투스
1994년 에릭슨 개발, 2000년대 본격 사용 시작
3-1


## Slide 4
블루투스 소개
블루투스
2.4GHz 주파수 대역
Classic BT(79개 채널), BLE(40개 채널, 3개의 broadcast)
주파수 호핑 (frequency hopping)
다수의 채널 사이를 특정 순서에 따라 이동하면 데이터를 분할 전송하는 방법
기기간 주파수 간섭에 대응 가능 
초당 1600(800)번 호핑
마스터 기기가 생성한 호핑 패턴에 슬레이브 기기가 동기화
3-1


## Slide 5
블루투스 소개
프로파일
Slave 장치 종류를 인식할 수 있도록 만든 표준
2Byte UUID 로 구분

HSP (Headset Profile, 0x1108)
HFP (Hands-Free Profile, 0x111E)
A2DP (Advanced Audio Distribution Profile, 0x110A)
HID (Human Interface Device, 0x1124)
SPP (Serial Port Profile, 0x1101)
Profile 테이블 참고 : https://goo.gl/pVoEui
3-1


## Slide 6
3장. Part1. 클래식 블루투스

  3-1. 블루투스 소개
  3-2. 모바일 – 센서장치 classic BT 통신
  3-3. 센서장치 – 서버 classic BT 통신
  3-4. 모바일 – 모바일 classic BT 통신

Contents


## Slide 7
모바일-센서장치 클래식 BT 통신
Android BT Master – HC-06 BT Slave
실습 예제


## Slide 8
모바일 - 센서장치 Classic BT 통신
테스트 목표
아두이노와 모바일 폰이 BT로 연결
상호 채팅 구현
Serial/USB
Serial
Bluetooth
3-2


## Slide 9
모바일 - 센서장치 Classic BT 통신
블루투스 (HC-06) 모듈
Serial 지원 블루투스 통신 모듈
Slave/Master/Dual 모듈
Bluetooth 2.0 지원, 2.4GHz 안테나 내장

Serial 통신 지원
시리얼로 받은 데이터를 BT로 송신 (반대로도 동작)
아두이노와 TX-RX, RX-TX 크로스 해서 연결

간단한 사용법
전원만 넣어도 자체 동작이 가능
FTDI (USB to UART) 모듈을 이용해서 PC, 라즈베리파이와 연결 후 설정 및 사용가능
3-2


## Slide 10
모바일 - 센서장치 Classic BT 통신
아두이노와 연결

3-2


## Slide 11
모바일 - 센서장치 Classic BT 통신
Echo 예제 아두이노에 업로드
PC와 블루투스 모듈이 통신할 수 있도록 아두이노가 중계
PC  아두이노  블루투스
블루투스  아두이노  PC
3-2


## Slide 12
모바일 - 센서장치 Classic BT 통신
소스 코드
예제소스\3_2_ClassicBt_Arduino_Android\Arduino\Bt_Usb_Echo
#include <SoftwareSerial.h>
SoftwareSerial BTSerial(2, 3); //Connect HC-06. Use your (TX, RX) settings
void setup()  {
  Serial.begin(9600);
  Serial.println("Hello!");
  BTSerial.begin(9600);  // set the data rate for the BT port
}

void loop() {
  // BT –> Data –> Serial
  if (BTSerial.available()) {
    Serial.write(BTSerial.read());
  }
  // Serial –> Data –> BT
  if (Serial.available()) {
    BTSerial.write(Serial.read());
  }
}
라이브러리 include
라이브러리 초기화



BT에서 받은 데이터가 있으면
데이터를 읽어서 PC로 전달



PC에서 받은 데이터가 있으면
데이터를 읽어서 BT로 전달
3-2


## Slide 13
모바일 - 센서장치 Classic BT 통신
AT command 사용 방법
Serial Monitor 창에서 command 입력 후 응답을 확인
블루투스 모듈 초기 설정
Name=????, Password=1234, BAUD RATE=9600

Serial Monitor 창에서 command 입력 후 응답을 확인
AT → OK
AT+VERSION → OKLinvorV1.8

장치명 변경
AT+NAMExxxx (mybt01 로 변경 한다면... AT+NAMEmybt01)
3-2


## Slide 14
모바일 - 센서장치 Classic BT 통신
아두이노 - 안드로이드 연동
HC-06 모듈과 안드로이드 폰을 블루투스로 연결
페어링 & 연결 된 상태에서는 PC 의 데이터가 폰까지 전달됨
Paired & Connected
3-2


## Slide 15
모바일 - 센서장치 Classic BT 통신
안드로이드 앱 설치 및 테스트
설치 방법
Google Play Store 에서 “BT Chat 아두이노” 검색


테스트 순서
1. 아두이노를 켜서 HC-06 슬레이브 모듈이 페어링 대기상태에 들어가도록 합니다. (LED 깜빡깜빡)
2. 링크에서 APK 파일을 받아서 폰에 설치합니다.
3. 폰의 설정 > 블루투스 에서 off 상태이면 BT on 으로 바꿉니다.
4. BluetoothChat 앱을 실행 - 메뉴키 - Connect a device 선택
5. Device List 에 HC-06 슬레이브 모듈이 보이는지 확인. 안보이면 Scan 버튼을 눌러서 찾아보고 그래도 안되면 1부터 다시합니다.
6. HC-06 모듈이 보이면 선택 - 연결이 정상적으로 완료되면 챗팅 가능
7.폰으로 글 적으면 PC의 Serial Monitor에서 보이는지 확인합니다. 반대도 확인.

3-2


## Slide 16
모바일 - 센서장치 Classic BT 통신
활용
가장 기본적인 Bluetooth 활용 방법
간단하게 구현 가능

iOS 통신 어려움
상업용보다는 데모용, Tech DIY 에 적합
상대적으로 빠른 속도를 요하는 일부 전자기기에 사용
3-2


## Slide 17
3장. Part1. 클래식 블루투스

  3-1. 블루투스 소개
  3-2. 모바일 – 센서장치 classic BT 통신
  3-3. 센서장치 – 서버 classic BT 통신
  3-4. 모바일 – 모바일 classic BT 통신
Contents


## Slide 18
실습 예제
센서장치-서버 클래식 BT 통신
Raspberry Pi BT Master – HC-06 BT Slave


## Slide 19
센서장치 - 서버 Classic BT 통신
테스트 목표
아두이노와 라즈베리파이가 BT로 연결
상호 채팅 구현
라즈베리파이 3 버전만 가능
Serial/USB
Serial
Bluetooth
3-3


## Slide 20
센서장치 - 서버 Classic BT 통신
라즈베리파이 설정 1
블루투스 모듈(PyBlueZ) 설치
sudo apt-get install bluez libbluetooth-dev pi-bluetooth

Python 3.6 이후 PIP 이용시 SSL 인증 요구
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

파이썬 재설치
파이썬 관련 유틸리티가 설치된 상태에서 파이썬을 재빌드- 설치해야 블루투스 동작

mkdir temp
cd temp
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
tar -xvf Python-3.6.5.tgz
cd Python-3.6.5
./configure
sudo make && sudo make install
3-3


## Slide 21
센서장치 - 서버 Classic BT 통신
라즈베리파이 설정 2
시리얼 포트 등록
sudo sdptool add SP

블루투스 서비스 실행 옵션 수정
sudo vi /lib/systemd/system/bluetooth.service
ExecStart=/usr/lib/bluetooth/bluetoothd -C  로 수정
sudo systemctl daemon-reload -  설정 수정사항 재로딩
sudo systemctl restart bluetooth - 블루투스 서비스 재실행
sudo systemctl enable bluetooth - 재부팅 시 서비스 자동 등록
3-3


## Slide 22
센서장치 - 서버 Classic BT 통신
라즈베리파이 설정 3
장치 내 블루투스 DISCOVERABLE 상태로 변경
sudo hciconfig hci0 piscan
 이후 스마트폰 – 블루투스 설정에서 라즈베리파이가 검색되는지 확인

PYBLUEZ, PYBLENO 모듈 설치
sudo pip3 install pybluez pybleno

3-3


## Slide 23
센서장치 - 서버 Classic BT 통신
아두이노와 HC-06 연결
(앞선 예제 3-2와 연결 상태와 같음)
3-3


## Slide 24
센서장치 - 서버 Classic BT 통신
Echo 예제 아두이노에 업로드
PC와 블루투스 모듈이 통신할 수 있도록 아두이노가 중계
PC  아두이노  블루투스
블루투스  아두이노  PC
(앞선 예제 3-2 의 아두이노 스케치를 그대로 사용)
3-3


## Slide 25
센서장치 - 서버 Classic BT 통신
라즈베리파이 python 예제 실행 준비
일단 블루투스 쉘을 이용해서 BT 장치와 연결을 시도
블루투스 쉘로 접속해서 주변 BT 장치들을 스캔





6 Byte MAC address 를 이용해서 접속
sudo bluetoothctl

[bluetooth] scan on
......
Discovery started
[CHG] Controller B8:27:EB:11:19:07 Discovering: yes
[NEW] Device 00:07:79:0C:90:6F 00-07-79-0C-90-6F
[NEW] Device 98:D3:31:FC:3B:E7 iot_test
[NEW] Device C4:73:1E:96:61:75 C4-73-1E-96-61-75

[bluetooth] scan off
[bluetooth] agent NoInputNoOutput
......
[bluetooth] pair xx:xx:xx:xx:xx:xx
......
==> PIN 코드 입력
......
[bluetooth] connect xx:xx:xx:xx:xx:xx
......
[bluetooth] disconnect xx:xx:xx:xx:xx:xx

[bluetooth] quit
일부 BT 기기에 연결할 때 PIN 코드 입력 메시지가 
뜨지 않는 문제가 발생하곤 합니다. 
그런 기기들은 Python 코드로 접속할 때도 
"연결 요청이 거부되었습니다" 
에러 메시지 뱉으면서 접속이 안됩니다.
그런 경우 bluetoothctl 쉘에서 
agent NoInputNoOutput 명령어 실행해주고 
pairing, connection 한번 해주면 됩니다.
3-3


## Slide 26
센서장치 - 서버 Classic BT 통신
라즈베리파이 python 예제 실행
Chat_master.py 코드를 수정
예제소스\3_3_ClassicBt_RPi\RPi\BtChat_Master
예제소스에서 연결할 BT 장치 이름을 수정


수정한 코드를 라즈베리파이에 올려서 실행
sudo python3 BtChat_master.py
target_name = "iot_test" # target device name
3-3


## Slide 27
센서장치 - 서버 Classic BT 통신
연결 확인
아두이노와 HC-06이 동작하는 상태라면
라즈베리파이에서 BtChat_master.py 실행했을 때 자동 연결됨

아두이노 시리얼 모니터에서챗을 입력하면 Rpi 까지 전달
Rpi 에서 받은 메시지를 똑같이되돌려 줌
따라서 시리얼 모니터에 입력한메시지와 같은 메시지가도착하면 정상.
Serial/USB
Serial
Bluetooth
3-3


## Slide 28
센서장치 - 서버 Classic BT 통신
소스코드

from bluetooth import *

target_name = "iot_test"   # target device name
target_address = None
port = 1         # RFCOMM port

# Scan
nearby_devices = discover_devices()

# scanning for target device
for bdaddr in nearby_devices:
    print(lookup_name( bdaddr ))
    if target_name == lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print('device found. target address %s' % target_address)
else:
    print('could not find target bluetooth device nearby')

# establishing a bluetooth connection
try:
    sock=BluetoothSocket( RFCOMM )
    sock.connect((target_address, port))

    while True:         
        try:
            recv_data = sock.recv(1024)
            print(recv_data)
            sock.send(recv_data)
        except KeyboardInterrupt:
            print("disconnected")
            sock.close()
            print("all done")
except btcommon.BluetoothError as err:
    print('An error occurred : %s ' % err)
    pass
BtChat_master.py
3-3


## Slide 29
센서장치 - 서버 Classic BT 통신
활용
각종 Tech DIY
라즈베리파이와 상시적 연결이 필요한 센서장치 연결
아두이노에서 처리하기 버거운 작업이 필요한 경우

라즈베리파이와 모바일을 연결할 때는
라즈베리파이를 Slave 장치로 동작시키는게 더 쉬움
모바일이 라즈베리파이를 스캔 후 연결

3-3


## Slide 30
실습 예제
모바일-서버 클래식 BT 통신
Raspberry Pi BT Master – HC-06 BT Slave


## Slide 31
모바일과 서버의 Classic BT 통신
라즈베리파이 – 모바일 연결
라즈베리파이와 모바일을 연결할 때는
라즈베리파이를 Slave 장치로 동작

모바일 폰에서 스캔 후 연결
예제 3-2 에서 사용했던 BT Chat 앱을 사용
Bluetooth
Slave
Master
3-3


## Slide 32
모바일과 센서장치의 시리얼 통신
라즈베리파이 – 모바일 연결
라즈베리파이에서 BtChat_slave.py 실행
예제소스\3_3_ClassicBt_RPi\RPi\BtChat_Slave
BtChat_slave.py 파일을 라즈베리파이에 업로드
실행
sudo python3 BtChat_slave.py

모바일 폰에서 스캔 후 연결
BT Chat 앱에서 라즈베리파이 스캔
raspberrypi (혹은 지정한 이름) 로 검색되는 장치를 찾아 연결

연결 후 메시지를 보내면
메시지를 뒤집어서 회신을 줌
3-3


## Slide 33
모바일과 센서장치의 시리얼 통신
소스코드
from bluetooth import *

def receiveMsg():
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

    # RFCOMM 포트를 통해 데이터 통신을 하기 위한 준비    
    server_sock=BluetoothSocket( RFCOMM )
    server_sock.bind(('',PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    # 블루투스 서비스를 Advertise
    advertise_service( server_sock, "BtChat",
            service_id = uuid,
            service_classes = [ uuid, SERIAL_PORT_CLASS ],
            profiles = [ SERIAL_PORT_PROFILE ] )
    
    print("Waiting for connection : channel %d" % port)
    # 클라이언트가 연결될 때까지 대기
    client_sock, client_info = server_sock.accept()
    print('accepted')
    while True:          
        print("Accepted connection from ", client_info)
        try:
            # 들어온 데이터를 역순으로 뒤집어 전달
            data = client_sock.recv(1024)
            if len(data) == 0: break
            print("received [%s]" % data)
            print("send [%s]" % data[::-1])
            client_sock.send(data[::-1])
        except IOError:
            ……
            break
        except KeyboardInterrupt:
            ……
            break

receiveMsg()
3-3
BtChat_slave.py


## Slide 34
3장. Part1. 클래식 블루투스

  3-1. 블루투스 소개
  3-2. 모바일 – 센서장치 classic BT 통신
  3-3. 센서장치 – 서버 classic BT 통신
  3-4. 모바일 – 모바일 classic BT 통신
Contents


## Slide 35
모바일-모바일 클래식 BT 통신
실습 예제


## Slide 36
모바일 - 모바일 Classic BT 통신
모바일 – 모바일 연결
모바일 폰 두 대를 서로 연결하는 방법
한 대는 Master 장치로 동작 (스캔 및 연결 주도, client socket)
한 대는 Slave 장치로 동작 (센서장치 역할, server socket)

앱을 실행 후 서로 연결
예제 3-2 에서 사용했던 BT Chat 앱을 사용
Bluetooth
Slave
Master
3-4


## Slide 37
모바일 - 모바일 Classic BT 통신
Master 장치 
BT Chat 앱을 실행
[Scan for devices] 클릭 후 상대 폰을 스캔 및 연결

3-4


## Slide 38
모바일 - 모바일 Classic BT 통신
Slave 장치 
안드로이드 설정  블루투스  기기이름 변경
BT Chat 앱을 실행
[Make discoverable] 클릭 후 연결 대기
연결 후 채팅

3-4


## Slide 39
모바일 - 모바일 Classic BT 통신
Slave 장치 
안드로이드 설정  블루투스  기기이름 변경
BT Chat 앱을 실행
Make discoverable


3-4


## Slide 40
모바일 - 모바일 Classic BT 통신
테스트
 2인 1조 테스트

3-4


## Slide 41
모바일 - 모바일 Classic BT 통신
소스코드
UI 구조 및 기능
예제소스\3_2_ClassicBt_Arduino_Android\Android\BtChat
SplashActivity.kt
Bluetooth 사용을 위한 Permission 체크
MainActivity.kt
메인 화면 / 스캔 후 연결 장치가 선택되면, 연결을 시작
DeviceListActivity.kt
Paired device(Bonded device)를 표시 / 스캔 후 결과 표시

3-4


## Slide 42
모바일 - 모바일 Classic BT 통신
소스코드
블루투스 제어
BtChat\app\src\main\java\com\hardcopy\btchat\bluetooth
BluetoothManager.kt
class BluetoothManager {
    ……
    private val mAdapter = BluetoothAdapter.getDefaultAdapter()
    private var mAcceptThread: AcceptThread? = null
    private var mConnectThread: ConnectThread? = null
    private var mConnectedThread: ConnectedThread? = null
    private var mHandler: Handler? = null

    fun start() { …… }
    fun startDiscovery() { …… }
    fun cancelDiscovery() { …… }
    fun connect() { …… }
    fun stop() { …… }
    fun write() { …… }

}
Broadcast Receiver 로 수신
3-4


## Slide 43
모바일 - 모바일 Classic BT 통신
활용
간단한 코드로 손쉽게 구현
iOS 연결은...
Phone to Phone 파일 전송, 데이터 전송 등에 활용
구형 폰도 지원 가능
3-4


## Slide 44


## Slide 45
제작/

사용범위/
홈페이지이메일
서영배

본 문서의 내용 중 일부 또는 전체를 게시, 배포할 수 없습니다. 또한 상업적인 용도로 사용하실 수 없습니다.http://www.hardcopyworld.com

godstale@hotmail.com
홈페이지를 통해 본 강좌의 전체 내용 및 다양한 모듈 정보, 소스코드를 얻으실 수 있습니다.
HardCopyWorld.com 

