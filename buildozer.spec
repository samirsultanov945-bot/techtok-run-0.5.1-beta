[app]
title = TechTok Run
package.name = techtokrun
package.domain = org.techtok
source.dir = .
source.include_exts = py,png,jpg,jpeg,ogg,wav,ttf,json
version = 1.0
requirements = python3,kivy,pyjnius,plyer
orientation = landscape
fullscreen = 1

android.permissions = INTERNET,VIBRATE,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE
android.api = 35
android.minapi = 23

[buildozer]
log_level = 2
warn_on_root = 1
