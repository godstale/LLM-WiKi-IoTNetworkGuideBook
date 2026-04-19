---
title: "4장. WiFi"
type: source
tags: [IoT, Network, WiFi, ESP32, HTTP, WebSocket, Course]
sources: [chap4-wifi]
source_file: wiki/originals/chap4-wifi.md
last_updated: 2026-04-19
---

# 4장. WiFi
[[사물인터넷과 네트워크 강의]]의 하위 과정입니다.

## 개요
[[ESP32]]의 [[WiFi]] 기능을 활용한 네트워크 접속, HTTP 통신(GET/POST), 웹 서버 구축 및 [[WebSocket]]을 통한 실시간 양방향 통신을 다룹니다.

## WiFi 접속 및 설정
- **동작 모드**:
    - **STA(Station)**: 무선 공유기(AP)에 접속하는 클라이언트 모드.
    - **[[SoftAP]]**: ESP32 자체가 접속 지점(AP)이 되는 모드.
    - **STA+AP**: 클라이언트와 AP 역할을 동시에 수행.
- **주요 기능**:
    - **WiFi 스캔**: 주변 AP의 SSID와 신호 세기(RSSI) 확인.
    - **[[WiFiMulti]]**: 여러 공유기를 등록하고 신호가 강한 곳에 자동 접속.
    - **[[SmartConfig]]**: 모바일 앱을 통해 SSID/PW 정보를 기기에 전달하는 설정 방식.

## HTTP 통신 및 데이터 처리
- **[[HTTP-GET]]**: URL 파라미터를 통해 데이터를 요청 (길이 제한 있음).
- **[[HTTP-POST]]**: 바디(Body)에 데이터를 실어 전송 (대용량 및 보안 유리).
- **[[JSON]]**: (Key-Value) 쌍의 텍스트 포맷. IoT API 통신 표준.
- **[[ArduinoJson]]**: ESP32에서 JSON 데이터를 파싱하고 생성하기 위한 라이브러리.

## 웹 서버 구축
- **[[ESPAsyncWebServer]]**: 비동기 방식으로 동작하는 고성능 웹 서버 라이브러리.
- **[[SPIFFS]]**: 플래시 메모리를 파일 시스템으로 사용. HTML, 이미지 등 정적 리소스를 저장하고 웹으로 서비스 가능.

## 실시간 양방향 통신 (WebSocket)
- **[[WebSocket]]**: HTTP의 Polling 방식 한계를 극복하기 위한 양방향 소켓 통신.
- **활용**: ESP32(Server)와 [[RaspberryPi]](Client) 간 실시간 제어 및 모니터링 구현.
- **장점**: 지속적인 연결 유지를 통해 데이터 전송 지연이 적음.
