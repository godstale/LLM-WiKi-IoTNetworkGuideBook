---
title: "2장. 유선통신"
type: source
tags: [iot, wired-communication, serial, arduino, raspberry-pi, Course]
date: 2026-04-19
source_file: wiki/originals/chap2-wired-comm.md
sources: [chap2-wired-comm]
last_updated: 2026-04-19
---

# 2장. 유선통신
[[사물인터넷과 네트워크 강의]]의 하위 과정입니다.

## Summary
이 장에서는 IoT 네트워크의 기초가 되는 유선 통신, 특히 비동기식 직렬 통신(Serial Communication)에 대해 다룹니다. 아두이노와 라즈베리파이 간의 시리얼 통신 설정 및 실습, 그리고 안드로이드 모바일 기기와 아두이노 간의 OTG를 이용한 시리얼 연결 방법을 설명합니다.

## Key Claims
- 시리얼 통신은 TX(송신)와 RX(수신) 핀을 사용하며, 클럭 동기화를 위해 Baudrate(통신속도) 설정이 필수적입니다.
- 아두이노는 하드웨어 시리얼(D0, D1) 외에도 SoftwareSerial 라이브러리를 통해 일반 디지털 핀으로 시리얼 통신을 구현할 수 있습니다.
- 라즈베리파이에서 시리얼 통신을 사용하려면 커널 로그 출력 포트 설정을 해제하고 UART를 활성화해야 합니다.
- 모바일 기기와 아두이노 연결 시 OTG 케이블을 사용하여 전원 문제 해결 및 안정적인 데이터 통신이 가능합니다.

## Key Quotes
> "비동기식 직렬 통신... 전송핀 (TX), 수신핀(RX) 클럭 동기화  Baudrate(통신속도 BPS)" — Slide 3
> "모바일 폰이 데이터 수집 및 1차 처리... 실시간성" — Slide 15

## Connections
- [[SerialCommunication]] — 핵심 통신 방식
- [[Arduino]] — 센서 장치로 활용
- [[RaspberryPi]] — 홈 서버로 활용
- [[SoftwareSerial]] — 아두이노 라이브러리

## Contradictions
- 없음.
