---
title: "3장. Part1. 클래식 블루투스"
type: source
tags: [iot, bluetooth, classic-bt, arduino, raspberry-pi, android, Course]
date: 2026-04-19
source_file: wiki/originals/chap3-1-classic-bt.md
sources: [chap3-1-classic-bt]
last_updated: 2026-04-19
---

# 3장. Part1. 클래식 블루투스
[[사물인터넷과 네트워크 강의]]의 하위 과정입니다.

## Summary
블루투스 기술의 기초와 클래식 블루투스(Classic BT)를 이용한 통신 실습을 다룹니다. 아두이노(HC-06 슬레이브)와 안드로이드 모바일, 라즈베리파이(마스터), 그리고 모바일 기기 간의 통신 구현 방법을 설명합니다.

## Key Claims
- 블루투스는 2.4GHz 대역을 사용하며, 주파수 호핑(Frequency Hopping) 기술을 통해 간섭에 대응합니다.
- 장치 종류를 인식하기 위해 프로파일(Profile)을 사용하며, 데이터 통신에는 주로 SPP(Serial Port Profile)가 활용됩니다.
- HC-06 모듈은 AT 커맨드를 통해 장치명, 암호, Baudrate 등을 설정할 수 있습니다.
- 라즈베리파이 3 이상에서 PyBluez 등을 이용해 블루투스 마스터 또는 슬레이브로 동작시킬 수 있습니다.

## Key Quotes
> "주파수 호핑 (frequency hopping) 다수의 채널 사이를 특정 순서에 따라 이동하며 데이터를 분할 전송하는 방법" — Slide 4
> "프로파일 Slave 장치 종류를 인식할 수 있도록 만든 표준" — Slide 5

## Connections
- [[Bluetooth]] — 핵심 기술
- [[ClassicBT]] — 구현 방식
- [[Profile]] — 블루투스 표준
- [[SPP]] — 시리얼 포트 프로파일
- [[HC-06]] — 블루투스 모듈

## Contradictions
- 없음.
