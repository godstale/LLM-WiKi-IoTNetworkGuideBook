---
title: "5장. 센서장치-모바일-서버 연동"
type: source
tags: [IoT, Integration, Node.js, Telegram, MQTT, Course]
sources: [chap5-sensor-server-mobile]
source_file: wiki/originals/chap5-sensor-server-mobile.md
last_updated: 2026-04-19
---

# 5장. 센서장치-모바일-서버 연동
[[사물인터넷과 네트워크 강의]]의 하위 과정입니다.

## 개요
센서 장치, 서버, 모바일 기기를 하나로 묶어 통합 서비스를 구축하는 세 가지 주요 방법([[Node.js]], 메신저 챗봇, [[MQTT]])을 다룹니다.

## 1. Node.js 서버 연동
- **특징**: [[JavaScript]] 기반의 고성능 서버 프레임워크인 [[Node.js]]와 [[Express]]를 사용.
- **구현**:
    - 센서 장치에서 [[HTTP-POST]]로 데이터를 서버에 전송.
    - 서버는 데이터를 저장하고, 사용자 요청 시 HTML(Pug 등)로 시각화하여 제공.
    - [[body-parser]]를 통해 HTTP 요청 바디의 데이터를 처리.

## 2. 메신저(Telegram) 연동
- **특징**: 별도의 전용 앱 개발 없이 메신저의 [[ChatBot]] 기능을 UI로 활용.
- **구현**:
    - [[BotFather]]를 통해 텔레그램 봇 생성 및 API Token 발급.
    - [[RaspberryPi]]에서 [[telepot]] 라이브러리를 사용해 봇 컨트롤러 구현.
    - 사용자가 "status" 등의 명령어를 입력하면 센서 데이터를 채팅창에 응답.
- **장점**: 빠른 프로토타이핑, 디버깅 및 실시간 모니터링에 유용.

## 3. MQTT를 이용한 연동
- **[[MQTT]] (Message Queuing Telemetry Transport)**: 저대역폭, 저전력 환경에 최적화된 Pub/Sub 기반 메시징 프로토콜.
- **구성 요소**:
    - **Broker**: 메시지를 중계하는 서버 (예: [[Mosquitto]]).
    - **Client**: 메시지를 발행([[Publish]])하거나 구독([[Subscribe]])하는 장치.
- **핵심 개념**:
    - **[[Topic]]**: 메시지가 전달되는 채널 (계층 구조 지원).
    - **[[QoS]]**: 메시지 전달 품질 단계 (0: 최저 부하, 2: 최고 신뢰성).
- **라이브러리**: [[PubSubClient]](Arduino), [[Paho]](Python/Android).
