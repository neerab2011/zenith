#!/bin/bash

# Zenith APK Build Script
# Automates the process of building an Android APK from the Kivy app

set -e

echo "=========================================="
echo "  Zenith APK Builder"
echo "=========================================="
echo ""

# Check if buildozer is installed
if ! command -v buildozer &> /dev/null; then
    echo "❌ Buildozer not found. Installing..."
    pip install buildozer cython
fi

# Check if we're on macOS with Java issues
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "🍎 macOS detected. Setting up Java..."
    if ! command -v java &> /dev/null; then
        echo "❌ Java not found. Install with: brew install openjdk@11"
        exit 1
    fi
    export JAVA_HOME=/usr/local/opt/openjdk@11
fi

echo "📦 Building APK..."
echo ""

# Build the APK
buildozer android debug

echo ""
echo "=========================================="
echo "✅ APK Build Complete!"
echo "=========================================="
echo ""
echo "📱 Your APK is ready at:"
echo "   bin/zenith-1.0.0-debug.apk"
echo ""
echo "💡 To install on your phone:"
echo "   adb install -r bin/zenith-1.0.0-debug.apk"
echo ""
