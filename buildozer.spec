[app]

# App title
title = AuricM v1

# Package name (all lowercase, no spaces)
package.name = com.userballs.auricmv1

# Package domain (used for generating package ID)
package.domain = org.userballs

# Source code directory (root of the repo)
source.dir = .

# File extensions to include from source.dir
source.include_exts = py,png,jpg,kv,json

# Python dependencies (add hostpython3, six, setuptools for modern Kivy/Buildozer builds)
requirements = python3,kivy,kivymd,mutagen,yt_dlp,requests,pygame,pillow,six,setuptools,hostpython3

# Entry point of the app
entrypoint = newv2.py

# Orientation (portrait, landscape, or all)
orientation = portrait

# Fullscreen mode
fullscreen = 1

# Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,FOREGROUND_SERVICE

# Android minimum API
android.minapi = 21

# Android target API
android.api = 33

# Android architectures
android.archs = armeabi-v7a,arm64-v8a

# Version
version = 1.0.0

# Debug mode (1=debug, 0=release)
android.debug = 1

[buildozer]

# Build and bin directories
build_dir = .build
bin_dir = bin

# Log level (0=debug, 1=info, 2=warning)
log_level = 2

# Number of concurrent jobs for compilation
jobs = 4

# Clean build every time
clean_build = 1
