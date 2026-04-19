---
title: "1장. 사물인터넷과 네트워크"
type: source
tags: [IoT, Network, Introduction, Course]
sources: [chap1-iot-network]
source_file: wiki/originals/chap1-iot-network.md
last_updated: 2026-04-19
---

# 1장. 사물인터넷과 네트워크
[[사물인터넷과 네트워크 강의]]의 하위 과정입니다.

## 개요
사물인터넷(IoT)의 정의와 목표, 구성 요소, 그리고 구현을 위한 유무선 통신 기술의 종류를 다룹니다.

## 사물인터넷의 정의
- **유비쿼터스([[Ubiquitous]])**: 언제, 어디서나 존재한다는 의미.
- **IoT**: 기술 그 자체가 아니라, 사물들이 연결되어 목표를 달성하는 상태를 의미.

## IoT의 4대 요소
1. **센서 장치**: [[Arduino]], [[ESP32]] 등 임베디드 장치.
2. **서버**: [[RaspberryPi]] 등 데이터 처리 및 관리 장치.
3. **모바일**: 사용자 인터페이스 및 제어 (Android/iOS).
4. **네트워크/프로토콜**: 장치 간 데이터 송수신 규약.

## 주요 구현 도구
- **하드웨어**: [[Arduino]], [[RaspberryPi]], [[ESP32]], [[ESP8266]].
- **소프트웨어**: C/C++, Python, Node.js, Kotlin, Java.

## 유무선 통신 기술
### 유선 통신
- **시리얼([[SerialCommunication]])**: USB/UART 기반 1:1 통신.
- **이더넷**: 인터넷 직접 연결, 안정적이나 공간 제약 있음.

### 무선 통신
- **근거리**: 적외선(IR), NFC, [[Bluetooth]]([[ClassicBT]]/[[BLE]]), [[WiFi]].
- **중장거리/특수**: [[RF-Communication]](NRF24L01 등), [[Zigbee]], [[LoRa]], 3G/LTE.

## 개발 환경 설정
- 아두이노 IDE 설치 및 ESP32 애드온 설정.
- 라즈베리파이 및 안드로이드 스튜디오 설치.
- [[ESP32]]용 BLE 라이브러리 및 Framework 설정.
