# Zenith — Smart Detox & Digital Wellness
# Kivy Android Wrapper
# This file wraps the Flask web app inside a native Android app

import os
import sys
import threading
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.webview import WebView
from kivy.core.window import Window
from kivy.logger import Logger

# Configure window
Window.size = (540, 960)

class ZenithApp(App):
    """Zenith Kivy Application - Wraps Flask backend"""
    
    def build(self):
        """Build the main UI"""
        self.title = 'Zenith — Smart Detox & Digital Wellness'
        
        # Start Flask server in background thread
        self.flask_thread = threading.Thread(target=self.start_flask_server, daemon=True)
        self.flask_thread.start()
        
        # Wait for Flask to initialize
        time.sleep(3)
        
        # Create layout
        layout = BoxLayout(orientation='vertical')
        
        # Create WebView to display Flask app
        try:
            self.webview = WebView(url='http://127.0.0.1:5050/')
            layout.add_widget(self.webview)
        except Exception as e:
            Logger.error('ZenithApp', f'WebView Error: {str(e)}')
        
        return layout
    
    def start_flask_server(self):
        """Start Flask development server"""
        try:
            # Import Flask app from your original file
            from app_2 import app
            
            # Run Flask on localhost
            app.run(
                host='127.0.0.1',
                port=5050,
                debug=False,
                use_reloader=False,
                threaded=True
            )
        except ImportError:
            Logger.error('ZenithApp', 'Could not import Flask app from app_2.py')
        except Exception as e:
            Logger.error('ZenithApp', f'Flask Server Error: {str(e)}')
    
    def on_stop(self):
        """Handle app closure"""
        return True

if __name__ == '__main__':
    app = ZenithApp()
    app.run()
