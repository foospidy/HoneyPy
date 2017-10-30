# HoneyPy Plugins

## DNS

Responds to DNS queries with a random ip address.

- Medium interaction
    - udp: `plugins/DnsUdp`

## Echo

Echos back data sent by connected clients.

- Low interaction
    - tcp: `plugins/Echo`
    - udp: `plugins/Echo_udp`

## Elasticsearch

Simple Elasticsearch emulation. Responds to requests for `/`, request for node information `/_nodes`, and search requests `/_search`.

- Low interaction
    - tcp: `plugins/Elasticsearch`

## HashCountRandom

A bogus service. For each instance of data sent by a connected client it increments a counter and returns a md5 hash of the count and some random data.

- Low interaction
    - tcp: `plugins/HashCountRandom`

## MOTD

For each connection it returns a message and closes the connection.

- Low interaction
    - tcp: `plugins/MOTD`
    - udp: `plugins/MOTD_udp`

## NTP

Accepts NTP requests, returns a packet with the current system time.

- Low interaction
    - udp: `plugins/NtpUdp`

## Random

For each instance of data sent by a connected client it returns some random data.

- Low interaction
    - tcp: `plugins/Random`

## SIP

Simple SIP (Session Initiation Protocol) emulation.

- Low interaction
    - udp: `plugins/SIP`

## SMTP

Simple SMTP server emulation. Provides interaction with a subset of commands.

- Low interaction
    - tcp: `plugins/SmtpExim`

## TFTP

TFTP (Trivial File Transfer Protocol) emulation.

- Medium interaction
    - udp: `plugins/TFTP`

## Telnet

Emulates a Telnet service.

- Medium interaction
    - tcp: `plugins/TelnetUnix`

## Web

Simple web server emulation. Responds to `/robots.txt`, `/wp-login.php`, and various PhpMysqlAdmin pages. All other requests receive a simple 200 OK response.

- Low interaction
    - tcp: `plugins/Web`
