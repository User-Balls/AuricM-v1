[app]

# (str) Title of your application
title = AuricM v1

# (str) Package name (must be lowercase, no spaces)
package.name = com.userballs.auricmv1

# (str) Package domain (used to generate package name)
package.domain = org.userballs

# (str) Source code location
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Application requirements
requirements = python3,kivy,kivymd,mutagen,yt_dlp,requests,pygame,pillow

# (str) Application versioning
version = 1.0.0

# (str) Entry point of the application
entrypoint = workingdesktopappdownloader.py

# (str) Orientation (portrait, landscape or all)
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Minimum API your app will support
android.minapi = 21

# (int) Target API for build
android.api = 33

# (str) Android SDK path (optional, will auto-download if not set)
# android.sdk_path = /path/to/android/sdk

# (str) Android NDK path (optional, will auto-download if not set)
# android.ndk_path = /path/to/android/ndk

# (str) Android entry point (default is org.kivy.android.PythonActivity)
android.entrypoint = org.kivy.android.PythonActivity

# (str) Supported orientation
android.orientation = portrait

# (bool) Allow the app to be debuggable
android.debug = 1

# (list) Android architecture targets
android.archs = armeabi-v7a, arm64-v8a

# (bool) Enable splash screen
#android.show_splash_screen = 1

# (str) Icon (optional)
#icon.filename = %(source.dir)s/icon.png

# (str) Presplash image (optional)
#presplash.filename = %(source.dir)s/presplash.png

[buildozer]

# (str) Path to build directory
build_dir = .build

# (str) Path to bin directory
bin_dir = bin

# (str) Log level (0=debug, 1=info, 2=warning)
log_level = 2

# (int) Number of concurrent jobs for compilation
jobs = 4

# (bool) Clean build every time
clean_build = 1
