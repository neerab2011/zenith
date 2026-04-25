[app]
title = Zenith — Smart Detox & Digital Wellness
package.name = zenith
package.domain = org.zenith

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0.0
requirements = python3,kivy,flask,requests,werkzeug,jinja2

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

android.features = android.hardware.touchscreen

android.logcat_filters = *:S python:D

android.gradle_options = org.gradle.jvmargs=-Xmx2048m

[buildozer]
log_level = 2
warn_on_root = 1
