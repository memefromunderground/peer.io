from flask import Flask, render_template
from pyngrok import ngrok, conf
import os

app = Flask(__name__)

# Configure pyngrok to use your existing ngrok.exe
# Replace this path with the actual path to your ngrok.exe
# ngrok_path = "ngrok.exe"  # Update this path
# conf.get_default().ngrok_path = ngrok_path

# Global variable to store tunnel
tunnel = None

@app.route('/')
def index():
    # global tunnel
    
    # try:
    #     # Create tunnel if it doesn't exist
    #     if tunnel is None:
    #         tunnel = ngrok.connect(5000)
        
    #     tunnel_url = tunnel.public_url
    #     tunnel_info = {
    #         'public_url': tunnel_url,
    #         'local_url': 'http://localhost:5000',
    #         'status': 'active'
    #     }
        
    # except Exception as e:
    #     tunnel_info = {
    #         'public_url': None,
    #         'local_url': 'http://localhost:5000',
    #         'status': f'error: {str(e)}'
    #     }
    
    return render_template('index.html')

# @app.route('/stop-tunnel')
# def stop_tunnel():
#     global tunnel
#     try:
#         if tunnel:
#             ngrok.disconnect(tunnel.public_url)
#             tunnel = None
#         return "Tunnel stopped"
#     except Exception as e:
#         return f"Error stopping tunnel: {e}"

if __name__ == '__main__':
    # try:
        app.run(debug=True, host='0.0.0.0', port=8080)
    # finally:
    #     # Clean up on exit
    #     if tunnel:
    #         ngrok.kill()

# To install pyngrok: pip install pyngrok