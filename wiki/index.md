---
title: "Wiki Index"
type: index
last_updated: 2026-04-19
---

# Wiki Index

## Sources
- [1장. 사물인터넷과 네트워크](sources/chap1-iot-network.md) — IoT의 구성 요소 및 다양한 유무선 통신 기술 입문
- [2장. 유선통신](sources/chap2-wired-comm.md) — IoT 유선 통신 기초 및 시리얼 통신 실습
- [3장. Part1. 클래식 블루투스](sources/chap3-1-classic-bt.md) — 클래식 블루투스 기초 및 장치 간 통신
- [3장. Part2. BLE](sources/chap3-5-ble.md) — BLE 프로토콜, iBeacon 및 GATT 구조 이해
- [4장. WiFi](sources/chap4-wifi.md) — ESP32 WiFi 접속, HTTP 통신 및 웹 서버/소켓 실습
- [5장. 센서장치-모바일-서버 연동](sources/chap5-sensor-server-mobile.md) — Node.js, Telegram, MQTT를 활용한 통합 서비스 구축
- [7장. 홈 오토메이션 구현](sources/chap7-home-automation.md) — 센서-서버-모바일 통합 홈 오토메이션 실전 프로젝트

## Entities
- [Arduino](entities/Arduino.md) — 오픈소스 마이크로컨트롤러 플랫폼
- [RaspberryPi](entities/RaspberryPi.md) — 리눅스 기반 싱글 보드 컴퓨터 (홈 서버용)
- [ESP32](entities/ESP32.md) — WiFi 및 Dual-mode Bluetooth를 지원하는 MCU
- [ESP8266](entities/ESP8266.md) — 저렴한 WiFi 제어 모듈 및 MCU
- [HC-06](entities/HC-06.md) — 클래식 블루투스(SPP) 지원 통신 모듈
- [HM-10](entities/HM-10.md) — BLE v4.0 통신 지원 모듈
- [ESPAsyncWebServer](entities/ESPAsyncWebServer.md) — ESP32용 비동기 HTTP 웹 서버 라이브러리
- [ArduinoJson](entities/ArduinoJson.md) — 아두이노용 JSON 라이브러리
- [Node.js](entities/Node.js.md) — 확장성 있는 네트워크 애플리케이션 개발을 위한 JS 런타임
- [Mosquitto](entities/Mosquitto.md) — 경량 메시징을 위한 오픈소스 MQTT 브로커
- [Express](entities/Express.md) — Node.js를 위한 빠르고 개방적인 웹 프레임워크
- [MariaDB](entities/MariaDB.md) — IoT 데이터 저장을 위한 관계형 데이터베이스
- [DHT11](entities/DHT11.md) — 디지털 온습도 측정 센서
- [Chart.js](entities/Chart.js.md) — 데이터 시각화를 위한 JS 라이브러리

## Concepts
- [사물인터넷과 네트워크 강의](concepts/IoTNetworkCourse.md) — IoT 통합 커리큘럼 메인 페이지
- [SerialCommunication](concepts/SerialCommunication.md) — 비동기식 직렬 통신 방식
- [Bluetooth](concepts/Bluetooth.md) — 근거리 무선 통신 기술 표준
- [ClassicBT](concepts/ClassicBT.md) — 기존 블루투스 통신 방식 (SPP 등)
- [BLE](concepts/BLE.md) — 저전력 블루투스 프로토콜 (GATT 기반)
- [GATT](concepts/GATT.md) — BLE 데이터 구조 및 통신 규격
- [iBeacon](concepts/iBeacon.md) — 애플이 정의한 BLE 비컨 표준
- [Ubiquitous](concepts/Ubiquitous.md) — '언제 어디서나' 존재하는 정보 통신 환경
- [WiFi](concepts/WiFi.md) — 근거리 무선 네트워크 기술 표준
- [LoRa](concepts/LoRa.md) — 저전력 장거리 무선 통신 기술
- [Zigbee](concepts/Zigbee.md) — 저전력 고속 메시 네트워크 기술
- [RF-Communication](concepts/RF-Communication.md) — 단순 무선 주파수 데이터 송수신
- [WiFiMulti](concepts/WiFiMulti.md) — 다중 AP 자동 연결 관리 기능
- [SmartConfig](concepts/SmartConfig.md) — 모바일 앱 기반 WiFi 간편 설정 프로토콜
- [HTTP-GET](concepts/HTTP-GET.md) — URL 기반 데이터 요청 방식
- [HTTP-POST](concepts/HTTP-POST.md) — Body 기반 데이터 전송 방식
- [WebSocket](concepts/WebSocket.md) — 전이중 양방향 소켓 통신 프로토콜
- [SPIFFS](concepts/SPIFFS.md) — 아두이노용 직렬 플래시 파일 시스템
- [SoftAP](concepts/SoftAP.md) — 소프트웨어 방식으로 구현된 액세스 포인트
- [JSON](concepts/JSON.md) — 사람이 읽기 쉬운 데이터 교환 표준 포맷
- [MQTT](concepts/MQTT.md) — 지연 시간이 짧은 Pub/Sub 기반 메시징 프로토콜
- [Publish](concepts/Publish.md) — MQTT 토픽에 메시지를 보내는 행위
- [Subscribe](concepts/Subscribe.md) — MQTT 토픽으로부터 메시지를 받기 위해 등록하는 행위
- [Topic](concepts/Topic.md) — MQTT 메시지가 발행 및 구독되는 채널
- [QoS](concepts/QoS.md) — MQTT 메시지 전송의 신뢰성 품질 단계
- [ChatBot](concepts/ChatBot.md) — 채팅 인터페이스를 통해 자동화된 서비스를 제공하는 프로그램
- [Home-Automation](concepts/Home-Automation.md) — 가전 및 장치들을 통합 제어하는 자동화 시스템
- [Channel-Management](concepts/Channel-Management.md) — 서버에서 장치별로 할당된 논리적 채널 관리
- [Auth-Code](concepts/Auth-Code.md) — 장치 인증 및 보안을 위한 고유 코드
- [Data-Query-API](concepts/Data-Query-API.md) — 저장된 데이터를 조회하기 위한 인터페이스
